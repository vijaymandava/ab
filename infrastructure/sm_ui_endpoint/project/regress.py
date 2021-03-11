from datetime import datetime
import os


timestamp = "regression_" + datetime.now().strftime('%y%m%d_%H%M')
switches = ''
# switches = '--collect-only'

cmd = "pytest -m sm_frontend_tests --html={}{} {}".format(timestamp, "_frontend.html", switches)
os.system(cmd)

print('done')
