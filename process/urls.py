from django.urls import path
from . import views

urlpatterns = [
	path('', views.AllShortenerLink.as_view(), name='show_links'),
	path('create/', views.CreateShortnerLink.as_view(), name='create_shortener_link'),
]