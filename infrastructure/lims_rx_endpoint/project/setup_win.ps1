################################################
# common setup
..\..\..\common_testbench\common_setup_win.ps1

################################################
# local setup
$Env:PYTHONPATH= $Env:PYTHONPATH + ';' + $PWD
$Env:PYTHONPATH= $Env:PYTHONPATH + ';' + $PWD + '\lims_server'
$Env:PYTHONPATH= $Env:PYTHONPATH + ';' + $PWD + '\lims_server\lims_server'


echo PYTHONPATH=$Env:PYTHONPATH

#################################################
# print instructions
" "
"Next steps: Start the LIMS RX endpoint or open visual studio code - refer to readme.txt"
" "
