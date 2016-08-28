from rest_framework.routers import DefaultRouter
from api import views

router = DefaultRouter()
router.register(r'provinces', views.ProvinceViewSet)

urlpatterns = router.urls
