from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Comment
from .serializers import CommentSerializer


@api_view(['GET', 'POST'])
def comment_list(request):

    if request.method == 'GET':
        comments = Comment.objects.all()
        serializer = CommentSerializer(comments, many=True)
        return Response(serializer.data)

    if request.method == 'POST':
        serializer = CommentSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        return Response(serializer.errors)


@api_view(['GET', 'PUT', 'DELETE'])
def comment_detail(request, id):

    try:
        comment = Comment.objects.get(id=id)
    except Comment.DoesNotExist:
        return Response({"error": "Not found"}, status=404)

    if request.method == 'GET':
        serializer = CommentSerializer(comment)
        return Response(serializer.data)

    if request.method == 'PUT':
        serializer = CommentSerializer(comment, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        return Response(serializer.errors)

    if request.method == 'DELETE':
        comment.delete()
        return Response({"message": "Deleted successfully"})
