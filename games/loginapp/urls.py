from django.conf.urls import url
from loginapp.views import login, logout, register
from mytest.views import index

# urlpatterns = [
#     url(r'^login$', login, name='login'),
#     url(r'^register$', register, name='register'),
#     url(r'^logout$', logout, name='logout'),
# ]