from django.urls import path
from .views import HomeView,SnacksCreateView,SnacksDetailView,SnacksUpdateView,SnacksDeleteView,SnacksListView


urlpatterns = [
    path('', HomeView.as_view(), name = "home"),
    path('create/', SnacksCreateView.as_view(), name = "create_snack"),
    path('<int:pk>', SnacksDetailView.as_view(), name = "detail_snack"),
    path('snacks-list', SnacksListView.as_view(), name = "snack_list"),
    path('update/<int:pk>', SnacksUpdateView.as_view(), name = "update_snack"),
    path('delete/<int:pk>', SnacksDeleteView.as_view(), name = "delete_snack"),
]
