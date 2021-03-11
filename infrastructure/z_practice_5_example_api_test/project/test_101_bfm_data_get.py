from urllib import request

# perform a GET to the BFM url /
# expect a "200" response


def test_1_sm_bfm():

    req = request.Request(url='http://127.0.0.1:9000')

    res = request.urlopen(url=req, timeout=4)

    print("here")
    print(res)
    print('-----geturl-------')
    print(res.geturl())
    print('----info--------')
    print(res.info())
    print('------------')
    print(res.getcode())

    assert res.getcode() == 200
    #assert(False)
