from django.db import models
import os
from django_mysql.models import JSONField
# Create your models here.
from players.models import Player



class RawData(models.Model):
    raw_data = JSONField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Phases(models.Model):
    key = models.CharField(max_length=100)
    desc = models.CharField(max_length=200)
    evkey = models.CharField(max_length=100)
    phase_type = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.desc

class Table(models.Model):
    key = models.CharField(max_length=100)
    desc = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.desc


class Competition(models.Model):
    champ = models.CharField(primary_key=True,max_length=100)
    description = models.TextField(max_length=1000)
    location = models.TextField(max_length=1000)
    isfinished = models.BooleanField()
    url = models.URLField(max_length=1000)
    compdates = models.TextField(max_length=1000)
    raw_comp = models.ForeignKey(RawData,related_name="competition_rawdata",on_delete=models.PROTECT,blank=True,null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.champ


class MatchRawData(models.Model):
    url = models.URLField(max_length=1000)
    json_data = JSONField()
    comp = models.ForeignKey(Competition,related_name="competition",on_delete=models.PROTECT)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def Competition_id(self):
        try:
            return self.comp.champ
        except Exception as e:
            return "Error:%s" % str(e)


class Player(models.Model):
    player_id = models.CharField(primary_key=True,max_length=200)
    name = models.OneToOneField(Player,related_name='player',on_delete=models.PROTECT)




# class Match(models.Model):
#     comp = models.ForeignKey(Competition,related_name="champ_competition",on_delete=models.PROTECT)
#     home = models.ForeignKey(Player,related_name="home",on_delete=models.PROTECT,blank=True,null=True)
#     away = models.ForeignKey(Player,related_name="away",on_delete=models.PROTECT,blank=True,null=True)
#     team_home = models.ForeignKey(Team,related_name="teams_home",on_delete=models.PROTECT,blank=True,null=True)
#     team_away = models.ForeignKey(Team,related_name="teams_away",on_delete=models.PROTECT,blank=True,null=True)
#     match = models.CharField(max_length=200)
#     time = models.CharField(max_length=100)
#     venue = models.CharField(max_length=250)
#     phase = models.ForeignKey(Phases,related_name='match_phase',on_delete=models.PROTECT)
#     table = models.ForeignKey(Table,related_name="loc",on_delete=models.PROTECT)
#     status = models.IntegerField()
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)


#     def delete(self,*args,**kwargs):
#         fix = DeletedFixture(fixture = self)
#         fix.save()
#         super().delete(*args,**kwargs)


#     def comp_id(self):
#         try:
#             return self.comp.champ
#         except Exception as e:
#             return "Error:%s" % str(e)

#     def home_player(self):
#         try:
#             return self.home.name
#         except Exception as e:
#             return "NA"

#     def away_player(self):
#         try:
#             return self.away.name
#         except Exception as e:
#             return "NA"

#     def away_team(self):
#         if self.team_away:
#             p1 = self.team_away.player1.name
#             p2 = self.team_away.player2.name
#             return (p1+"/"+p2)
#         else:
#             return "NA"

#     def table_(self):
#         return self.table.desc
    
#     def home_team(self):
#         if self.team_home:
#             p1 = self.team_home.player1.name
#             p2 = self.team_home.player2.name
#             return (p1+"/"+p2)
#         else:
#             return "NA"

    
#     def phase_(self):
#         try:
#             return self.phase.desc
#         except Exception as e:
#             return "Error:%s" % str(e)

