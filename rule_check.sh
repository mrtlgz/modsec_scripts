#!/bin/bash

# ./rule_check.sh -q {Question_Number}
# ./rule_check.sh -q 1

while getopts q: flag
do
    case "${flag}" in
        q) question_number=${OPTARG};;
    esac
done
echo "Testing Question: $question_number";
if apachectl configtest
then
        systemctl restart apache2
        echo "$(tput setaf 6)Apache restarted!$(tput sgr0)"
        $question_number.py
else
        echo "$(tput blink)$(tput setaf 1)Rule syntax error. Please read the description above and fix it accordingly..."$(tput sgr0)

fi
