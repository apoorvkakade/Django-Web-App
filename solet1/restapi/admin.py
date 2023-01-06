from django.contrib import admin
from .models import *

admin.site.register(Metric)
admin.site.register(Skill)
admin.site.register(MentorText)
admin.site.register(Prompt)
admin.site.register(Rubric)

# Register your models here.
