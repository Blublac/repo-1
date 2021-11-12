from rest_framework import serializers, status
from rest_framework.response import Response
from rest_framework.decorators import api_view

from .serializers import Studentserializer,Bookserializer
from .models import Book, Student


@api_view(['GET','POST'])


def students(request):

    if request.method=='GET':
        all_students = Student.objects.all()
        serializer = Studentserializer(all_students, many =True)

        data = {'message':'success',
                'data': serializer.data
                }
        return Response(data,status.HTTP_200_OK)

    elif request.method=='POST':
        serializer = Studentserializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            data = {
                'message':'success',
                'data':serializer.data
            }
            return Response(data,status.HTTP_201_CREATED)

        else:
            error = {
                'message':'failed',
                'errors': serializer.errors
            }
            return Response(error,status.HTTP_400_BAD_REQUEST)

@api_view(['GET','POST'])
def books(request):
    
    if request.method=='GET':
        all_books = Book.objects.all()
        serializer = Bookserializer(all_books, many =True)

        data = {'message':'success',
                'data': serializer.data
                }
        return Response(data,status.HTTP_200_OK)

    elif request.method=='POST':
        serializer = Bookserializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            data = {
                'message':'success',
                'data':serializer.data
            }
            return Response(data,status.HTTP_201_CREATED)

        else:
            error = {
                'message':'failed',
                'errors': serializer.errors
            }
            return Response(error,status.HTTP_400_BAD_REQUEST)
