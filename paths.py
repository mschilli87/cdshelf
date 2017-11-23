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

# file:        paths.py
# created:     2017-08-30
# last update: 2017-11-23
# author:      Marcel Schilling <marcel.schilling@mdc-berlin.de>
# license:     GNU Affero General Public License Version 3 (GNU AGPL v3)
# purpose:     define path-related functions for cdshelf Audio CD backup &
#              conversion tool


######################################
# change log (reverse chronological) #
######################################

# 2017-11-23: added ID basename format (new default)
# 2017-10-15: added passing down of open_submission_url parameter
# 2017-08-30: fixed placing of '-' in separators regular expression definition
#             initial version (path-related constants / functions from disc.py)


###########
# imports #
###########

import re
import metadata


#############
# constants #
#############

# regular expression matching string separators
separators_re = re.compile(r"[./ -]")

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
def get_basename(disc_data, open_submission_url, pretty=False):

  # fetch metadata
  meta_data = metadata.lookup_disc_id(disc_data, open_submission_url)

  # pretty basename dir: <artist>/<year>_<release>
  # ID basename dir: <release_group_id>/<release_id>
  basename_dir = ((
      pathify_string(metadata.extract_artist_sort_name(meta_data)) + "/"
      + metadata.extract_year(meta_data) + "_"
      + pathify_string(metadata.extract_title(meta_data)))
    if pretty else (
      metadata.extract_release_group_id(meta_data) + "/"
      + metadata.extract_release_id(meta_data)))

  # basename file: <medium_index>-<Disc ID>
  basename_file = (metadata.get_medium_index(meta_data["medium-list"],
                                             disc_data.id)
                   + "-" + disc_data.id)

  # return full basename
  return(basename_dir + "/" + basename_file)
