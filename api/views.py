from django.shortcuts import render

from api.models import Category, Toy, Order
from api.serializers import CategorySerializer, ToySerializer, OrderSerializer

from rest_framework.decorators import api_view
from rest_framework.views import APIView 

from django.http.response import JsonResponse

@api_view(['GET'])
def categories(request):
    return JsonResponse(CategorySerializer(Category.objects.all(), many=True).data, safe=False)

@api_view(['GET'])
def toy_detailed(request, id):
    return JsonResponse(ToySerializer(Toy.objects.get(id=id)).data, safe=False)


@api_view(['POST'])
def category(request):
    category = Category.objects.get(name=request.data['name'])
    serializer = ToySerializer(category.toy_set.all(), many=True)
    return JsonResponse(serializer.data, safe=False)

class Toys(APIView):
    def get(self, request):
        return JsonResponse(ToySerializer(Toy.objects.all(), many=True).data, safe=False)

@api_view(['GET', 'POST'])
def order(request):
    if request.method == 'GET':
        return JsonResponse(OrderSerializer(Order.objects.all(), many=True).data, safe=False)

    elif request.method == 'POST':
        toy = Toy.objects.get(id=request.data['toy'])
        Order.objects.create(
            name= request.data['name'],
            phone = request.data['phone'],
            toy = toy
        )
        return JsonResponse({"": "order created"}, safe=False)

@api_view(['DELETE'])
def order_delete(request, id):
    toy = Toy.objects.get(id=id)
    toy.delete()
    return JsonResponse({"": "order deleted"}, safe=False)
