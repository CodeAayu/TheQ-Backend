from django.db import models

class EventData(models.Model):
	event_name = models.CharField(max_length=100,null=False)
	event_cover_image = models.ImageField(upload_to="./media", blank=True, null=True)
	date_start = models.DateTimeField(null = False)
	date_end = models.DateTimeField(null = False)
	description = models.CharField(max_length=2000,null=False)
	event_id = models.AutoField(primary_key=True)
	city = models.CharField(max_length=30)
	genre = models.CharField(max_length=50)


class EventQueue(models.Model):
	event_id = models.IntegerField(primary_key=True)
	start_point = models.IntegerField()
	end_point = models.IntegerField()


class Queue(models.Model):
	event_id = models.IntegerField()
	username = models.CharField(max_length=50)
	token_number = models.IntegerField()

# class UserData(models.Model):
# 	user_name = models.CharField(max_length=100,null=False)
# 	user_profile_image = models.ImageField(upload_to="../media", blank=True, null=True)
# 	user_cover_image = models.ImageField(upload_to="../media", blank=True, null=True)
