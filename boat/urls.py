from django.urls import path

from boat.apps import BoatConfig
from boat.views import BoatListView

app_name = BoatConfig.name

urlpatterns = [
    path('', BoatListView.as_view(), name='boat_list')
]

