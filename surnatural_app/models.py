from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Services(models.Model):
    titre = models.CharField(max_length=20, unique=True)
    description = models.TextField(max_length=300)
    logo = models.ImageField(upload_to='img', null=True)
    img = models.ImageField(upload_to='img', null=True)

    class Meta():
        db_table = 'Services'
 
    def __str__(self):
        return self.titre
  
class Commentaires(models.Model):
    nom_complet = models.CharField(max_length=50)
    email = models.EmailField()
    commentaire = models.TextField(max_length=400)
    date = models.DateTimeField(auto_now=True, null=True)

    class Meta():
        db_table = 'Commentaires'

    def __str__(self):
        return self.commentaire
    
class Publicites(models.Model):
    img = models.ImageField(upload_to='img')
    title = models.CharField(max_length=50)
    description = models.TextField(max_length=300)

    def __str__(self):
        return self.title

    class Meta():
        db_table = 'Publicites'

class Publications(models.Model):
    img = models.ImageField(upload_to='img')
    designation = models.CharField(max_length=50)
    date_pub = models.DateField(auto_now=True)
    user = models.ManyToManyField(User, through='Reactions')

    class Meta():
        db_table = 'Publications'
    
    def __str__(self):
        return self.designation

class Reactions(models.Model):
    commentaire = models.TextField(max_length=500, null=True)
    date_rea = models.DateField(auto_now=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    publication = models.ForeignKey(Publications, on_delete=models.CASCADE)

    class Meta():
        db_table = 'Reaction'
    
    def __str__(self):
        return self.commentaire

class Likes(models.Model):
    like = models.BooleanField(default=False)
    date_like = models.DateField(auto_now=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    publication = models.ForeignKey(Publications, on_delete=models.CASCADE)

    class Meta():
        db_table = 'Likes'
    
    def __str__(self):
        return self.like
