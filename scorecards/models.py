from django.db import models
from users.models import Profile
from courses.models import Course, Hole, Round

class Scorecard(models.Model):
    # ScorecardLinkId(will this be necessary?)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    users = models.ManyToManyField(Profile)
    num_players = models.IntegerField()

    date = models.DateTimeField()

    def get_total_score(self):
        raise NotImplementedError

    def get_players(self):
        raise NotImplementedError

    def get_total_holes_played(self):
        raise NotImplementedError

    def get_aces(self):
        raise NotImplementedError

    def get_birdies(self):
        raise NotImplementedError

    def get_pars(self):
        raise NotImplementedError

    def get_boogies(self):
        raise NotImplementedError

    def get_score_equal(self, score):
        # Get scores in scorecard equal to score
        raise NotImplementedError

class Score(models.Model):
    scorecard = models.ForeignKey(Scorecard, on_delete=models.CASCADE)
    score = models.PositiveIntegerField()
    hole = models.ForeignKey(Hole, on_delete=models.CASCADE)