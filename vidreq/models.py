from django.db import models
from django.utils import timezone

class video(models.Model):
	title = models.CharField(max_length=50, null=True)
	body = models.TextField(null=True)
	pub_date = models.DateTimeField(default=timezone.now)


	def __str__(self):
		return ' {}. {}'.format(self.id, self.title)