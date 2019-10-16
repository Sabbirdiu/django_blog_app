from django.urls import path

from .views import BlogView,About,Detail,NewPost,UpdateBlog,DeletePost

urlpatterns = [
    path('',BlogView.as_view(),name='home'),
    path('about/',About.as_view(),name='about'),
    path('post/<int:pk>/',Detail.as_view(),name='detail_view'),
    path('post/new/',NewPost.as_view(),name = 'post_new'),
    path('post/<int:pk>/edit/',UpdateBlog.as_view(),name='update'),
    path('post/<int:pk>/delete/',DeletePost.as_view(),name='delete'),

]