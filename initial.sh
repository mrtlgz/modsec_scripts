#!/bin/bash

chmod +x rule_check.sh
ln -s $PWD/rule_check.sh /usr/local/bin/
for i in {1..8}
do
   ln -s $PWD/python/$i.py /usr/local/bin/
done
