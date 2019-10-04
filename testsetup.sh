#!/bin/bash
## begin license ##
#
# "Seecr Test Extra" provides extra test tools - which bring in lots of dependencies.
#
# Copyright (C) 2019 Seecr (Seek You Too B.V.) http://seecr.nl
#
# This file is part of "Seecr Test Extra"
#
# "Seecr Test Extra" is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
#
# "Seecr Test Extra" is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with "Seecr Test Extra"; if not, write to the Free Software
# Foundation, Inc., 51 Franklin St, Fifth Floor, Boston, MA  02110-1301  USA
#
## end license ##

set -e

rm -rf tmp build

python3 setup.py install --root tmp

export PYTHONPATH=`pwd`/tmp/usr/local/lib/`py3versions -d`/dist-packages
cp -r test tmp/test
#cp seecr/__init__.py $PYTHONPATH/seecr/
#cp seecr/test/__init__.py $PYTHONPATH/seecr/test/

set +e
(
    cd tmp/test
    ./alltests.sh
)
set -e

rm -rf tmp build