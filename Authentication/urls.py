from django.urls import path,include
from Authentication import views
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken.views import obtain_auth_token
from Authentication.auth import CustomAuthToken

router = DefaultRouter()

router.register('userapi1',views.UserModelViewSet1,basename='userapi1')
router.register('userapi2',views.UserModelViewSet2,basename='userapi2')
router.register('userapi3',views.UserModelViewSet3,basename='userapi3')
router.register('userapi4',views.UserModelViewSet4,basename='userapi4')
router.register('userapi5',views.UserModelViewSet5,basename='userapi5')
router.register('userapi6',views.UserModelViewSet6,basename='userapi6')
router.register('userapi7',views.UserModelViewSet7,basename='userapi7')
router.register('userapi8',views.UserModelViewSet8,basename='userapi8')
router.register('userapi9',views.UserModelViewSet9,basename='userapi9')
router.register('userapi10',views.UserModelViewSet10,basename='userapi10')
router.register('studentapi',views.StudentModelViewSet,basename='student')
router.register('studentapi2',views.StudentModelViewSet2,basename='student2')




urlpatterns = [
    path('',include(router.urls)),
    path('auth/',include('rest_framework.urls',namespace='rest_framework')),
    path('gettoken/',obtain_auth_token),
    # path('getcustomtoken/',CustomAuthToken.as_view()),
]