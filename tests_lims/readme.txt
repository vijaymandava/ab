
Prerequisites:
CM is running on an EC2 host
SM is running on an EC2 host
sm_ui_endpoint is running on the SM server.  See the readme in infrastructure/sm_ui_endpoint folder for instructions.
lims_customer_receive_endpoint is running.  See the readme in infrastructure/lims_customer_receive_endpoint folder for instructions

Set up the environment:
./setup_win.ps1

Run tests:
pytest .\tests\test_001_cm_get_health_live.py           # confirm CM is working
pytest .\tests\test_029e2_order_load_using_case_91.py   # confirm cm can order assay on SM using LIMS
pytest .\tests\test_013_sm_retrieve_get_test_list.py    # confirm testbench can get to SM user interface
pytest .\tests\test_030_customer_rx_endpoint_get_about.py   # confirm testbench can get to Customer LIMS Receive Endpoint (database)


Run regression:
pytest -m regression_infrastructure     --self-contained-html --html=report_infrastructure.html
pytest -m regression_lims_order_cancel  --self-contained-html --html=report_lims_order_cancel.html
pytest -m regression_lims_timepoints    --self-contained-html --html=report_lims_timepoints.html

Option switches for regression include:
 --collect-only

