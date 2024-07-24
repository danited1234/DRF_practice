from .models import Carlist,Showroomlist
from .api_file.serializers import CarSerializer,ShowroomSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.views import APIView


class showroom_view(APIView):
    
    def get(self,request):
        showrooms = Showroomlist.objects.all()
        serializer = ShowroomSerializer(showrooms, many=True)
        return Response(serializer.data)

    def post(self,request):
        serializer = ShowroomSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class showroom_details(APIView):
    
    def get(self,request,pk):
        try:
            showroom = Showroomlist.objects.get(pk=pk)
        except Showroomlist.DoesNotExist:
            return Response({"Error":"Showroom Not Found"},status=status.HTTP_404_NOT_FOUND)
        serializer = ShowroomSerializer(showroom)
        return Response(serializer.data)
    
    def put(self,request,pk):
        try:
            showroom_details = Showroomlist.objects.get(pk=pk)
        except Showroomlist.DoesNotExist:
            return Response({"Error":"Showroom Not Found"},status=status.HTTP_404_NOT_FOUND)
        serializer = CarSerializer(showroom_details, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request,pk):
        showroom = Carlist.objects.get(pk=pk)
        showroom.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
@api_view(['GET', 'POST'])
def car_list_view(request):
    if request.method == 'GET':
        car = Carlist.objects.all()
        serializer = CarSerializer(car,many=True)
        return Response(serializer.data)
    if request.method == 'POST':
        serializer = CarSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT','DELETE'])
def car_detail_view(request,pk):
    if request.method == 'GET':
        try:
            car = Carlist.objects.get(pk=pk)
        except:
            return Response({"Error":"Car Not Found"},status=status.HTTP_204_NO_CONTENT)
        serializer = CarSerializer(car)
        return Response(serializer.data)
    if request.method == 'PUT':
        car = Carlist.objects.get(pk=pk)
        serializer = CarSerializer(car, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    if request.method == 'DELETE':
        car = Carlist.objects.get(pk=pk)
        car.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
            
            
            
# def car_list_view(request):
#     cars = Carlist.objects.all()
#     data = {
#         'cars':list(cars.values())
#     }
    
#     return JsonResponse(data)


# def car_detail_view(request,pk):
#     car = Carlist.objects.get(pk=pk)
#     data = {
#         'car': car.name,
#         'description': car.description,
#         'active': car.active
#     }
    
#     return JsonResponse(data)
