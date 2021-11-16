from django.urls import path

from planes.views import *

urlpatterns = [
    # path('', home, name='home'),
    path('', PlaneListView.as_view(), name='home'),
    path('detail/<int:pk>/', PlaneDetailView.as_view(), name='detail'),
    path('update/<int:pk>/', PlaneUpdateView.as_view(), name='update'),
    path('delete/<int:pk>/', PlaneDeleteView.as_view(), name='delete'),
    path('add/', PlaneCreateView.as_view(), name='create'),

]