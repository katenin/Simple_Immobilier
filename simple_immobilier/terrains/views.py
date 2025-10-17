from django.shortcuts import render
from .models import Terrain
from django.core.paginator import Paginator

def liste_terrains(request):
    terrains = Terrain.objects.filter(disponible=True).order_by('-date_ajout')

    # Récupération des filtres depuis la requête
    localisation = request.GET.get('localisation')
    prix_max = request.GET.get('prix_max')
    superficie_min = request.GET.get('superficie_min')

    if localisation:
        terrains = terrains.filter(localisation__icontains=localisation)

    if prix_max:
        terrains = terrains.filter(prix__lte=prix_max)

    if superficie_min:
        terrains = terrains.filter(superficie__gte=superficie_min)

   # Pagination
    paginator = Paginator(terrains, 5)  # 5 terrains par page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    contexte = {
        'page_obj': page_obj,
        'valeurs': {
            'localisation': localisation or '',
            'prix_max': prix_max or '',
            'superficie_min': superficie_min or '',
        }
    }

    return render(request, 'terrains/liste_terrains.html', contexte)
