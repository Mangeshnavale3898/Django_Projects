from django.urls import path
from .views import *


urlpatterns = [
    path('', HomePage.as_view()),
    path('videos', VideosPage.as_view()),
    path('details', Guitardetails.as_view()),
    path('batches', BatchesPage.as_view()),
    path('contact', ContactPage.as_view()),
    path('about', AboutPage.as_view()),
    path('feestructure', feestructurePage.as_view()),
    path('buyguitar', BuyguitarPage.as_view()),
]
