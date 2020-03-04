from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from api.serializers import ModelSerializer, TicketSerializer, CommentSerializer
from api.models import Model, Ticket, Comment
from api.permissions import IsOwner
from django.contrib.auth import get_user_model
User = get_user_model()


class CommentViewSet(viewsets.ModelViewSet):
    serializer_class = CommentSerializer
    permission_classes = (IsAuthenticated, IsOwner)

    def get_queryset(self):
        user = self.request.user
        return Comment.objects.filter(user=user)


class ModelViewSet(viewsets.ModelViewSet):
    serializer_class = ModelSerializer
    permission_classes = (IsAuthenticated, IsOwner)

    def get_queryset(self):
        user = self.request.user
        return Model.objects.filter(user=user)


class TicketViewSet(viewsets.ModelViewSet):
    serializer_class = TicketSerializer
    permission_classes = (IsAuthenticated, IsOwner)

    def get_queryset(self):
        user = self.request.user
        return Ticket.objects.filter(user=user)
