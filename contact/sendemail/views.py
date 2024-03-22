from django.http import HttpRequest
from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.urls import reverse

def contact_view(request):
    if request.method == 'POST':
        # Récupération des données du formulaire
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        website = request.POST.get('website')
        message = request.POST.get('message')

        # Construire le sujet et le corps de l'e-mail
        subject = f"Message de {name}"
        body = f"""
        Nom: {name}
        Email: {email}
        Téléphone: {phone}
        Site Web: {website}
        Message:
        {message}
        """

        # Envoi de l'e-mail
        send_mail(
            subject,
            body,
            email,  # Email de l'envoyeur
            ['savagedeveloppement@gmail.com'],  # Adresse e-mail destinataire
        )

        # Rediriger vers une page de confirmation après avoir traité le formulaire
        return redirect(reverse('confirmation') + f'?name={name}&email={email}')

    else:
        # Si la méthode n'est pas POST, afficher simplement le formulaire
        return render(request, 'index.html')
    
def confirmation_view(request: HttpRequest):
    name = request.GET.get('name')
    email = request.GET.get('email')
    # Autres informations à récupérer si nécessaire

    context = {'name': name, 'email': email}
    return render(request, 'confirmation.html', context)
