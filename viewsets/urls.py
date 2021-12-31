from django.urls import path,include
from viewsets import views
from rest_framework.routers import DefaultRouter

# Creating Router Object
router = DefaultRouter()

# Register CustomerViewSet with Router

router.register('customerapi', views.CustomerViewSet , basename='customer')
router.register('customerapi1', views.CustomerModelViewSet , basename='customer1')
router.register('customerapi2', views.CustomerReadOnlyViewSet , basename='customer2')

urlpatterns = [
    path('', include(router.urls)),
]