#!/bin/bash

if apachectl configtest
then
        systemctl restart apache2
        echo "$(tput setaf 6)Apache restarted!$(tput sgr0)"
        1.py
else
        echo "$(tput blink)$(tput setaf 1)Rule syntax error. Please read the description above and fix it accordingly..."$(tput sgr0)

fi
