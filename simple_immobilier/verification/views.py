from django.shortcuts import render, redirect
from .forms_verification import DocumentVerificationForm

def verification_view(request):
    if request.method == "POST":
        form = DocumentVerificationForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()  # Sauvegarde la demande dans la base
            return redirect('verification_success')  # Redirige vers la page de succès
    else:
        form = DocumentVerificationForm()
    
    return render(request, 'verification/form_verification.html', {'form': form})

def verification_success_view(request):
    return render(request, 'verification/success_verification.html')
