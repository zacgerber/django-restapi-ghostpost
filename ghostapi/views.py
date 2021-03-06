from django.shortcuts import render

from rest_framework import status, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from ghostapi.serializers import RoastBoastSerializer
from ghostapi.models import RoastBoastModel

class RoastBoastViewSets(viewsets.ModelViewSet):
    queryset = RoastBoastModel.objects.all()
    serializer_class = RoastBoastSerializer

    @action(detail=False)
    def BoastViewSets(self, request, pk=None):
        boast = RoastBoastModel.objects.filter(choices=True).order_by('-post_date')
        serializer = self.get_serializer(boast, many=True)
        return Response(serializer.data)


    @action(detail=False)
    def RoastViewSets(self, request, pk=None):
        roast = RoastBoastModel.objects.filter(choices=False).order_by('-post_date')
        serializer = self.get_serializer(roast, many=True)
        return Response(serializer.data)


    @action(detail=True, methods=['post'])
    def upvote(self, request, pk=None):
        post = self.get_object()
        post.upvote = post.upvote + 1
        post.total_vote = post.total_vote + 1
        post.save()
        return Response({'status': 'upvote added'})


    @action(detail=True, methods=['post'])
    def downvote(self, request, pk=None):
        post = self.get_object()
        post.downvote = post.downvote - 1
        post.total_vote = post.total_vote - 1
        post.save()
        return Response({'status': 'downvote added'})

    @action(detail=False)
    def TotalVoteViewSet(self, request):
        boast = RoastBoastModel.objects.order_by('total_vote')
        serializer = self.get_serializer(boast, many=True)
        return Response(serializer.data)


            
# class RoastViewSets(viewsets.ModelViewSet):
#     queryset = RoastBoastModel.objects.filter(choices=False).order_by('post_date')
#     serializer_class = RoastBoastSerializer

