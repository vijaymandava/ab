from django.db import models



# -----------------------------------------------
# This file establishes database schema that
# implements the customer-facing Web-LIMS API as defined in
# TSVNNN Growth Direct LIMS Integration Specification R4.0 Rev "B"
# References to chapter in the spec are provided, see "------ X.Y ------"

class LimsCustomerDefines():
    MAXLEN_INSTR_ID = 9
    MAXLEN_LIMS_ID = 200  # zona what is max length?
    MAXLEN_SERIAL_NUMBER = 9
    MAXLEN_SAMPLE_ID = 20
    MAXLEN_LOT_BATCH_ID = 7
    MAXLEN_METHOD_NAME = 15
    MAXLEN_HANDLING_RULE_NAME = 15
    MAXLEN_ACTION_ALERT_LEVEL_NAME = 15
    MAXLEN_AAL_CFU_THRESHOLD_ALERT = 4
    MAXLEN_AAL_CFU_THRESHOLD_ACTION = 4
    MAXLEN_AAL_CFU_THRESHOLD_SPECIFICATION = 4
    MAXLEN_AAL_CFU_THRESHOLD_PASS = 4
    MAXLEN_COMMENT = 60

    MAXLEN_STATUS_STATE = 20
    MAXLEN_STATUS_TYPE = 50
    MAXLEN_STATUS_MESSAGE = 500

    MAXLEN_OPERATORNAME = 30
    MAXLEN_DURATION_HOURS = 20  # ZONA DevOps 3069

    MAXLEN_ACKNOWLEDGE = 20

    MAXLEN_CASSETTE_ID = 20 # zona really ?!
    MAXLEN_TEMPERATURE = 5
    MAXLEN_MEDIA_TYPE = 20

    MAXLEN_CFU_COUNT = 10
    MAXLEN_MOLD_COUNT = 10
    MAXLEN_APPROVAL_MESSAGE = 10

    MAXLEN_STATUS_FLAG = 300  # possible duplicate/reedundant with...


# zona to get around
# RuntimeError: Model class models.CustomerToCmPostOrderRequest doesn't declare an explicit app_label and isn't in an application in INSTALLED_APPS.
# apply workaround discussed at
# https://stackoverflow.com/questions/45268246/model-class-doesnt-declare-an-explicit-app-label-and-isnt-in-an-application-in
class MyBaseModel(models.Model):

    foo = "bar"
    #app_label = 'blahblah'
    class Meta:
        abstract = True  # specify this model as an Abstract Model
        app_label = 'app_sm_rx'


# --------------- 7.1 ---------------
# API Endpoint - /postOrder 
# {
# "instr_id": "string",
# "lims_id": "string",
# "serial_number": "string",
# "sample_id": "string",
# "lot_batch_id": "string",
# "method_name": "string",
# "handling_rule_name": "string",
# "action_alert_level_name": "string",
# "aal_cfu_threshold_alert": "string",
# "aal_cfu_threshold_action": "string",
# "aal_cfu_threshold_specification": "string",
# "aal_cfu_threshold_pass": "string",
# "comment": "string",
# }
class CustomerToCmPostOrderRequest(MyBaseModel):
    instr_id = models.CharField(max_length=LimsCustomerDefines.MAXLEN_INSTR_ID, blank=True)
    lims_id = models.CharField(max_length=LimsCustomerDefines.MAXLEN_LIMS_ID, blank=True)
    serial_number = models.CharField(max_length=LimsCustomerDefines.MAXLEN_SERIAL_NUMBER, blank=True)
    sample_id = models.CharField(max_length=LimsCustomerDefines.MAXLEN_SAMPLE_ID, blank=True)
    lot_batch_id = models.CharField(max_length=LimsCustomerDefines.MAXLEN_LOT_BATCH_ID, blank=True)
    method_name = models.CharField(max_length=LimsCustomerDefines.MAXLEN_METHOD_NAME, blank=True)
    handling_rule_name = models.CharField(max_length=LimsCustomerDefines.MAXLEN_HANDLING_RULE_NAME, blank=True)
    action_alert_level_name = models.CharField(max_length=LimsCustomerDefines.MAXLEN_ACTION_ALERT_LEVEL_NAME, blank=True)
    aal_cfu_threshold_alert = models.CharField(max_length=LimsCustomerDefines.MAXLEN_AAL_CFU_THRESHOLD_ALERT, blank=True)
    aal_cfu_threshold_action = models.CharField(max_length=LimsCustomerDefines.MAXLEN_AAL_CFU_THRESHOLD_ACTION, blank=True)
    aal_cfu_threshold_specification = models.CharField(max_length=LimsCustomerDefines.MAXLEN_AAL_CFU_THRESHOLD_SPECIFICATION, blank=True)
    aal_cfu_threshold_pass = models.CharField(max_length=LimsCustomerDefines.MAXLEN_AAL_CFU_THRESHOLD_PASS, blank=True)
    comment = models.CharField(max_length=LimsCustomerDefines.MAXLEN_COMMENT, blank=True)

