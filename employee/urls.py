from django.urls import path, re_path
from . import views

urlpatterns = [
    re_path(
        r'^api/employee/(?P<pk>[0-9]+)$',
        views.get_delete_update_employee,
        name='get_delete_update_employee'
    ),
    path(
        'api/employee/',
        views.get_post_employee,
        name='get_post_employee'
    )
]

# from django.conf.urls import url
# from . import views

# urlpatterns = [
#     url(
#         r'^api/employee/(?P<pk>[0-9]+)$',
#         views.get_delete_update_employee,
#         name='get_delete_update_employee'
#     ),
#     url(
#         r'^api/employee/$',
#         views.get_post_employee,
#         name='get_post_employee'
#     )
# ]
