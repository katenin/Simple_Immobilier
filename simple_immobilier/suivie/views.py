from django.shortcuts import render, redirect
from django.core.mail import send_mail
from .models import DemandeSuivie

def demande_suivie(request):
    if request.method == 'POST':
        nom = request.POST.get('nom')
        email = request.POST.get('email')
        telephone = request.POST.get('telephone')
        numero = request.POST.get('numero_dossier')
        message = request.POST.get('message')

        # Enregistrer dans la base
        demande = DemandeSuivie.objects.create(
            nom=nom,
            email=email,
            telephone=telephone,
            numero_dossier=numero,
            message=message
        )

        # Envoyer un mail de confirmation
        sujet = "Confirmation de votre demande de suivi"
        contenu = (
            f"Bonjour {nom},\n\n"
            f"Votre demande de suivi pour le dossier N° {numero} a bien été reçue.\n"
            f"Nous vous contacterons sous peu.\n\n"
            f"Merci pour votre confiance.\n"
            f"L’équipe Simple Immobilier."
        )
        send_mail(
            sujet,
            contenu,
            'no-reply@simpleimmobilier.com',
            [email],
            fail_silently=False,
        )

        return render(request, 'suivie/suivie_succes.html', {'nom': nom})

    return render(request, 'suivie/formulaire_suivie.html')