# API Endpoint - /postResponse 
# {
# "status": "success/failure"
# "status_type": "string"
# "status_message": "string"
# }
class CustomerToCmPostOrderResponse(MyBaseModel):
    status = models.CharField(max_length=LimsCustomerDefines.MAXLEN_STATUS_STATE, blank=True)
    status_type = models.CharField(max_length=LimsCustomerDefines.MAXLEN_STATUS_TYPE, blank=True)
    status_message = models.CharField(max_length=LimsCustomerDefines.MAXLEN_STATUS_MESSAGE, blank=True)


# --------------- 8.6 ---------------
# API Endpoint - /postCancel 
#  {
# "instr_id": "string",
# "lims_id": "string",
# "serial_number": "string",
# "sample_id": "string",
# "lot_batch_id": "string",
#  }	
class CustomerToCmPostCancelRequest(MyBaseModel):
    instr_id = models.CharField(max_length=LimsCustomerDefines.MAXLEN_INSTR_ID, blank=True)
    lims_id = models.CharField(max_length=LimsCustomerDefines.MAXLEN_LIMS_ID, blank=True)
    serial_number = models.CharField(max_length=LimsCustomerDefines.MAXLEN_SERIAL_NUMBER, blank=True)
    sample_id = models.CharField(max_length=LimsCustomerDefines.MAXLEN_SAMPLE_ID, blank=True)
    lot_batch_id = models.CharField(max_length=LimsCustomerDefines.MAXLEN_LOT_BATCH_ID, blank=True)

# API Endpoint - /postResponse 
# {
# "status": "success/failure"
# "status_type": "string"
# "status_message": "string"
# }
class CustomerToCmPostCancelResponse(MyBaseModel):
    status = models.CharField(max_length=LimsCustomerDefines.MAXLEN_STATUS_STATE, blank=True)
    status_type = models.CharField(max_length=LimsCustomerDefines.MAXLEN_STATUS_TYPE, blank=True)
    status_message = models.CharField(max_length=LimsCustomerDefines.MAXLEN_STATUS_MESSAGE, blank=True)


# # --------------- 9.1 ---------------
# API Endpoint - /postLoaded
# {
# "instr_id": "string",
# "lims_id": "string",
# "serial_number": "string",
# "loaded_on": "string",
# "loaded_by": "string",
# }
class CmToCustomerPostLoadedRequest(MyBaseModel):
    instr_id = models.CharField(max_length=LimsCustomerDefines.MAXLEN_INSTR_ID, blank=True)
    lims_id = models.CharField(max_length=LimsCustomerDefines.MAXLEN_LIMS_ID, blank=True)
    serial_number = models.CharField(max_length=LimsCustomerDefines.MAXLEN_SERIAL_NUMBER, blank=True)
    loaded_on = models.DateTimeField(blank=True, null=True)
    loaded_by = models.CharField(max_length=LimsCustomerDefines.MAXLEN_OPERATORNAME, blank=True)

# API Endpoint - /postResponse 
# {
# "acknowledge": "string",
# }
class CmToCustomerPostLoadedResponse(MyBaseModel):
       acknowledge = models.CharField(max_length=LimsCustomerDefines.MAXLEN_ACKNOWLEDGE, blank=True)
   

# --------------- 9.2 ---------------
# API Endpoint - /postCanceled
# {
# "instr_id": "string",
# "lims_id": "string",
# "serial_number": "string",
# "canceled_on": "string",
# "canceled_by": "string",
# }
class CmToCustomerPostCanceledRequest(MyBaseModel):
    instr_id = models.CharField(max_length=LimsCustomerDefines.MAXLEN_INSTR_ID, blank=True)
    lims_id = models.CharField(max_length=LimsCustomerDefines.MAXLEN_LIMS_ID, blank=True)
    serial_number = models.CharField(max_length=LimsCustomerDefines.MAXLEN_SERIAL_NUMBER, blank=True)
    canceled_on = models.DateTimeField(blank=True, null=True)
    canceled_by = models.CharField(max_length=LimsCustomerDefines.MAXLEN_OPERATORNAME, blank=True)

