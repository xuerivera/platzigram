#django
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView, CreateView
#forms
from posts.forms import PostForm
# models
from posts.models import Post

# Create your views here.


# The PostsFeedView class is a subclass of ListView. 
# It displays a list of posts ordered by the created field in descending order. 
# It uses the template post/feed.html. 
# It will paginate the posts using the paginate_by field. 
# The context object name is posts.
class PostsFeedView(LoginRequiredMixin, ListView):
    template_name = 'post/feed.html'
    model = Post
    ordering = ('-created')
    paginate_by = 30
    context_object_name = 'posts'


# We create a new class PostDetailView that inherits from the generic DetailView class.
# The DetailView class is designed to display data for an individual object.
# We also specify the template to use (detail.html) and the context_object_name to be 'post' so that
# we have access to the post object in the template.
class PostDetailView(LoginRequiredMixin, DetailView):
    template_name = 'post/detail.html'
    queryset = Post.objects.all()
    context_object_name = 'post'



# The CreatePostView class is a subclass of the generic CreateView class. 
# also a subclass of the LoginRequiredMixin class. 
# The LoginRequiredMixin is a mixin class that forces a login to view the content. 
# The CreateView class is a generic view that provides a default create form and a default
# form_valid() method. 
# The form_valid() method saves the form and redirects to the success_url. 
# The get_context_data() method adds the user and profile to the context.
class CreatePostView(LoginRequiredMixin, CreateView):
    template_name = 'post/new.html'
    form_class = PostForm
    success_url = reverse_lazy('posts:feed')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user'] = self.request.user
        context['profile'] = self.request.user.profile
        return context

