from planes.models import Plane

def dfs_paths(graph, start, goal):
    """Function looking all possible routes from one city to another. No city repetition."""
    stack = [(start, [start])]
    while stack:
        (vertex, path) = stack.pop()
        if vertex in graph.keys():
            for next_ in graph[vertex] - set(path):
                if next_ == goal:
                    yield path + [next_]
                else:
                    stack.append((next_, path + [next_]))


def get_graph(qs):
    graph = {}
    for q in qs:
        graph.setdefault(q.from_city_id, set())
        graph[q.from_city_id].add(q.to_city_id)
    return graph


def get_routes(request, form) -> dict:
    context = {'form': form}
    qs = Plane.objects.all().select_related('from_city', 'to_city')
    graph = get_graph(qs)
    data = form.cleaned_data
    from_city = data['from_city']
    to_city = data['to_city']
    cities = data['cities']
    travelling_time = data['travelling_time']
    all_ways = list(dfs_paths(graph, from_city.id, to_city.id))
    if not len(all_ways):
        raise ValueError('No Routes are satisfying the conditions')
    if cities:
        # if there is the cities to stop through
        _cities = [city.id for city in cities]
        right_ways = []
        for route in all_ways:
            if all(city in route for city in _cities):
                right_ways.append(route)
        if not right_ways:
            # when route list is empty
            raise ValueError('No Routes with the stops at required cities.')
    else:
        right_ways = all_ways
    routes = []
    all_plains = {}
    for q in qs:
        all_plains.setdefault((q.from_city_id, q.to_city_id), [])
        all_plains[(q.from_city_id, q.to_city_id)].append(q)
    for route in right_ways:
        tmp = {'planes': []}
        total_time = 0
        for i in range(len(route) - 1):
            qs = all_plains[(route[i], route[i + 1])]
            q = qs[0]
            total_time += q.travel_time
            tmp['planes'].append(q)
        tmp['total_time'] = total_time
        if total_time <= travelling_time:
            # if travel time less= than required, adding route to list
            routes.append(tmp)
    if not routes:
        # if list is empty
        raise ValueError('Travel time more than required')
    sorted_routes = []
    # sorting by time
    if len(routes) == 1:
        sorted_routes = routes
    else:
        times = list(set(r['total_time'] for r in routes))
        times = sorted(times)
        for time in times:
            for route in routes:
                if time == route['total_time']:
                    sorted_routes.append(route)
    context['routes'] = sorted_routes
    context['cities'] = {'from_city': from_city, 'to_city': to_city}
    return context
