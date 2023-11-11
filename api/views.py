from .serializer import ProfileSerializer, PostSerializer
from users.models import Profile
from blog.models import Post
from rest_framework import status
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.generics import ListAPIView
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.pagination import PageNumberPagination




class ProfileView(APIView):
   '''ALLOW AUTHENTICATED USER TO CONSUME CUSTOM REST API AND PERFORM READ, UPDATE, AND DELETE OPERATIONS ON THEIR PROFILE'''
   permission_classes = (IsAuthenticated,) # If not logged in will return HTTP 403
   
   def get(self, request):
      query = Profile.objects.get(user=self.request.user)
      serializer_class = ProfileSerializer(query)
      return Response(serializer_class.data)
   
   def put(self,request):
      query = Profile.objects.get(user=self.request.user)
      serializer_obj = ProfileSerializer(query, data=request.data)
      if serializer_obj.is_valid(raise_exception=True):
         save = serializer_obj.save()
         return Response({"Successfully updated '{}'".format(save.username)}, status = status.HTTP_200_OK)
      return Response(serializer_obj.errors, status=status.HTTP_400_BAD_REQUEST)

   def delete(self,request):
      Profile.objects.get(user=self.request.user).delete()
      return Response(status=status.HTTP_200_OK)





class AllPostListView(ListAPIView):
   '''ALL USERS AUTOMATICALLY CONSUME CUSTOM REST API TO READ BLOG POSTS'''
   queryset = Post.objects.all()
   serializer_class = PostSerializer
   pagination_class = PageNumberPagination
   filter_backends = (SearchFilter, OrderingFilter)
   search_fields = ('title', 'author', 'content', 'date_posted')





class PostListView(APIView):
   '''ALLOW AUTHENTICATED USER TO CONSUME CUSTOM REST API. THEY CAN READ ALL THEIR POSTS AND CREATE NEW ONES
      ---PLANNING TO ADD PAGINATION TO THIS VIEW---   
   '''
   permission_classes = (IsAuthenticated,)
   def get(self, request):
         query = Post.objects.filter(user=self.request.user)
         serializer_class = PostSerializer(query, many=True)
         return Response(serializer_class.data)
   
   def post(self, request):
      serializer_obj = PostSerializer(data=request.data)
      if serializer_obj.is_valid(raise_exception=True):
         serializer_obj.save()
         return Response('Successfully created post', status = status.HTTP_201_CREATED)
      return Response(serializer_obj.errors, status=status.HTTP_400_BAD_REQUEST)
   




class PostDetailView(APIView):
   '''ALLOW AUTHENTICATED USER TO CONSUME CUSTOM REST API. THEY CAN READ, UPDATE, DELETE ON THEIR INDUVIDUAL POSTS'''
   permission_classes = (IsAuthenticated,) # If not logged in will return HTTP 403
   def get(self, request, id):
      query = Post.objects.get(user=self.request.user, id=id)
      serializer_class = PostSerializer(query)
      return Response(serializer_class.data)
  
   def patch(self,request, id):
      query = Post.objects.get(user=self.request.user, id=id)
      serializer_obj = PostSerializer(query, data=request.data, partial=True)
      if serializer_obj.is_valid(raise_exception=True):
         save = serializer_obj.save()
         return Response({"Successfully updated '{}'".format(save.author)}, status = status.HTTP_200_OK)
      return Response(serializer_obj.errors, status=status.HTTP_400_BAD_REQUEST)

   def delete(self,request, id):
      Post.objects.get(user=self.request.user, id=id).delete()
      return Response(status=status.HTTP_200_OK)
