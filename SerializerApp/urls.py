from django.urls import path,include
from . import views
from rest_framework.routers import DefaultRouter

# Creating Router Object
router = DefaultRouter()

# Register StudentViewSet with Router
router.register('singer', views.SingerViewSet, basename='singer')
router.register('song',views.SongViewSet,basename='song')
router.register('person',views.PersonModelViewSet,basename='person')


urlpatterns= [
    path('', include(router.urls)),
    path('musician/<int:pk>/',views.musician_detail),
    path('musician/',views.musician_list),

]