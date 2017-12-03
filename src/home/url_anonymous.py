from django.conf.urls import url, include

from .views import anonymous_tip, anonymous_user_login, anonymous_dashboard

urlpatterns = [

    url(r'^$', anonymous_tip, name='anonymous_tip'),
    url(r'^login$', anonymous_user_login, name='anonymous_user_login'),
    url(r'^dashboard$', anonymous_dashboard, name="anonymous_dashboard")

]
