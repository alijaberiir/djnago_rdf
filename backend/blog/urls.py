from blog.models import Article
from django.urls import path
from .views import ArticleList, ArticleDetail
urlpatterns = [
	path("", ArticleList.as_view(), name='list'),
	path("<int:pk>", ArticleDetail.as_view(), name='detail'),
]
