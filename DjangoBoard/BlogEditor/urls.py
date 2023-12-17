from django.urls import path
from .views.views import home, edithome

urlpatterns = [
    path('', home, name='blog_home'),
    path("post/<int:pk>/", edithome, name="blog_edit"),
]