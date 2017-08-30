# cdshelf path-related functions
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

# file:    paths.py
# created: 2017-08-30
# author:  Marcel Schilling <marcel.schilling@mdc-berlin.de>
# license: GNU Affero General Public License Version 3 (GNU AGPL v3)
# purpose: define path-related functions for cdshelf Audio CD backup &
#          conversion tool


######################################
# change log (reverse chronological) #
######################################

# 2017-08-30: initial version (path-related constants / functions from disc.py)


###########
# imports #
###########

import re
import metadata


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
