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
  
SET(CATKIN_HRP2_PACKAGE_SHARE_DESTINATION
  ${CMAKE_INSTALL_DATAROOTDIR}/hrp2-rbprm)
  
SET(CATKIN_HYQ_PACKAGE_SHARE_DESTINATION
  ${CMAKE_INSTALL_DATAROOTDIR}/hyq-rbprm)

install(FILES
  data/hrp2/package.xml
  DESTINATION ${CATKIN_HRP2_PACKAGE_SHARE_DESTINATION}
  )
install(FILES
  data/hyq/package.xml
  DESTINATION ${CATKIN_HYQ_PACKAGE_SHARE_DESTINATION}
  )
install(FILES
  data/hrp2/urdf/hrp2_trunk.urdf
  data/hrp2/urdf/hrp2_trunk_flexible.urdf
  data/hrp2/urdf/hrp2_rom.urdf
  data/hrp2/urdf/hrp2_larm_rom.urdf
  data/hrp2/urdf/hrp2_rarm_rom.urdf
  data/hrp2/urdf/hrp2_lleg_rom.urdf
  data/hrp2/urdf/hrp2_rleg_rom.urdf
  DESTINATION ${CATKIN_HRP2_PACKAGE_SHARE_DESTINATION}/urdf
  )
install(FILES
  data/hyq/urdf/hyq_trunk.urdf
  data/hyq/urdf/hyq_trunk_large.urdf
  data/hyq/urdf/hyq_rhleg_rom.urdf
  data/hyq/urdf/hyq_rfleg_rom.urdf
  data/hyq/urdf/hyq_lhleg_rom.urdf
  data/hyq/urdf/hyq_lfleg_rom.urdf
  data/hyq/urdf/hyq_rom.urdf
  DESTINATION ${CATKIN_HYQ_PACKAGE_SHARE_DESTINATION}/urdf
  )
install(FILES
  data/hrp2/srdf/hrp2_trunk.srdf
  data/hrp2/srdf/hrp2_trunk_flexible.srdf
  data/hrp2/srdf/hrp2_rom.srdf
  data/hrp2/srdf/hrp2_larm_rom.srdf
  data/hrp2/srdf/hrp2_rarm_rom.srdf
  data/hrp2/srdf/hrp2_lleg_rom.srdf
  data/hrp2/srdf/hrp2_rleg_rom.srdf
  DESTINATION ${CATKIN_HRP2_PACKAGE_SHARE_DESTINATION}/srdf
  )
  
install(FILES
  data/hyq/srdf/hyq_trunk.srdf
  data/hyq/srdf/hyq_trunk_large.srdf
  data/hyq/srdf/hyq_rhleg_rom.srdf
  data/hyq/srdf/hyq_rfleg_rom.srdf
  data/hyq/srdf/hyq_lhleg_rom.srdf
  data/hyq/srdf/hyq_lfleg_rom.srdf
  data/hyq/srdf/hyq_rom.srdf
  DESTINATION ${CATKIN_HYQ_PACKAGE_SHARE_DESTINATION}/srdf
  )
install(FILES
	data/hrp2/meshes/hrp2_trunk.stl
	data/hrp2/meshes/hrp2_trunk_body.stl
	data/hrp2/meshes/hrp2_trunk_torso.stl
	data/hrp2/meshes/hrp2_trunk_body_view.dae
	data/hrp2/meshes/hrp2_trunk_torso_view.dae
	data/hrp2/meshes/hrp2_rom.stl
	data/hrp2/meshes/hrp2_larm_rom.stl
	data/hrp2/meshes/hrp2_rarm_rom.stl
	data/hrp2/meshes/hrp2_lleg_rom.stl
	data/hrp2/meshes/hrp2_rleg_rom.stl
  DESTINATION ${CATKIN_HRP2_PACKAGE_SHARE_DESTINATION}/meshes
  )
install(FILES
	data/hyq/meshes/hyq_all.stl
	data/hyq/meshes/hyq_trunk.stl
	data/hyq/meshes/hyq_trunk_large.stl
	data/hyq/meshes/hyq_rom.stl
	data/hyq/meshes/hyq_rhleg_rom.stl
	data/hyq/meshes/hyq_rfleg_rom.stl
	data/hyq/meshes/hyq_lhleg_rom.stl
	data/hyq/meshes/hyq_lfleg_rom.stl
  DESTINATION ${CATKIN_HYQ_PACKAGE_SHARE_DESTINATION}/meshes
  )
install(FILES
	data/hrp2/database/hrp2_larm.db
	data/hrp2/database/hrp2_lleg.db
	data/hrp2/database/hrp2_rleg.db
	data/hrp2/database/hrp2_rarm.db
  DESTINATION ${CATKIN_HRP2_PACKAGE_SHARE_DESTINATION}/database
  )

  
SETUP_PROJECT_FINALIZE()

