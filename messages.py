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
# last update: 2017-12-25
# author:      Marcel Schilling <marcel.schilling@mdc-berlin.de>
# license:     GNU Affero General Public License Version 3 (GNU AGPL v3)
# purpose:     define messages for cdshelf Audio CD backup & conversion tool


######################################
# change log (reverse chronological) #
######################################

# 2017-12-25: added get_metadata command & release ID lookup messages
# 2017-10-15: added pretend_image command & correspondig message
#             added open_submission_url parameter
# 2017-08-30: added submission URL to Disc ID lookup error message
#             removed ambiguous artist credit error message
#             added ambiguous artist credit error message
#             fixed typo in function name
# 2017-08-29: added tmpdir_prefix & tmpdir_suffix parameters
# 2017-04-23: re-factored parameter-related message definition (functions
#             instead of copy/paste code)
#             corrected capitalization of 'Disc ID'
# 2017-03-28: added image & directory commands & directory parameter to usage
#             message / added metadata-, directory- & image-related messages
# 2017-03-26: added discid command to usage message / added messages related to
#             disc data reading & Disc ID extraction
#             added device command & parameter to usage message / added
#             device-related messages
#             initial version (help, usage & license)


###########
# imports #
###########

import defaults


#######################
# message definitions #
#######################

# define usage message
usage="""\
usage: cdshelf <command> [<command> ...] [--config <parameter>=<value> [<parameter>=<value>]]

The following commands are currently supported:

help          print help message
pretend_image pretend to create CD image (dry-run)
image         create CD image
get_metadata  fetch missing metadata for shelved releases from MusicBrainz
usage         show usage
license       print license
discid        print Disc ID of Audio CD in CD device
device        print CD device to be used for reading Audio CDs
directory     print cdshelf base directory

The following parameters are currently supported:

device              device to read Audio CDs from (default: detect default device)
directory           cdshelf base directory (default: '""" + \
                    defaults.directory + """')
open_submission_url choice on wether ("yes") or not ("no" [or any other value])
                    to (attempt to) open the submission URL of an unknown Disc
                    ID in the (default) web browser (default: '""" + \
                    defaults.open_submission_url + """')
tmpdir_prefix       cdshelf temporary directory prefix (default: '""" + \
                    defaults.tmpdir_prefix + """')
tmpdir_suffix       cdshelf temporary directory suffix (default: '""" + \
                    defaults.tmpdir_suffix + """')
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


##############################
# parameter-related messages #
##############################

# verbose text description to use in messages instead of parameter name
param_label = {
  "device": "CD device",
  "directory": "shelf directory",
  "open_submission_url": "choice on wether ('yes') or not ('no' [or any " + \
                         "other value]) to (attempt to) open the " + \
                         "submission URL of an unknown Disc ID in the " + \
                         "(default) web browser",
  "tmpdir_prefix": "cdshelf temporary directory prefix",
  "tmpdir_suffix": "cdshelf temporary directory suffix",
}


# message indicating user specified parameter
def user_param(parameter):
  return(param_label[parameter] + " specified by user...")

# text description of how default parameter is obtained
param_default_action = {
  "device": "detecting default device",
}


# message indicating default parameter usage
def default_param(parameter):

  # get parameter label
  param = param_label[parameter]

  # if specific default parameter action was defined, use it
  try:
    default_action = param_default_action[parameter]

  # otherwise, use default description
  except KeyError:
    default_action = "using default " + param

  # compose message from parts & return
  return("\nno " + param + " specified by user; " + default_action + "...\n" +
         "overwrite by setting --config " + parameter + "=<" + parameter +
         ">\n")

# message indicating selected value for parameter
def selected_param(parameter, selected_value):
  return("using " + param_label[parameter] + " '" + selected_value + "'")


#########################
# disc-related messages #
#########################

# message indicating disc reading
def read_disc(device):
  return("reading disc in device '" + device + "'...")

# message indicating disc reading error
def disc_error(device):
  return("ERROR: Cannot read disc in device '" + device + "'!")

# message indicating read Disc ID
def disc_id(disc_id):
  return("read Disc ID '" + disc_id + "'")


#############################
# metadata-related messages #
#############################

# message indicating Disc ID lookup
def lookup_disc_id(disc_id):
  return("fetching metadata for Disc ID '" + disc_id + "' from MusicBrainz...")

# message indicating Disc ID lookup error
def disc_id_unknown(disc_id, submission_url):
  return("ERROR: Disc ID '" + disc_id + "' is not associated to any release on MusicBrainz.\n" +\
         "Please submit it using the following URL: '" + submission_url + "'.")

# message indicating ambiguous Disc ID lookup result
def disc_id_ambiguous(disc_id):
  return("ERROR: Disc ID '" + disc_id + "' is associated to several releases on MusicBrainz")

# message indicating release ID lookup
def lookup_release_id(release_id):
  return("fetching metadata for release ID '" + release_id + "' from MusicBrainz...")

# message indicating release ID lookup error
def release_id_unknown(release_id):
  return("ERROR: Release ID '" + release_id +\
         "' is not associated to any release on MusicBrainz.")


##########################
# image-related messages #
##########################

# message indicating image generation target
def image_target(device, directory, basename):
    return(" an image of CD in device '" + device + "' in directory '" +
           directory + "' using basename '" + basename + "'")

# message pretending image generation
def pretend_image(device, directory, basename):
    return("cdshelf image would create" +
           image_target(device, directory, basename))

# message indicating image generation
def create_image(device, directory, basename):
    return("creating" + image_target(device, directory, basename))
