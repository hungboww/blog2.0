from rest_framework import serializers
from .models import *


class BlogSerializer(serializers.ModelSerializer):
    author_id = serializers.SerializerMethodField()
    category_id = serializers.SerializerMethodField()
    author_name = serializers.SerializerMethodField()
    rank = serializers.SerializerMethodField()
    category_name = serializers.SerializerMethodField()

    class Meta:
        model = BlogModel
        fields = ['id', 'author_id', 'author_name', 'category_id', 'rank', 'category_name', 'title', 'content', 'slug',
                  'image', 'source', 'view_count', 'time_post', 'time_update', 'description','featured']

    def get_author_id(self, obj):
        return obj.author_id

    def get_author_name(self, obj):
        return obj.author.user_name

    def get_rank(self, obj):
        return obj.author.rank

    def get_category_id(self, obj):
        return obj.category_id

    def get_category_name(self, obj):
        return obj.category.name


class BlogDetailSerializer(serializers.ModelSerializer):
    author_id = serializers.SerializerMethodField()
    category_id = serializers.SerializerMethodField()
    author_name = serializers.SerializerMethodField()
    rank = serializers.SerializerMethodField()
    category_name = serializers.SerializerMethodField()
    upvote = serializers.SerializerMethodField()

    class Meta:
        model = BlogModel
        fields = ['id', 'author_id', 'author_name', 'category_id', 'rank', 'category_name', 'title', 'content', 'slug',
                  'image', 'source', 'view_count', 'time_post', 'time_update', 'upvote', 'description','featured']

    def get_author_id(self, obj):
        return obj.author_id

    def get_author_name(self, obj):
        return obj.author.user_name

    def get_rank(self, obj):
        return obj.author.rank

    def get_category_id(self, obj):
        return obj.category_id

    def get_category_name(self, obj):
        return obj.category.name

    def get_upvote(self, obj):
        upvote_list = obj.blog.all()
        counter = 0
        for upvote in upvote_list:
            counter += upvote.value
        return counter


class UpvoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = UpvoteModel
        fields = ('id', 'author', 'blog', 'series', 'value')