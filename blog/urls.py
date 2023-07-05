from django.urls import path
from .views import *

urlpatterns = [
    path('', ArticleListView.as_view()),
    path("<slug:slug>", ArticleDetailView.as_view()),
    path("<slug:slug>/comments", CommentListView.as_view()),
]
