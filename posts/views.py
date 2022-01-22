#django
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView
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
    paginate_by = 4
    context_object_name = 'posts'


@login_required
def create_post(request):
    """Create new post view."""
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('posts:feed')

    else:
        form = PostForm()

    return render(
        request=request,
        template_name='post/new.html',
        context={
            'form': form,
            'user': request.user,
            'profile': request.user.profile
        }
    )