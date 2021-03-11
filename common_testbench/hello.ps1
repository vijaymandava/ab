echo "hello"

echo "powershell version"
$PSVersionTable.PSVersion
$PSVersionTable.PSVersion.Major

if ($PSVersionTable.PSVersion.Major -eq 22) {
	$commonUtilitiesPath = split-path -parent $MyInvocation.MyCommand.Definition
} else {
	echo '------- FATAL ---------'
	echo 'only powershell V2 is currently tested/supported'
	echo 'attempting to continue...'
	$commonUtilitiesPath = $PSScriptRoot
}



if(1 -eq 1) {
   # // Executes when the Boolean expression is true
}else {
   # // Executes when the Boolean expression is false
}

echo "my command defintion"
echo $MyInvocation.MyCommand.Definition 


# echo "my command"
# echo $MyInvocation.MyCommand 


echo "script path"
$scriptPath = split-path -parent $MyInvocation.MyCommand.Definition
echo $scriptPath



echo "script root"
$x = $PSScriptRoot
echo $x

echo "command path"
$x = $PSCommandPath 
echo $x

echo "execution context"
echo $ExecutionContext


echo "good bye"
