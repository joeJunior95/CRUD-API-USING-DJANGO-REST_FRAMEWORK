from django.urls import path
from . import views
urlpatterns = [
    path("",views.ShowUser.as_view()),
    path('create',views.CreateUser.as_view()),
    path('search/',views.SearchUser.as_view()),
    path('update/<int:id>',views.UpdateUser.as_view()),
    path('delete/<int:id>',views.DeleteUser.as_view())
   
]
