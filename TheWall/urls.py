from django.urls import path
from .views import (
    ProfileOnDayIce,
    ProfileOnDayCost,
    ProfileOverview,
    TotalCostOverview,
    DayOverview,
    home,
)

urlpatterns = [
    path("", home, name="home"),
    path(
        "profiles/<int:profile_id>/days/<int:day_number>/",
        ProfileOnDayIce.as_view(),
        name="profile-on-day-ice-amount",
    ),
    path(
        "profiles/<int:profile_id>/overview/<int:day_number>/",
        ProfileOnDayCost.as_view(),
        name="profile-on-day-cost",
    ),
    path(
        "profiles/<int:profile_id>/overview/",
        ProfileOverview.as_view(),
        name="profile-overall-cost",
    ),
    path(
        "profiles/overview/<int:day_number>/",
        DayOverview.as_view(),
        name="day-overall-cost",
    ),
    path("profiles/overview/", TotalCostOverview.as_view(), name="total-cost-overview"),
]
