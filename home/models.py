from django.db import models


class LeagueTeam(models.Model):
    name = models.CharField(max_length=50)
    points = models.IntegerField(default=0)
    matches_played = models.IntegerField(default=0)
    win = models.IntegerField(default=0)
    lost = models.IntegerField(default=0)
    draw = models.IntegerField(default=0)
    goal_scored = models.IntegerField(default=0)
    goal_recieved = models.IntegerField(default=0)
    logo_url =models.URLField(max_length=200)


    class Meta:
        ordering = ('-points',)

    def __str__(self):
        return self.name



class Player(models.Model):
    full_name = models.CharField(max_length=50)
    position = models.CharField(max_length=50)
    image_url = models.URLField(max_length=200)

    def __str__(self):
        return self.full_name


class Squad(models.Model):
    image_url = models.URLField(max_length=200)
    role = models.CharField(max_length=50)
    full_name = models.CharField(max_length=50)
    rank = models.IntegerField()


    class Meta:
        ordering = ('rank',)

    def __str__(self):
        return self.role

class News(models.Model):
    image_url = models.URLField(max_length=200)
    title = models.CharField(max_length=250)
    date_added = models.DateTimeField(auto_now_add=True)
    text = models.TextField()


    class Meta:
        ordering = ('-date_added',)
        verbose_name = 'News'
        verbose_name_plural = 'News'


    def __str__(self):
        return self.title
    

# Create your models here.
class Match(models.Model):
    match_number = models.IntegerField()
    host_team = models.CharField(max_length=250)
    host_team_logo_url = models.URLField(max_length=200, null=True, blank=True)
    host_team_score = models.IntegerField(default=0)
    guest_team_score = models.IntegerField(default=0)
    guest_team = models.CharField(max_length=250)
    guest_team_logo_url = models.URLField(max_length=200, null=True, blank=True)
    stadium = models.CharField(max_length=250, default='Oq-Tepa Stadium')
    date = models.DateTimeField(auto_now_add=False)
    previous_match = models.BooleanField(default=True)

    class Meta:
        ordering = ('-match_number',)


    def __str__(self):
        return f'Match {self.match_number} between {self.host_team} and {self.guest_team}'