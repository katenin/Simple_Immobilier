"""
URL configuration for simple_immobilier project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from terrains.views import liste_terrains
from suivie.views import demande_suivie


"""
from verification.views import verifier_terrain
from blog.views import liste_articles
"""

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', liste_terrains, name='accueil'),
    path('suivie/', demande_suivie, name='demande_suivie'),
    path('verification/', include('verification.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)