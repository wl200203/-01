from rest_framework import serializers # type: ignore
from .models import Post
from django.contrib.auth.models import User


class PostSerializer(serializers.ModelSerializer):
    #author = serializers.PrimaryKeyRelatedField(read_only=True)
    author = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())  # 使用用户的ID
    
    class Meta:
        model = Post
        fields = ['id','author', 'title', 'text',  'created_date', 'published_date', 'image']



