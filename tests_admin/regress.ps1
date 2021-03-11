
pytest -m createrole       --self-contained-html --html=report_createrole.html
pytest -m createroleAPI    --self-contained-html --html=report_createroleAPI.html
pytest -m updateroleAPI    --self-contained-html --html=report_updateroleAPI.html
pytest -m createuser       --self-contained-html --html=report_createuser.html
pytest -m createuserAPI    --self-contained-html --html=report_createuserAPI.html
pytest -m updateuserAPI    --self-contained-html --html=report_updateuserAPI.html
pytest -m activatebutton   --self-contained-html --html=report_activatebutton.html
pytest -m infrastructureExamplesSmUiRoles --self-contained-html --html=report_zz_infrastructureExamplesSmUiRoles.html
pytest -m infrastructureExamplesSmUiUsers --self-contained-html --html=report_zz_infrastructureExamplesSmUiUsers.html

echo "---done---"
