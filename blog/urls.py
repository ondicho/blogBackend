from django.urls import path
from blog import views

urlpatterns = [
    path('posts/',views.blogView),
    path('posts/<int:pk>',views.blogDetailView.as_view()),
]
