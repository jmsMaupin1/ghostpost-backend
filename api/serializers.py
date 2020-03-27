from rest_framework import serializers

from api.models import GhostPost

class GhostPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = GhostPost
        fields = [
            'id',
            'isBoast',
            'content',
            'upvotes',
            'downvotes',
            'datetime'
        ]