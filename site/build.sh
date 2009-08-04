#!/bin/sh
cheetah-compile --idir egbdf --iext tmpl --odir egbdf --oext py -R --nobackup
find . -iname \*.py > python-files.tmp
xgettext --language=Python --keyword=_ -f python-files.tmp -D . -o strings.pot --force-po
rm python-files.tmp
