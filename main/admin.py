from django.contrib import admin
from .models import *
# Register your models here.

admin.site.register(LogicQuiz)

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['name','surname','unique_field',"ways"]


class AnswerAdmin(admin.TabularInline):
    model = Answer

@admin.register(Results)
class UserAdmin(admin.ModelAdmin):
    list_display = ['user','quiz','user_answer','logic_quiz','logic_answer']
    readonly_fields =  ['user','quiz','user_answer']



@admin.register(Quiz)
class QuizzesAdmin(admin.ModelAdmin):
    list_display = ['title']
    inlines = [AnswerAdmin]


@admin.register(Ways)
class WaysAdmin(admin.ModelAdmin):
    list_display = ['name','slug']
    prepopulated_fields = {'slug':('name',)}