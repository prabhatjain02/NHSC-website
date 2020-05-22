from rest_framework import routers
from .views import ComplaintView

router = routers.DefaultRouter()
router.register(r'complaint', ComplaintView, 'complaint')

urlpatterns = router.urls