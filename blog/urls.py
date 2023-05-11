from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import index, about, post_single, post_form, PostViewSet

router=DefaultRouter()
router.register('post',PostViewSet,basename='post')


urlpatterns=[
    path('',index,name='index'),
    path('<int:pk>/',post_single,name='single'),
    path('post/new/',post_form,name="post_form"),
    path('about/',about,name='about'),
    path('api/post/list/',PostViewSet.as_view({'get':'list'})),
    path('api/',include(router.urls)),
]