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
INCLUDE(cmake/python.cmake)

SET(PROJECT_NAME hpp-rbprm-robot-data)
SET(PROJECT_DESCRIPTION "Database for robots using hpp-rbprm")
SET(PROJECT_URL "")

SETUP_PROJECT ()

PKG_CONFIG_APPEND_LIBS(${PROJECT_NAME})

SET(CATKIN_PACKAGE_SHARE_DESTINATION
  ${CMAKE_INSTALL_DATAROOTDIR}/${PROJECT_NAME})

install(FILES
  data/package.xml
  DESTINATION ${CATKIN_PACKAGE_SHARE_DESTINATION}
  )
install(FILES
  data/urdf/hrp2/hrp2_trunk.urdf
  data/urdf/hrp2/hrp2_trunk_flexible.urdf
  data/urdf/hrp2/hrp2_rom.urdf
  data/urdf/hrp2/hrp2_larm_rom.urdf
  data/urdf/hrp2/hrp2_rarm_rom.urdf
  data/urdf/hrp2/hrp2_lleg_rom.urdf
  data/urdf/hrp2/hrp2_rleg_rom.urdf
  DESTINATION ${CATKIN_PACKAGE_SHARE_DESTINATION}/urdf/hrp2
  )
install(FILES
  data/urdf/hyq/hyq_trunk.urdf
  data/urdf/hyq/hyq_trunk_large.urdf
  data/urdf/hyq/hyq_rhleg_rom.urdf
  data/urdf/hyq/hyq_rfleg_rom.urdf
  data/urdf/hyq/hyq_lhleg_rom.urdf
  data/urdf/hyq/hyq_lfleg_rom.urdf
  data/urdf/hyq/hyq_rom.urdf
  DESTINATION ${CATKIN_PACKAGE_SHARE_DESTINATION}/urdf/hyq
  )
install(FILES
  data/srdf/hrp2/hrp2_trunk.srdf
  data/srdf/hrp2/hrp2_trunk_flexible.srdf
  data/srdf/hrp2/hrp2_rom.srdf
  data/srdf/hrp2/hrp2_larm_rom.srdf
  data/srdf/hrp2/hrp2_rarm_rom.srdf
  data/srdf/hrp2/hrp2_lleg_rom.srdf
  data/srdf/hrp2/hrp2_rleg_rom.srdf
  DESTINATION ${CATKIN_PACKAGE_SHARE_DESTINATION}/srdf/hrp2
  )
  
install(FILES
  data/srdf/hyq/hyq_trunk.srdf
  data/srdf/hyq/hyq_trunk_large.srdf
  data/srdf/hyq/hyq_rhleg_rom.srdf
  data/srdf/hyq/hyq_rfleg_rom.srdf
  data/srdf/hyq/hyq_lhleg_rom.srdf
  data/srdf/hyq/hyq_lfleg_rom.srdf
  data/srdf/hyq/hyq_rom.srdf
  DESTINATION ${CATKIN_PACKAGE_SHARE_DESTINATION}/srdf
  )
install(FILES
	data/meshes/hrp2/hrp2_trunk.stl
	data/meshes/hrp2/hrp2_trunk_body.stl
	data/meshes/hrp2/hrp2_trunk_torso.stl
	data/meshes/hrp2/hrp2_trunk_body_view.dae
	data/meshes/hrp2/hrp2_trunk_torso_view.dae
	data/meshes/hrp2/hrp2_rom.stl
	data/meshes/hrp2/hrp2_larm_rom.stl
	data/meshes/hrp2/hrp2_rarm_rom.stl
	data/meshes/hrp2/hrp2_lleg_rom.stl
	data/meshes/hrp2/hrp2_rleg_rom.stl
  DESTINATION ${CATKIN_PACKAGE_SHARE_DESTINATION}/meshes/hrp2
  )
install(FILES
	data/meshes/hyq/hyq_all.stl
	data/meshes/hyq/hyq_trunk.stl
	data/meshes/hyq/hyq_trunk_large.stl
	data/meshes/hyq/hyq_rom.stl
	data/meshes/hyq/hyq_rhleg_rom.stl
	data/meshes/hyq/hyq_rfleg_rom.stl
	data/meshes/hyq/hyq_lhleg_rom.stl
	data/meshes/hyq/hyq_lfleg_rom.stl
  DESTINATION ${CATKIN_PACKAGE_SHARE_DESTINATION}/meshes/hyq
  )

  
SETUP_PROJECT_FINALIZE()

