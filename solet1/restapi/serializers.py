from rest_framework import serializers
from .models import *


class MetricSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Metric
        fields = ('title', 'description', 'category')


class PromptSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Prompt
        fields = ('title', 'description', 'category')


class SkillSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Skill
        fields = ('title', 'description')


class RubricSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Rubric
        fields = ('title', 'description', 'category')


class MentorTextSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = MentorText
        fields = ('title', 'description', 'category', 'skill', 'createdOn')
