from django.contrib import admin
from .models import Category, Questions
# Register your models here.


@admin.register(Category)
class Categoryadmin(admin.ModelAdmin):
    list_display = ['category_text', 'create_time', ]
    list_filter = ['create_time', ]


@admin.register(Questions)
class Questionsadmin(admin.ModelAdmin):
    list_display = ['question_text', 'category', 'votes', ]
    list_filter = ['category', 'votes', ]

    actions = ['votes_initialize', ]

    @admin.action(description="투표수 초기화")
    def votes_initialize(modeladmin, request, queryset): queryset.update(votes=0)
