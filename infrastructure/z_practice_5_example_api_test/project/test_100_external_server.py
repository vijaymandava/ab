from urllib import request

# perform a GET to an external website
# expect a "200" response


def test_1_external_site():

    req = request.Request(
        url='http://www.example.com',
        data=None,
        headers={},
        origin_req_host=None,
        unverifiable=False,
        method='GET')
    # method='POST',
    # method=None

    res = request.urlopen(
        url=req,
        data=None,
        timeout=4,
        cafile=None,
        capath=None,
        cadefault=False,
        context=None)

    print("here")
    print(res)
    print('------------')
    print(res.geturl())
    print('------------')
    print(res.info())
    print('------------')
    print(res.getcode())

    assert res.getcode() == 200
    # assert(False)
