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

from hpp.corbaserver.rbprm.rbprmfullbody import FullBody as Parent
from pinocchio import SE3, Quaternion
import numpy as np

class Robot (Parent):
    ##
    #  Information to retrieve urdf and srdf files.

    packageName = "hyq_description"
    meshPackageName = "hyq_description"
    rootJointType = "freeflyer"
    urdfName = "hyq"
    urdfSuffix = ""
    srdfSuffix = ""

    ## Information about the names of thes joints defining the limbs of the robot
    rLegId = 'rfleg'
    rleg = 'rf_haa_joint'
    rfoot = 'rf_foot_joint'
    lLegId = 'lhleg'
    lleg = 'lh_haa_joint'
    lfoot = 'lh_foot_joint'
    rArmId = 'rhleg'
    rarm = 'rh_haa_joint'
    rHand = 'rh_foot_joint'
    lArmId = 'lfleg'
    larm = 'lf_haa_joint'
    lHand = 'lf_foot_joint'

    referenceConfig = [0.,
 0.,
 0.6638277139631803,
 0.,
 0.,
 0.,
 1.,
 0.17905666752078864,
 0.9253512562075908,
 -0.8776870832724601,
 0.11147422537786231,
 -0.15843632504615043,
 1.150049183494211,
 -0.1704998924604114,
 0.6859376445755911,
 -1.1831277202117043,
 0.06262698472369518,
 -0.42708925470675,
 1.2855999319965081]
    
    # informations required to generate the limbs databases the limbs : 

    offset = [0.,0.,-0.021]
    normal = [0,0,1]
    legx = 0.02; legy = 0.02
    kinematicConstraintsPath="package://hyq-rbprm/com_inequalities/"
    rLegKinematicConstraints=kinematicConstraintsPath+rleg+"_com_constraints.obj"
    lLegKinematicConstraints=kinematicConstraintsPath+lleg+"_com_constraints.obj" 
    rArmKinematicConstraints=kinematicConstraintsPath+rarm+"_com_constraints.obj" 
    lArmKinematicConstraints=kinematicConstraintsPath+larm+"_com_constraints.obj"

    # data used by scripts :
    limbs_names = [rLegId,lLegId,rArmId,lArmId]
    #various offset used by scripts
    MRsole_offset = SE3.Identity()
    rot = np.matrix([[0.,0,1],[0.,1.,0.],[-1.,0.,0.]])
    MRsole_offset.rotation = rot
    MLsole_offset = SE3.Identity()
    rot = np.matrix([[0.,0,1],[0.,1.,0.],[-1.,0.,0.]])
    MLsole_offset.rotation = rot
    MRhand_offset = SE3.Identity()
    rot = np.matrix([[0.,0,1],[0.,1.,0.],[-1.,0.,0.]])
    MRhand_offset.rotation = rot
    MLhand_offset = SE3.Identity()
    rot = np.matrix([[0.,0,1],[0.,1.,0.],[-1.,0.,0.]])
    MLhand_offset.rotation = rot

    # display transform :

    MRsole_display = SE3.Identity()
    MLsole_display = SE3.Identity()
    MRhand_display = SE3.Identity()
    MLhand_display = SE3.Identity()


    def __init__ (self, name = None,load = True):
        Parent.__init__ (self,load)
        if load:
            self.loadFullBodyModel(self.urdfName, self.rootJointType, self.meshPackageName, self.packageName, self.urdfSuffix, self.srdfSuffix)
        if name != None:
            self.name = name
