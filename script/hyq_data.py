from hpp.corbaserver.rbprm.rbprmfullbody import FullBody
from hpp.corbaserver.rbprm.tools.plot_analytics  import plotOctreeValues

packageName = "hyq_description"
meshPackageName = "hyq_description"
rootJointType = "freeflyer"

#  Information to retrieve urdf and srdf files.
urdfName = "hyq"
urdfSuffix = ""
srdfSuffix = ""

#  This time we load the full body model of HyQ
fullBody = FullBody () 
fullBody.loadFullBodyModel(urdfName, rootJointType, meshPackageName, packageName, urdfSuffix, srdfSuffix)
fullBody.setJointBounds ("base_joint_xyz", [-2,5, -1, 1, 0.3, 4])

#  Setting a number of sample configurations used
nbSamples = 20000



rootName = 'base_joint_xyz'

#  Creating limbs
# cType is "_3_DOF": positional constraint, but no rotation (contacts are punctual)
cType = "_3_DOF"
# string identifying the limb
rLegId = 'rfleg'
# First joint of the limb, as in urdf file
rLeg = 'rf_haa_joint'
# Last joint of the limb, as in urdf file
rfoot = 'rf_foot_joint'
# Specifying the distance between last joint and contact surface
offset = [0.,-0.021,0.]
# Specifying the contact surface direction when the limb is in rest pose
normal = [0,1,0]
# Specifying the rectangular contact surface length
legx = 0.02; legy = 0.02
# remaining parameters are the chosen heuristic (here, manipulability), and the resolution of the octree (here, 10 cm).
fullBody.addLimb(rLegId,rLeg,rfoot,offset,normal, legx, legy, nbSamples, "manipulability", 0.05, cType)

lLegId = 'lhleg'
lLeg = 'lh_haa_joint'
lfoot = 'lh_foot_joint'
fullBody.addLimb(lLegId,lLeg,lfoot,offset,normal, legx, legy, nbSamples, "manipulability", 0.05, cType)

rarmId = 'rhleg'
rarm = 'rh_haa_joint'
rHand = 'rh_foot_joint'
fullBody.addLimb(rarmId,rarm,rHand,offset,normal, legx, legy, nbSamples, "manipulability", 0.05, cType)

larmId = 'lfleg'
larm = 'lf_haa_joint'
lHand = 'lf_foot_joint'
fullBody.addLimb(larmId,larm,lHand,offset,normal, legx, legy, nbSamples, "manipulability", 0.05, cType)


q_0 = fullBody.getCurrentConfig(); 


def runall(lid, dbName):
	fullBody.runLimbSampleAnalysis(lid, "isotropy", True)
	fullBody.runLimbSampleAnalysis(lid, "minimumSingularValue", False)
	#~ fullBody.runLimbSampleAnalysis(lid, "selfCollisionProbability", False)
	fullBody.runLimbSampleAnalysis(lid, "manipulability", False)
	fullBody.runLimbSampleAnalysis(lid, "jointLimitsDistance", True)
	fullBody.saveLimbDatabase(lid, dbName)

runall(rarmId, './hyq_rarm.db')
runall(larmId, './hyq_larm.db')
runall(lLegId, './hyq_lleg.db')
runall(rLegId, './hyq_rleg.db')
plotOctreeValues(fullBody, "minimumSingularValue", rarmId)

