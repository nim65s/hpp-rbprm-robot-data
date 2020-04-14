# Copyright (c) 2012, 2020 CNRS
# Author: Florent Lamiraux, Guilhem Saurel
#
# This file is part of hpp-rbprm-corba.
# hpp-rbprm-corba is free software: you can redistribute it
# and/or modify it under the terms of the GNU Lesser General Public
# License as published by the Free Software Foundation, either version
# 3 of the License, or (at your option) any later version.
#
# hpp-rbprm-corba is distributed in the hope that it will be
# useful, but WITHOUT ANY WARRANTY; without even the implied warranty
# of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
# General Lesser Public License for more details.  You should have
# received a copy of the GNU Lesser General Public License along with
# hpp-rbprm-corba.  If not, see
# <http://www.gnu.org/licenses/>.

CMAKE_MINIMUM_REQUIRED(VERSION 3.1)

SET(PROJECT_NAME hpp-rbprm-robot-data)
SET(PROJECT_DESCRIPTION "Database for robots using hpp-rbprm")

SET(PROJECT_USE_CMAKE_EXPORT TRUE)
SET(CXX_DISABLE_WERROR TRUE)

INCLUDE(cmake/hpp.cmake)
INCLUDE(cmake/idl.cmake)
INCLUDE(cmake/python.cmake)

SET(CUSTOM_HEADER_DIR "hpp/rbprm-robot-data")

COMPUTE_PROJECT_ARGS(PROJECT_ARGS LANGUAGES CXX)
PROJECT(${PROJECT_NAME} ${PROJECT_ARGS})

FINDPYTHON()

ADD_LIBRARY(${PROJECT_NAME} INTERFACE)
INSTALL(TARGETS ${PROJECT_NAME} EXPORT ${TARGETS_EXPORT_NAME} DESTINATION lib)

install(DIRECTORY data/hyq_description
  DESTINATION share)

install(DIRECTORY data/hyq/
  DESTINATION share/hyq-rbprm)

install(DIRECTORY data/hyq_description
  DESTINATION share)

install(DIRECTORY data/simpleHumanoid/
  DESTINATION share/simpleHumanoid-rbprm)

ADD_SUBDIRECTORY(src)
