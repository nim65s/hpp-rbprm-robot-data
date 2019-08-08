# Copyright (c) 2012 CNRS
# Author: Florent Lamiraux
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

# Requires at least CMake 2.6 to configure the package.
CMAKE_MINIMUM_REQUIRED(VERSION 2.6)

SET(CXX_DISABLE_WERROR true)

INCLUDE(cmake/base.cmake)
INCLUDE(cmake/idl.cmake)
INCLUDE(cmake/hpp.cmake)
INCLUDE(cmake/hpp/python.cmake)

SET(PROJECT_NAME hpp-rbprm-robot-data)
SET(PROJECT_DESCRIPTION "Database for robots using hpp-rbprm")

SET(CUSTOM_HEADER_DIR "hpp/rbprm-robot-data")

SETUP_HPP_PROJECT ()

HPP_FINDPYTHON()

SET(CATKIN_PACKAGE_SHARE_DESTINATION
  ${CMAKE_INSTALL_DATAROOTDIR}/${PROJECT_NAME})


SET(CATKIN_HYQ_PACKAGE_SHARE_DESTINATION
  ${CMAKE_INSTALL_DATAROOTDIR}/hyq-rbprm)

SET(CATKIN_SIMPLEHUMANOID_PACKAGE_SHARE_DESTINATION
  ${CMAKE_INSTALL_DATAROOTDIR}/simpleHumanoid-rbprm)

install(FILES
  data/hyq/package.xml
  DESTINATION ${CATKIN_HYQ_PACKAGE_SHARE_DESTINATION})

install(DIRECTORY
  data/hyq_description
  DESTINATION ${CMAKE_INSTALL_DATAROOTDIR}
  )

install(DIRECTORY
  data/hyq/
  DESTINATION ${CATKIN_HYQ_PACKAGE_SHARE_DESTINATION}
  )

install(DIRECTORY
  data/hyq_description
  DESTINATION ${CMAKE_INSTALL_DATAROOTDIR}
  )

install(DIRECTORY
  data/simpleHumanoid/
  DESTINATION ${CATKIN_SIMPLEHUMANOID_PACKAGE_SHARE_DESTINATION}
  )

install (FILES
  src/hpp/corbaserver/rbprm/hyq_abstract/robot.py
  src/hpp/corbaserver/rbprm/hyq_abstract/__init__.py
  DESTINATION ${PYTHON_SITELIB}/hpp/corbaserver/rbprm/hyq_abstract)

install (FILES
  src/hpp/corbaserver/rbprm/simpleHumanoid_abstract/robot.py
  src/hpp/corbaserver/rbprm/simpleHumanoid_abstract/__init__.py
  DESTINATION ${PYTHON_SITELIB}/hpp/corbaserver/rbprm/simpleHumanoid_abstract)

install (FILES
  src/hpp/corbaserver/rbprm/hyq/robot.py
  src/hpp/corbaserver/rbprm/hyq/__init__.py
  DESTINATION ${PYTHON_SITELIB}/hpp/corbaserver/rbprm/hyq)

install (FILES
  src/hpp/corbaserver/rbprm/hyq_contact6D/robot.py
  src/hpp/corbaserver/rbprm/hyq_contact6D/__init__.py
  DESTINATION ${PYTHON_SITELIB}/hpp/corbaserver/rbprm/hyq_contact6D)

install (FILES
  src/hpp/corbaserver/rbprm/hyq_abstract/robot.py
  src/hpp/corbaserver/rbprm/hyq_abstract/__init__.py
  DESTINATION ${PYTHON_SITELIB}/hpp/corbaserver/rbprm/hyq_abstract)



SETUP_HPP_PROJECT_FINALIZE()
