from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json

from .models import Post


@csrf_exempt
def create_post(request):
    if request.method == "POST":
        data = json.loads(request.body)

        post = Post.objects.create(
            title=data.get("title"),
            content=data.get("content")
        )

        return JsonResponse({
            "message": "Post created successfully",
            "id": post.id
        })


def get_posts(request):
    if request.method == "GET":
        posts = Post.objects.all()

        data = []
        for post in posts:
            data.append({
                "id": post.id,
                "title": post.title,
                "content": post.content
            })

        return JsonResponse(data, safe=False)


def get_post(request, id):
    try:
        post = Post.objects.get(id=id)
        return JsonResponse({
            "id": post.id,
            "title": post.title,
            "content": post.content
        })
    except Post.DoesNotExist:
        return JsonResponse({"error": "Not found"}, status=404)


@csrf_exempt
def update_post(request, id):
    if request.method == "PUT":
        try:
            post = Post.objects.get(id=id)
            data = json.loads(request.body)

            post.title = data.get("title", post.title)
            post.content = data.get("content", post.content)
            post.save()

            return JsonResponse({"message": "Updated"})
        except Post.DoesNotExist:
            return JsonResponse({"error": "Not found"}, status=404)


@csrf_exempt
def delete_post(request, id):
    if request.method == "DELETE":
        try:
            post = Post.objects.get(id=id)
            post.delete()
            return JsonResponse({"message": "Deleted"})
        except Post.DoesNotExist:
            return JsonResponse({"error": "Not found"}, status=404)