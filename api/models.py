from django.db import models
from django.contrib.auth import get_user_model
User = get_user_model()


class Models(models.Model):
    id = models.AutoField(db_column='model_id', primary_key=True)
    model_name = models.CharField(max_length=64)
    #model_author = models.ForeignKey('Users', models.DO_NOTHING, db_column='model_author')
    model_photo = models.CharField(max_length=255, blank=True, null=True)
    model_url = models.CharField(max_length=256, blank=True, null=True)

    def __str__(self):
        return self.model_name

    class Meta:
        managed = False
        db_table = 'models'


class Status(models.Model):
    id = models.AutoField(db_column='status_id', primary_key=True)
    status_name = models.CharField(max_length=24)
    status_style = models.CharField(max_length=8)
    status_icon = models.CharField(max_length=16)

    def __str__(self):
        return self.status_name

    class Meta:
        managed = False
        db_table = 'status'


class Tickets(models.Model):
    id = models.AutoField(db_column='ticket_id', primary_key=True)
    user = models.ForeignKey(User, db_column='user_id', on_delete=models.CASCADE)
    model = models.ForeignKey(Models, db_column='model_id', on_delete=models.CASCADE)
    client_name = models.CharField(max_length=48)
    client_phone = models.CharField(max_length=18, blank=True, null=True)
    imei = models.BigIntegerField(blank=True, null=True)
    status = models.ForeignKey(Status, on_delete=models.CASCADE)
    date_create = models.DateTimeField()
    date_update = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tickets'


#class Comments(models.Model):
#    comment_id = models.AutoField(primary_key=True)
#    ticket = models.ForeignKey('Tickets', models.DO_NOTHING)
#    user = models.ForeignKey('Users', models.DO_NOTHING)
#    comment = models.CharField(max_length=254)
#    date_create = models.DateTimeField()

#    class Meta:
#        managed = False
#        db_table = 'comments'
