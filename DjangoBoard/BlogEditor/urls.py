from django.urls import path
from .views.views import home
from .views.blogeditview import blogedit

urlpatterns = [
    path('', home, name='blog_home'),
    path("post/<int:pk>/", blogedit, name="blog_edit"),
]