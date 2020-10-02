from django.shortcuts import render, get_object_or_404, redirect
from rest_framework import status
from rest_framework.response import Response
from rest_framework.pagination import PageNumberPagination
from rest_framework.decorators import api_view
from rest_framework.generics import ListAPIView


from post.models import Post
from post.api.serializers import PostSerializer

#<----------- To get List view of Posts ------------------------------------>
class api_list_view(ListAPIView):
    queryset = Post.objects.all() #Query all posts
    serializer_class = PostSerializer #Add Serializer
    pagination_class = PageNumberPagination #Add Pagination
# <-------------------------------------------------------------------------->

#<----------- To get detail view of Post ------------------------------------>
@api_view(['GET']) #GET request only
def api_detail_view(request, post_id):
    try:
        post = Post.objects.get(id=post_id) #query single post with id
    except:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET': #no need of if statement because this is a GET request, for a double check using if statement
    #<----------- To get all liked users ----------------->
        total_liked_users = post.Likes.all() #This will give a queryset of USERS who liked this post
        contents = []
        for content in total_liked_users: #converting the queryset to list so that it can returned as JSON response
            contents.append(content)
        all_liked_users=[]
        for i in range(0,len(contents)):
            all_liked_users.append(str(contents[i])) #converting to string
    # <--------------------------------------------------->

    # <---------- To get likes and unlikes number -------->
        if request.method == 'GET': #no need of if statement because this is a GET request, for a double check using if statement
            user = request.user
            current_user = str(user) #For getting current users

            liked = False
            if user in post.Likes.all(): 
                liked = True
            else:
                liked = False
            like = post.total_likes()
            unlike = post.total_unlikes()
    # <---------------------------------------------------->
            
            serialzer = PostSerializer(post)
            
            return Response(
                    ({'current_user':current_user},
                        serialzer.data,
                        {'total likes':like},
                        {'total unlikes':unlike}, 
                        {'user liked':liked},
                        {'all liked users':all_liked_users}
                    )
                ) #This will give a Json response
# <-------------------------------------------------------------------------->