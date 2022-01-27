"""Users views."""

# Django
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import views as auth_views
from django.urls import reverse, reverse_lazy
from django.views.generic import DetailView, FormView, UpdateView

# models
from django.contrib.auth.models import User
from posts.models import Post
from users.models import Profile

#forms
from users.forms import SignupForm


# The UserDetailView class is a subclass of the generic DetailView class. 
# It displays a user's profile. 
# The template_name attribute is used to tell Django to use a specific template. 
# The slug_field attribute tells Django which field to use as the slug. 
# The slug_url_kwarg attribute tells Django to use the username as the name of the URL parameter. 
# The queryset attribute tells Django to use a specific model to build the view. 
# The context_object_name attribute tells Django to use the
class UserDetailView(LoginRequiredMixin, DetailView):
    """user detail view"""
    template_name = 'users/detail.html'
    slug_field = 'username'
    slug_url_kwarg = 'username'
    queryset = User.objects.all()
    context_object_name = 'user'


    def get_context_data(self, **kwargs):
        '''
        Get the context data for the user profile page.
        
        
        :return: The user's profile page.
        '''
        context = super().get_context_data(**kwargs)
        user = self.get_object()
        context['posts'] = Post.objects.filter(user=user).order_by('-created')
        return context


# The SignupView class inherits from FormView, which is a generic class-based view that handles the
# rendering of a form and the processing of that form.
# 
# The template_name attribute is used to tell Django to use a specific template to render this view.
# 
# The form_class attribute is used to tell Django which form should be used to handle data in this
# view.
# 
# The success_url attribute is used to tell Django what URL should be used after the form has been
# successfully processed.
# 
# The form_valid method is used to handle the data
class SignupView(FormView):
    template_name = 'users/signup.html'
    form_class = SignupForm
    success_url = reverse_lazy('users:login')

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)



class UpdateProfileView(LoginRequiredMixin, UpdateView):
    """
    The UpdateProfileView class inherits from both LoginRequiredMixin and UpdateView. 
    The LoginRequiredMixin class will ensure that only authenticated users can access the view. 
    The UpdateView class will provide the mechanisms required to update the profile.
    """
    template_name = 'users/update_profile.html'
    model = Profile
    fields = ['website', 'biography', 'phone_number', 'picture']

    def get_object(self):
        '''
        The get_object() method is a built-in method in the ModelViewSet class. 
        It does exactly what its name implies. It returns the object the view is displaying. 
        In our case, it returns the user's profile.
        
        
        :return: The user's profile.
        '''
        return self.request.user.profile

    def get_success_url(self):
        '''
        The get_success_url function is a method that returns the URL to redirect to after a successful
        form submission. 
        '''
        username = self.object.user.username
        return reverse('users:detail', kwargs={'username': username})

# Overriding the default login view in Django.
class LoginView(auth_views.LoginView):
    template_name = 'users/login.html'
    redirect_authenticated_user = True

class LogoutView(LoginRequiredMixin, auth_views.LogoutView):
    template_name = 'users/logout.html'