from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.core.paginator import Paginator
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import (
    DetailView, CreateView, UpdateView, DeleteView,
    ListView
)

from planes.forms import PlaneForm
from planes.models import Plane

__all__ = (
    'home', 'PlaneListView',
    'PlaneDetailView',
    'PlaneCreateView', 'PlaneUpdateView',
    'PlaneDeleteView',
)


def home(request, pk=None):
    qs = Plane.objects.all()
    lst = Paginator(qs, 5)
    page_number = request.GET.get('page')
    page_obj = lst.get_page(page_number)
    context = {'page_obj': page_obj,}
    return render(request, 'planes/home.html', context)


class PlaneListView(ListView):
    paginate_by = 10
    model = Plane
    template_name = 'planes/home.html'


class PlaneDetailView(DetailView):
    queryset = Plane.objects.all()
    template_name = 'planes/detail.html'


class PlaneCreateView(SuccessMessageMixin, LoginRequiredMixin, CreateView):
    model = Plane
    form_class = PlaneForm
    template_name = 'planes/create.html'
    success_url = reverse_lazy('planes:home')
    success_message = "Plane was created successfully"


class PlaneUpdateView(SuccessMessageMixin, LoginRequiredMixin, UpdateView):
    model = Plane
    form_class = PlaneForm
    template_name = 'planes/update.html'
    success_url = reverse_lazy('planes:home')
    success_message = "Plane was updated successfully"


class PlaneDeleteView(LoginRequiredMixin, DeleteView):
    model = Plane
    # template_name = 'planes/delete.html'
    success_url = reverse_lazy('planes:home')

    def get(self, request, *args, **kwargs):
        messages.success(request, 'Plane was deleted successfully')
        return self.post(request, *args, **kwargs)