from rest_framework import routers
from .views import NoticeView

router = routers.DefaultRouter()
router.register(r'notices', NoticeView, 'notices')

urlpatterns = router.urls