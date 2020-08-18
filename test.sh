#!/bin/sh 
 
RESULT=`/Library/Application\ Support/JAMF/bin/jamfHelper.app/Contents/MacOS/jamfHelper "-windowType" "hud" "-title" "sorry already running" "-description" "asdf here are a craploadn of words" "-icon" "/System/Library/CoreServices/Problem Reporter.app/Contents/Resources/ProblemReporter.icns" "-defaultbutton" "1" "-button1" "great"` 

if [ $RESULT == 0 ]; then
# do button1 stuff
    open -a "Self Service.app"

elif [ $RESULT == 2 ]; then
# do button2 stuff
echo "Cancel was pressed!"
fi
    