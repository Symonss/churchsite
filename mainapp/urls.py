from django.urls import path
from mainapp.views import mainview,pastors

urlpatterns = [
    path('', mainview.index, name='index'),
    path('pastor/dashboard/home', pastors.pastorHome, name = 'pastors_home'),
    path('add/group', pastors.GroupCreateView.as_view(), name = 'add_group'),
    path('pastor/dashboard/group', pastors.groupView, name = 'pastor_groups')
]