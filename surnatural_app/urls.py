from django.urls import path
from .views import service, all_comment, delete_user, work, gst_user, comment, like, gst_service, dashboard, gst_publication, gst_comm, gst_publicite, form_service, form_publication, delete_comm, form_publicite, delete_service, delete_publication, delete_pub

urlpatterns = [
    path('service<int:id>', service, name='services'),
    path('nos_oeuvres', work, name='work'),
    path('all_comments', all_comment, name='all_comment'),
    path('Commentaire<int:id>', comment, name='commentaires'),
    path('like<int:id>', like),
    path('private_page/dashboard', dashboard, name='dashboard'),
    path('private_page/dashboard/gestion_service', gst_service, name='gst_service'),
    path('private_page/dashboard/gestion_service/ajout', form_service, name='form_service'),
    path('private_page/dashboard/gestion_service/delete<int:id>', delete_service, name='delete_service'),
    path('private_page/dashboard/gestion_publication', gst_publication, name='gst_publication'),
    path('private_page/dashboard/gestion_publication/ajout', form_publication, name='form_publication'),
    path('private_page/dashboard/gestion_publication/delete<int:id>', delete_publication, name='delete_publication'),
    path('private_page/dashboard/gestion_commentaire', gst_comm, name='gst_commentaire'),
    path('private_page/dashboard/gestion_commentaire/delete<int:id>', delete_comm, name='delete_commentaire'),
    path('private_page/dashboard/gestion_pubs', gst_publicite, name='gst_publicites'),
    path('private_page/dashboard/gestion_pubs/ajout', form_publicite, name='form_pubs'),
    path('private_page/dashboard/gestion_pubs/delete<int:id>', delete_pub, name='delete_pubs'),
    path('private_page/dashboard/gestion_users', gst_user, name='gst_users'),
    path('private_page/dashboard/gestion_users/delete<int:id>', delete_user, name='delete_users'),
]

