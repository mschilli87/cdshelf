# cdshelf parameter-related functions
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

# file:    parameters.py
# created: 2017-04-23
# author:  Marcel Schilling <marcel.schilling@mdc-berlin.de>
# license: GNU Affero General Public License Version 3 (GNU AGPL v3)
# purpose: define parameter-related functions for cdshelf Audio CD backup &
#          conversion tool


######################################
# change log (reverse chronological) #
######################################

# 2017-03-28: initial version (get_param)


###########
# imports #
###########

import messages
import defaults


#############
# functions #
#############

# get parameter
def get_param(param, params):

  # if user specified parameter: use user specified value
  try:
    value = params[param]
    print(messages.user_param(param))

  # if parameter not specified: use default value
  except KeyError:
    print(messages.default_param(param))
    value = eval("defaults." + param)

  # output value to be used before returning it
  print(messages.selected_param(param, value))
  return(value)
