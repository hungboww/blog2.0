from django.urls import path
from .views import BlogView, BlogDetailView, UpvoteView, DownvoteView, CountBlogView, ListFeaturedView, TagBlog, \
    ListCategoryView, ListTagView, PostListDetailFilter

app_name = 'blog_it'

urlpatterns = [
    path('', BlogView.as_view(), name='blog-list'),
    path('tag/', TagBlog.as_view(), name='tag'),
    path('upvote/<int:pk>', UpvoteView.as_view(), name='upvote'),
    path('downvote/<int:pk>', DownvoteView.as_view(), name='down_vote'),
    path('featured/', ListFeaturedView.as_view(), name='blog-detail'),
    path('count/', CountBlogView.as_view(), name='count-blog'),
    path('category/<pk>', ListCategoryView.as_view(), name='blog-category'),
    path('tag/<pk>', ListTagView.as_view(), name='blog-tag'),
    path('slug/<str:slug>/', BlogDetailView.as_view(), name='blog-detail'),
    path('search/', PostListDetailFilter.as_view(), name='search_post'),

]
