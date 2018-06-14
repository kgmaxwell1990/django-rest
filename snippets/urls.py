from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from snippets.views import *

urlpatterns = [
    path('', snippet_list),
    path('<int:pk>/', snippet_detail),
]

urlpatterns = format_suffix_patterns(urlpatterns)