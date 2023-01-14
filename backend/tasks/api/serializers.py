from rest_framework import serializers

from tasks.models import Task


class TaskSerializer(serializers.ModelSerializer):
    title = serializers.StringRelatedField()
    responsible = serializers.StringRelatedField()
    created_at = serializers.SerializerMethodField()
    slug = serializers.SlugField(read_only=True)
    # subtask_count = serializers.SerializerMethodField()
    

    class Meta:
        model = Task
        exclude = ["updated_at"]

    def get_created_at(slef, instance):
        return instance.created_at.strftime("%B %d, %Y")

    # def get_subtask_count(self, instance):
    #     return instance.task.count()