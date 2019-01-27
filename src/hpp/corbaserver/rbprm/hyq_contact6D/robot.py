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
    urdfSuffix = "_contact6D"
    srdfSuffix = ""

    ## Information about the names of thes joints defining the limbs of the robot
    rLegId = 'rfleg'
    rleg = 'rf_haa_joint'
    rfoot = 'rf_foot_Z'
    lLegId = 'lhleg'
    lleg = 'lh_haa_joint'
    lfoot = 'lh_foot_Z'
    rArmId = 'rhleg'
    rarm = 'rh_haa_joint'
    rhand = 'rh_foot_Z'
    lArmId = 'lfleg'
    larm = 'lf_haa_joint'
    lhand = 'lf_foot_Z'

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
       0, 0, 0,
     0.11147422537786231,
     -0.15843632504615043,
     1.150049183494211,
        0, 0, 0,
     -0.1704998924604114,
     0.6859376445755911,
     -1.1831277202117043,
    0, 0, 0,
     0.06262698472369518,
     -0.42708925470675,
     1.2855999319965081,
     0, 0, 0,]
    
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
    dict_limb_joint = {rLegId:rfoot, lLegId:lfoot, rArmId:rhand, lArmId:lhand}
    dict_limb_color_traj = {rfoot:[0,1,0,1], lfoot:[1,0,0,1],rhand:[0,0,1,1],lhand:[0.9,0.5,0,1]}
    FOOT_SAFETY_SIZE = 0.01
    # size of the contact surface (x,y)
    dict_size={rfoot:[0.02 , 0.02], lfoot:[0.02 , 0.02],rhand:[0.02 , 0.02],lhand:[0.02 , 0.02]}

    #various offset used by scripts
    MRsole_offset = SE3.Identity()
    MRsole_offset.translation = np.matrix(offset).T
    MLsole_offset = MRsole_offset.copy()
    MRhand_offset = MRsole_offset.copy()
    MLhand_offset = MRsole_offset.copy()
    dict_offset = {rfoot:MRsole_offset, lfoot:MLsole_offset, rhand:MRhand_offset, lhand:MLhand_offset}

    # display transform :
    MRsole_display = SE3.Identity()
    MLsole_display = SE3.Identity()
    MRhand_display = SE3.Identity()
    MLhand_display = SE3.Identity()
    dict_display_offset = {rfoot:MRsole_display, lfoot:MLsole_display, rhand:MRhand_display, lhand:MLhand_display}

    def __init__ (self, name = None,load = True):
        Parent.__init__ (self,load)
        if load:
            self.loadFullBodyModel(self.urdfName, self.rootJointType, self.meshPackageName, self.packageName, self.urdfSuffix, self.srdfSuffix)
        if name != None:
            self.name = name
