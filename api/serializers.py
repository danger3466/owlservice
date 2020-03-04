from django.utils import timezone
from rest_framework import serializers
from api.models import Model, Ticket, Comment


class CommentSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Comment
        fields = '__all__'


class ModelSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Model
        fields = ('id', 'model_name', 'user')


class TicketSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    date_create = serializers.ReadOnlyField()
    date_update = serializers.HiddenField(default=timezone.now)

    model_name = serializers.SerializerMethodField()

    def get_model_name(self, obj):
        model = obj.model
        if model:
            return str(model.model_name)
        return None

    status_name = serializers.SerializerMethodField()

    def get_status_name(self, obj):
        status = obj.status
        if status:
            return str(status.status_name)
        return None

    class Meta:
        model = Ticket
        fields = '__all__'
