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


class Robot(Parent):
    ##
    #  Information to retrieve urdf and srdf files.
    rootJointType = 'freeflyer'
    packageName = 'simpleHumanoid-rbprm'
    meshPackageName = 'simpleHumanoid-rbprm'
    urdfName = 'simpleHumanoid_trunk'
    urdfNameRom = ['simpleHumanoid_lleg_rom', 'simpleHumanoid_rleg_rom']
    urdfSuffix = ""
    srdfSuffix = ""

    # reference position of the end effector position for each ROM
    # TODO
    ref_EE_lLeg = [0, 0.1, -1.]
    ref_EE_rLeg = [0, -0.1, -1.]

    def __init__(self, name=None, load=True):
        Parent.__init__(self, load)
        if load:
            self.loadModel(self.urdfName, self.urdfNameRom, self.rootJointType, self.meshPackageName, self.packageName,
                           self.urdfSuffix, self.srdfSuffix)
        if name != None:
            self.name = name
        self.setReferenceEndEffector('simpleHumanoid_lleg_rom', self.ref_EE_lLeg)
        self.setReferenceEndEffector('simpleHumanoid_rleg_rom', self.ref_EE_rLeg)
