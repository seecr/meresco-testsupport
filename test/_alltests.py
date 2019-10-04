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

from os import getuid
assert getuid() != 0, "Do not run tests as 'root'"

from seecrdeps import includeParentAndDeps, cleanup  #DO_NOT_DISTRIBUTE
includeParentAndDeps(__file__, scanForDeps=True)     #DO_NOT_DISTRIBUTE
cleanup(__file__)                                    #DO_NOT_DISTRIBUTE

from unittest import main

from onetest import OneTest


if __name__ == '__main__':
    main()