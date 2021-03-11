

This is the API endpoint to the System Manager User Interface

To start the endpoint cd into "/project" folder and follow the readme there.
The sections below provide an overview of the API and detail the API commands.
The readme_2.txt and readme_3.doc files (in this folder) provide additional information on initial setup of CM and SM instances and initial setup.


========== Overview ==========

The endppoint allows a test to control the SM user interface through GET/POST http commands.
In other words, the test can use the API to push buttons on the UI or get data from UI screens.

+========== API Commands ==========

The API commands are:

-------------------------------------
Home page:

    r = http.request('GET', URL+'home/get_test_list', retries=False, timeout=60.0)

-------------------------------------
Load Button:

    r = http.request('GET', URL+'home/left_load', retries=False, timeout=60.0)

-------------------------------------
Approve page:

    r = http.request(
        method='GET',
        url=URL+'approve/get_test_list',
        retries=False,
        timeout=60.0)


    fields = {
        'serial_number': serial_number,
        'test_comment': uuid.uuid4().hex.upper()[0:comment_max_len],
        'oos_comment': uuid.uuid4().hex.upper()[0:comment_max_len],
        'general_comment': uuid.uuid4().hex.upper()[0:comment_max_len],
        'mold_count': random.randrange(2, 20, 2)
    }

    r = http.request(
        method='POST',
        url=URL+'approve/approve_test_by_serial_number',
        fields=fields,
        retries=False,
        timeout=120.0,)


    fields = {
        'lims_id': lims_id,
        'test_comment': uuid.uuid4().hex.upper()[0:comment_max_len],
        'oos_comment': uuid.uuid4().hex.upper()[0:comment_max_len],
        'general_comment': uuid.uuid4().hex.upper()[0:comment_max_len],
        'mold_count': random.randrange(2, 20, 2)
    }

    print('------- issue the post -------')
    r = http.request(
        method='POST',
        url=URL+'approve/approve_test_by_lims_id',
        fields=fields,
        retries=False,
        timeout=120.0,)

-------------------------------------
Retrieve page:

    r = http.request(
        method='GET',
        url=URL+'retrieve/get_test_list',
        retries=False,
        timeout=60.0)


    fields = {
        'serial_number': serial_number,
    }

    r = http.request(
        method='POST',
        url=URL+'retrieve/cancel_test_by_serial_number',
        fields=fields,
        retries=False,
        timeout=120.0,)


    fields = {
        'lims_id': lims_id,
    }

    r = http.request(
        method='POST',
        url=URL+'retrieve/cancel_test_by_lims_id',
        fields=fields,
        retries=False,
        timeout=120.0,)

-------------------------------------
User Roles page:

get list
    r = common.http.request(
        method='GET',
        url=common.url + 'roles/get_list',
        fields={},
        retries=False,
        timeout=common.timeout)


get individual
    name = "Administrator"
    fields = {
        'name': name,
    }

    r = common.http.request(
        method='GET',
        url=common.url + 'roles/get_role',
        fields=fields,
        retries=False,
        timeout=common.timeout)

create
    body_raw = {
        'name': role_name,
        'privs_set': {
            'methods_create': '1',
            'methods_edit': '0',
            'methods_delete': '1',
            'aa_create': '0',
            'aa_edit': '1',
            'aa_delete': '0'}}
    body_encoded = json.dumps(body_raw).encode('utf-8')

    r = common.http.request(
        method='POST',
        url=common.url + 'roles/create_role',
        body=body_encoded,
        headers={'Content-Type': 'application/json'},
        retries=False,
        timeout=common.timeout)

update
    body_raw = {
        'name': role_name,
        'privs_set': {
            'methods_create': '1',
            'methods_edit': '0',
            #'methods_delete': '1',
            'aa_create': '1',
            'aa_edit': '0',
            #'aa_delete': '0'
            }}
    body_encoded = json.dumps(body_raw).encode('utf-8')

    r = common.http.request(
        method='POST',
        url=common.url + 'roles/update_role',
        body=body_encoded,
        headers={'Content-Type': 'application/json'},
        retries=False,
        timeout=common.timeout)


delete
    body_raw = {
        'name': role_name,
        }
    body_encoded = json.dumps(body_raw).encode('utf-8')

    r = common.http.request(
        method='POST',
        url=common.url + 'roles/delete_role',
        body=body_encoded,
        headers={'Content-Type': 'application/json'},
        retries=False,
        timeout=common.timeout)

-------------------------------------
Users page:

get list
    r = common.http.request(
        method='GET',
        url=common.url + 'users/get_list',
        fields={},
        retries=False,
        timeout=common.timeout)

get individual:
    user_name = "Operator"
    fields = {
        'user_name': user_name
    }

    r = common.http.request(
        method='get',
        url=common.url + 'users/get_user',
        fields=fields,
        retries=False,
        timeout=common.timeout)

create:
    body_raw = {
        'first': first,
        'middle': middle,
        'last': last,
        'username': username,
        'email': email,
        'password': password,
        'phone': phone,
        'extension': extension,
        'role_name': role_name}
    body_encoded = json.dumps(body_raw).encode('utf-8')

    r = common.http.request(
        method='POST',
        url=common.url + 'users/create_user',
        body=body_encoded,
        headers={'Content-Type': 'application/json'},
        retries=False,
        timeout=common.timeout)

update:
    letters = string.ascii_lowercase

    first =    ''.join(random.choice(letters) for i in range(6))
    middle =   ''.join(random.choice(letters))
    last =     ''.join(random.choice(letters) for i in range(6))
    email =    uuid.uuid4().hex.upper()[0:6] + r'@rapidmicrobio.com'
    password = r'Foofoo123@'
    phone =   '456-789-0123'
    extension = '456'

    body_raw = {
        'first': first,
        'middle': middle,
        'last': last,
        'username': username,
        'email': email,
        'password': password,
        'phone': phone,
        'extension': extension,
        'role_name': role_name}
    body_encoded = json.dumps(body_raw).encode('utf-8')

    r = common.http.request(
        method='POST',
        url=common.url + 'users/update_user',
        body=body_encoded,
        headers={'Content-Type': 'application/json'},
        retries=False,
        timeout=common.timeout)


disable:
    body_raw = {
        'username': username,
        }
    body_encoded = json.dumps(body_raw).encode('utf-8')

    r = common.http.request(
        method='POST',
        url=common.url + 'users/disable_user',
        body=body_encoded,
        headers={'Content-Type': 'application/json'},
        retries=False,
        timeout=120.0,)

enable:
    body_raw = {
        'username': username,
        }
    body_encoded = json.dumps(body_raw).encode('utf-8')

    r = common.http.request(
        method='POST',
        url=common.url + 'users/enable_user',
        body=body_encoded,
        headers={'Content-Type': 'application/json'},
        retries=False,
        timeout=120.0,)