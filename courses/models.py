from django.db import models

class Course(models.Model):
    name = models.CharField(max_length=255, default="COURSE NAME")
    location = models.CharField(max_length=255)
    num_of_holes = models.PositiveIntegerField()
    sun_hours = models.PositiveIntegerField()

class Hole(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    number = models.PositiveIntegerField(null=True, blank=True)
    par = models.PositiveIntegerField()

class Round(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    total_par = models.PositiveIntegerField()
    num_of_holes = models.PositiveIntegerField()
    highscore = models.PositiveIntegerField()
    holes = models.ManyToManyField(Hole)

    # Custom save
    def save(self, *args, **kwargs):
        # TODO: Implement automatic calculation of total_par, num_of_holes
        super(Round, self).save()

    def update_highscore(self):
        raise NotImplementedError