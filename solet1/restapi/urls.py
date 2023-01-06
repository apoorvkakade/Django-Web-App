from django.urls import include, path
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'metrics', views.MetricViewSet)
router.register(r'prompts', views.PromptViewSet)
router.register(r'rubrics', views.RubricViewSet)
router.register(r'skills', views.SkillViewSet)
router.register(r'mentortexts', views.MentorTextViewSet)


#/metrics/{title}
urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/',include('rest_framework.urls', namespace='rest_framework'))
]