from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response 
from rest_framework.request import Request 
from django.db.models import Q
from .models import Advocate
from .serializers import AdvocateSerializer

# display all users that were created using django createsuperuser
class ShowUser(APIView):
    def get(self,request:Request):
        if request.method == 'GET':
            advocate = Advocate.objects.all()
            serializer = AdvocateSerializer(advocate,many=True)
            return Response(serializer.data,status=status.HTTP_200_OK)
        
# create user
class CreateUser(APIView):
    def post(self,request:Request):
        if request.method == 'POST':
            advocate = Advocate.objects.create(
                username = request.data['username'],
                bio = request.data['bio']
            )
            serializer = AdvocateSerializer(advocate,many=False)
            return Response(serializer.data, status=status.HTTP_201_CREATED)    

# search for user using username and bio   
class SearchUser(APIView):
    def get(self,request:Request):
        # if request.method == 'GET':
            query = request.GET.get('query')
            if query == None:
                query = ''
            advocate =Advocate.objects.filter(Q(username__icontains=query) | Q(bio__icontains=query))
            serializer = AdvocateSerializer(advocate,many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
                        
# update user
class UpdateUser(APIView):
    def post(self,request:Request,id):
        if request.method == 'POST':
            advocate = Advocate.objects.get(id=id)
            advocate.username = request.data['username']
            advocate.bio = request.data['bio']
            advocate.save()
            serializer = AdvocateSerializer(advocate,many=False)
            return Response(serializer.data,status=status.HTTP_201_CREATED)    
        
# delete user
class DeleteUser(APIView):
    def delete(self,request:Request,id):
        if request.method == 'DELETE':
            advocate = Advocate.objects.get(id=id)
            advocate.delete()
            return Response('User Deleted Successfully')
        