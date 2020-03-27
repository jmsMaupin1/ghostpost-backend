from django.shortcuts import render

from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from api.models import GhostPost
from api.serializers import GhostPostSerializer

# Create your views here.
class GhostPostViewSet(viewsets.ModelViewSet):
    queryset = GhostPost.objects.all()
    serializer_class = GhostPostSerializer

    @action(detail=True, methods=['get'])
    def upvote(self, request, pk=None):
        try:
            post = GhostPost.objects.get(pk=pk)
            post.upvotes += 1
            post.save()

            return Response({'status': 'upvoted'})
        except Exception as e:
            return Response({'status': '', 'err': e})
    
    @action(detail=True, methods=['get'])
    def downvote(self, request, pk=None):
        try:
            post = GhostPost.objects.get(pk=pk)
            post.downvotes += 1
            post.save()

            return Response({'status': 'downvoted'})
        except Exception as e:
            return Response({'status': '', 'err': e})    
    
    @action(detail=True, methods=['delete'])
    def remove(detail=True, request, pk=None)
        try:
            GhostPost.objects.filter(secret_id=pk).delete()
        except Exception as e:
            return Response({'status': '', 'err': e})
        
        return Response({'status', 'deleted'})