from django.conf.urls import url
from django.contrib import admin
from .apis import user

urlpatterns = [
	#apis
    url(r'^api/user/storezip/$', user.user_storezip),
    url(r'^api/user/storepic/$', user.user_storepic),
    
]