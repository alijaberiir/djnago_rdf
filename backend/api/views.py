from rest_framework.generics import ListCreateAPIView,  RetrieveUpdateDestroyAPIView
from blog.models import Article
from rest_framework.permissions import IsAdminUser
from .serializer import ArticleSerializer, UserSerializer
from django.contrib.auth.models import User



class Articlelist(ListCreateAPIView):
	queryset  = Article.objects.all()
	serializer_class = ArticleSerializer

class ArticleDetail(RetrieveUpdateDestroyAPIView ):
	queryset  = Article.objects.all()
	serializer_class = ArticleSerializer
	


class Userlist(ListCreateAPIView):
	queryset  = User.objects.all()
	serializer_class = UserSerializer
	permission_classes = (IsAdminUser,)

	
class UserDetail(RetrieveUpdateDestroyAPIView ):
	queryset  = User.objects.all()
	serializer_class = UserSerializer
	permission_classes = (IsAdminUser,)
