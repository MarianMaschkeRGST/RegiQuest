from rest_framework import serializers

from projects.models import Project


class ProjectSerializer(serializers.ModelSerializer):
    responsible = serializers.StringRelatedField()
    created_at = serializers.SerializerMethodField()
    slug = serializers.SlugField(read_only=True)
    task_count = serializers.SerializerMethodField()


    class Meta:
        model = Project
        exclude = ["updated_at"]

    def get_created_at(slef, instance):
        return instance.created_at.strftime("%B %d, %Y")

    def get_task_count(self, instance):
        return instance.task.count()

    def get_user_has_task(self, instance):
        request = self.context.get("request")
        return instance.task.filter(responsible=request.user).exists()