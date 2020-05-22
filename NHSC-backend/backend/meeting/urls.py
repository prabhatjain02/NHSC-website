from rest_framework import routers
from .views import MeetingView

router = routers.DefaultRouter()
router.register(r'meeting', MeetingView, 'meeting')

urlpatterns = router.urls