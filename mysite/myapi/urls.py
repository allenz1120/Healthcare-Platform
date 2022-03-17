from django.urls import include, path
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'billing', views.BillingViewSet)
router.register(r'medical_history', views.MedicalHistoryViewSet)
router.register(r'role_relation', views.RoleRelationViewSet)
router.register(r'roles', views.RolesViewSet)
router.register(r'device_bp', views.DeviceBPViewSet)
router.register(r'device_temp', views.DeviceTempViewSet)



# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
