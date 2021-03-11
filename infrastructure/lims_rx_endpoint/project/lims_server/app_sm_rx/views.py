from django.http import JsonResponse

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView

from common_testbench import common_logging

from app_sm_rx.models import CustomerToCmPostOrderRequest
from app_sm_rx.models import CustomerToCmPostCancelRequest
from app_sm_rx.models import CmToCustomerPostLoadedRequest
from app_sm_rx.models import CmToCustomerPostCanceledRequest
from app_sm_rx.models import CmToCustomerPostCompletedRequest
from app_sm_rx.models import CmToCustomerPostAssayStatusRequest
from app_sm_rx.models import CustomerToCmGetAssayDetailsRequest
from app_sm_rx.models import CustomerToCmGetAssayStatusRequest
from app_sm_rx.models import CmToCustomerPostResultsRequest
from app_sm_rx.models import CmToCustomerPostResultsOnApprovalRequest

# from app_sm_rx.serializers import WelcomeSerializer
from app_sm_rx.serializers import CustomerToCmPostOrderRequestSerializer
from app_sm_rx.serializers import CustomerToCmPostCancelRequestSerializer
from app_sm_rx.serializers import CmToCustomerPostLoadedRequestSerializer
from app_sm_rx.serializers import CmToCustomerPostCanceledRequestSerializer
from app_sm_rx.serializers import CmToCustomerPostCompletedRequestSerializer
from app_sm_rx.serializers import CmToCustomerPostAssayStatusRequestSerializer
from app_sm_rx.serializers import CustomerToCmGetAssayDetailsRequestSerializer
from app_sm_rx.serializers import CustomerToCmGetAssayStatusRequestSerializer
from app_sm_rx.serializers import CmToCustomerPostResultsRequestSerializer
from app_sm_rx.serializers import CmToCustomerPostResultsOnApprovalRequestSerializer


logger = common_logging.get_logger('lims')


# # -----------------------------
# # API Endpoint - /welcome
# class WelcomeView(APIView):
#     def get(self, request):
#         HTTP_200_OK

#         return Response({'message': 'welcome'})


@api_view(['GET', 'POST'])
def get_welcome(request, format=None):
    content = {'message': 'welcome'}
    return Response(content, status=status.HTTP_200_OK)


#     class MyOwnView(APIView):
#         def get(self, request):
#             return Response({'some': 'data'})

#     data = {'message': 'Welcome'}

#     return JsonResponse({'message': 'Welcome'})




