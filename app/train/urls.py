from django.urls import path, include
# from .views import listProduct, listmessages
from .views import TrainUserListView, StationListView, TrainListView, StationDetailedView

urlpatterns = [
    path('users', TrainUserListView.as_view() ),
    path('users/', TrainUserListView.as_view()),

    path('stations', StationListView.as_view()),
    path('stations/', StationListView.as_view()),
    path('stations/<int:station_id>/trains', StationDetailedView.as_view(), name="bookDetails"),

    path('trains', TrainListView.as_view()),
    path('trains/', TrainListView.as_view()),
    # path('/<int:pid>', BookDetailedView.as_view(), name="bookDetails"),
    # path('/<int:pid>/', BookDetailedView.as_view(), name="bookDetails")
]
