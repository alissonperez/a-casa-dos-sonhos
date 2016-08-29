from rest_framework.routers import DefaultRouter
from api import views

router = DefaultRouter()
router.register(r'provinces', views.ProvinceViewSet)
router.register(r'properties', views.PropertyViewSet)

urlpatterns = router.urls
