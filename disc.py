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

# 2017-08-30: switched to using artist sort name for basename (unambiguous
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
import commands
from os.path import dirname
from discid import get_default_device, DiscError
from discid import read as read_disc
from musicbrainzngs import set_useragent, ResponseError
from musicbrainzngs import get_releases_by_discid as fetch_metadata


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


# get disc metadata
def lookup_disc_id(disc):

  # set user agent
  set_useragent("cdshelf", "alpha",
                "https://github.com/mschilli87/cdshelf/issues")

  # fetch metadata for Disc ID
  print(messages.lookup_disc_id(disc.id))
  try:
    disc_metadata = fetch_metadata(disc.id, cdstubs=False, includes=["artists"])

  # abort with error if unsuccessful
  except ResponseError:
    print(messages.disc_id_unknown(disc.id))
    exit(1)

  # get associated releases
  disc_metadata = disc_metadata["disc"]["release-list"]

  # abort with error if unambiguous
  if(len(disc_metadata) > 1):
    print(messages.disc_ambiguous(disc_id))
    exit(1)

  # return metadata
  return(disc_metadata[0])


# extract artist credit from release metadata
def extract_artist_sort_name(metadata):

  # get artist credit
  artist_credit = metadata["artist-credit"]

  # abort with error if ambiguous
  if(len(artist_credit) > 1):
    print(messages.artist_credit_ambiguous(metadata["id"]))
    exit(1)

  # return artist sort name
  return(artist_credit[0]["artist"]["sort-name"])


# extract release year from release metadata
def extract_year(metadata):
  return(metadata["date"][0:4])


# extract release title from release metadata
def extract_title(metadata):
  return(metadata["title"])


# extract index of medium matching given Disc ID from release metadata
def get_medium_index(mediums, disc_id):

  # count mediums
  n_mediums = len(mediums)

  # match Disc ID
  medium_index = [i + 1 for i in range(n_mediums)
                  if mediums[i]["disc-list"][0]["id"] == disc_id][0]

  # pad medium index with as many zeroes as nessecary before returning it
  digits_medium = len(str(n_mediums))
  return(str(medium_index).zfill(digits_medium))


# get CD image basename from disc data
def get_basename(disc_data):

  # fetch metadata
  metadata = lookup_disc_id(disc_data)

  # return basename: <artist>/<year>_<release>/<medium_index>-<Disc ID>
  return(extract_artist_sort_name(metadata).lower().replace(", "," ").replace(" ","_") + \
         "/" + extract_year(metadata) + "_" + \
         extract_title(metadata).lower().replace(" ","_") + "/" + \
         get_medium_index(metadata["medium-list"], disc_data.id) + "-" + \
         disc_data.id)


# create CD image
def create_image(device, directory, basename):

    # assemble shell command to create output directory & generate image:
    print(messages.create_image(device, directory, basename))
    return(commands.create_directory(dirname(directory + "/" + basename)) +
           " && " + commands.create_image(device, directory, basename))
