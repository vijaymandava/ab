# from test_001_cm_get_health_live import test
# from test_003_cm_get_auth_token_raw import test
# from test_004_cm_get_auth_token import test
# from test_010_lims_order import test
# from test_011_sm_home_get_test_list import test
# from test_012a_sm_home_load import test
# from test_012b_sm_home_wait_for_all_tests_loaded import test
# from test_013_sm_retrieve_get_test_list import test
# from test_014a_sm_retrieve_cancel_test_by_lims_id import test
# from test_014b_sm_retrieve_cancel_test_by_serial_number import test
# from test_014c_lims_cancel import test
# from test_015_sm_home_wait_for_all_tests_cancelled
# from test_016a_sm_approve_approve_test_by_lims_id import test
# from test_016b_sm_approve_approve_test_by_serial_number import test
# from test_016c_lims_approve import test

# from test_020_order_case_0_LID_01__assay_by_default import test   # DEVOPS 2988 "Request is missing assay parameters, Method: , Handling Rule: , Action Alert Level:  \\"}
# from test_020_order_case_0_LID_03a__assay_by_m_aa_hr_no_cancel import test  # PASS
# from test_020_order_case_0_LID_03b__assay_by_m_aa_hr_with_cancel import test  # PASS
# from test_020_order_case_0_LID_04__common_infrastructure import test  # FAIL
# from test_020_order_case_0_LID_10__assay_by_m_aa_hr_error_check_duplicate import test   # PASS <------- good
# from test_020_order_case_0_LID_99__common_infrastructure

# from test_021_order_case_1_LIDSID_02__assay_by_sample import test # DEVOPS 2987 "lot_batch_id" is not allowed to be empty',
# from test_021_order_case_1_LIDSID_99__common_infrastructure import test

# from test_022_order_case_2_SN_01__assay_by_default import test # DEVOPS 2988 "Request is missing assay parameters, Method: , Handling Rule: 
# from test_022_order_case_2_SN_02__assay_by_sample_no_cancel import test  #  FAIL "lot_batch_id\\" is not allowed to be empty
# from test_022_order_case_2_SN_03a__assay_by_m_aa_hr_no_cancel import test  # PASS <------ this is important it can be ordered and LOADED
# from test_022_order_case_2_SN_03b__assay_by_m_aa_hr_with_cancel import test  #  DEVOPS 2989 :"\\"lims_id\\" is not allowed to be empty"
# from test_022_order_case_2_SN_99__common_infrastructure import test

# from test_023_order_case_3_LBSID_03__directed import test  # fails on cancel <---------- devops needed - unable to cancel
# from test_023_order_case_3_LBSID_03b__directed_nocancel import test  # <----PASS----- important we can create multi-assay runs
# from test_023_order_case_3_LBSID_03c__directed_cancel_via_limsid import test  # <---FAIL ---- lims_id is not allowed to be empty

# from test_029e_order_cancel_using_case_91 import test # <---------- PASS important as this creates and cancels an order
# from test_029f_order_cancel_busing_case_93 import test  # <-------- FAIL "lot_batch_id" is not allowed to be empty'

# from test_030_order_load_timepoints_approve import test  # this is based on "91" - it orders but push "Load" button results in GD crash

# test()
