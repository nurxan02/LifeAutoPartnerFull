from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics
# from django.shortcuts import render
# from rest_framework import viewsets
from .models import Blog,  Contact
from .serializers import BlogSerializer,  ContactSerializer

# class BlogViewSet(viewsets.ModelViewSet):
#     queryset = Blog.objects.all()
#     serializer_class = BlogSerializer

# class BlogImageViewSet(viewsets.ModelViewSet):
#     queryset = BlogImage.objects.all()
#     serializer_class = BlogImageSerializer

# class ContactViewSet(viewsets.ModelViewSet):
#     queryset = Contact.objects.all()
#     serializer_class = ContactSerializer


class ContactCreateView(generics.CreateAPIView):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return Response(serializer.data, status=201)  
    

class BlogListView(APIView):
    def get(self, request):
        blogs = Blog.objects.filter(active=True) 
        serializer = BlogSerializer(blogs, many=True)
        return Response(serializer.data)
    
class BlogDetailView(APIView):
    def get(self, request, pk):
        blog = get_object_or_404(Blog, pk=pk)  
        serializer = BlogSerializer(blog)
        return Response(serializer.data)