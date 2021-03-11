import pytest
from tests_admin.utilities.customLogger import LogGen


@pytest.mark.infrastructureExamplesSmUiUsers
def test():
    logger = LogGen.loggen()

    logger.info('------- test start --------')

    assert False, "re-enable user is not coded, specifically on re-enable there is a popup requiring new password"
  
    logger.info('------- test done --------')

