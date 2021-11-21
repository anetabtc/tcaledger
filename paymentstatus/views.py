from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render, redirect
from django.urls import reverse
from django.views import View, generic
from django.views.generic.base import TemplateView
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework import viewsets, status
from .serializers import OrderSerializer
from .models import Order

# Create your views here.
class IndexView(generic.ListView):
    template_name = 'paymentstatus/index.html'
    def get_queryset(self):
        return HttpResponse("Hello, world. You're at the paymentstatus index")

class OrderViews(APIView):
 def get(self, request, id=None):
        if id:
            item = Order.objects.get(id=id)
            serializer = OrderSerializer(item)
            return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)
        items = Order.objects.all()
        serializer = OrderSerializer(items, many=True)
        return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)