# --------------- 7.1 ---------------
# API Endpoint - /postOrder 
@api_view(['GET', 'POST'])
def post_order_request_list(request, format=None):
    """
    List all Order Requests, or create a new Order Request
    """
    logger.info(request)

    if request.method == 'GET':
        order_requests = CustomerToCmPostOrderRequest.objects.all()
        serializer = CustomerToCmPostOrderRequestSerializer(order_requests, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = CustomerToCmPostOrderRequestSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def post_order_request_detail(request, pk, format=None):
    """
    Retrieve, update or delete an Order Request
    """
    try:
        order_request = CustomerToCmPostOrderRequest.objects.get(pk=pk)
    except CustomerToCmPostOrderRequest.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = CustomerToCmPostOrderRequestSerializer(order_request)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = CustomerToCmPostOrderRequestSerializer(order_request, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        order_request.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# --------------- 8.6 ---------------
# API Endpoint - /postCancel 
@api_view(['GET', 'POST'])
def post_cancel_request_list(request, format=None):
    """
    List all Order Requests, or create a new Order Request
    """
    if request.method == 'GET':
        order_requests = CustomerToCmPostCancelRequest.objects.all()
        serializer = CustomerToCmPostCancelRequestSerializer(order_requests, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = CustomerToCmPostCancelRequestSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def post_cancel_request_detail(request, pk, format=None):
    """
    Retrieve, update or delete an Order Request
    """
    try:
        order_request = CustomerToCmPostCancelRequest.objects.get(pk=pk)
    except CustomerToCmPostCancelRequest.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = CustomerToCmPostCancelRequestSerializer(order_request)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = CustomerToCmPostCancelRequestSerializer(order_request, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        order_request.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# # --------------- 9.1 ---------------
# API Endpoint - /postLoaded
@api_view(['GET', 'POST'])
def post_loaded_request_list(request, format=None):
    """
    List all Loaded Requests, or create a new Loaded Request
    """
    if request.method == 'GET':
        order_requests = CmToCustomerPostLoadedRequest.objects.all()
        serializer = CmToCustomerPostLoadedRequestSerializer(order_requests, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = CmToCustomerPostLoadedRequestSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def post_loaded_request_detail(request, pk, format=None):
    """
    Retrieve, update or delete a Loaded Request
    """
    try:
        order_request = CmToCustomerPostLoadedRequest.objects.get(pk=pk)
    except CmToCustomerPostLoadedRequest.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = CmToCustomerPostLoadedRequestSerializer(order_request)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = CmToCustomerPostLoadedRequestSerializer(order_request, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        order_request.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# --------------- 9.2 ---------------
# API Endpoint - /postCanceled
@api_view(['GET', 'POST'])
def post_canceled_request_list(request, format=None):
    """
    List all Canceled Requests, or create a new Canceled Request
    """
    if request.method == 'GET':
        order_requests = CmToCustomerPostCanceledRequest.objects.all()
        serializer = CmToCustomerPostCanceledRequestSerializer(order_requests, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = CmToCustomerPostCanceledRequestSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def post_canceled_request_detail(request, pk, format=None):
    """
    Retrieve, update or delete a Canceled Request
    """
    try:
        order_request = CmToCustomerPostCanceledRequest.objects.get(pk=pk)
    except CmToCustomerPostCanceledRequest.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = CmToCustomerPostCanceledRequestSerializer(order_request)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = CmToCustomerPostCanceledRequestSerializer(order_request, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        order_request.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# --------------- 9.3 ---------------
# API Endpoint - /postCompleted
@api_view(['GET', 'POST'])
def post_completed_request_list(request, format=None):
    """
    List all Completed Requests, or create a new Completed Request
    """
    if request.method == 'GET':
        order_requests = CmToCustomerPostCompletedRequest.objects.all()
        serializer = CmToCustomerPostCompletedRequestSerializer(order_requests, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = CmToCustomerPostCompletedRequestSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def post_completed_request_detail(request, pk, format=None):
    """
    Retrieve, update or delete a Completed Request
    """
    try:
        order_request = CmToCustomerPostCompletedRequest.objects.get(pk=pk)
    except CmToCustomerPostCompletedRequest.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = CmToCustomerPostCompletedRequestSerializer(order_request)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = CmToCustomerPostCompletedRequestSerializer(order_request, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        order_request.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# --------------- 9.4 ---------------
# API Endpoint - /postAssayStatus
@api_view(['GET', 'POST'])
def post_assay_status_request_list(request, format=None):
    """
    List all AssayStatus Requests, or create a new AssayStatus Request
    """
    logger.info('--- inbound: request.data={}'.format(request.data))

    if request.method == 'GET':
        order_requests = CmToCustomerPostAssayStatusRequest.objects.all()
        serializer = CmToCustomerPostAssayStatusRequestSerializer(order_requests, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = CmToCustomerPostAssayStatusRequestSerializer(data=request.data)
        if serializer.is_valid():
            logger.info('--- constructing from data: type(serializer)={}'.format(type(serializer)))
            logger.info('--- constructing from data: type(serializer.data)={}'.format(type(serializer.validated_data)))
            logger.info('--- constructing from data: repr(serializer.data)={}'.format(repr(serializer.validated_data)))
            serializer.save()
            logger.info('--- constructing from data: save is done')
            quick_test = serializer.data 
            logger.info('--- constructing from data: save is done')
            logger.info('--- constructing from data: save is done {}'.format(repr(serializer.data)))
            return Response(serializer.data, status.HTTP_201_CREATED)
        # log the error
        logger.info('--- error when parsing Datetime ----')
        logger.info('{}'.format(repr(request)))
        logger.info('{}'.format(repr(request.data)))
        logger.info('{}'.format(repr(serializer.errors)))
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def post_assay_status_request_detail(request, pk, format=None):
    """
    Retrieve, update or delete a AssayStatus Request
    """
    try:
        order_request = CmToCustomerPostAssayStatusRequest.objects.get(pk=pk)
    except CmToCustomerPostAssayStatusRequest.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = CmToCustomerPostAssayStatusRequestSerializer(order_request)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = CmToCustomerPostAssayStatusRequestSerializer(order_request, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        order_request.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# --------- 10.1.1 --------
# API Endpoint - /getAssayDetails
@api_view(['GET', 'POST'])
def get_assay_details_request_list(request, format=None):
    """
    List all AssayDetails Requests, or create a new AssayDetails Request
    """
    if request.method == 'GET':
        order_requests = CustomerToCmGetAssayDetailsRequest.objects.all()
        serializer = CustomerToCmGetAssayDetailsRequestSerializer(order_requests, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = CustomerToCmGetAssayDetailsRequestSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def get_assay_details_request_detail(request, pk, format=None):
    """
    Retrieve, update or delete a AssayDetails Request
    """
    try:
        order_request = CustomerToCmGetAssayDetailsRequest.objects.get(pk=pk)
    except CustomerToCmGetAssayDetailsRequest.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = CustomerToCmGetAssayDetailsRequestSerializer(order_request)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = CustomerToCmGetAssayDetailsRequestSerializer(order_request, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        order_request.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# --------- 10.1.2--------
# API Endpoint - /getAssayStatus
def get_assay_status_request_list(request, format=None):
    """
    List all AssayStatus Requests, or create a new AssayStatus Request
    """
    if request.method == 'GET':
        order_requests = CustomerToCmGetAssayStatusRequest.objects.all()
        serializer = CustomerToCmGetAssayStatusRequestSerializer(order_requests, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = CustomerToCmGetAssayStatusRequestSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def get_assay_status_request_detail(request, pk, format=None):
    """
    Retrieve, update or delete a AssayStatus Request
    """
    try:
        order_request = CustomerToCmGetAssayStatusRequest.objects.get(pk=pk)
    except CustomerToCmGetAssayStatusRequest.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = CustomerToCmGetAssayStatusRequestSerializer(order_request)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = CustomerToCmGetAssayStatusRequestSerializer(order_request, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        order_request.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# ---------11--------
# API Endpoint - /postResults 
@api_view(['GET', 'POST'])
def post_results_request_list(request, format=None):
    """
    List all Results Requests, or create a new Results Request
    """
    if request.method == 'GET':
        order_requests = CmToCustomerPostResultsRequest.objects.all()
        serializer = CmToCustomerPostResultsRequestSerializer(order_requests, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = CmToCustomerPostResultsRequestSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def post_results_request_detail(request, pk, format=None):
    """
    Retrieve, update or delete a Results Request
    """
    try:
        order_request = CmToCustomerPostResultsRequest.objects.get(pk=pk)
    except CmToCustomerPostResultsRequest.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = CmToCustomerPostResultsRequestSerializer(order_request)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = CmToCustomerPostResultsRequestSerializer(order_request, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        order_request.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# ---------13--------
# API Endpoint - /postResultsOnApproval 
@api_view(['GET', 'POST'])
def post_results_on_approval_request_list(request, format=None):
    """
    List all ResultsOnApproval Requests, or create a new ResultsOnApproval Request
    """
    if request.method == 'GET':
        order_requests = CmToCustomerPostResultsOnApprovalRequest.objects.all()
        serializer = CmToCustomerPostResultsOnApprovalRequestSerializer(order_requests, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = CmToCustomerPostResultsOnApprovalRequestSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def post_results_on_approval_request_detail(request, pk, format=None):
    """
    Retrieve, update or delete a ResultsOnApproval Request
    """
    try:
        order_request = CmToCustomerPostResultsOnApprovalRequest.objects.get(pk=pk)
    except CmToCustomerPostResultsOnApprovalRequest.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = CmToCustomerPostResultsOnApprovalRequestSerializer(order_request)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = CmToCustomerPostResultsOnApprovalRequestSerializer(order_request, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        order_request.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

