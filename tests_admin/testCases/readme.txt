This is the CM(central manager) - SM(System Manager) User Interface and API Testcase automation.

Testcases are automated for below requirements.

1. Create Role.
2. Create User.
3. Update Role.
4. Update User.
5. Get Role.
6. Get Roles.
7. Get User.
8. Get Users.
9. Delete Role.

To start executing the Testcases -

1. Set-up the python interpreter (files -> settings ->Project:(project name) -> python interpreter)
2. Please make sure all the packages,libraries and files installed which are mentioned in the ("tests_admin/testCases/requirements.txt").


Execution Steps:-
1. Open the Terminal

2. Execute individual Testcase::

Pytest -v -s "Testcase location"
example:-  pytest -v -s tests_admin/testCases/AdminCentral/Create_Role_API/test_001_CreateRole_api.py

-v    =   is the command which will display the methods name and pass/fail status.
-s    =   is the command which will display all the print statements.

3. Execute folders
Pytest -v -s "Testcase folder location"
example:-  pytest -v -s tests_admin/testCases/AdminCentral/Create_Role_API

4. Html - Report Generation
pytest -v -s --html=./Reports/report.html "Testcase location"
Example::- pytest -v -s  --html=./Reports/report.html tests_admin/testCases/AdminCentral/Create_Role_API/test_001_CreateRole_api.py

5. Allure - Report Generation
pytest -v -s --alluredir="Report generation location" "Testcase location"
Example:- pytest -v -s --alluredir="C:\Users\Vijay\Desktop\rmb\Reports\allure\reports" tests_admin/testCases/AdminCentral/Create_Role_API
    * After completing the execution
    * Navigate to report generation location
    example:- above we generated roports in "C:\Users\Vijay\Desktop\rmb\Reports\allure\reports"
    * Open CMD AND run the below command
    * allure serve C:\Users\Vijay\Desktop\rmb\Reports\allure\reports
    