#!/usr/bin/env python
# Copyright (c) 2019 CNRS
# Author: Pierre Fernbach
#
# This file is part of hpp-rbprm-robot-data.
# hpp_tutorial is free software: you can redistribute it
# and/or modify it under the terms of the GNU Lesser General Public
# License as published by the Free Software Foundation, either version
# 3 of the License, or (at your option) any later version.
#
# hpp_tutorial is distributed in the hope that it will be
# useful, but WITHOUT ANY WARRANTY; without even the implied warranty
# of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
# General Lesser Public License for more details.  You should have
# received a copy of the GNU Lesser General Public License along with
# hpp_tutorial.  If not, see
# <http://www.gnu.org/licenses/>.

from hpp.corbaserver.rbprm.rbprmbuilder import Builder as Parent

class Robot (Parent):
    ##
    #  Information to retrieve urdf and srdf files.
    rootJointType = 'freeflyer'
    packageName = 'hyq-rbprm'
    meshPackageName = 'hyq-rbprm'
    # URDF file describing the trunk of the robot HyQ
    urdfName = 'hyq_trunk_large'
    # URDF files describing the reachable workspace of each limb of HyQ
    urdfNameRom = ['hyq_lhleg_rom','hyq_lfleg_rom','hyq_rfleg_rom','hyq_rhleg_rom']
    urdfSuffix = ""
    srdfSuffix = ""

    ref_EE_lLeg = [0.3735, 0.207 , -0.57697]
    ref_EE_rLeg = [0.3735, -0.207 , -0.57697]
    ref_EE_lArm = [-0.3735, 0.207 , -0.57697]
    ref_EE_rArm = [-0.3735, -0.207 , -0.57697]

    def __init__ (self, name = None, load = True):
        Parent.__init__ (self,load)
        if load:
            self.loadModel(self.urdfName, self.urdfNameRom, self.rootJointType, self.meshPackageName, self.packageName, self.urdfSuffix, self.srdfSuffix)
        if name != None:
            self.name = name
        self.setReferenceEndEffector('hyq_lfleg_rom',self.ref_EE_lLeg)
        self.setReferenceEndEffector('hyq_rfleg_rom',self.ref_EE_rLeg)
        self.setReferenceEndEffector('hyq_lhleg_rom',self.ref_EE_lArm)
        self.setReferenceEndEffector('hyq_rhleg_rom',self.ref_EE_rArm)
