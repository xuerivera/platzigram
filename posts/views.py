#django
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView, CreateView
#forms
from posts.forms import PostForm
# models
from posts.models import Post

# Create your views here.


class PostsFeedView(LoginRequiredMixin, ListView):
    """return all published posts"""
    template_name = 'post/feed.html'
    model = Post
    ordering = ('-created')
    paginate_by = 30
    context_object_name = 'posts'

class PostDetailView(LoginRequiredMixin, DetailView):
    """Return post detail."""

    template_name = 'post/detail.html'
    queryset = Post.objects.all()
    context_object_name = 'post'



class CreatePostView(LoginRequiredMixin, CreateView):
    """Create a new post"""
    template_name = 'post/new.html'
    form_class = PostForm
    success_url = reverse_lazy('posts:feed')
    
    def get_context_data(self, **kwargs):
        """add user and profile to context"""
        context = super().get_context_data(**kwargs)
        context['user'] = self.request.user
        context['profile'] = self.request.user.profile
        return context

