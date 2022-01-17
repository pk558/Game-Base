from django.contrib import admin
from django.urls import path
from Game.views import *
from django.conf.urls.static import static
from django.conf import settings
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),   #Przypisuje funkcje do głównego adresu strony
    path('game/<id>/', game, name='game'),
    path('category/<id>/', category, name='category'),   #Przypisuje funkcje do głównego adresu strony
    path('platform/<id>/', platform, name='platform'),   #Przypisuje funkcje do głównego adresu strony
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)