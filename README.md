makes a simple bash script you can copy paste into jamf with the results of the window you wanted

cd into the tool directory and setup the module via pip -e github address because it's not on pip

`pip3 install -e git+https://github.com/zackn9ne/module_jamf_helper_window.git#egg=jhw`

minimal usage:

`python3 generate.py -b 'Here are a bunch of words'  -o test.sh`

full usage:

`python3 generate.py -b 'Here are a bunch of words'  -o test.sh -btn 'Agree' -title 'Hello World'`

