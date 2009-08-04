#!/bin/sh
find . -iname \*.pyc -exec rm {} \;
find ./egbdf/templates -iname \*.py -exec rm {} \;
rm ./strings.pot
