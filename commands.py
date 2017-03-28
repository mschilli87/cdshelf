# cdshelf command definitions
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

# file:    commands.py
# created: 2017-03-28
# author:  Marcel Schilling <marcel.schilling@mdc-berlin.de>
# license: GNU Affero General Public License Version 3 (GNU AGPL v3)
# purpose: define commands for cdshelf Audio CD backup & conversion tool


######################################
# change log (reverse chronological) #
######################################

# 2017-03-28: initial version (create_directory & create_image)


#######################
# command definitions #
#######################

# command used to create directory
def create_directory(directory):
  return("mkdir --parent " + directory)

# command used to create CD image
def create_image(device, directory, basename):
  return("cdrdao read-cd --read-raw" +
                       " --device '" + device + "' " +
                       " --datafile '" + directory + "/" + basename + "'.bin" +
                                  " '" + directory + "/" + basename + "'.toc")
