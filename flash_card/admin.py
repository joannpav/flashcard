from django.contrib import admin
from flash_card.models import Question, Quiz


class QuestionAdmin(admin.ModelAdmin):
    list_display = ('question','answer',)

admin.site.register(Question)


class QuizAdmin(admin.ModelAdmin):
    list_display = ('quizName', 'question')

admin.site.register(Quiz)
