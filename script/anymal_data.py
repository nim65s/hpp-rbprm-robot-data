from __future__ import print_function
from hpp.corbaserver.rbprm.rbprmfullbody import FullBody
from hpp.corbaserver.rbprm.tools.plot_analytics  import plotOctreeValues

packageName = "anymal_bedi_description"
meshPackageName = "anymal_bedi_description"
rootJointType = "freeflyer"

#  Information to retrieve urdf and srdf files.
urdfName = "anymal_bedi"
urdfSuffix = ""
srdfSuffix = ""

fullBody = FullBody ()
fullBody.loadFullBodyModel(urdfName, rootJointType, meshPackageName, packageName, urdfSuffix, srdfSuffix)
fullBody.setJointBounds ("root_joint", [0,0,0,0,0,0])

nbSamples = 50000 #used to be 20000 

cType = "_3_DOF"
rLegId = 'rfleg'
rLeg = 'RF_HAA'
rfoot = 'RF_MOUNT_TO_FOOT'
offset = [0.,-0.034625,0.] #originally [0.,-0.031,0.]
normal = [0,1,0] #hyq needs [0,1,0], also for anymal
legx = 0.03; legy = 0.03

def addLimbDb(limbId, heuristicName, loadValues = True, disableEffectorCollision = False):
	fullBody.addLimbDatabase(str(db_dir+limbId+'.db'), limbId, heuristicName,loadValues, disableEffectorCollision)


#fullBody.addLimb(rLegId,rLeg,rfoot,offset,normal, legx, legy, nbSamples, "forward", 0.1, cType)
fullBody.addLimb(rLegId,rLeg,rfoot,offset,normal, legx, legy, nbSamples, "manipulability", 0.1, cType)

lLegId = 'lhleg'
lLeg = 'LH_HAA'
lfoot = 'LH_MOUNT_TO_FOOT'
fullBody.addLimb(lLegId,lLeg,lfoot,offset,normal, legx, legy, nbSamples, "manipulability", 0.1, cType)
#~ 
rarmId = 'rhleg'
rarm = 'RH_HAA'
rHand = 'RH_MOUNT_TO_FOOT'
fullBody.addLimb(rarmId,rarm,rHand,offset,normal, legx, legy, nbSamples, "manipulability", 0.1, cType)

larmId = 'lfleg'
larm = 'LF_HAA'
lHand = 'LF_MOUNT_TO_FOOT'
#fullBody.addLimb(larmId,larm,lHand,offset,normal, legx, legy, nbSamples, "forward", 0.1, cType)
fullBody.addLimb(larmId,larm,lHand,offset,normal, legx, legy, nbSamples, "manipulability", 0.1, cType)

q_0 = fullBody.getCurrentConfig(); 
q_init = [-2.5, 0.0, 0.38418442387922846, 0.0, 0.0, 0.0, 1.0,  0.28621482125006287, 0.389380188410535, -1.0701831582488357, 0.18103701803493258, -0.3633371504537386, 1.1405892092366712, -0.32541312483462415, 0.47768600410524753, -1.0819534508855166, -0.29647189017581244, -0.23659478921159968, 0.9527203353688805]

fullBody.setCurrentConfig (q_init)

def runall(lid, dbName):
	fullBody.runLimbSampleAnalysis(lid, "ReferenceConfiguration", False)
	fullBody.runLimbSampleAnalysis(lid, "minimumSingularValue", False)
	#~ fullBody.runLimbSampleAnalysis(lid, "selfCollisionProbability", False)
	#~ fullBody.runLimbSampleAnalysis(lid, "jointLimitsDistance", False)
	fullBody.runLimbSampleAnalysis(lid, "manipulability", True)
	fullBody.saveLimbDatabase(lid, dbName)

#~ runall(rarmId, './hrp2_rarm.db')
#~ runall(larmId, './hrp2_larm.db')
runall(lLegId, './anymal_'+lLegId+'.db')
print("ok")
runall(rarmId, './anymal_'+rarmId+'.db')
runall(larmId, './anymal_'+larmId+'.db')
runall(rLegId, './anymal_'+rLegId+'.db')
#~ plotOctreeValues(fullBody, "selfCollisionProbability", rarmId)

