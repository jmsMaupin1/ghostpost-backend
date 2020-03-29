from django.shortcuts import render
from django.core import serializers
from django.forms import model_to_dict

from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from api.models import GhostPost
from api.serializers import GhostPostSerializer

# Create your views here.
class GhostPostViewSet(viewsets.ModelViewSet):
    queryset = GhostPost.objects.all()
    serializer_class = GhostPostSerializer

    def create(self, request):
        post = GhostPost.objects.create(
            isBoast=request.data['isBoast'],
            content=request.data['content']
        )
        serialized_post = model_to_dict(post)
        return Response(serialized_post)

    @action(detail=True, methods=['get'])
    def upvote(self, request, pk=None):
        try:
            post = GhostPost.objects.get(pk=pk)
            post.upvotes += 1
            post.save()

            return Response(model_to_dict(post))
        except Exception as e:
            return Response({'status': '', 'err': e})
    
    @action(detail=True, methods=['get'])
    def downvote(self, request, pk=None):
        try:
            post = GhostPost.objects.get(pk=pk)
            post.downvotes += 1
            post.save()

            return Response(model_to_dict(post))
        except Exception as e:
            return Response({'status': '', 'err': e})    
    
    @action(detail=True, methods=['delete'])
    def remove(self, request, pk=None):
        try:
            GhostPost.objects.filter(secret_id=pk).delete()
        except Exception as e:
            return Response({'status': '', 'err': e})
        
        return Response({'status', 'deleted'})