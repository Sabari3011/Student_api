from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Person
from . serializers import PersonSerializer
from rest_framework import viewsets
from rest_framework import status


@api_view(['GET','POST'])
def index(req):
    person={
        "name":"sabari",
        "course":"eee"
    }
    if req.method == "GET":
        print(req.GET['s'])
        return Response(person)
    elif req.method == "POST":
        data = req.data
        print("POST", data)
        return Response(data)
    

@api_view(["GET","POST","PATCH","PUT","DELETE"])
def person(req):
    print("here")
    if req.method == "GET":
        person= Person.objects.all()
        serializer = PersonSerializer(person , many = True)
        return Response(serializer.data)
    
    elif req.method == "POST":
        data=req.data
        serializer = PersonSerializer (data=  data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response (serializer.errors)

    elif req.method == "PUT":
        data=req.data
        obj = Person.objects.get(id=data['id'])
        serializer = PersonSerializer (obj, data = data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response (serializer.errors)
    
    elif req.method == "PATCH":
        data=req.data
        obj = Person.objects.get(id=data['id'])
        serializer = PersonSerializer (obj, data = data , partial = True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response (serializer.errors)

    elif req.method == "DELETE":
        data = req.data
        try:
            obj = Person.objects.get(id = data['id'])
            obj.delete()
            return Response ({"message":"data deleted successfully"})
        except:
            return Response({"err":"invalid id"})

class Peopleviewset(viewsets.ModelViewSet):
    serializer_class= PersonSerializer
    queryset=Person.objects.all()