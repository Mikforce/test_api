
from rest_framework import serializers
from .models import Mailing, Client, Message

class MailingSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Mailing
        fields = "__all__"

class ClientSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Client
        fields = "__all__"

class MessageSerializer(serializers.HyperlinkedModelSerializer):
            class Meta:
                model = Message
                fields = "__all__"
