# cdshelf tmpdir-related functions
# Copyright (C) 2017  Marcel Schilling
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as
# published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.


#######################
# general information #
#######################

# file:      tmpdir.py
# created:   2017-08-29
# author:    Marcel Schilling <marcel.schilling@mdc-berlin.de>
# license:   GNU Affero General Public License Version 3 (GNU AGPL v3)
# purpose:   define functions used to create temporary directory for cdshelf
#            Audio CD backup & conversion tool


######################################
# change log (reverse chronological) #
######################################

# 2017-08-29: initial version (create_tmpdir)


###########
# imports #
###########

from tempfile import mkdtemp


#############
# functions #
#############

# create temporary directory
def create_tmpdir(pref, suff):
  return(mkdtemp(suffix = suff, prefix = pref))
