
from django.urls import path
from . import views
from .views import ReviewListView, ReviewDetailView,ReviewDeleteView


urlpatterns = [
    path('',ReviewListView.as_view(), name='review-list' ),
    path('review/<int:pk>',ReviewDetailView.as_view(), name='review-detail' ),
    path('reviewform/', views.ReviewCreateView.as_view(), name='review-form' ),
    path('reviewform/<int:pk>',views.ReviewUpdateView.as_view(), name='review-update' ),
    path('reviewform/<int:pk>/delete',views.ReviewDeleteView.as_view(), name='review-delete' )
    ]

