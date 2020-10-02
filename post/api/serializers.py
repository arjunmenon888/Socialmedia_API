from rest_framework import serializers
from post.models import Post


class PostSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)    
    content = serializers.CharField(required=False, allow_blank=True, max_length=240)
    image = serializers.ImageField(max_length=None, allow_empty_file=False, use_url='images/')
    image1 = serializers.ImageField(max_length=None, allow_empty_file=False, use_url='images/')
    timestamp = serializers.DateTimeField()
    tag = serializers.CharField(required=False, allow_blank=True, max_length=1)
    def create(self, validated_data):
        return Post.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.content = validated_data.get('title', instance.title)
        instance.image = validated_data.get('image', instance.image)
        instance.image1 = validated_data.get('image1', instance.image1)
        instance.timestamp = validated_data.get('timestamp', instance.timestamp)
        
        instance.save() 
        return instance
