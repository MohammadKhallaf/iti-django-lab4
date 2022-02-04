from django.urls import path, include
from rest_framework import routers

from myapiapp import views

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)
router.register(r'students', views.StudentViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('updt/<int:pk>', views.update_student, name="updt"),
    path('del/<int:pk>', views.delete_student, name="del")
]
