from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
# Create your models here.
class Article(models.Model):

	title = models.CharField(max_length = 200, verbose_name = 'عنوان خبر')
	slug = models.SlugField(max_length = 200, unique = True, verbose_name = 'لینک')
	author = models.ForeignKey(User, verbose_name = 'نویسنده', related_name = 'blog_posts', on_delete = models.CASCADE)
	context = models.TextField(verbose_name = 'متن خبر')
	publish = models.DateTimeField(default = timezone.now, verbose_name = 'زمان انتشار')
	created = models.DateTimeField(auto_now_add = True)
	updated = models.DateTimeField(auto_now = True)
	status = models.BooleanField(default = False, verbose_name = "وضعیت")


	

	class Meta:
		verbose_name = "مقاله"
		verbose_name_plural = "مقاله ها"

	def __str__(self):
		return self.title

   
