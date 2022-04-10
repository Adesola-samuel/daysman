from django.contrib import admin
from .models import Session, Term, Subject, Score, Level, StudentTermlyProfile, Clas, StudentProgress

class ScoreAdmin(admin.ModelAdmin):
    list_display = ('level','subject','student','first_test', 'second_test', 'third_test', 'examination','total_score')
    fieldsets = [('Score', {'fields':(('level','subject'),'student',('first_test', 'second_test', 'third_test', 'examination'),)}),
]

class SubjectAdmin(admin.ModelAdmin):
    list_display = ('subject',)

admin.site.register(StudentProgress)
admin.site.register(Session)
admin.site.register(Term)
admin.site.register(Subject,SubjectAdmin)
admin.site.register(Score, ScoreAdmin)
admin.site.register(Level)
admin.site.register(StudentTermlyProfile)
admin.site.register(Clas)


