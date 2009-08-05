#!/bin/sh
#cheetah-compile --idir egbdf --iext tmpl --odir egbdf --oext py -R --nobackup
find . -iname \*.py > python-files.tmp
find . -iname \*.html >> python-files.tmp
xgettext --language=Python --keyword=_ -f python-files.tmp -D . -o strings.pot --force-po --from-code=utf-8
rm python-files.tmp
