from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path
from mainapp.views import pastors, elders, treasurers, group_leaders,content_managers

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('mainapp.urls')),
    path('accounts/', include('django.contrib.auth.urls')),

    path('accounts/signup/pastor/', pastors.PastorSignUpView.as_view(), name='pastors_signup'),
    path('accounts/signup/elder/', elders.ElderSignUpView.as_view(), name='elders_signup'),
    path('accounts/signup/treasurer/', treasurers.TreasurerSignUpView.as_view(), name='trasurer_signup'),
    path('accounts/signup/gl/', group_leaders.GroupLeaderSignUpView.as_view(), name='gl_signup'),
    path('accounts/signup/cm/', content_managers.ContentManagerSignUpView.as_view(), name='cl_signup'),
]