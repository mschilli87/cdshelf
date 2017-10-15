# cdshelf default parameter definitions
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

# file:        defaults.py
# created:     2017-03-28
# last update: 2017-10-15
# author:      Marcel Schilling <marcel.schilling@mdc-berlin.de>
# license:     GNU Affero General Public License Version 3 (GNU AGPL v3)
# purpose:     define default parameters for cdshelf Audio CD backup &
#              conversion tool


######################################
# change log (reverse chronological) #
######################################

# 2017-10-15: added open_submission_url parameter
# 2017-08-29: added tmpdir_prefix & tmpdir_suffix parameters
# 2017-03-28: initial version (directory)


#################################
# default parameter definitions #
#################################

# default cdshelf base directory
directory = "/home/lecram/music"

# default choice on wether ("yes") or not ("no" [or any other value]) to
# (attempt to) open the submission URL for an unknown Disc ID in the (default)
# web browser
open_submission_url = "yes"

# default cdshelf temporary directory prefix
tmpdir_prefix = "cdshelf."

# default cdshelf temporary directory suffix
tmpdir_suffix = ".tmpdir"
