from django.db import models
from django.conf import settings
from django.urls import reverse


# Content Table
class Content(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    type = models.CharField(max_length=200, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('content_detail', kwargs={'pk': self.pk})


# Resource Table
class Resource(models.Model):
    name = models.CharField(max_length=150)
    description = models.TextField()
    resource_url = models.URLField()
    video = models.FileField(upload_to='videos/')  # Removed default, as FileField doesn't support default string

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('resource_detail', kwargs={'pk': self.pk})


# Event Table
class Event(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    location = models.CharField(max_length=255)
    date = models.DateTimeField()
    organizer = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)  # Using the auth user model

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('event_detail', kwargs={'pk': self.pk})


# Feedback Table
class Feedback(models.Model):
    resource = models.ForeignKey(Resource, on_delete=models.CASCADE, related_name="feedbacks")
    rating = models.IntegerField(choices=[(i, i) for i in range(1, 6)])  # Rating from 1 to 5
    comments = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)  # Added user reference

    def __str__(self):
        return f"Feedback by {self.user} - Rating: {self.rating}"

    def get_absolute_url(self):
        return reverse('feedback_detail', kwargs={'pk': self.pk})  # Corrected URL reference
