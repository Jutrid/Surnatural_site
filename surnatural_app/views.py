from django.shortcuts import render, redirect
from .models import Services, Commentaires, Publicites, Publications, Reactions, Likes
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
import os
from surnatural_site import settings

# Create your views here.

def index(request):
    data = Services.objects.all()
    data_com = Commentaires.objects.all().order_by('-id')[:3]
    pubs = Publicites.objects.all().order_by('-id')

    d1 = pubs[0]
    d2 = pubs[1]
    d3 = pubs[2]

    if request.method == 'POST':
        if request.user.is_authenticated:
            commentaire = request.POST['commentaire']
            user = request.user

            comm = Commentaires(nom_complet=user.username, email=user.email, commentaire=commentaire)
            comm.save()
        
        else:
            messages.error(request, 'Veuillez vous authentifier pour poursuivre')
            return redirect('login')


    return render(request, 'index.html', context={'data':data,  'commentaires':data_com, 'pubs':pubs, 'd1':d1, 'd2':d2, 'd3':d3})

def logIn (request):
    if request.method == 'POST':
        username = request.POST['username']
        pwd = request.POST['pwd'] 

        my_user = authenticate(username=username, password=pwd)

        if my_user is not None:
            login(request, my_user)
            return redirect('home')
        else:
            messages.error(request, 'Le mot de passe ou le nom d\'utilisateur est incorrect')
            return redirect('login')
        
    return render(request, 'login.html')

