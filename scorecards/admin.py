from django.contrib import admin
from .models import Scorecard, Score

# Register your models here.
class ScoreInLine(admin.TabularInline):
    model = Score

class ScorecardAdmin(admin.ModelAdmin):
    inlines = [
        Scorecard,
    ]

admin.site.register(Scorecard)
