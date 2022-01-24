"""users urls"""
# django
from django.urls import path

#views
from users import views


urlpatterns = [
    
    

    #management
    path(
        route='login/', 
        view=views.login_view, 
        name='login'),

    path(
        route='logout/', 
        view=views.logout_view,
         name='logout'),

    path(
        route='signup/', 
        view=views.SignupView.as_view(), 
        name='signup'),

    path(
        route='me/profile/', 
        view=views.UpdateProfileView.as_view(), 
        name='update_profile'),
    
    #posts
    path(
        route='<str:username>/',
        view=views.UserDetailView.as_view(),
        name='detail',
    ),
]
