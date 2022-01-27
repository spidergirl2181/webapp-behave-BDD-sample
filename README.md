# webapp-behave-BDD-sample

[Pre-requisites]

1. Install python version >= 3.6 (Download at: https://www.python.org/downloads/)
2. Install pip on your local machine if you don't have pip pre-installed (Guideline: https://pip.pypa.io/en/stable/installation/)
3. Install other necessary packages (behave, nose, selenium) via pip:

_$ pip install -r requirements.txt_

[How-to: run the sample test]

1. Clone this repository to your local machine
2. Standing at root directory: 'webapp-behave-BDD-sample', open terminal/command-line window
3. Run the sample test with log on console only:

_$ behave_

4. Run the sample test with generated xml report:

_$ behave --junit --junit-director PATH_

5. Run the sample test in parallel:

Unfortunately, Behave doesn't support parallel test. Thus, if you want to execute your test in parallel, you can implement it by yourself using multiprocess in Python or choose some workaround DevOp solution.

[How-to: shortcut an environment config]

**TBD**
