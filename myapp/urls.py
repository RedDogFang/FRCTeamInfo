from django.urls import path
from .views import example_endpoint, index

urlpatterns = [
    path('', index, name='index'),
    path('example-endpoint/', example_endpoint, name='example-endpoint'),

]
