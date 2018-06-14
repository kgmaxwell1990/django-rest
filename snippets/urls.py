from django.urls import path
from snippets import views

urlpatterns = [
    path('', views.snippet_list),
    path('snippets/(?P<pk>[0-9]+)/', views.snippet_detail),
]