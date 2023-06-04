from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import index, about, post_single, post_form, TokenObtainPairView, TokenRefreshView,\
    RegisterView, UserView, PostView, CourierView, ProductCardView, PostCreateView, PostListView
from . import views

router = DefaultRouter()
router.register('post', PostView, basename='post')
router.register('products', ProductCardView, basename='products')


urlpatterns = [
    path('token/', TokenObtainPairView.as_view()),
    path('token/refresh/', TokenRefreshView.as_view()),
    path('register/', RegisterView.as_view({'post': 'create'})),
    path('user/me/', UserView.as_view({'get': 'get_current_user'})),
    path('', index, name='index'),
    path('<int:pk>/', post_single, name='post_single'),
    path('post/new/', post_form, name="post_form"),
    path('about/', about, name='about'),
    path('courier/get/', CourierView.as_view()),
    path('api/', include(router.urls)),
    path('post/<int:pk>/', views.single_post, name='single'),
    path('api/products/', PostListView.as_view(), name='post_list'),
    path('api/post/create/', PostCreateView.as_view(), name='post-create'),
] + router.urls
