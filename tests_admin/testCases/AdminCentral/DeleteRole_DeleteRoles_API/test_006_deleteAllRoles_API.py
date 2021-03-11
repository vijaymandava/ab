import pytest
import requests
import json
from tests_admin.testCases.AdminCentral.Create_Role_API.common_role_api import Common_role_api
from tests_admin.utilities.customLogger import LogGen
from tests_admin.utilities.readProperties import ReadConfig


@pytest.mark.test_api
@pytest.mark.regression
@pytest.mark.deleteroleAPI
def test_deleteAll_roles_006():
    logger=LogGen.loggen()
    com = Common_role_api()
    headers = com.headers()
    logger.info("****************  Test_006: Test delete All Roles when user sends  -  Valid Request ****************")
    logger.info("https://rapidmicrobiosystems.jamacloud.com/perspective.req#/testCases/164305?projectId=50")
    print("****************  Test_006: Test delete All Roles when user sends  -  Valid Request ****************")
    print("Jama link is ::https://rapidmicrobiosystems.jamacloud.com/perspective.req#/testCases/164305?projectId=50")
    url = ReadConfig.sm()
    cmurl = ReadConfig.cm_for_decryption()
    r = requests.get(url + "/getRoles", headers=headers)
    data = r.json()
    # print("Data from SM::\n", r.json())
    resp1 = requests.post(cmurl + '/encryptDecrypt/decrypt', headers=headers, data=json.dumps(data, indent=4))
    roles = resp1.json()
    # print("Roles are ::", roles)
    # extracting data in json format
    list = []
    for item in roles:
        userroles = item.get('userRoleName')
        list.append(userroles)
    print("Before deletion Roles are :::\n", list)
    for i in list:
        print("\n Deleting role :::", i)
        body = {'deletedBy': 1, 'userRoleName': i}
        encryption = requests.post(cmurl + '/encryptDecrypt/encrypt', headers=headers,
                                   data=json.dumps(body, indent=4))
        encrypted_body = encryption.text
        a = json.loads(encrypted_body)
        url = ReadConfig.sm()
        r = requests.delete(url + "/deleteRole", data=json.dumps(a, indent=4), headers=headers)
        # r = requests.delete(url + "/deleteRole", headers=headers, data=json.dumps(body, indent=4))
        d = r.json()
        # print("Response is ::", r.json())
        status = d["status"]
        print("Status is :::", status)
        if status == "Failure":
            print(i, " ::Role deletion not possible may be assigned to USER (or) may be Default Role")
            # status_message= d['status_message']
            # print("Status message is :::", status_message)
            # resp2 = requests.post(cmurl + '/encryptDecrypt/decrypt', headers=headers, data=json.dumps(status_message, indent=4))
            # resp2_text = resp1.text
            # print("Decrypted Response is :::", resp2_text)

        else:
            print("Role deleted successfully - Deleted Role is   ::", i)