def signIn(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password1 = request.POST['password1']

        if User.objects.filter(username=username):
            messages.error(request, 'Ce nom d\'utilisateur existe déja')
            return redirect('signin')

        # if User.objects.filter(email=email):
        #     messages.error(request, 'Ce email est déja enregistré')
        #     return redirect('signin')

        if User.objects.filter(username=username):
            messages.error(request, 'Ce compte email est déjà utilisé')
            return redirect('signin')

        if len(password) < 8:
            messages.error(request, 'Les mots de passe doit avoir au moins 8 caractères')
            return redirect('signin')

        if password != password1:
            messages.error(request, 'Les mots de passe ne sont pas identiques')
            return redirect('signin')
        
        if not password.isalnum():
            messages.error(request, 'Le mot de passe doit pas que contenir des chiffres et des lettre')
            return redirect('signin')
        
        u = User.objects.create_user(username=username, email=email, password=password)
        u.save()

        return redirect('login')

    return render(request, 'signin.html')

def service(request, id):
    data = Services.objects.get(id=id)
    services = Services.objects.all()
    return render(request, 'application/one.html', context={'service':data, 'services':services})

def work(request):
    publications = Publications.objects.all().order_by('-id')[:6]
    nb_like = []
    services = Services.objects.all()

    if request.user.is_authenticated:
        for publication in publications:
            a = Likes.objects.filter(publication_id=publication.id, like=True)
            print(len(a))
            nb_like.append(len(a))

        p1=publications[0]
        p2=publications[1]
        p3=publications[2]
        p4=publications[3]
        p5=publications[4]
        p6=publications[5]

        for i in publications:
            if not Likes.objects.filter(publication=i, user=request.user):
                p = Likes(publication=i, user=request.user, like=False)
                p.save()

        l1 = Likes.objects.get(publication=p1, user=request.user)
        l2 = Likes.objects.get(publication=p2, user=request.user)
        l3 = Likes.objects.get(publication=p3, user=request.user)
        l4 = Likes.objects.get(publication=p4, user=request.user)
        l5 = Likes.objects.get(publication=p5, user=request.user)
        l6 = Likes.objects.get(publication=p6, user=request.user)

        return render(request, 'application/work.html', context={'data':services, 'p1':p1, 'p2':p2, 'p3':p3, 'p4':p4, 'p5':p5, 'p6':p6, 'n1':nb_like[0], 'n2':nb_like[1], 'n3':nb_like[2], 'n3':nb_like[2], 'n3':nb_like[2], 'n4':nb_like[3], 'n5':nb_like[4], 'n6':nb_like[5], 'l1': l1, 'l2':l2, 'l3':l3, 'l4':l4, 'l5':l5, 'l6':l6}) #
    else:
        return render(request, 'application/work2.html', context={'data':services, 'publications':publications})

def comment(request, id):
    pub = Publications.objects.get(id=id)
    reaction = Reactions.objects.filter(publication_id=id)

    if request.method == 'POST':
        if request.user.is_authenticated:
            commentaire = request.POST['commentaire']
            user = request.user

            rea = Reactions(commentaire=commentaire, user=user, publication=pub)
            rea.save()

        else:
            messages.error(request, 'Veuillez vous connnecter avant de commenter ou aimer une photo')
            return redirect('login')

    return render(request, 'application/comment.html', context={'reactions':reaction, 'pub':pub})

def like(request, id):
    pub = Publications.objects.get(id=id)
    user = request.user

    if Likes.objects.filter(publication_id=id, user=user):
        rea = Likes.objects.get(publication_id=id, user=user)
        if rea.like == True:
            rea.like = False
        else:
            rea.like = True

        rea.save()
    else:
        rea = Likes(publication=pub, user=user, like=True)
        rea.save()

    return redirect('work')

def dashboard(request):
    services = len(Services.objects.all())
    publication = len(Publications.objects.all())
    comm = len(Commentaires.objects.all())
    publicite = len(Publicites.objects.all())
    users = len(User.objects.all())
    return render(request, 'application/dashboard.html', context={'services':services, 'publications':publication, 'comm':comm, 'publicites':publicite, 'users':users})

def gst_service(request):
    services = Services.objects.all()
    return render(request, 'application/gst_service.html', context={'services':services})

def delete_service(request, id):
    service = Services.objects.get(id=id)
    service.delete()

    return redirect('gst_service')

def form_service(request):
    if request.method == 'POST':
        designation = request.POST['designation']
        img = request.FILES['img']
        logo = request.FILES['logo']
        description = request.POST['description']

        with open(os.path.join(settings.MEDIA_ROOT, img.name),'wb') as file:
            for chunk in img.chunks():
                img.write(chunk)

        with open(os.path.join(settings.MEDIA_ROOT, logo.name),'wb') as file:
            for chunk in logo.chunks():
                logo.write(chunk)

        data = Services(description=description, img=img, titre=designation, logo=logo)
        data.save()

        return redirect('gst_service')
    
    return render(request, 'application/form_service.html')

def gst_publication(request):
    publications = Publications.objects.all()
    return render(request, 'application/gst_publication.html', context={'publications':publications})

def delete_publication(request, id):
    publication = Publications.objects.get(id=id)
    publication.delete()

    return redirect('gst_publication')

def form_publication(request):
    if request.method == 'POST':
        designation = request.POST['designation']
        img = request.FILES['img']

        with open(os.path.join(settings.MEDIA_ROOT, img.name),'wb') as file:
            for chunk in img.chunks():
                img.write(chunk)

        data = Publications(designation=designation, img=img)
        data.save()

        return redirect('gst_publication')

    return render(request, 'application/form_publication.html')

def gst_comm(request):
    comm = Commentaires.objects.all()
    return render(request, 'application/gst_comm.html', context={'comm':comm})

def delete_comm(request, id):
    comm = Commentaires.objects.get(id=id)
    comm.delete()

    return redirect('gst_commentaire')

def gst_publicite(request):
    pub = Publicites.objects.all()
    return render(request, 'application/gst_pubs.html', context={'pubs':pub})

def delete_pub(request, id):
    pub = Publicites.objects.get(id=id)
    pub.delete()

    return redirect('gst_publicites')

def form_publicite(request):
    if request.method == 'POST':
        titre = request.POST['titre']
        img = request.FILES['img']
        description = request.POST['description']

        with open(os.path.join(settings.MEDIA_ROOT, img.name),'wb') as file:
            for chunk in img.chunks():
                img.write(chunk)

        data = Publicites(description=description, img=img, title=titre)
        data.save()

        return redirect('gst_publicites')
    
    return render(request, 'application/form_pub.html')

def gst_user(request):
    users = User.objects.all()
    return render(request, 'application/gst_user.html', context={'users':users})

def delete_user(request, id):
    user = User.objects.get(id=id)
    user.delete()

    return redirect('gst_users')

def all_comment(request):
    comms = Commentaires.objects.all().order_by('-id')
    return render(request, 'application/all_comment.html', context={'comms':comms})
