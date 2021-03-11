################################################
# activate the virtual environment
# reference:   https://packaging.python.org/tutorials/installing-packages/#optionally-create-a-virtual-environment

# if venv folder does not exist - create it
if (-NOT (Test-Path '.\venv\Scripts\activate' -PathType Leaf)) {

    " "
    "did not find venv\Scripts\activate - creating now..."

    # confirm at least we have python with pip
    python --version
    python -m pip --version


    # create an empty virtualenv
    python -m venv venv

    }

# activate the venv
.\venv\Scripts\activate

# ensure pip, setuptools and wheels are up to date
python -m pip install --upgrade pip setuptools wheel

# get the libraries specified in requirements.txt and show a list
pip install -r requirements.txt
pip list


################################################
# add to PYTHONPATH for python modules
$Env:PYTHONPATH= '.'
$Env:PYTHONPATH= $Env:PYTHONPATH + ';' + $PSScriptRoot + ';'
$Env:PYTHONPATH= $Env:PYTHONPATH + ';' + $PSScriptRoot + '.\tests;'

$Env:PYTHONPATH= $Env:PYTHONPATH + ';' + $PSScriptRoot + '.\backend_sm_windows_ui;'
$Env:PYTHONPATH= $Env:PYTHONPATH + ';' + $PSScriptRoot + '.\backend_sm_windows_ui\lib;'
$Env:PYTHONPATH= $Env:PYTHONPATH + ';' + $PSScriptRoot + '.\backend_sm_windows_ui\tests;'

$Env:PYTHONPATH= $Env:PYTHONPATH + ';' + $PSScriptRoot + '.\pymote_env\Lib\site-packages\pywinauto;'

$Env:PYTHONPATH= $Env:PYTHONPATH + ';' + $PSScriptRoot + '.\frontend_api_endpoint\project_endpoint;'


################################################
# add to PATH for selenium web drivers
$Env:PATH= $Env:PATH + ';' + $PSScriptRoot + '\lib_webdriver_chrome\83\chromedriver_win32;'


#################################################
# print instructions on what to do next...
" "
"Environment setup is complete"
" "
