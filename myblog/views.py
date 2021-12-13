from django.views import generic
from .models import Post

# Create your views here. We will use class based views

class PostList(generic.ListView): # Render all posts via generic List_View
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = 'myblog/index.html'
 
class PostDetail(generic.DetailView): # Render specific post via Detail_View
    model = Post
    template_name = 'myblog/post_detail.html'

