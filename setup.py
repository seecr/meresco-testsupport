#!/usr/bin/env python3
## begin license ##
#
# "Meresco Testsupport" provides extra test tools.
#
# Copyright (C) 2019, 2021 Seecr (Seek You Too B.V.) https://seecr.nl
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

from distutils.core import setup
from os import walk
from os.path import join

scripts = []
for path, dirs, files in walk('bin'):
    for file in files:
        scripts.append(join(path, file))

setup(
    name='seecr-test-extra',
    version='%VERSION%',
    packages=[
        'seecr',       # DO_NOT_DISTRIBUTE
        'seecr.test',  # DO_NOT_DISTRIBUTE
        'seecr.test.extra',
        'seecr.test.extra.selenium',
    ],
    scripts=scripts,
    url='http://www.seecr.nl',
    author='Seecr',
    author_email='info@seecr.nl',
    description='Seecr Test Extra provides extra test tools',
    long_description='Seecr Test Extra provides extra test tools - which bring in lots of dependencies.',
    platforms=['linux'],
)

