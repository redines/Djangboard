from rest_framework.decorators import api_view
from rest_framework.response import Response
from BlogEditor.models import Post
from .serializers import PostsSerializer

@api_view(['GET'])
def getRouter(request):
    routes = ['get /api']

    return Response(routes)


@api_view(['GET'])
def getPosts(request):
    posts = Post.objects.all().order_by("-created_on")
    serializer = PostsSerializer(posts, many=True)
    return Response(serializer.data)