from django.core.validators import MinValueValidator, MaxValueValidator
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

class Stat(models.Model):
    player = models.ForeignKey(Player, on_delete=models.CASCADE, related_name='stats')
    games_played = models.IntegerField()
    wins = models.IntegerField()
    losses = models.IntegerField()
    mpg = models.DecimalField(max_digits=5, decimal_places=2, help_text="Minutes per game")
    pts = models.DecimalField(max_digits=5, decimal_places=2, help_text="Points per game")
    fgm = models.IntegerField(help_text="Field Goals Made")
    fga = models.IntegerField(help_text="Field Goals Attempted")
    fg_pct = models.DecimalField(max_digits=5, decimal_places=2, validators=[MinValueValidator(0), MaxValueValidator(100)], help_text="Field Goal Percentage")
    threepm = models.IntegerField(help_text="3 Points Made")
    threepa = models.IntegerField(help_text="3 Points Attempted")
    three_pct = models.DecimalField(max_digits=5, decimal_places=2, validators=[MinValueValidator(0), MaxValueValidator(100)], help_text="3 Point Percentage")
    ftm = models.IntegerField(help_text="Free Throws Made")
    fta = models.IntegerField(help_text="Free Throws Attempted")
    ft_pct = models.DecimalField(max_digits=5, decimal_places=2, validators=[MinValueValidator(0), MaxValueValidator(100)], help_text="Free Throw Percentage")
    oreb = models.IntegerField(help_text="Offensive Rebounds")
    dreb = models.IntegerField(help_text="Defensive Rebounds")
    reb = models.IntegerField(help_text="Total Rebounds")
    ast = models.IntegerField(help_text="Assists")
    tov = models.IntegerField(help_text="Turnovers")
    stl = models.IntegerField(help_text="Steals")
    blk = models.IntegerField(help_text="Blocks")
    pf = models.IntegerField(help_text="Personal Fouls")
    plus_minus = models.IntegerField(help_text="+/-")

    def __str__(self):
        return f"Stats for {self.player.name}"

    class Meta:                            #not too sure about this as of right now
        verbose_name = 'Stat'
        verbose_name_plural = 'Stats'

from django.db import models

# Assuming the Player model and other models are already defined above

class Accolade(models.Model):
    player = models.ForeignKey(Player, on_delete=models.CASCADE, related_name='accolades')
    title = models.CharField(max_length=255)
    year = models.IntegerField(help_text="The year the accolade was awarded.")
    details = models.TextField(blank=True, null=True, help_text="Additional details about the accolade.")

    def __str__(self):
        return f"{self.title} ({self.year}) - {self.player.name}"