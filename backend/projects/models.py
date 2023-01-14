from django.conf import settings
from django.db import models
from core.models import TimeStampedModel
from users.models import CustomUser


class Project(TimeStampedModel):
    title = models.CharField(
        verbose_name='タイトル',
        max_length=255
    )
    slug = models.SlugField(
        max_length=255, 
        unique=True
    )
    deadline = models.TimeField(
        verbose_name="期限",
        blank=True
    )
    description = models.TextField(
        verbose_name='備考',
        default='',
        blank=True,
    )
    responsible = models.ForeignKey( 
        settings.AUTH_USER_MODEL,
        verbose_name='担当者', 
        on_delete=models.SET_NULL, 
        null=True, 
        related_name="project"
    )
    members = models.ManyToManyField(
        CustomUser, 
        verbose_name='メンバー',
        blank=True, 
        related_name="members"
    )

    def __str__(self):
        return self.title