# API Endpoint - /postResponse 
# {
# "acknowledge": "string",
# }
class CmToCustomerPostCanceledResponse(MyBaseModel):
       acknowledge = models.CharField(max_length=LimsCustomerDefines.MAXLEN_ACKNOWLEDGE, blank=True)
   

# --------------- 9.3 ---------------
# API Endpoint - /postCompleted
# {
# "instr_id": "string",
# "lims_id": "string",
# "serial_number": "string",
# "completed_on": "string",
# }
class CmToCustomerPostCompletedRequest(MyBaseModel):
    instr_id = models.CharField(max_length=LimsCustomerDefines.MAXLEN_INSTR_ID, blank=True)
    lims_id = models.CharField(max_length=LimsCustomerDefines.MAXLEN_LIMS_ID, blank=True)
    serial_number = models.CharField(max_length=LimsCustomerDefines.MAXLEN_SERIAL_NUMBER, blank=True)
    completed_on = models.DateTimeField(blank=True, null=True)


# API Endpoint - /postResponse 
# {
# "acknowledge": "string",
# }
class CmToCustomerPostCompletedResponse(MyBaseModel):
    acknowledge = models.CharField(max_length=LimsCustomerDefines.MAXLEN_ACKNOWLEDGE, blank=True)


# --------------- 9.4 ---------------
# API Endpoint - /postAssayStatus
# {
# "instr_id": "string",
# 			"lims_id": "string",
# 			"serial_number": "string",
# 			"elapsed_assay_time": "string",
# 			"status": "string",
# "status_flag": "string",
# 			"status_update_time": "string",
# }
class CmToCustomerPostAssayStatusRequest(MyBaseModel):
    instr_id = models.CharField(max_length=LimsCustomerDefines.MAXLEN_INSTR_ID, blank=True)
    lims_id = models.CharField(max_length=LimsCustomerDefines.MAXLEN_LIMS_ID, blank=True)
    serial_number = models.CharField(max_length=LimsCustomerDefines.MAXLEN_SERIAL_NUMBER, blank=True)
    elapsed_assay_time = models.CharField(max_length=LimsCustomerDefines.MAXLEN_DURATION_HOURS, blank=True)
    status = models.CharField(max_length=LimsCustomerDefines.MAXLEN_STATUS_STATE, blank=True)
    status_flag = models.CharField(max_length=LimsCustomerDefines.MAXLEN_STATUS_FLAG, blank=True)
    status_update_time_db = models.DateTimeField(blank=True, null=True)
    # status_update_time = models.CharField(max_length=64, blank=True)

    def __str__(self):
        return "blahblah {} {} {} {} {} {} {}".format(
            self.instr_id,
            self.lims_id,
            self.serial_number,
            self.elapsed_assay_time,
            self.status,
            self.status_flag,
            self.status_update_time_db)


# API Endpoint - /postResponse 
# {
# "acknowledge": "string",
# }
class CmToCustomerPostAssayStatusResponse(MyBaseModel):
       acknowledge = models.CharField(max_length=LimsCustomerDefines.MAXLEN_ACKNOWLEDGE, blank=True)

# --------- 10.1.1 --------
# API Endpoint - /getAssayDetails
# {
# "instr_id": "string",
# "lims_id": "string",
# "sample_id": “string”,
# "serial_number": "string",
# }
class CustomerToCmGetAssayDetailsRequest(MyBaseModel):
    instr_id = models.CharField(max_length=LimsCustomerDefines.MAXLEN_INSTR_ID, blank=True)
    lims_id = models.CharField(max_length=LimsCustomerDefines.MAXLEN_LIMS_ID, blank=True)
    sample_id = models.CharField(max_length=LimsCustomerDefines.MAXLEN_SAMPLE_ID, blank=True)
    serial_number = models.CharField(max_length=LimsCustomerDefines.MAXLEN_SERIAL_NUMBER, blank=True)

