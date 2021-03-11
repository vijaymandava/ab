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
$Env:PYTHONPATH= $Env:PYTHONPATH + ';' + $PWD


#################################################
# print instructions to start vs-code
" "
"next steps: start the LIMS RX endpoint or open visual studio code - refer to readme.txt"
" "
