from django.urls import include, path
from rest_framework import routers




# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    # path('api', include(router.urls)),
    path('', include('app.urls')),

    # path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]