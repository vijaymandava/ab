from datetime import datetime

from rest_framework import serializers
# from models import Snippet, LANGUAGE_CHOICES, STYLE_CHOICES

from common_testbench import common_logging

from app_sm_rx.models import CustomerToCmPostOrderRequest
from app_sm_rx.models import CustomerToCmPostOrderResponse
from app_sm_rx.models import CustomerToCmPostCancelRequest
from app_sm_rx.models import CustomerToCmPostCancelResponse
from app_sm_rx.models import CmToCustomerPostLoadedRequest
from app_sm_rx.models import CmToCustomerPostLoadedResponse
from app_sm_rx.models import CmToCustomerPostCanceledRequest
from app_sm_rx.models import CmToCustomerPostCanceledResponse
from app_sm_rx.models import CmToCustomerPostCompletedRequest
from app_sm_rx.models import CmToCustomerPostCompletedResponse
from app_sm_rx.models import CmToCustomerPostAssayStatusRequest
from app_sm_rx.models import CmToCustomerPostAssayStatusResponse
from app_sm_rx.models import CustomerToCmGetAssayDetailsRequest
from app_sm_rx.models import CustomerToCmGetAssayDetailsResponse
from app_sm_rx.models import CustomerToCmGetAssayStatusRequest
from app_sm_rx.models import CustomerToCmGetAssayStatusResponse
from app_sm_rx.models import CmToCustomerPostResultsRequest
from app_sm_rx.models import CmToCustomerPostResultsResponse
from app_sm_rx.models import CmToCustomerPostResultsOnApprovalRequest
from app_sm_rx.models import CmToCustomerPostResultsOnApprovalResponse

logger = common_logging.get_logger('lims')


class CustomerToCmPostOrderRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomerToCmPostOrderRequest
        fields = '__all__'
        # fields = ['id', 'title', 'code', 'linenos', 'language', 'style']


class CustomerToCmPostOrderResponseSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomerToCmPostOrderResponse
        fields = '__all__'


class CustomerToCmPostCancelRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomerToCmPostCancelRequest
        fields = '__all__'


class CustomerToCmPostCancelResponseSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomerToCmPostCancelResponse
        fields = '__all__'


class CmToCustomerPostLoadedRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = CmToCustomerPostLoadedRequest
        fields = '__all__'


class CmToCustomerPostLoadedResponseSerializer(serializers.ModelSerializer):
    class Meta:
        model = CmToCustomerPostLoadedResponse
        fields = '__all__'


class CmToCustomerPostCanceledRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = CmToCustomerPostCanceledRequest
        fields = '__all__'


class CmToCustomerPostCanceledResponseSerializer(serializers.ModelSerializer):
    class Meta:
        model = CmToCustomerPostCanceledResponse
        fields = '__all__'


class CmToCustomerPostCompletedRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = CmToCustomerPostCompletedRequest
        fields = '__all__'


class CmToCustomerPostCompletedResponseSerializer(serializers.ModelSerializer):
    class Meta:
        model = CmToCustomerPostCompletedResponse
        fields = '__all__'


# reference: https://www.django-rest-framework.org/api-guide/fields/#a-basic-custom-field
# 1/7/2021 8:47:11 PM
# class RmbCustomDateTime():
#     """
#     A date/time representation
#     """
#     def __init__(self, month, day, year, hour, minute, second, am_pm):
#         self.month = month
#         self.day = day
#         self.year = year
#         self.hour = hour
#         self.minute = minute
#         self.second = second
#         self.am_pm = am_pm

# serializers.DateTimeField

# class RmbCustomDateTimeFieldSerializer(serializers.DateTimeField):
#     """
#     objects are serialized to/from '1/7/2021 8:55:00 PM'
#     """
#     def to_representation(self, as_class):
#         print('------------ here 1 -------------')
#         return "{}/{}/{} {}:{}:{} {}".format(
#             as_class.month,
#             as_class.day,
#             as_class.year,
#             as_class.hour,
#             as_class.minute,
#             as_class.second,
#             as_class.am_pm)

