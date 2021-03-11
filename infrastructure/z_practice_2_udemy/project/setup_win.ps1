################################################
# activate the virtual environment
# if the pymote_env does not exist - create it

if (-NOT (Test-Path '.\pymote_env\Scripts\activate' -PathType Leaf)) {

    " "
    "did not find pymote_env\Scripts\activate - creating virtualenv now..."

    # confirm at least we have python with pip
    python --version
    python -m pip --version

    # add virtualenv to global libraries
    python -m pip install virtualenv

    # create an empty virtualenv
    python -m virtualenv pymote_env
    }

# activate the virtualenv
.\pymote_env\Scripts\activate

# get the libraries specified in requirements.txt
pip install -r requirements.txt

pip list



################################################
# add to PYTHONPATH for python modules
$Env:PYTHONPATH= '.'
$Env:PYTHONPATH= $Env:PYTHONPATH + ';' + $PSScriptRoot + '\lib;'

################################################
# add to PATH for selenium web drivers
$Env:PATH= $Env:PATH + ';' + $PSScriptRoot + '\lib_webdriver_chrome\83\chromedriver_win32;'


#################################################
# print instructions to start vs-code
" "
"to start visual studio code:"
"code -n ."
" "

#################################################
# print instructions to start jupyter notebook
#" "
#"to start jupyter notebook:"
#"jupyter notebook"
