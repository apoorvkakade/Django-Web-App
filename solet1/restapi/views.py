from rest_framework import viewsets

from .serializers import *
from .models import Metric


class MetricViewSet(viewsets.ModelViewSet):
    queryset = Metric.objects.all().order_by('title')
    serializer_class = MetricSerializer


class PromptViewSet(viewsets.ModelViewSet):
    queryset = Prompt.objects.all().order_by('title')
    serializer_class = PromptSerializer


class RubricViewSet(viewsets.ModelViewSet):
    queryset = Rubric.objects.all().order_by('title')
    serializer_class = RubricSerializer


class SkillViewSet(viewsets.ModelViewSet):
    queryset = Skill.objects.all().order_by('title')
    serializer_class = SkillSerializer


class MentorTextViewSet(viewsets.ModelViewSet):
    queryset = MentorText.objects.all().order_by('createdOn')
    serializer_class = MentorTextSerializer
