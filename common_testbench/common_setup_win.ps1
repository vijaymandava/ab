################################################
# Reference:  https://packaging.python.org/tutorials/installing-packages/#optionally-create-a-virtual-environment
#
# Description:
# commmon setup activates virtual environment, clears PYTHONPATH and adds this folder (common_testbench) to PYTHONPATH

# activate virtual environment
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
# get current folder (common_testbench) so it can be added to PYTHONPATH

$the_ps_version = $PSVersionTable.PSVersion.Major
echo "powershell version = $the_ps_version"

if ($the_ps_version -ge 2) {
	$commonTestbenchPath= split-path -parent $MyInvocation.MyCommand.Definition
} else {
	echo '------- FATAL ---------'
	echo 'only powershell V2 and greater is currently supported'
	echo 'attempting to continue...'
	$commonTestbenchPath = $PSScriptRoot
}

################################################
# prepare PYTHONPATH for python modules
$Env:PYTHONPATH= '.'
$Env:PYTHONPATH= $Env:PYTHONPATH + ';' + $commonTestbenchPath + '\..'




