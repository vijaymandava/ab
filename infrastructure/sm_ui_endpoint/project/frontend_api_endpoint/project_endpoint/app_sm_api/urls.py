from django.conf.urls import re_path

from .views import home_get_test_list
from .views import home_left_load
from .views import approve_get_test_list
from .views import approve_approve_test_by_serial_number
from .views import approve_approve_test_by_lims_id
from .views import retrieve_get_test_list
from .views import retrieve_cancel_test_by_serial_number
from .views import retrieve_cancel_test_by_lims_id

from .views import roles_get_list
from .views import roles_get_role 
from .views import roles_create_role
from .views import roles_update_role
from .views import roles_delete_role
from .views import users_get_list
from .views import users_get_user
from .views import users_create_user
from .views import users_update_user
from .views import users_disable_user
from .views import users_enable_user

urlpatterns = [

    re_path(
        route=r'home/get_test_list',
        view=home_get_test_list,
        name='home_get_test_list'),

    re_path(
        route=r'home/left_load',
        view=home_left_load,
        name='home_left_load'),

    re_path(
        route=r'approve/get_test_list',
        view=approve_get_test_list,
        name='approve_get_test_list'),

    re_path(
        route=r'approve/approve_test_by_serial_number',
        view=approve_approve_test_by_serial_number,
        name='approve_approve_test_by_serial_number'),

    re_path(
        route=r'approve/approve_test_by_lims_id',
        view=approve_approve_test_by_lims_id,
        name='approve_approve_test_by_lims_id'),

    re_path(
        route=r'retrieve/get_test_list',
        view=retrieve_get_test_list,
        name='retrieve_get_test_list'),

    re_path(
        route=r'retrieve/cancel_test_by_serial_number',
        view=retrieve_cancel_test_by_serial_number,
        name='retrieve_cancel_test_by_serial_number'),

    re_path(
        route=r'retrieve/cancel_test_by_lims_id',
        view=   retrieve_cancel_test_by_lims_id,
        name = 'retrieve_cancel_test_by_lims_id'),

    re_path(
        route=r'roles/get_list',
        view=   roles_get_list,
        name = 'roles_get_list'),

    re_path(
        route=r'roles/get_role',
        view=   roles_get_role,
        name = 'roles_get_role'),

    re_path(
        route=r'roles/create_role',
        view=   roles_create_role,
        name = 'roles_create_role'),

    re_path(
        route=r'roles/update_role',
        view=   roles_update_role,
        name = 'roles_update_role'),

    re_path(
        route=r'roles/delete_role',
        view=   roles_delete_role,
        name = 'roles_delete_role'),

    re_path(
        route=r'users/get_list',
        view=   users_get_list,
        name = 'users_get_list'),

    re_path(
        route=r'users/get_user',
        view=   users_get_user,
        name = 'users_get_user'),

    re_path(
        route=r'users/create_user',
        view=   users_create_user,
        name = 'users_create_user'),

    re_path(
        route=r'users/update_user',
        view=   users_update_user,
        name = 'users_update_user'),

    re_path(
        route=r'users/disable_user',
        view=   users_disable_user,
        name = 'users_disable_user'),

    re_path(
        route=r'users/enable_user',
        view=   users_enable_user,
        name = 'users_enable_user'),

]
