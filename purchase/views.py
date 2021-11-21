import requests
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
from datetime import datetime

class IndexView(generic.ListView):
    template_name = 'purchase/index.html'
    def get_queryset(self):
        return HttpResponse("Hello, world. You're at the purchase index")

class Page1(generic.ListView):
    template_name = 'purchase/page1.html'
    def get_queryset(self):
        return HttpResponse("Hello, world. You're at the purchase page1")

class Page3(generic.ListView):
    template_name = 'purchase/page3.html'
    def get_queryset(self):
        return HttpResponse("Hello, world. You're at the purchase page3")

class OrderViews(APIView):
    def post(self, request):
        #check balance from Cardano Wallet and save in a variable START
        walletId = 'acdc0d96c1406aeb57ab95e58eaf549c4bb19f83'
        r = requests.get('http://localhost:1339/v2/wallets/%s' % walletId, params=request.GET)
        wallet = r.json()
        balance = wallet['balance']['total']['quantity']
        #check balance from Cardano Wallet and save in a variable END
        request.data['order_start'] = datetime.now().replace(microsecond=0)
        request.data['order_end'] = datetime.now().replace(microsecond=0)
        request.data['order_price'] = '8880'
        request.data['order_paid'] = 'not received'
        request.data['order_status'] = "started"
        request.data['wallet_balance'] = balance
        serializer = OrderSerializer(data=request.data)
        if serializer.is_valid():
            order = serializer.save()
            id = order.id
            print("id in post is ", id)
            return Response({"status": "success", "id": id}, status=status.HTTP_200_OK)
        else:
            return Response({"status": "error", "data": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, id=None):
           if id:
               # check balance value at the start of transaction from database
               item = Order.objects.get(id=id)
               serializer = OrderSerializer(item)
               balance1 = serializer.data['wallet_balance']

               # check actual balance from Cardano wallet
               walletId = 'acdc0d96c1406aeb57ab95e58eaf549c4bb19f83'
               r = requests.get('http://localhost:1339/v2/wallets/%s' % walletId, params=request.GET)
               wallet = r.json()
               balance2 = wallet['balance']['total']['quantity']

               # check if amount on balance was increased by price value
               if (int(balance2) - int(balance1) == 8880000000):
                   isPaymentComplete = True
               else:
                   isPaymentComplete = False


               if isPaymentComplete:
                   now2 = datetime.now().replace(microsecond=0)
                   request.data['order_end'] = now2
                   request.data['order_paid'] = 'received'
                   request.data['order_status'] = "complete"
                   serializer = OrderSerializer(item, data=request.data, partial=True)
                   if serializer.is_valid():
                       serializer.save()
                       return Response({"status": "success", "payment": "received"}, status=status.HTTP_200_OK)
                   else:
                       return Response({"status": "error", "payment": "not received"}, status=status.HTTP_200_OK)
               else:
                   date_2 = datetime.now().replace(microsecond=0)
                   date_1 = serializer.data['order_start']
                   date_1 = date_1.replace("T", " ").replace("Z", "")
                   date_1 = datetime.strptime(date_1, "%Y-%m-%d %H:%M:%S")
                   time_delta = (date_2 - date_1)
                   total_seconds = time_delta.total_seconds()
                   minutes = total_seconds/60

                   # check if 5 minutes passed so transaction is failed
                   if (total_seconds >= 300 and total_seconds <= 309):
                       request.data['order_end'] = date_2
                       request.data['order_status'] = "error"
                       serializer = OrderSerializer(item, data=request.data, partial=True)
                       if serializer.is_valid():
                           serializer.save()
                           return Response({"status": "success", "payment": "not received"}, status=status.HTTP_200_OK)
                       else:
                           return Response({"status": "error", "payment": "not received"}, status=status.HTTP_200_OK)
                   # check if time was prolonged by user and 10 minutes instead of 5 passed
                   elif total_seconds > 550:
                        if (total_seconds >= 601 and total_seconds <= 609):
                            request.data['order_end'] = date_2
                            request.data['order_status'] = "error"
                            serializer = OrderSerializer(item, data=request.data, partial=True)
                            if serializer.is_valid():
                                serializer.save()
                                return Response({"status": "success", "payment": "not received"}, status=status.HTTP_200_OK)
                            else:
                                return Response({"status": "error", "payment": "not received"}, status=status.HTTP_200_OK)
                   return Response({"status": "error", "payment": "not received"}, status=status.HTTP_200_OK)
           items = Order.objects.all()
           serializer = OrderSerializer(items, many=True)
           return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)


def page2(request):
    if request.method == 'POST':
        firstName = request.POST.get('firstName')
        lastName = request.POST.get('lastName')
        email = request.POST.get('email')
        walletAddress = request.POST.get('walletAddress')
        streetAddress = request.POST.get('streetAddress')
        Rs = "firstName = " + firstName + "; lastName = "+lastName+"; email = "+email
        Rs = Rs + "; walletAddress = " + walletAddress + "; streetAddress " + streetAddress

        print(Rs)
        return HttpResponseRedirect(reverse('purchase:page3'))
