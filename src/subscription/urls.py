from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import SubscriptionView, SubscriptionViewSet, GetSubscriptionDetail


router = DefaultRouter()
router.register('admin', SubscriptionViewSet)

urlpatterns = [
    # path('admin/', SubscriptionViewSet.as_view()),
    path('reg/create/', SubscriptionView.as_view(), name="subscription"),
    # path('admin/get/subscription/all/', GetSubscriptionDetail.as_view(), name="get_all_subscription"),
    path('admin/get/subscription/<int:id>/', GetSubscriptionDetail.as_view(), name="get_subscription_detail")
]

urlpatterns += router.urls
