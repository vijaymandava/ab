import pytest
from tests_lims.tests.common import Common

@pytest.mark.regression_infrastructure
def test():

    com = Common()

    print('------- start test -------')

    token = com.get_auth_token()

    # check the auth token is the right length
    assert len(token) == com.AUTH_TOKEN_EXPECTED_LENGTH_TO_CM, 'auth token length: expected {}, observed {}'.format(
        com.AUTH_TOKEN_EXPECTED_LENGTH_TO_CM,
        len(token))

    print('------- test done --------')

