from rest_framework import serializers
from fb_fetch.models import article


class FB_fetchSerializer(serializers.ModelSerializer):
    class Meta:
        model = article
        fields = '__all__'
        #fields = ('id', 'cid', 'email', 'message' )
