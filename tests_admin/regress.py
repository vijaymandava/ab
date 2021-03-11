from datetime import datetime
import os


timestamp = "regression_" + datetime.now().strftime('%y%m%d_%H%M')
switches = ''
#switches = '--collect-only'

cmd = "pytest -m infrastructureExamplesSmUiRoles --html={}{} {}".format(timestamp, "_infrastructure_roles.html", switches)
os.system(cmd)

cmd = "pytest -m infrastructureExamplesSmUiUsers --html={}{} {}".format(timestamp, "_infrastructure_users.html", switches)
os.system(cmd)

print('done')
