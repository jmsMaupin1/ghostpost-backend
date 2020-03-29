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

            post_dict = model_to_dict(post)

            return Response({
                'id': post_dict['id'],
                'upvotes': post_dict['upvotes'],
                'downvotes': post_dict['downvotes']
            })
        except Exception as e:
            return Response({'status': '', 'err': e})
    
    @action(detail=True, methods=['get'])
    def downvote(self, request, pk=None):
        try:
            post = GhostPost.objects.get(pk=pk)
            post.downvotes += 1
            post.save()

            post_dict = model_to_dict(post)

            return Response({
                'id': post_dict['id'],
                'upvotes': post_dict['upvotes'],
                'downvotes': post_dict['downvotes']
            })
        except Exception as e:
            return Response({'status': '', 'err': e})    
    
    @action(detail=True, methods=['delete'])
    def remove(self, request, pk=None):
        post_res = None
        try:
            post = GhostPost.objects.get(secret_id=pk)
            post_res = model_to_dict(post)['id']
            post.delete()
        except Exception as e:
            return Response({'error': f"{e}"})
        
        return Response({post_res})