from rest_framework.serializers import ModelSerializer, StringRelatedField
from ghostapi.models import RoastBoastModel


class RoastBoastSerializer(ModelSerializer):
    class Meta:
        model = RoastBoastModel
        fields = [
            'body',
            'choices',
            'upvote',
            'downvote',
            'total_vote',
            'post_date',
        ]