import uuid as uuid_lib

from django.conf import settings
from django.db import models

from core.models import TimeStampedModel
from projects.models import Project


class Task(TimeStampedModel):

    #Task Type Choices
    TASK_UNSET = 'UNSET'
    TASK_COMMUNITY = 'COMMUNITY'
    TASK_DIRECTION = 'DIRECTION'
    TASK_DESIGN = 'DESIGN'
    TASK_DTP = 'DTP'
    TASK_CODING = 'CODING'
    TASK_WEB = 'WEB'
    TASK_SUPPORT = 'SUPPORT'
    TASK_INTERNAL = 'INTERNAL'
    TASK_OTHER = 'OTHER'
    TASK_TYPE_CHOICES = [
        (TASK_UNSET, '---'),
        (TASK_COMMUNITY, 'まちづくり'),
        (TASK_DIRECTION, 'ダイレクション'),
        (TASK_DESIGN, 'デザイン'),
        (TASK_DTP, 'DTP'),
        (TASK_CODING, 'コーディング'),
        (TASK_WEB, 'WEB制作'),
        (TASK_SUPPORT, '月々サポート'),
        (TASK_INTERNAL, '社内'),
        (TASK_OTHER, '他'),
    ]

    #Task Status Choices
    STATUS_NOT_STARTED = 'NOT_STARTED'
    STATUS_IN_PROGRESS = 'IN_PROGRESS'
    STATUS_COMPLETE = 'COMPLETE'
    STATUS_WAIT_EXTERNAL = 'WAIT_EXTERNAL'
    STATUS_WAIT_INTERNAL = 'WAIT_INTERNAL'
    STATUS_ON_HOLD = 'ON_HOLD'
    STATUS_CANCEL = 'CANCEL'
    STATUS_FAIL = 'FAIL'
    STATUS_TYPE_CHOICES = [
        (STATUS_NOT_STARTED, '未開始'),
        (STATUS_IN_PROGRESS, '作業中'),
        (STATUS_COMPLETE, '完了'),
        (STATUS_WAIT_EXTERNAL, '社外対応待ち'),
        (STATUS_WAIT_INTERNAL, '社内対応待ち'),
        (STATUS_ON_HOLD, '一時停止'),
        (STATUS_CANCEL, '中止'),
        (STATUS_FAIL, '失敗'),
    ]


    uuid = models.UUIDField(
        db_index=True, 
        default=uuid_lib.uuid4, 
        editable=False
    )
    title = models.CharField(
        verbose_name='タイトル',
        max_length=255
    )
    slug = models.SlugField(
        max_length=255, 
        unique=True
    )
    task_type = models.CharField(
        verbose_name="タスク種",
        max_length=64,
        choices=TASK_TYPE_CHOICES,
        default=TASK_UNSET,
    )
    content = models.TextField(
        verbose_name='備考',
        default='',
        blank=True,
    )
    task_status = models.CharField(
        verbose_name="ステタス",
        max_length=64,
        choices=STATUS_TYPE_CHOICES,
        default=STATUS_NOT_STARTED,
    )
    deadline = models.DateTimeField(
        verbose_name="期限",
        blank=True
    )
    project = models.ForeignKey(
        Project, 
        verbose_name='関連プロジェクト',
        on_delete=models.CASCADE, 
        related_name="task", 
        blank=True, 
        null=True
    )
    responsible = models.ForeignKey( 
        settings.AUTH_USER_MODEL,
        verbose_name='担当者', 
        on_delete=models.CASCADE, 
        related_name="responsible"
    )
    voters = models.ManyToManyField(
        settings.AUTH_USER_MODEL, 
        related_name="likes"
    )

    def __str__(self):
        return self.title