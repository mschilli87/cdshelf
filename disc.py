# cdshelf disc-related functions
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

# file:        disc.py
# created:     2017-03-26
# last update: 2017-08-30
# author:      Marcel Schilling <marcel.schilling@mdc-berlin.de>
# license:     GNU Affero General Public License Version 3 (GNU AGPL v3)
# purpose:     define disc-related functions for cdshelf Audio CD backup &
#              conversion tool


######################################
# change log (reverse chronological) #
######################################

# 2017-08-30: moved metadata-related functions into separate module
#             extended artist sort name retrieval to handle multiple artist
#             credits
#             adjusted medium index retrieval to handle empty disc list mediums
#             introduced string-pathification function based on regular
#             expressions
#             switched to using artist sort name for basename (unambiguous
#             artist credits only)
#             added missing print statement / fixed typo in comment
# 2017-04-23: removed get_directory in favor of parameters.get_param
#             adopted re-factored parameter-related messages
#             corrected user specified shelf-directory message (copy/paste
#             error)
#             corrected capitalization of 'Disc ID'
# 2017-03-28: added metadata fetching & disc image creation functions
# 2017-03-26: added read_disc_data & get_disc_id functions
#             initial version (get_device)


###########
# imports #
###########

import messages
import defaults
import metadata
import commands
import re
from os.path import dirname
from discid import get_default_device, DiscError
from discid import read as read_disc


#############
# constants #
#############

# regular expression matching string separators
separators_re = re.compile(r"[.-/ ]")

# regular expression matching several underscores
underscores_re = re.compile(r"_+")

# regular expression matching illegal characters
illegal_chars_re = re.compile(r"[^a-z0-9_]")


#############
# functions #
#############

# get device to read Audio CDs from
def get_device(params):

  # if user specified device parameter: use user specified device
  try:
    device = params["device"]
    print(messages.user_param("device"))

  # if no device parameter specified: detect default device
  except KeyError:
    print(messages.default_param("device"))
    device = get_default_device()

  # output device to be used before returning it
  print(messages.selected_param("device",device))
  return(device)


# read disc data of Audio CD
def read_disc_data(device):

  # read disc data from specified device
  print(messages.read_disc(device))
  try:
    disc = read_disc(device)
    return(disc)

  # abort with error if unsuccessful
  except DiscError:
    print(messages.disc_error(device))
    exit(1)


# get Disc ID of Audio CD
def get_disc_id(params):

  # read disc data and get Disc ID
  disc_id = read_disc_data(params).id

  # output Disc ID read before returning it
  print(messages.disc_id(disc_id))
  return(disc_id)


# convert string into a valid path element (not incl. any '/')
def pathify_string(string):

  # convert string to lower case
  string = string.lower()

  # replace separators by underscores
  string = separators_re.sub("_", string)

  # collapse several underscores to a single one
  string = underscores_re.sub("_", string)

  # replace ampersand by full word "and"
  string = string.replace("&", "and")

  # remove illegal characters
  string = illegal_chars_re.sub("", string)

  # return modified string
  return(string)


# get CD image basename from disc data
def get_basename(disc_data):

  # fetch metadata
  meta_data = metadata.lookup_disc_id(disc_data)

  # return basename: <artist>/<year>_<release>/<medium_index>-<Disc ID>
  return(pathify_string(metadata.extract_artist_sort_name(meta_data)) + "/" + \
         metadata.extract_year(meta_data) + "_" + \
         pathify_string(metadata.extract_title(meta_data)) + "/" + \
         metadata.get_medium_index(meta_data["medium-list"], disc_data.id) + \
         "-" + disc_data.id)


# create CD image
def create_image(device, directory, basename):

    # assemble shell command to create output directory & generate image:
    print(messages.create_image(device, directory, basename))
    return(commands.create_directory(dirname(directory + "/" + basename)) +
           " && " + commands.create_image(device, directory, basename))
