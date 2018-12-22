from django.contrib import admin

from .models import Course, Round, Hole

class HoleInLine(admin.TabularInline):
    model = Hole
    fields = ("number", "par",)
    extra = 3

class RoundInLine(admin.TabularInline):
    model = Round
    fields = ("holes",)
    extra = 1

class CourseAdmin(admin.ModelAdmin):

    inlines = [
        RoundInLine,
        HoleInLine,
    ]

admin.site.register(Course, CourseAdmin)