#     def to_internal_value(self, as_string):
#         date, time, am_pm = as_string.split(' ')
#         month, day, year = date.split('/')
#         hour, minute, second = time.split('/')
#         rcdt = RmbCustomDateTime(
#             month, day, year, hour, minute, second, am_pm)
#         return rcdt

class CmToCustomerPostAssayStatusRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = CmToCustomerPostAssayStatusRequest
        fields = ['instr_id', 'lims_id', 'elapsed_assay_time', 'serial_number', 'status', 'status_flag', 'status_update_time']
        # fields = '__all__'
        # fields = ['instr_id', 'lims_id', 'elapsed_assay_time', 'serial_number', 'status', 'status_flag']

    status_update_time = serializers.CharField(max_length=100)

    def validate_status_update_time(self, value):
        """
        Validate the incoming data
        """
        logger.info('--- field validate (status_update_time) received  {}'.format(repr(value)))
        # #raise serializers.ValidationError("zonazonazona!")
        # validated_date_time_object = datetime.now()
        # return validated_date_time_object
        value = datetime.now().isoformat()
        logger.info('--- field validate (status_update_time) returning {}'.format(repr(value)))
        return value

    def validate(self, data):
        """
        Object-level validation
        """
        logger.info('--- object validate received type(data): {}'.format(type(data)))
        logger.info('--- object validate received repr(data): {}'.format(repr(data)))
        # map Native fields to Model fields
        # To do this: add/remove/rename the native ("data") fields to be consistent
        # with those defined in the Model. Then call super.validate()  [ZONA need to test this last step "super()"...]
        data['status_update_time_db'] = data.pop('status_update_time')
        return data

    def create(self, validated_data):
        logger.info('--- inbound (create) 1: {}'.format(validated_data))
        rtn = CmToCustomerPostAssayStatusRequest.objects.create(**validated_data)
        logger.info('--- inbound (create) 2')
        return rtn

    def update(self, instance, validated_data):
        logger.info('--- inbound (update) 1')
        assert False, "code is untested... zona"
        instance.status_update_time_db = validated_data.get('status_update_time', instance.status_update_time_db)
        super().update(instance, validated_data)
        instance.save()
        return instance

    def to_representation(self, instance):
        # map Model fields to Native fields
        # to do this: update the Model instance to add/update fields to be consistent
        # with those identified in 'fields' above.  Then use super.to_representation()
        logger.info('--- outbound (to_representation) 1: instance = {}'.format(repr(instance)))
        instance.status_update_time = instance.status_update_time_db
        logger.info('--- outbound (to_representation) 2: instance = {}'.format(repr(instance)))
        rtn = super().to_representation(instance)
        logger.info('--- outbound (to_representation) 3: returning {}'.format(repr(rtn)))
        return rtn


        # return {
        #     'score': instance.score,
        #     'player_name': instance.player_name
        # }




class CmToCustomerPostAssayStatusResponseSerializer(serializers.ModelSerializer):
    class Meta:
        model = CmToCustomerPostAssayStatusResponse
        fields = '__all__'


class CustomerToCmGetAssayDetailsRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomerToCmGetAssayDetailsRequest
        fields = '__all__'


class CustomerToCmGetAssayDetailsResponseSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomerToCmGetAssayDetailsResponse
        fields = '__all__'


class CustomerToCmGetAssayStatusRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomerToCmGetAssayStatusRequest
        fields = '__all__'


class CustomerToCmGetAssayStatusResponseSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomerToCmGetAssayStatusResponse
        fields = '__all__'


class CmToCustomerPostResultsRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = CmToCustomerPostResultsRequest
        fields = '__all__'


class CmToCustomerPostResultsResponseSerializer(serializers.ModelSerializer):
    class Meta:
        model = CmToCustomerPostResultsResponse
        fields = '__all__'


class CmToCustomerPostResultsOnApprovalRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = CmToCustomerPostResultsOnApprovalRequest
        fields = '__all__'


class CmToCustomerPostResultsOnApprovalResponseSerializer(serializers.ModelSerializer):
    class Meta:
        model = CmToCustomerPostResultsOnApprovalResponse
        fields = '__all__'