# API Endpoint - /getResponse 
# {
# "instr_id": "string",
# "lims_id": "string",
# "cassette_id": "string",
# "serial_number": "string",
# "lot_batch_id": "string",
# "incubation _start": "string"
# "incubation _end": "string",
# "target_temperature": "string",
# "media_type": "string",
# "method_name": "string",
# "action_alert_level_name": "string",
# "ordered_on": "string",
# "ordered_by": "string",
# }
class CustomerToCmGetAssayDetailsResponse(MyBaseModel):
    instr_id = models.CharField(max_length=LimsCustomerDefines.MAXLEN_INSTR_ID, blank=True)
    lims_id = models.CharField(max_length=LimsCustomerDefines.MAXLEN_LIMS_ID, blank=True)
    cassette_id = models.CharField(max_length=LimsCustomerDefines.MAXLEN_CASSETTE_ID, blank=True)
    serial_number = models.CharField(max_length=LimsCustomerDefines.MAXLEN_SERIAL_NUMBER, blank=True)
    lot_batch_id = models.CharField(max_length=LimsCustomerDefines.MAXLEN_LOT_BATCH_ID, blank=True)
    incubation_start = models.DateTimeField(blank=True, null=True)
    incubation_end = models.DateTimeField(blank=True, null=True)
    target_temperature = models.CharField(max_length=LimsCustomerDefines.MAXLEN_TEMPERATURE, blank=True)
    media_type = models.CharField(max_length=LimsCustomerDefines.MAXLEN_MEDIA_TYPE, blank=True)
    action_alert_level = models.CharField(max_length=LimsCustomerDefines.MAXLEN_ACTION_ALERT_LEVEL_NAME, blank=True)
    ordered_on = models.DateTimeField(blank=True, null=True)
    ordered_by = models.CharField(max_length=LimsCustomerDefines.MAXLEN_OPERATORNAME, blank=True)


# --------- 10.1.2--------
# API Endpoint - /getAssayStatus
# {
# "instr_id": "string",
# "lims_id": "string",
# "sample_id": "string",
# "serial_number": "string",
# }
class CustomerToCmGetAssayStatusRequest(MyBaseModel):
    instr_id = models.CharField(max_length=LimsCustomerDefines.MAXLEN_INSTR_ID, blank=True)
    lims_id = models.CharField(max_length=LimsCustomerDefines.MAXLEN_LIMS_ID, blank=True)
    sample_id = models.CharField(max_length=LimsCustomerDefines.MAXLEN_SAMPLE_ID, blank=True)
    serial_number = models.CharField(max_length=LimsCustomerDefines.MAXLEN_SERIAL_NUMBER, blank=True)

# API Endpoint - /getResponse 
# {
# "instr_id": "string",
# "lims_id": "string",
# "serial_number": "string",
# "status": "string",
# "loaded_on": "string",
# "loaded_by": "string",
# "elapsed_assay_time": "string",
# "status_flags": "string",
# "status_update_time": "string",
# }
class CustomerToCmGetAssayStatusResponse(MyBaseModel):
    instr_id = models.CharField(max_length=LimsCustomerDefines.MAXLEN_INSTR_ID, blank=True)
    lims_id = models.CharField(max_length=LimsCustomerDefines.MAXLEN_LIMS_ID, blank=True)
    sample_id = models.CharField(max_length=LimsCustomerDefines.MAXLEN_SAMPLE_ID, blank=True)
    status = models.CharField(max_length=LimsCustomerDefines.MAXLEN_STATUS_STATE, blank=True)
    loaded_on = models.DateTimeField(blank=True, null=True)
    loaded_by = models.CharField(max_length=LimsCustomerDefines.MAXLEN_OPERATORNAME, blank=True)
    elapsed_assay_time = models.CharField(max_length=LimsCustomerDefines.MAXLEN_DURATION_HOURS, blank=True)
    status_flag = models.CharField(max_length=LimsCustomerDefines.MAXLEN_STATUS_FLAG, blank=True)
    status_update_time = models.DateTimeField(blank=True, null=True)


