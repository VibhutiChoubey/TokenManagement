from django.urls import path
from apis import views

urlpatterns = [
    path('generate/', views.generate_token, name='generate_token'),
    path('assign/', views.assign_token, name='assign_token'),
    path('unblock/<str:token>/', views.unblock_token, name='unblock_token'),
    path('delete/<str:token>/', views.delete_token, name='delete_token'),
    path('keep-alive/<str:token>/', views.keep_alive_token, name='keep_alive_token'),
]
