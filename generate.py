#!/usr/bin/env python3

import argparse

from src.jhw import main 

my_parser = argparse.ArgumentParser(prog='generate',
                                    description='Makes a chunk of text you can paste into jamf')
my_parser.add_argument('-b',
                       metavar='body',
                       type=str,
                       help='window body')
my_parser.add_argument('-o',
                       type=str,
                       help='outfile')
my_parser.add_argument('-btn',
                       type=str,
                       help='button label')
my_parser.add_argument('-title',
                       type=str,
                       help='button label')

args = my_parser.parse_args()

# make required args into english
body = args.b
out_file = args.o

# make rest of buttons
if args.title:
    title = args.title
else:
    title = 'Management Action Needed'
if args.btn:
    button_label = args.btn
else:
    button_label = 'Default Button'

# hand over the window ingredients
wind = main.mw(
    title,
    body,
    button_label
    )

formed_window_command =  main.mw.create(wind)
bash_header = "#!/bin/sh \n \n"
do = 'open -a "Self Service.app"'

def save_file(contents):
    with open(out_file, 'w') as file:
        file.write(contents)    

def handle_response_maker(action):
    stuff = '''

if [ $RESULT == 0 ]; then
# do button1 stuff
    '''
    rest = '''

elif [ $RESULT == 2 ]; then
# do button2 stuff
echo "Cancel was pressed!"
fi
    '''
    
    return stuff + action + rest

def flatten_for_bash():
    bash_command = ''

    '''take the list and combine it to a proper bash command, seperate with a blankspace'''
    for index, item in enumerate(formed_window_command):
        if index == 0:
            bash_command += item
        else:
            bash_command += ' "' + item + '"'
        # else:
        #     bash_command += ' ' + item
    return bash_command

contents = str(f"{bash_header}RESULT=`{flatten_for_bash()}` {handle_response_maker(do)}")
print(contents)
save_file(contents)
