from urllib import request

# demonstrate BFM controls
# specifically ability to set response code (200, 400, 500)

def test_1_post_api():

    req = request.Request(url='http://127.0.0.1:9000')

    rsp = request.urlopen(url=req, timeout=4)

    print("here")
    print(rsp)
    print('------------')
    print(rsp.geturl())
    print('------------')
    print(rsp.info())
    print('------------')
    print(rsp.getcode())

    # assert(False)
