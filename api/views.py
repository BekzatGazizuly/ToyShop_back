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

class ToyAdmin(APIView):
    def post(self, request):
        category = Category.objects.get(name=request.data['category'])
        Toy.objects.create(
            category = category,
            name = request.data['name'],
            imageURL = request.data['image'],
            description = request.data['description'],
            price = request.data['price']
        )
        return JsonResponse({"":"toy Created"}, safe=False)
    
    def put(self, request):
        category = Category.objects.get(name=request.data['category'])
        toy = Toy.objects.get(id=request.data.get('id'))
        toy.category = category
        toy.name = request.data.get('name')
        toy.description = request.data.get('description')
        toy.imageURL = request.data.get('image')
        toy.price = request.data.get('price')
        toy.save()
        return JsonResponse({"":"update"}, safe=False)

@api_view(['DELETE'])
def deleteToy(request, id):
    toy = Toy.objects.get(id=id)
    toy.delete()
    return JsonResponse({"":"removed"}, safe=False)



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
