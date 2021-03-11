import urllib3
import json
import random
import uuid
from datetime import datetime


# these are common routines and values used by all tests
class Common():

    def __init__(self):

        # Chris CM/SM
        self.__CM_IP = 'http://192.168.2.110:3002/'
        # self.__CUSTOMER_LIMS = 'http://192.168.2.29:9101/'
        # self.__CUSTOMER_LIMS = 'http://0.0.0.0:9101/'
        self.__CUSTOMER_LIMS = 'http://localhost:9101/'


        self.__SM1_IP = 'http://127.0.0.1:9100/sm_ui/'
        self.__SM1_INSTRUMENT_ID = "E01014000"


        # Vijay CM/SM
        #self.__CM_IP = 'http://192.168.1.40:3002/'
        #self.__CUSTOMER_LIMS = 'http://0.0.0.0:9001/'
        #self.__SM1_IP = 'http://localhost:9100/sm_ui/'
        ## self.__SM1_IP = 'http://127.0.1.34:9100/sm_ui/'
        #self.__SM1_INSTRUMENT_ID = "E01014000"


        self.AUTH_TOKEN_EXPECTED_LENGTH_FROM_CM = 157
        self.AUTH_TOKEN_EXPECTED_LENGTH_TO_CM = 164
        self.REQUEST_COMMENT_MAX_LEN = 20
        self.APPROVE_COMMENT_MAX_LEN = 20
        self.APPROVE_MOLD_MAX_VAL = 20

        self.http = urllib3.PoolManager()

    def get_cm_ip(self):
        return self.__CM_IP

    def get_sm_ip(self, sm_number):
        assert (sm_number >=1) and (sm_number <=1), "sm number needs to be == 1"
        if sm_number == 1:
            return self.__SM1_IP
        # if sm_number == 2:
        #    return self.__SM2_IP

    def get_sm_inst_id(self, sm_number):
        assert (sm_number >=1) and (sm_number <=1), "sm number needs to be == 1"
        if sm_number == 1:
            return self.__SM1_INSTRUMENT_ID
        # if sm_number == 2:
        #    return self.__SM2_INSTRUMENT_ID

    def get_customer_lims_ip(self):
        # we assume the LIMS Customer Rx Endpoint is running on the SM #1
        return self.__CUSTOMER_LIMS


    def get_auth_token(self):

        print('------- get auth token -------')

        method = 'POST'
        url = self.get_cm_ip() + 'auth/login'
        headers = {
            'Content-Type': 'application/json',
            }
        fields = {}
        body_raw = {
            'userName': 'rmbadmin',
            'password': 'test@123',
        }
        body_encoded = json.dumps(body_raw).encode('utf-8')

        r = self.http.request(
            method=method,
            url=url,
            headers=headers,
            fields=fields,
            body=body_encoded,
            retries=False)
            # zona timeout=120.0)

        # check response status == 200
        assert r.status == 200, "response for auth token: expected 200 observed {}".format(r.status)

        # check the auth token is the right length
        jdata = json.loads(r.data.decode('utf-8'))
        token = jdata['authToken']
        assert len(token) == self.AUTH_TOKEN_EXPECTED_LENGTH_FROM_CM, 'auth token length: expected {}, observed {}'.format(
            self.AUTH_TOKEN_EXPECTED_LENGTH_FROM_CM,
            len(token))

        bearer_token = 'Bearer ' + token
        return bearer_token

    def get_unique_serial_number_em_bb(self):
        sn = self.__get_unique_serial_number()
        return 'E' + sn

    def get_unique_serial_number_sterility(self):
        sn = self.__get_unique_serial_number()
        return 'B' + sn

    def __get_unique_serial_number(self):
        x = datetime.today().strftime("%d")
        y = random.randrange(100000,999999)
        return str(x) + str(y)
        
    def get_unique_lims_id(self):
        x = datetime.today().strftime("%d")
        y = random.randrange(100000,999999)
        return str(x) + str(y)

    def get_unique_lot_batch_id(self):
        x = datetime.today().strftime("%d")
        y = random.randrange(100000,999999)
        return str(x) + str(y)

    def get_random_comment_order(self):
        comment = uuid.uuid4().hex.upper()[0:self.REQUEST_COMMENT_MAX_LEN]
        return comment

    def get_random_approve_comment(self):
        comment = uuid.uuid4().hex.upper()[0:self.APPROVE_COMMENT_MAX_LEN]
        return comment

    def get_random_approve_mold_count(self):
        value = random.randrange(0, self.APPROVE_MOLD_MAX_VAL+1)
        return value

    def sm_home_get_test_list(self, sm_number):

        method = 'GET'
        url = self.get_sm_ip(sm_number) + 'home/get_test_list'
        
        r = self.http.request(
            method=method,
            url=url,
            retries=False)
            # zona timeout=60.0)

        assert r.status == 200, "response has bad status"
        jdata = json.loads(r.data.decode('utf-8'))

        # print...
        for n, row in jdata.items():
            print('{} {}'.format(n, row))

        return jdata

    def sm_home_load(self, sm_number):
        method = 'GET'
        url = self.get_sm_ip(sm_number) + 'home/left_load'
        
        r = self.http.request(
            method=method,
            url=url,
            retries=False)
            # zona timeout=60.0)

        assert r.status == 200, "response has bad status"

    def sm_retrieve_get_test_list(self, sm_number):

        method = 'GET'
        url = self.get_sm_ip(sm_number) + 'retrieve/get_test_list'
        
        r = self.http.request(
            method=method,
            url=url,
            retries=False)
            # zona timeout=60.0)

        assert r.status == 200, "response has bad status"
        jdata = json.loads(r.data.decode('utf-8'))

        # print...
        for n, row in jdata.items():
            print('{} {}'.format(n, row))

        return jdata

    def sm_approve_get_test_list(self, sm_number):

        method = 'GET'
        url = self.get_sm_ip(sm_number) + 'approve/get_test_list'
        
        r = self.http.request(
            method=method,
            url=url,
            retries=False)
            # zona  timeout=60.0)

        assert r.status == 200, "response has bad status"
        jdata = json.loads(r.data.decode('utf-8'))

        # print...
        for n, row in jdata.items():
            print('{} {}'.format(n, row))

        return jdata

    def sm_retrieve_cancel_test_by_serial_number_or_lims_id(
        self, sm_number, by, serial_number_or_lims_id,
        test_comment, oos_comment, general_comment,
        mold_count):
        
        method = 'POST'
        if by == "serial_number":
            url = self.get_sm_ip(sm_number) + 'retrieve/cancel_test_by_serial_number'
            fields = {
                'serial_number': serial_number_or_lims_id,
            }
        if by == "lims_id":
            url = self.get_sm_ip(sm_number) + 'retrieve/cancel_test_by_lims_id'
            fields = {
                'lims_id': serial_number_or_lims_id,
            }

        r = self.http.request(
            method=method,
            url=url,
            fields=fields,
            retries=False)
            # zona timeout=120.0,)
    
        assert r.status == 200, "response has bad status"


    def sm_approve_approve_test_by_serial_number_or_lims_id(
        self, sm_number, by, serial_number_or_lims_id,
        test_comment, oos_comment, general_comment,
        mold_count):
        
        method = 'POST'
        if by == "serial_number":
            url = self.get_sm_ip(sm_number) + 'approve/approve_test_by_serial_number'
            fields = {
                'serial_number': serial_number_or_lims_id,
                'test_comment': test_comment,
                'oos_comment': oos_comment,
                'general_comment': general_comment,
                'mold_count': mold_count,
            }
        if by == "lims_id":
            url = self.get_sm_ip(sm_number) + 'approve/approve_test_by_lims_id'
            fields = {
                'lims_id': serial_number_or_lims_id,
                'test_comment': test_comment,
                'oos_comment': oos_comment,
                'general_comment': general_comment,
                'mold_count': mold_count,
            }

        r = self.http.request(
            method=method,
            url=url,
            fields=fields,
            retries=False)
            # zona timeout=120.0,)
    
        assert r.status == 200, "response has bad status"


    def no_assays_in_any_of_the_following_states(
            self, actual_states, unacceptable_states):
            
            acceptable = True
            for key,value in actual_states.items():
                # workaround in case we don't get complete status from UI...
                if 'status' in value:
                    if value['status'] in unacceptable_states:
                        acceptable = False
                else:
                    print('hmmm...(zona)')
                    acceptable = False
            return acceptable

    def all_assays_in_one_of_the_following_states(
            self, actual_states, acceptable_states):
            
            acceptable = True
            for key,value in actual_states.items():
                # workaround in case we don't get complete status from UI...
                if 'status' in value:
                    if value['status'] not in acceptable_states:
                        acceptable = False
                else:
                    print('hmmm...(zona)')
                    acceptable = False
            return acceptable



    # WEB-LIMS specification (currently in draft form)
    # "Growth Direct LIMS Integration Specification - R4.0 - Rev A 070620"
    # establishes several ways to establish TEST IDENTIFIER.
    # The following attempts to summarize that draft:
    #
    # Section 4.1 LIMS_ID
    #             LIMS_ID can be used as primary identifier (one per test)
    #
    # Section 4.2 LIMS_ID AS A "TEST" IDENTIFIER
    #             LIMS_ID can be used as a ***GROUP*** identifier where Sample ID makes it unique (see Section 4.4)
    #
    # Section 4.3 CASSETTE SERIAL NUMBER
    #             Cassette serial number can be used as primary identifier
    #
    # Section 4.4: 
    #             There are two ways to use SAMPLE_ID to create a unique identifier.
    #
    #             LIMS_ID + SAMPLE_ID
    #             Per Section 4.2 - LIMS_ID establishes "group" and SAMPLE_ID makes each assay unique
    #
    #             LOT_BATCH + Sample_ID
    #             LOT_BATCH can be any string. Similar to LIMS_ID it can be used to establish a "group" with SAMPLE_ID making it unique.
    #
    #
    # As such there are 4 cases we need to support and test
    #
    #   case_0_lims_id:                   LIMS_ID (one per cassette)
    #   case_1_lims_id_plus_sample_id:    LIMS_ID (group) + SAMPLE_ID (to make unique)
    #   case_2_serial_number:             SERIAL_NUMBER (one pur cassette)
    #   case_3_lot_batch_plus_sample_id:  LOT_BATCH (group) + SAMPLE_ID (to make unique)
    #
    #
    # What does this look like on a physical instrument?
    # 
    #   case_0_lims_id
    #              (file-based)
    #              Customer system conjures up unique LIMS IDs (one per cassette)
    #              Customer system creates LIMS order (file) specifying LIMS_ID
    #              Customer system throws file onto SM via Bridge
    #              Customer uses SM LIMS interface to print LIMS label.
    #              Customer applies the LIMS label to cassette and loads
    #              During load SM reads LIMS_ID which is unique to cassette.
    #
    #              (web-based):
    #              Customer system conjures up unique LIMS IDs (one per cassette)
    #              Customer system creates LIMS order (web-api request) specifying LIMS_ID
    #              Customer system sends api-request to SM via CM
    #              Customer uses SM LIMS interface to print LIMS label.
    #              Customer applies the LIMS label to cassette and loads
    #              During load SM reads LIMS_ID which is unique to cassette.
    #
    #   case_1_lims_id_plus_sample_id
    #              (file-based)
    #              Customer system conjures up LIMS ID that defines group of tests, and has previously established Sample IDs unique within group
    #              Customer system creates LIMS order (file) specifying LIMS ID + Sample ID
    #              Customer system throws file onto SM via Bridge
    #              Customer uses SM LIMS interface to print LIMS label.
    #              Customer applies the LIMS label to cassette and loads
    #              During load SM reads LIMS_ID + Sample ID which is unique to cassette.
    #
    #              (web-based):
    #              Customer system conjures up LIMS ID that defines group of tests, and has previously established Sample IDs unique within group
    #              Customer system creates LIMS order (web-api request) LIMS ID + Sample ID
    #              Customer system sends api-request to SM via CM
    #              Customer uses SM LIMS interface to print LIMS label.
    #              Customer applies the LIMS label to cassette and loads
    #              During load SM reads LIMS_ID + Sample ID which is unique to cassette.
    #
    #   case_2_serial_number
    #              (file-based) 
    #              Customer system somehow knows Serial Number of cassettes (e.g. barcode scan)
    #              Customer system creates LIMS order (file) specifying Serial Number
    #              Customer system throws file onto SM via Bridge
    #              There is no Sample or LIMS label.
    #              During load SM reads Serial Number which is unique to cassette.
    #
    #              (web-based):
    #              Customer system somehow knows Serial Number of cassettes (e.g. barcode scan)
    #              Customer system creates LIMS order (web-api request) specifying Serial Number
    #              Customer system sends api-request to SM via CM
    #              There is no Sample or LIMS label.
    #              During load SM reads Serial Number which is unique to cassette.
    #   case_3_lot_batch_plus_sample_id:
    #              (file-based)
    #              Customer system conjures up LOT_BATCH that defines group of tests, and has previously established Sample IDs unique within group
    #              Customer system creates LIMS order (file) specifying LOT_BATCH + Sample ID
    #              Customer system throws file onto SM via Bridge
    #          ??? Customer uses (??????) UI to print LIMS label  <--print from what UI?  Can we print from LIMS UI?
    #              Customer applies the LIMS label to cassette and loads
    #              During load SM reads LOT_BATCH + Sample ID which is unique to cassette.
    #
    #              (web-based):
    #              Customer system conjures up LOT_BATCH that defines group of tests, and has previously established Sample IDs unique within group
    #              Customer system creates LIMS order (web-api request) LOT_BATCH + Sample ID
    #              Customer system sends api-request to SM via CM
    #          ??? Customer uses (??????) UI SM LIMS interface to print LIMS label. <--print from what UI?  Can we print from LIMS UI?
    #              Customer applies the LIMS label to cassette and loads
    #              During load SM reads LOT_BATCH + Sample ID which is unique to cassette.

    def order_using_lims_file(self, case, number_of_tests):
        print('------- order_using_lims_file {} number_of_tests={} ------'.format(case, number_of_tests))
        assert False, "not implemented"

    def order_using_lims_web_api(self, case, number_of_tests):

        assert case in [
            'case_0_lims_id',
            'case_1_lims_id_plus_sample_id',
            'case_2_serial_number',
            'case_3_lot_batch_plus_sample_id',
            'case_91_lims_id_plus_serial_number',
            'case_93_lims_id_plus_sample_id_plus_serial_number'
            ], '"{}" is not one of the supported case types'.format(case)

        print('------- order_using_lims_web_api {} number_of_tests={} ------'.format(case, number_of_tests))

        print('------- get the token -------')

        token = self.get_auth_token()

        method = 'POST'
        url = self.get_cm_ip() + 'lims/postOrder'

        # prepare to make a list of orders
        lims_id_list = []
        serial_number_list = []
        lot_batch_list = []
        sample_id_list = []
        mm_list = []
        aa_list = []
        hr_list = []

        if case == 'case_0_lims_id':
            for n in range(0, number_of_tests):
                lims_id_list.append(self.get_unique_lims_id())
                serial_number_list.append('')
                lot_batch_list.append('')
                sample_id_list.append('')
                mm_list.append('')
                aa_list.append('')
                hr_list.append('')

        if case == 'case_1_lims_id_plus_sample_id':
            lims_group_id = self.get_unique_lims_id()
            for n in range(0, number_of_tests):
                lims_id_list.append(lims_group_id)
                serial_number_list.append('')
                lot_batch_list.append('')
                # note this assumes sample IDs = s0, s1, s2, etc
                sample_id_list.append('s{}'.format(n))
                mm_list.append('')
                aa_list.append('')
                hr_list.append('')

        if case == 'case_2_serial_number':
            for n in range(0, number_of_tests):
                lims_id_list.append('')
                serial_number_list.append(self.get_unique_serial_number_em_bb())
                lot_batch_list.append('')
                sample_id_list.append('')
                mm_list.append('')
                aa_list.append('')
                hr_list.append('')

        if case == 'case_3_lot_batch_plus_sample_id':
            lims_group_id = self.get_unique_lims_id()
            for n in range(0, number_of_tests):
                lims_id_list.append('')
                serial_number_list.append('')
                lot_batch_list.append(self.get_unique_lot_batch_id())
                # note this assumes sample IDs = s0, s1, s2, etc
                sample_id_list.append('s{}'.format(n))
                mm_list.append('')
                aa_list.append('')
                hr_list.append('')

        # due to limitations of simulator (unable to load without Serial Number)
        # and
        # bugs 2186, 2192 (CM does not allow Order without LIMS_ID)
        # these are two cases that load and will allow SQA to make forward progress...
        if case == 'case_91_lims_id_plus_serial_number':
            for n in range(0, number_of_tests):
                lims_id_list.append('40' + self.get_unique_lims_id())
                serial_number_list.append(self.get_unique_serial_number_em_bb())
                lot_batch_list.append('')
                sample_id_list.append('')
                mm_list.append('mm10000')
                aa_list.append('aa')
                hr_list.append('hr')

        if case == 'case_93_lims_id_plus_sample_id_plus_serial_number':
            lims_group_id = self.get_unique_lims_id()
            for n in range(0, number_of_tests):
                lims_id_list.append(lims_group_id)
                serial_number_list.append(self.get_unique_serial_number_em_bb())
                lot_batch_list.append('')
                # note this assumes sample IDs = s0, s1, s2, etc
                sample_id_list.append('s{}'.format(n))
                mm_list.append('')
                aa_list.append('')
                hr_list.append('')


        # issue the requests
        headers = {
            'accept': 'application/json',
            'Content-Type': 'application/json',
            'Authorization': token,
            }

        fields = {}

        for n in range(len(lims_id_list)):
            body_raw = {
                "instr_id": self.get_sm_inst_id(1),
                "lims_id": lims_id_list[n],
                "serial_number": serial_number_list[n],
                "sample_id": sample_id_list[n],
                "lot_batch_id": lot_batch_list[n],
                "method_name": mm_list[n],
                "handling_rule_name": hr_list[n],
                "action_alert_level_name": aa_list[n],
                "aal_cfu_threshold_alert": '',
                "aal_cfu_threshold_action": '',
                "aal_cfu_threshold_specification": '',
                "aal_cfu_threshold_pass": '',
                "comment": self.get_random_comment_order(),
                }

            body_encoded = json.dumps(body_raw).encode('utf-8')

            print(body_encoded)

            print('------- issue the LIMS order request to CM -------')
            r = self.http.request(
                method=method,
                url=url,
                headers=headers,
                fields=fields,
                body=body_encoded,
                retries=False)
                # zona timeout=120.0)

            print('------- response from CM is here -------')
            print('r.headers = {}'.format(r.headers))
            print('r.status  = {}'.format(r.status))
            print('r.body    = {}'.format(json.loads(r.data.decode('utf-8'))))
            assert r.status == 200, "response has bad status {}".format(r.status)

        print('------- orders placed --------')
        return({"lims_id": lims_id_list,
                "sample_id": sample_id_list,
                "serial_number": serial_number_list,
                "lot_batch": lot_batch_list})



    # The specification states for canceling an assay "any primary identifier can be used." (Section 8.6)
    # From above we know there can be:
    #
    #   case_0_lims_id:                   LIMS_ID (one per cassette)
    #   case_1_serial_number:             SERIAL_NUMBER (one pur cassette)
    #   case_2_lims_id_plus_sample_id:    LIMS_ID (group) + SAMPLE_ID (to make unique)
    #   case_3_lot_batch_plus_sample_id:  LOT_BATCH (group) + SAMPLE_ID (to make unique)
    #
    # The method below takes as input the dictionary of primary_ids that came from the Order method above

    def cancel_from_primary_ids(self, primary_id_dict):

        print('------- get the token -------')

        token = self.get_auth_token()

        print('------- create the LIMS cancel requests -------')

        for n in range(len(primary_id_dict['lims_id'])):
            print("cancel lims={} serial={} lot_bat={} sample={}".format(
                primary_id_dict['lims_id'][n],
                primary_id_dict['serial_number'][n],
                primary_id_dict['lot_batch'][n],
                primary_id_dict['sample_id'][n]))


            method = 'POST'
            url = self.get_cm_ip() + 'lims/postCancel'

            headers = {
                'accept': 'application/json',
                'Content-Type': 'application/json',
                'Authorization': token,
                }

            fields = {}

            body_raw = {
                "instr_id": self.get_sm_inst_id(1),
                "lims_id":  primary_id_dict['lims_id'][n],
                "serial_number":  primary_id_dict['serial_number'][n],
                "sample_id":  primary_id_dict['sample_id'][n],
                "lot_batch_id":  primary_id_dict['lot_batch'][n],
                }

            body_encoded = json.dumps(body_raw).encode('utf-8')

            # print('------- issue the LIMS cancel request to CM -------')
            r = self.http.request(
                method=method,
                url=url,
                headers=headers,
                fields=fields,
                body=body_encoded,
                retries=False,
                timeout=120.0)

            # print('------- response from CM is here -------')
            assert r.status == 200, "response has bad status"

