
from .models import Post #, Comment
from .serializers import Postserializers 
from rest_framework import generics


# @api_view(['GET'])
# def post_list_api(request):
#     posts = Post.objects.all()
#     data = Postserializers(posts,many=True).data
#     return Response({'data':data})


class PostListAPI(generics.ListAPIView):
    queryset = Post.objects.all()
    serializer_class = Postserializers



class PostDetailAPI(generics.RetrieveAPIView):
    queryset = Post.objects.all()
    serializer_class = Postserializers