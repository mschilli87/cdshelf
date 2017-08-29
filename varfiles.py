# cdshelf varfiles-related functions
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

# file:      varfiles.py
# created:   2017-08-29
# author:    Marcel Schilling <marcel.schilling@mdc-berlin.de>
# license:   GNU Affero General Public License Version 3 (GNU AGPL v3)
# purpose:   define functions to store Python variables in (temporary) files for
#            cdshelf Audio CD backup & conversion tool


######################################
# change log (reverse chronological) #
######################################

# 2017-08-29: initial version (get_device)


###########
# imports #
###########

import tempfile
from os import linesep
from os.path import join as path_join


#############
# functions #
#############

# get varfile path
def get_varfile(variable, varfile_dir, varfile_suffix = ".cdshelf_varfile"):
    return(path_join(varfile_dir, variable + varfile_suffix))


# write variable to varfile
def write_varfile(variable, file_path):
    with open(file_path, 'w') as varfile:
      print(variable, file = varfile)


# read variable from varfile
def read_varfile(file_path):
    with open(file_path, 'r') as varfile:
      value = varfile.read().rstrip(linesep)
    return(value)
