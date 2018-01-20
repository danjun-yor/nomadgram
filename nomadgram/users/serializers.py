from rest_framework import serializers
from . import models
from nomadgram.images import serializers as image_serializers

class UserProfileSerializer(serializers.ModelSerializer):
  
  images = image_serializers.UserProfileImageSerializer(many=True)
  
  class Meta:
    model = models.User
    fields = (
      'id',
      'username',
      'name',
      'bio',
      'website',
      'post_count',
      'followers_count',
      'followings_count',
      'images'
    )

class ExploreUserSerializer(serializers.ModelSerializer):

  class Meta:
    model = models.User
    fields = (
      'id',
      'profile_image',
      'username',
      'name'
    )