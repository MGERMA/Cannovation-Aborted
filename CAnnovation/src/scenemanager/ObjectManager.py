from direct.showbase.DirectObject import DirectObject
from pandac.PandaModules import *

from WorldObject import WorldObject
from StaticObject import StaticObject
from StaticMeshObject import StaticMeshObject
from PointLightObject import PointLightObject
from DirectionalLightObject import DirectionalLightObject
from modCAO import *

'''
This class is a global-scoping sinlgeton and it's delegate to 
send add object requests, and sending messages to all the other components
regarding its actions.
'''
configsocket=('127.0.0.1', 80)

class ObjectManager(DirectObject):
	def __init__(self):
		self.objList = []
		self.lightList = []
		'''self.modifier = ObjectModifier(self)'''
	
	def addTerrain(self,filepath):
		print "INFO: requested adding terrain"
		print "TODO: implement loading terrain!"
	
	def addPointLight(self):
		p = PointLightObject()
		
		#adding reference to main light list
		self.lightList.append(p)
		#activating model object for light
		myCamera.getSelectionTool().appendObject(p)
	
	def addDirectionalLight(self):
		
		p = DirectionalLightObject()
		
		#adding reference to main light list
		self.lightList.append(p)
		#activating model object for light
		myCamera.getSelectionTool().appendObject(p)
	
	def addObject(self,filepath):
                envoy(configsocket, "a_") # Envoi de la donnee suffixe de commande
		envoy(configsocket, filepath) # Envoi de la premiere valable a transferer
		obj = StaticMeshObject(filepath)
		envoy(configsocket, obj) # Envoi de la seconde
	
		#setting space and hierarchy for model
		obj.getModel().setPos(base.camera,0,10,0)
		obj.getModel().wrtReparentTo(myApp.getSceneNode())
		
		#adding object to manager list
		self.objList.append(obj)
		#activating object
		myCamera.getSelectionTool().appendObject(obj)
	
	def removeSelectedObjects(self):
		if myCamera.getState() == "fly":
			return
		for obj in myCamera.st.listSelected[:]:
			self.removeObject(obj)
	
	def removeObject(self,obj):
		#removing pointers and switching gui
		myGui.noneObjSelected()
		obj.remove()
		envoy(configsocket, "e_")
		envoy(configsocket, obj)
		print("r_",obj)
		if obj.getType() == "StaticObject":
			self.objList.remove(obj)
		elif obj.getType() == "DirectionalLightObject":
			self.lightList.remove(obj)
		elif obj.getType() == "PointLightObject":
			self.lightList.remove(obj)
	
	def getObjectList(self):
		return self.objList
