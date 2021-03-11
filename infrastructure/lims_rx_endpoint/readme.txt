
This is the LIMS RX Endpoint. It implements the customer "receive" side of the
Growth Direct LIMS Integration Specification (currently rev C).
More specifically it implements sections:

10 POST for Assay Status Events (loaded, timepoints, cancelled)
12 Result Sent (POST) to LIMS Web Server
14 ResultOnApproval Sent (POST) to LIMS Web Server

The endpoint is intended for use in SQA testing. To assist in testing:
a) Scoreboard: the endpoint provides a scoreboard (database) where GET and POST transactions
are logged. This allows the test to find transactions issued by CM, and could be used,
for example, at end of test to confirm all expected updates have been received.
b) Error Injection: the endpoint provides faclities to respond with non-standard
responses. This allows the test to, for example, inject a "400" response instead of
a normal "200" response.

Reference:
Growth Direct LIMS Integration Specification (current Rev C)
https://rapidmicrobiosystems.sharepoint.com/:w:/r/sites/SoftwareEngineering/_layouts/15/Doc.aspx?sourcedoc=%7B53B1E04E-C318-41BA-BE25-F6132F7EE6A6%7D&file=Design%20Doc%20-%20Growth%20Direct%20LIMS%20Integration%20Specification%20-%20R4.0%20-%20Rev%20C%2012-16-20.docx&action=default&mobileredirect=true


============== Starting the Endpoint ============

To start the endpoint cd into the "/project" folder and follow the readme.
The sections below provide an overview of the endpoint.


============== API ================
The API is defined in TSVNNN Growth Direct LIMS Integration Specification R4.0 Rev "B"

--------------- 7.1 ---------------
LimsCustomerTxPostOrder

API Endpoint - /postOrder 
{
"instr_id": "string",
"lims_id": "string",
"serial_number": "string",
"sample_id": "string",
"lot_batch_id": "string",
"method_name": "string",
"handling_rule_name": "string",
"action_alert_level_name": "string",
"aal_cfu_threshold_alert": "string",
"aal_cfu_threshold_action": "string",
"aal_cfu_threshold_specification": "string",
"aal_cfu_threshold_pass": "string",
"comment": "string",
}

----------------- 8.6 ---------------
LimsCustomerTxPostCancel

API Endpoint - /postCancel 
 {
"instr_id": "string",
"lims_id": "string",
"serial_number": "string",
"sample_id": "string",
"lot_batch_id": "string",
 }	

 

---------9.1--------  
/postLoaded
{
"instr_id": "string",
"lims_id": "string",
"serial_number": "string",
"loaded_on": "string",
"loaded_by": "string",
}
/postResponse 
{
"acknowledge": "Acknowledge",
}

---------9.2--------
/postCanceled
{
"instr_id": "string",
"lims_id": "string",
"serial_number": "string",
"canceled_on": "string",
"canceled_by": "string",
}
/postResponse 
{
"acknowledge": "Acknowledge",
}

---------9.3--------
/postCompleted
{
"instr_id": "string",
"lims_id": "string",
"serial_number": "string",
"completed_on": "string",
}
/postResponse 
{
"acknowledge": "Acknowledge",
}

---------9.4--------
/postAssayStatus
{
"instr_id": "string",
"lims_id": "string",
"serial_number": "string",
"elapsed_assay_time": "string",
"status": "string",
"status_flag": "string",
"status_update_time": "string",
}
/postResponse 
{
"acknowledge": "Acknowledge",
}


10.1.1 is GetAssayDetails
10.1.2 is GetAssayStatus

---------11--------
/postResults 
{
"instr_id": "string",
"lims_id": "string",
"serial_number": "string",
"sample_id": "string",
"lot_batch_id": "string",
"method_name": "string",
"action_alert_level_name": "string",
"handling_rule_name": "string",
"cfu_count": "string",
"mold_count": "string",
"status": "string",
"test_status": "string",
"approval": "string",
}

API Endpoint - /postResponse 
{
"acknowledge-results":"Acknowledge",
}

---------13--------
/postResultsOnApproval 
{
"instr_id": "string",
"lims_id": "string",
"serial_number": "string",
"sample_id": "string",
"lot_batch_id": "string",
"method_name": "string",
"action_alert_level_name": "string",
"handling_rule_name": "string",
"cfu_count": "string",
"mold_count": "string",
"status": "string",
"test_status": "string",
"approval": "string",
}

API Endpoint - /postResponse
{
"acknowledge-resultsonapproval": "Acknowledge",
}


