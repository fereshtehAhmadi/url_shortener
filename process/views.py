from django.shortcuts import render, redirect
from django.views.generic import View
from rest_framework.generics import ListAPIView, CreateAPIView
from django.conf import settings

from process.serializers import LinkSerializer
from process.models import Link


class AllShortenerLink(ListAPIView):
	queryset = Link.objects.all()
	serializer_class = LinkSerializer


class CreateShortnerLink(CreateAPIView):
	serializer_class = LinkSerializer


class Redirect(View):
	def get(self, request, shorten_link, *args, **kwargs):
		shorten_link = settings.HOST_URL + '/' + self.kwargs['shorten_link']
		redirect_link = Link.objects.filter(shorten_link=shorten_link).first().main_link
		return redirect(redirect_link)
