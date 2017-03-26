# cdshelf message definitions
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

# file:        messages.py
# created:     2017-03-26
# last update: 2017-03-26
# author:      Marcel Schilling <marcel.schilling@mdc-berlin.de>
# license:     GNU Affero General Public License Version 3 (GNU AGPL v3)
# purpose:     define messages for cdshelf Audio CD backup & conversion tool


######################################
# change log (reverse chronological) #
######################################

# 2017-03-26: added discid command to usage message / added messages related to
#             disc data reading & disc ID extraction
#             added device command & parameter to usage message / added
#             device-related messages
#             initial version (help, usage & license)


#######################
# message definitions #
#######################

# define usage message
usage="""\
usage: cdshelf <command> [<command> ...] [--config <parameter>=<value>]

The following commands are currently supported:

help	print help message
usage	show usage
license	print license
discid	print disc ID of Audio CD in CD device
device	print CD device to be used for reading Audio CDs

The following parameter is currently supported:

device	device to read Audio CDs from (default: detect default device)
"""

# define help message
help="""\
cdshelf

Audio CD backup & conversion tool


""" + usage

# define license message
license="""\
Copyright (C) 2017  Marcel Schilling

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU Affero General Public License as
published by the Free Software Foundation, either version 3 of the
License, or (at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU Affero General Public License for more details.

You should have received a copy of the GNU Affero General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>.
"""

###########################
# device-related messages #
###########################

# message indicating user-specified device
user_device = "CD device specified by user..."

# message indicating default device detection
default_device = """\
no CD device specified by user; detecting default device...
overwrite by setting --config device=<device>\
"""

# message indicating selected device
def selected_device(device):
  return("using CD device '" + device + "'")


#########################
# disc-related messages #
#########################

# message indicating disc reading
def read_disc(device):
  return("reading disc in device '" + device + "'...")

# message indicating disc reading error
def disc_error(device):
  return("ERROR: Cannot read disc in device '" + device + "'!")

# message indicating read disc ID
def disc_id(disc_id):
  return("read disc ID '" + disc_id + "'")
