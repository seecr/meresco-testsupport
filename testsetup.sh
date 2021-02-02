#!/bin/bash
## begin license ##
#
# "Meresco Testsupport" provides extra test tools.
#
# Copyright (C) 2020-2021 Seecr (Seek You Too B.V.) https://seecr.nl
#
# This file is part of "Meresco Testsuport"
#
# "Meresco Testsuport" is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
#
# "Meresco Testsuport" is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with "Meresco Testsuport"; if not, write to the Free Software
# Foundation, Inc., 51 Franklin St, Fifth Floor, Boston, MA  02110-1301  USA
#
## end license ##

set -o errexit
rm -rf tmp build
mydir=$(cd $(dirname $0); pwd)
source /usr/share/seecr-tools/functions.d/test

definePythonVars
${PYTHON} setup.py install --root tmp

cp -r test tmp/test
removeDoNotDistribute tmp
find tmp -name '*.py' -exec sed -r -e "
    s,^usrSharePath = .*,usrSharePath = '$mydir/tmp/usr/share/meresco-testsupport',;
    " -i '{}' \;

runtests "$@"

rm -rf tmp build