# ---------11--------
# API Endpoint - /postResults 
# {
# 			"instr_id": "string",
# 			"lims_id": "string",
# 			"serial_number": "string",
# 			"sample_id": "string",
# 			"lot_batch_id": "string",
# 			"method_name": "string",
# 			"action_alert_level_name": "string",
# 			"handling_rule_name": "string",
# "cfu_count": "string",
# 			"mold_count": "string",
# 			"status": "string",
# 			"test_status": "string",
# 			"approval": "string",
# 		 }
class CmToCustomerPostResultsRequest(MyBaseModel):
    instr_id = models.CharField(max_length=LimsCustomerDefines.MAXLEN_INSTR_ID, blank=True)
    lims_id = models.CharField(max_length=LimsCustomerDefines.MAXLEN_LIMS_ID, blank=True)
    serial_number = models.CharField(max_length=LimsCustomerDefines.MAXLEN_SERIAL_NUMBER, blank=True)
    sample_id = models.CharField(max_length=LimsCustomerDefines.MAXLEN_SAMPLE_ID, blank=True)
    lot_batch_id = models.CharField(max_length=LimsCustomerDefines.MAXLEN_LOT_BATCH_ID, blank=True)
    method_name = models.CharField(max_length=LimsCustomerDefines.MAXLEN_METHOD_NAME, blank=True)
    handling_rule_name = models.CharField(max_length=LimsCustomerDefines.MAXLEN_HANDLING_RULE_NAME, blank=True)
    action_alert_level_name = models.CharField(max_length=LimsCustomerDefines.MAXLEN_ACTION_ALERT_LEVEL_NAME, blank=True)
    cfu_count = models.CharField(max_length=LimsCustomerDefines.MAXLEN_CFU_COUNT, blank=True)
    mold_count = models.CharField(max_length=LimsCustomerDefines.MAXLEN_MOLD_COUNT, blank=True)
    status = models.CharField(max_length=LimsCustomerDefines.MAXLEN_STATUS_STATE, blank=True) # zona status_state?
    test_status = models.CharField(max_length=LimsCustomerDefines.MAXLEN_STATUS_STATE, blank=True) # zona status_state?
    approval = models.CharField(max_length=LimsCustomerDefines.MAXLEN_APPROVAL_MESSAGE, blank=True) 

# API Endpoint - /postResponse
# {
# "acknowledge-results": "string",
#                              }
class CmToCustomerPostResultsResponse(MyBaseModel):
       acknowledge = models.CharField(max_length=LimsCustomerDefines.MAXLEN_ACKNOWLEDGE, blank=True)


# ---------13--------
# API Endpoint - /postResultsOnApproval 
# {
# 			"instr_id": "string",
# 			"lims_id": "string",
# 			"serial_number": "string",
# 			"sample_id": "string",
# 			"lot_batch_id": "string",
# 			"method_name": "string",
# 			"action_alert_level_name": "string",
# 			"handling_rule_name": "string",
# "cfu_count": "string",
# 			"mold_count": "string",
# 			"status": "string",
# 			"test_status": "string",
# 			"approval": "string",
# 		 }
class CmToCustomerPostResultsOnApprovalRequest(MyBaseModel):
    instr_id = models.CharField(max_length=LimsCustomerDefines.MAXLEN_INSTR_ID, blank=True)
    lims_id = models.CharField(max_length=LimsCustomerDefines.MAXLEN_LIMS_ID, blank=True)
    serial_number = models.CharField(max_length=LimsCustomerDefines.MAXLEN_SERIAL_NUMBER, blank=True)
    sample_id = models.CharField(max_length=LimsCustomerDefines.MAXLEN_SAMPLE_ID, blank=True)
    lot_batch_id = models.CharField(max_length=LimsCustomerDefines.MAXLEN_LOT_BATCH_ID, blank=True)
    method_name = models.CharField(max_length=LimsCustomerDefines.MAXLEN_METHOD_NAME, blank=True)
    handling_rule_name = models.CharField(max_length=LimsCustomerDefines.MAXLEN_HANDLING_RULE_NAME, blank=True)
    action_alert_level_name = models.CharField(max_length=LimsCustomerDefines.MAXLEN_ACTION_ALERT_LEVEL_NAME, blank=True)
    cfu_count = models.CharField(max_length=LimsCustomerDefines.MAXLEN_CFU_COUNT, blank=True)
    mold_count = models.CharField(max_length=LimsCustomerDefines.MAXLEN_MOLD_COUNT, blank=True)
    status = models.CharField(max_length=LimsCustomerDefines.MAXLEN_STATUS_STATE, blank=True) # zona status_state?
    test_status = models.CharField(max_length=LimsCustomerDefines.MAXLEN_STATUS_STATE, blank=True) # zona status_state?
    approval = models.CharField(max_length=LimsCustomerDefines.MAXLEN_APPROVAL_MESSAGE, blank=True) 

# API Endpoint - /postResponse
# {
# 			"acknowledge-resultsonapproval string",
#                              }
class CmToCustomerPostResultsOnApprovalResponse(MyBaseModel):
       acknowledge = models.CharField(max_length=LimsCustomerDefines.MAXLEN_ACKNOWLEDGE, blank=True)



