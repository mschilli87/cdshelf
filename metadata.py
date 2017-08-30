# cdshelf metadata-related functions
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

# file:        metadata.py
# created:     2017-08-30
# last update: 2017-08-30
# author:      Marcel Schilling <marcel.schilling@mdc-berlin.de>
# license:     GNU Affero General Public License Version 3 (GNU AGPL v3)
# purpose:     define metadata-related functions for cdshelf Audio CD backup &
#              conversion tool


######################################
# change log (reverse chronological) #
######################################

# 2017-08-30: fixed typos in ambiguous Disc ID catch
#             initial version (metadata-related functions from disc.py)


###########
# imports #
###########

import messages
from musicbrainzngs import set_useragent, ResponseError
from musicbrainzngs import get_releases_by_discid as fetch_metadata


#############
# functions #
#############

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
    print(messages.disc_id_ambiguous(disc.id))
    exit(1)

  # return metadata
  return(disc_metadata[0])


# extract artist credit from release metadata
def extract_artist_sort_name(metadata):
  return(''.join([entry["artist"]["sort-name"] if type(entry) is dict else entry
                   for entry in metadata["artist-credit"]]))


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
                  if len(mediums[i]["disc-list"]) > 0 and \
                     mediums[i]["disc-list"][0]["id"] == disc_id][0]

  # pad medium index with as many zeroes as nessecary before returning it
  digits_medium = len(str(n_mediums))
  return(str(medium_index).zfill(digits_medium))
