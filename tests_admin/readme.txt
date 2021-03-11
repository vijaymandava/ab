
Prerequisites:
CM is running on an EC2 host
SM is running on an EC2 host
sm_ui_endpoint is running on the SM server. See the readme in infrastructure/sm_ui_endpoint folder for instructions.

Set up the environment:
./setup_win.ps1

Run tests:
pytest .\testCases\AdminCentral...(?)    # confirm ability to see CM Admin Central User Interface
pytest .\testCases\InfrastructureExamples\test_014a_sm_ui__roles_get_list.py  # confirm ability to get to SM User Interface (roles)


Run regression:

pytest -m createrole       --self-contained-html --html=report_createrole.html
pytest -m createroleAPI    --self-contained-html --html=report_createroleAPI.html
pytest -m updateroleAPI    --self-contained-html --html=report_updateroleAPI.html
pytest -m createuser       --self-contained-html --html=report_createuser.html
pytest -m createuserAPI    --self-contained-html --html=report_createuserAPI.html
pytest -m updateuserAPI    --self-contained-html --html=report_updateuserAPIv
pytest -m activatebutton   --self-contained-html --html=report_activatebutton.html
pytest -m infrastructureExamplesSmUiRoles --self-contained-html --html=report_infrastructureExamplesSmUiRoles.html
pytest -m infrastructureExamplesSmUiUsers --self-contained-html --html=report_infrastructureExamplesSmUiUsers.html

Option switches for regression include:
 --collect-only

