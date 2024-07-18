from django.urls import  path
from launches.views import launch_index

# Will be every URL that starts with /launches/
urlpatterns = [
    path("", launch_index, name="launch-index"),
]
