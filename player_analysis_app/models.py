from django.db import models
class Team(models.Model):
    name = models.CharField(max_length=100, unique=True)
    city = models.CharField(max_length=50, unique=True)
    abbreviation = models.CharField(max_length=4, unique=True)
    established = models.IntegerField()

    def __str__(self):
        return f"{self.city} {self.name}"

class Player(models.Model):
    name = models.CharField(max_length=100, unique=False)
    age = models.IntegerField()
    jersey_number = models.CharField(max_length=3)
    college = models.CharField(max_length=100, blank=True, null=True) #college is optional
    birth_date = models.DateField()
    height = models.CharField(max_length=10)
    weight = models.IntegerField(help_text="Weight (in pounds)")
    position = models.CharField(max_length=10)
    team = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='players') #cascase: if a team is deleted, so are all the players

    def __str__(self):
        return f"{self.name} - {self.position} for {self.team.name}"