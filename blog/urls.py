from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('post/<int:pk>/', views.PostDetail.as_view(), name='post_detail'),
    path('review/<int:pk>/', views.AddComments.as_view(), name='add_comments')
]