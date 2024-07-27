from django.contrib import admin
from .models import Services, Commentaires, Publicites, Publications, Reactions, Likes

# Register your models here.

class ServicesAdmin(admin.ModelAdmin):
    list_display = ('id', 'titre', 'logo', 'img')

class CommentairesAdmin(admin.ModelAdmin):
    list_display = ('id', 'commentaire', 'nom_complet', 'email')

class PublicitesAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'img', 'description')

class PublicationsAdmin(admin.ModelAdmin):
    list_display = ('id', 'img', 'designation', 'date_pub')

class ReactionsAdmin(admin.ModelAdmin):
    list_display = ('id', 'commentaire', 'user', 'date_rea', 'publication')

class LikesAdmin(admin.ModelAdmin):
    list_display = ('id', 'like', 'date_like', 'user', 'publication')

admin.site.register(Services, ServicesAdmin)
admin.site.register(Commentaires, CommentairesAdmin)
admin.site.register(Publicites, PublicitesAdmin)
admin.site.register(Publications, PublicationsAdmin)
admin.site.register(Reactions, ReactionsAdmin)
admin.site.register(Likes, LikesAdmin)

