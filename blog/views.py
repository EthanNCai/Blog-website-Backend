from django.http import JsonResponse
from .models import BlogInfo
from django.http import HttpResponse
from django.conf import settings
import os
from django.shortcuts import get_object_or_404
def blogFlow(request):
    blog_objects = BlogInfo.objects.all()

    blog_list = []
    for blog in blog_objects:
        blog_dict = {
            'blog_id': blog.blog_id,
            'blog_name': blog.blog_name,
            'blog_likes': blog.blog_likes,
            'blog_hates': blog.blog_hates,
            'blog_date': blog.blog_date.strftime('%Y-%m-%d'),
            'blog_category': blog.blog_category,
            'blog_description': blog.blog_description,
            'blog_reads': blog.blog_reads
        }
        blog_list.append(blog_dict)

    return JsonResponse(blog_list, safe=False)

def blogAvatar(request, id):
    image_path = os.path.join(settings.BASE_DIR,'blog','Blogs', str(id), 'icon.jpg')

    try:
        with open(image_path, 'rb') as f:
            image_data = f.read()
        response = HttpResponse(content_type='image/jpeg')
        response.write(image_data)
        return response
    except IOError:
        return HttpResponse(status=404)
    
def blogArticle(request, id):
    markdown_path = os.path.join(settings.BASE_DIR, 'blog', 'Blogs', str(id), 'article.md')

    try:
        with open(markdown_path, 'r', encoding='utf-8') as f:
            markdown_content = f.read()
        
        response = HttpResponse(content_type='text/plain')
        response.write(markdown_content)
        return response
    except IOError:
        return HttpResponse(status=404)
    
def blog_find_id(request, id):
    blog = get_object_or_404(BlogInfo, blog_id=id)
    
    # 增加 blog_reads 值
    blog.blog_reads += 1
    blog.save()

    blog_dict = {
        'blog_id': blog.blog_id,
        'blog_name': blog.blog_name,
        'blog_likes': blog.blog_likes,
        'blog_hates': blog.blog_hates,
        'blog_date': blog.blog_date.strftime('%Y-%m-%d'),
        'blog_category': blog.blog_category,
        'blog_description': blog.blog_description,
        'blog_reads': blog.blog_reads
    }
    return JsonResponse(blog_dict)