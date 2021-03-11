
This is the SQA Testbench (infrastructure and tests).

# Getting Started
See the "readme" files in the respective folders:
* infrastructure: API endpoint to the SM User Interface, LIMS RXendpoint
* tests_admin: tests for the CM Admin application
* tests_lims: test for LIMS


### Basics
You shall use a linter and this will be flake-8.  To set it up in Visual Studio Code:
Open the Command Palette (Ctrl+Shift+P) and select the Python: Select Linter command and choose "flake8"
Reference https://code.visualstudio.com/docs/python/linting

You shall follow conventions for file_names, ClassNames and methodNames
Reference 1: https://softwareengineering.stackexchange.com/questions/308972/python-file-naming-convention
Reference 2: https://www.python.org/dev/peps/pep-0008/#package-and-module-names


### Contribute
We follow standard lightweight commit process.
Refer to https://guides.github.com/introduction/flow/   

You shall regress your tests before creating a pull request.  This is outlined in the steps above.
TLDR:
* create a branch
* add commits
* open a pull request
* discuss and review
* deploy
* merge

More specifically, the steps to contribute are:
* create a branch, make your changes, commit to branch
** git checkout -b myname_branch_001
** make your changes
** run your tests and fix things
** run your regression (pytest -m) and fix things
** git commit
* merge from head, resolve conflicts, commit to branch
** git checkout master
** git pull
** git checkout my_branch_name
** git pull master
** resolve any merge conflicts
** re-run regression if necessary
** git commit
* push to origin and make a pull request:
** git push origin myname_branch_abc
** browse to the DevOps repository
** https://dev.azure.com/RMBDevOps/Growth%20Direct%20Software/_git/SQA_Testbench
** to "Repos" -> "Pull requests" screen
** push button "New pull request"
** find the branch, add a comment and email notification to cwinsor

### Integrating pull requests
* The release manager will integrate your changes, test, put onto master branch
* To get those changes, in your workarea:
* git checkout master
* git pull origin master

### If you are the release manager the steps to integrate pull requests are:
* If the pull request has no conflicts then you can just review and accept it in the DevOps UI
* If there are conflicts then either reject (sending it back to user) or work through the merge yourself and update the pull request.
* To work through the merge yourself you get the submitters branch, merge from master, fix, and commit to their branch:
** save any ongoing work
** git checkout master
** git pull
** git checkout --track origin/the_submitters_pull_branchname
** git merge master
** regress/fix
** git commit  (here you are committing to the submitters branch, local)
** git push origin the_submitters_pull_branchname
* go to the UI and accept the updated pull request

