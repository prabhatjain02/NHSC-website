from rest_framework import routers
from .views import JoiningView

router = routers.DefaultRouter()
router.register(r'joining', JoiningView, 'joining')

urlpatterns = router.urls