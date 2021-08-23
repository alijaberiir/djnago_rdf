from django.urls import path, include
from .views import Articlelist, ArticleDetail, Userlist, UserDetail
urlpatterns = [
	path("", Articlelist.as_view(), name='list'),
	path("<int:pk>", ArticleDetail.as_view(), name='deatail'),
	path("user", Userlist.as_view(), name='userlist'),
	path("user/<int:pk>", UserDetail.as_view(), name='userdeatail'),
]
