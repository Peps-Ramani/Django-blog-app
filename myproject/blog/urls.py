from django.urls import path
from . import views

app_name = 'blog'
urlpatterns = [
    path('',views.HomePage.as_view(),name='homepage'),
    path('blog/',views.HomePage.as_view(),name='homepage'),
    path('blog/blogs/',views.BlogListView.as_view(),name='bloglistview'),
    path('blog/<int:pk>/',views.BlogDetailView.as_view(),name='blogdetailview'),
    path('blog/blogger/<int:pk>/',views.AuthorDetailView.as_view(),name='authordetailview'),
    path('blog/bloggers/',views.AuthorListView.as_view(),name='authorlistview'),
    path('blog/<int:pk>/create/',views.CommentPage,name='commentpage'),
]