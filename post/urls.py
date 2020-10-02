from django.contrib import admin
from django.urls import path, include

from .views import post_list, post_detail, like_post
from post.api.views import  api_list_view, api_detail_view


app_name = 'post'
urlpatterns = [
    path('', post_list, name='post-list'),
    path('like/', like_post, name='like-post'),
    path('<int:pk>/', post_detail, name='posts-detail'),
    path('api/post/', api_list_view.as_view(), name='api_list_view'),
    path('api/post/<int:post_id>', api_detail_view, name='api_detail_view'),

]
