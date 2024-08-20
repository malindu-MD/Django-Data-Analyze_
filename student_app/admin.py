from django.contrib import admin

# Register your models here.


from . models import School,Student,Subject,Answer,Award,AssessmentArea,Class,Summary

admin.site.register(Student)
admin.site.register(School)
admin.site.register(Class)
admin.site.register(AssessmentArea)
admin.site.register(Award)
admin.site.register(Subject)
admin.site.register(Answer)
admin.site.register(Summary)

