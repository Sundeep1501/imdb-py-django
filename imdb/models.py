# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models
from django.db import connection

class Namebasics(models.Model):
    nconst = models.CharField(primary_key=True, max_length=255)
    primaryname = models.CharField(db_column='primaryName', max_length=255, blank=True, null=True)  # Field name made lowercase.
    primaryprofession = models.TextField(db_column='primaryProfession', blank=True, null=True)  # Field name made lowercase.
    knownfortitles = models.TextField(db_column='knownForTitles', blank=True, null=True)  # Field name made lowercase.
    birthyear = models.SmallIntegerField(db_column='birthYear', blank=True, null=True)  # Field name made lowercase.
    deathyear = models.SmallIntegerField(db_column='deathYear', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'NameBasics'
    
    def __str__(self):
        return '{} is {}'.format(self.primaryname, self.primaryprofession)

class Titlebasics(models.Model):
    tconst = models.CharField(primary_key=True, max_length=255)
    titletype = models.CharField(db_column='titleType', max_length=255, blank=True, null=True)  # Field name made lowercase.
    primarytitle = models.CharField(db_column='primaryTitle', max_length=255, blank=True, null=True)  # Field name made lowercase.
    originaltitle = models.CharField(db_column='originalTitle', max_length=255, blank=True, null=True)  # Field name made lowercase.
    isadult = models.IntegerField(db_column='isAdult', blank=True, null=True)  # Field name made lowercase.
    runtimeminutes = models.IntegerField(db_column='runtimeMinutes', blank=True, null=True)  # Field name made lowercase.
    geners = models.TextField(blank=True, null=True)
    endyear = models.SmallIntegerField(db_column='endYear', blank=True, null=True)  # Field name made lowercase.
    startyear = models.SmallIntegerField(db_column='startYear', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TitleBasics'


class Titleakas(models.Model):
    titleid = models.ForeignKey(Titlebasics, models.DO_NOTHING, db_column='titleId', blank=True, null=True)  # Field name made lowercase.
    ordering = models.IntegerField(blank=True, null=True)
    region = models.CharField(max_length=255, blank=True, null=True)
    language = models.CharField(max_length=255, blank=True, null=True)
    types = models.TextField(blank=True, null=True)
    attributes = models.TextField(blank=True, null=True)
    isoriginaltitle = models.IntegerField(db_column='isOriginalTitle', blank=True, null=True)  # Field name made lowercase.
    title = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'TitleAkas'


class Titlecrew(models.Model):
    tconst = models.ForeignKey(Titlebasics, models.DO_NOTHING, db_column='tconst', blank=True, null=True)
    directors = models.TextField(blank=True, null=True)
    writers = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'TitleCrew'


class Titleepisode(models.Model):
    tconst = models.ForeignKey(Titlebasics, models.DO_NOTHING, db_column='tconst', related_name='tetconst', blank=True, null=True)
    parenttconst = models.ForeignKey(Titlebasics, models.DO_NOTHING, db_column='parentTconst', related_name='teptconst', blank=True, null=True)  # Field name made lowercase.
    seasonnumber = models.IntegerField(db_column='seasonNumber', blank=True, null=True)  # Field name made lowercase.
    episodenumber = models.IntegerField(db_column='episodeNumber', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TitleEpisode'


class Titleprincipals(models.Model):
    tconst = models.ForeignKey(Titlebasics, models.DO_NOTHING, db_column='tconst', blank=True, null=True)
    ordering = models.IntegerField(blank=True, null=True)
    nconst = models.ForeignKey(Namebasics, models.DO_NOTHING, db_column='nconst', blank=True, null=True)
    category = models.CharField(max_length=255, blank=True, null=True)
    job = models.CharField(max_length=255, blank=True, null=True)
    characters = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'TitlePrincipals'


class Titleratings(models.Model):
    tconst = models.ForeignKey(Titlebasics, models.DO_NOTHING, db_column='tconst', blank=True, null=True)
    numvotes = models.IntegerField(db_column='numVotes', blank=True, null=True)  # Field name made lowercase.
    averagerating = models.DecimalField(db_column='averageRating', max_digits=3, decimal_places=1, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TitleRatings'


class LegacySQLViews():

    def queryA():
        with connection.cursor() as cursor:
            cursor.execute("SELECT * FROM viewA;")
            rows = cursor.fetchall()
        
        return rows

    def queryB():
        with connection.cursor() as cursor:
            cursor.execute("SELECT * FROM viewB;")
            rows = cursor.fetchall()
        
        return rows
    def queryC():
        with connection.cursor() as cursor:
            cursor.execute("SELECT * FROM viewC;")
            rows = cursor.fetchall()
        
        return rows

    def queryD():
        with connection.cursor() as cursor:
            cursor.execute("SELECT * FROM viewD;")
            rows = cursor.fetchall()
        
        return rows

    def queryE():
        with connection.cursor() as cursor:
            cursor.execute("SELECT * FROM viewE;")
            rows = cursor.fetchall()
        
        return rows

    def queryF():
        with connection.cursor() as cursor:
            cursor.execute("SELECT * FROM viewF;")
            rows = cursor.fetchall()
        
        return rows

    def queryG():
        with connection.cursor() as cursor:
            cursor.execute("SELECT * FROM viewG;")
            rows = cursor.fetchall()
        
        return rows

    def queryH():
        with connection.cursor() as cursor:
            cursor.execute("SELECT * FROM Must_Watch_Movies;")
            rows = cursor.fetchall()
        
        return rows

    def queryI(yr):
        with connection.cursor() as cursor:
            cursor.callproc("MoviesForYear",[yr])
            rows = cursor.fetchall()
        
        return rows
