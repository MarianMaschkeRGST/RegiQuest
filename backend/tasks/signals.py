from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.utils.crypto import get_random_string
from django.utils.text import slugify

from tasks.models import Task

@receiver(pre_save, sender=Task)
def add_slug_to_question(sender, instance, *args, **kwargs):
    if instance and not instance.slug:
        slug = slugify(instance.content)
        random_string = get_random_string(length=8)
        instance.slug = slug + "-" + random_string