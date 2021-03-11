from django.urls import path
from django.conf.urls import include, url
from rest_framework.urlpatterns import format_suffix_patterns

from app_sm_rx import views

urlpatterns = [

    ## path('welcome', views.get_welcome),
    # path('welcome/', views.get_welcome),
    path('welcome/', views.get_welcome),
    path('welcome', views.get_welcome),

    # # path('smtolims/postAssayStatus', views.zona_post_assay_status),
    # # path('smtolims/postAssayStatus/', views.zona_post_assay_status),

    path('postOrder/', views.post_order_request_list),
    path('postCancel/', views.post_cancel_request_list),
    path('postLoaded/', views.post_loaded_request_list),
    path('postCanceled/', views.post_canceled_request_list),
    path('postCompleted/', views.post_completed_request_list),
    path('smtolims/postAssayStatus', views.post_assay_status_request_list),
    #path('smtolims/postAssayStatus/', views.post_assay_status_request_list),
    path('getAssayDetails/', views.get_assay_details_request_list),
    path('getAssayStatus/', views.get_assay_status_request_list),
    path('postResults/', views.post_results_request_list),
    path('postResultsOnApproval/', views.post_results_on_approval_request_list),

    path('postOrder/<int:pk>/', views.post_order_request_detail),
    path('postCancel/<int:pk>/', views.post_cancel_request_detail),
    path('postLoaded/<int:pk>/', views.post_loaded_request_detail),
    path('postCanceled/<int:pk>/', views.post_canceled_request_detail),
    path('postCompleted/<int:pk>/', views.post_completed_request_detail),
    path('postAssayStatus/<int:pk>/', views.post_assay_status_request_detail),
    path('getAssayDetails/<int:pk>/', views.get_assay_details_request_detail),
    path('getAssayStatus/<int:pk>/', views.get_assay_status_request_detail),
    path('postResults/<int:pk>/', views.post_results_request_detail),
    path('postResultsOnApproval/<int:pk>/', views.post_results_on_approval_request_detail),

    # url(
    #     r'.*',
    #     views.default_page,
    #     name='default_page'),
]

# this is to accomodate <int:pk> I believe
urlpatterns = format_suffix_patterns(urlpatterns)
