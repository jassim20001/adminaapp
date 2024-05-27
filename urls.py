from django.urls import path,include
from. import views
urlpatterns = [
    
    path('',views.home,name='home' ),
    path('add_product',views.add,name='add' ),
    path('login',views.Login_user,name='login'),
    path('products',views.product,name='product'),
    path('logout_view',views.logout_view,name='logout'),
    path('signup',views.signup,name='signup'),
    path('profile',views.profile,name='profile'),
    path('<slug:slug>/',views.detal_product,name='detal_product'),
    path('update/<str:pk>',views.update,name='update'),
    path('delete/<str:pk>',views.delete,name='delete'),

]
