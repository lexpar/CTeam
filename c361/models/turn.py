import uuid
from django.db import models
from c361.models.game_instance import GameInstanceModel
from jsonfield import JSONField

class TurnModel(models.Model):

    uuid = models.UUIDField(default=uuid.uuid4, unique=True)
    game = models.ForeignKey(GameInstanceModel, on_delete=models.CASCADE, related_name='turns')
    number = models.IntegerField(default=0)
    delta_dump = JSONField()
    diff = JSONField(default={})

    class Meta:
        ordering = ['number']