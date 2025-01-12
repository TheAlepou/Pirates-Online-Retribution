from pandac.PandaModules import *
from direct.fsm.FSM import FSM 
from direct.interval.IntervalGlobal import *
from direct.distributed.DistributedObject import DistributedObject

class Fixture(NodePath, FSM):
    def __init__(self, id, parent, pos, hpr, fov):
        NodePath.__init__(self, 'cam-%s' % id)
        FSM.__init__(self, '%s-fsm' % self.getName())
        self.id = id
        self.lens = PerspectiveLens()
        self.lens.setFov(base.camLens.getFov())
        
        model = loader.loadModel('models/misc/camera', okMissing = True)
        model.reparentTo(self)

        self.reparentTo(parent)
        self.setPos(pos)
        self.setHpr(hpr)
        self.setFov(fov)
        self.setLightOff(100)
        self.hide()

        self.scaleIval = None
        self.recordingInProgress = False
        self.dirty = False
        pass

    def __str__(self):
        return 'Fixture(%d, \'%s\', %s, %s, %s)' % (self.id, self.state, self.getPos(), self.getHpr(), self.getFov())

    def pack(self):
        return 'Camera(%s, %s, %s)' % (self.getPos(), self.getHpr(), self.getFov())

    def setId(self, id):
        self.id = id
        pass

    def setFov(self, fov):
        """
        fov should be a VBase2.  Use VBase2(0) to indicate default.
        """
        if fov != VBase2(0):
            self.lens.setFov(fov)
            pass
        self.setupFrustum()
        pass

    def adjustFov(self, x, y):
        fov = self.lens.getFov()
        self.lens.setFov(fov[0]+x, fov[1]+y)
        self.dirty = True
        pass
    
    def getFov(self):
        return self.lens.getFov()
    
    def setupFrustum(self):
        oldFrustum = self.find('frustum')
        if oldFrustum:
            oldFrustum.detachNode()
            pass
        
        self.attachNewNode(GeomNode('frustum')).node().addGeom(self.lens.makeGeometry())
        pass
        
        
    def setRecordingInProgress(self, inProgress):
        self.recordingInProgress = inProgress
        if self.recordingInProgress and \
           base.config.GetInt('camera-id', -1) >= 0:
            self.hide()
            pass
        else:
            self.show()
            pass
        pass
        
    def show(self):
        if base.config.GetBool('aware-of-cameras',0) and \
           not self.recordingInProgress:
            NodePath.show(self)
            pass
        pass

    def getScaleIval(self):
        if not self.scaleIval:
            self.scaleIval = Sequence(LerpScaleInterval(self.getChild(0), 0.25, 2, startScale = 1, blendType = 'easeInOut'),
                                      LerpScaleInterval(self.getChild(0), 0.25, 1, startScale = 2, blendType = 'easeInOut'))
            pass
        return self.scaleIval
    
    def setState(self, state):
        self.request(state)
        pass

    def defaultFilter(self, request, args):
        if request == self.getCurrentOrNextState():
            return None
        return FSM.defaultFilter(self, request, args)

    def exitOff(self):
        self.accept('recordingInProgress', self.setRecordingInProgress)
        pass

    def enterOff(self):
        self.ignore('recordingInProgress')

        if self.scaleIval:
            self.scaleIval.finish()
            self.scaleIval = None
            pass

        self.hide()
        pass
        
    def enterStandby(self):
        self.show()
        if self.id == base.config.GetInt('camera-id', -1):
            self.setColorScale(3,0,0,1)
            self.getScaleIval().loop()
        else:
            self.setColorScale(3,3,0,1)
            self.getScaleIval().finish()
            pass
        pass
    
    def enterBlinking(self):
        self.show()
        self.setColorScale(0,3,0,1)
        self.getScaleIval().loop()
        pass        

    def exitBlinking(self):
        if self.scaleIval:
            self.scaleIval.finish()
            pass
        pass

    def enterRecording(self):
        if base.config.GetInt('camera-id', -1) == self.id:
            self.demand('Using')
            pass
        else:
            self.show()
            self.setColorScale(3,0,0,1)
            self.getScaleIval().loop()
            pass
        pass

    def exitRecording(self):
        if self.scaleIval:
            self.scaleIval.finish()
            pass
        pass

    def enterUsing(self, args = []):
        localAvatar.b_setGameState('Camera')
        camera.setPosHpr(0,0,0,0,0,0)
        camera.reparentTo(self)
        self.hide()

        base.cam.node().setLens(self.lens)

        if args and args[0]:
            self.accept('arrow_left', self.adjustFov, [-0.5,0])
            self.accept('arrow_left-repeat', self.adjustFov, [-2,0])
            self.accept('arrow_right', self.adjustFov, [0.5,0])
            self.accept('arrow_right-repeat', self.adjustFov, [2,0])
            self.accept('arrow_down', self.adjustFov, [0,-0.5])
            self.accept('arrow_down-repeat', self.adjustFov, [0,-2])
            self.accept('arrow_up', self.adjustFov, [0,0.5])
            self.accept('arrow_up-repeat', self.adjustFov, [0,2])

        # Could be toggled on/off on a fixture by fixture basis
        # if added to the dc definition of the Fixture struct and
        # saved out to the Camera file.
        lodNodes = render.findAllMatches('**/+LODNode')
        for i in xrange(0,lodNodes.getNumPaths()):
            lodNodes[i].node().forceSwitch(lodNodes[i].node().getHighestSwitch())
            pass
        pass
    
    
    def exitUsing(self):
        self.ignore('arrow_left')
        self.ignore('arrow_left-repeat')
        self.ignore('arrow_right')
        self.ignore('arrow_right-repeat')
        self.ignore('arrow_down')
        self.ignore('arrow_down-repeat')
        self.ignore('arrow_up')
        self.ignore('arrow_up-repeat')

        base.cam.node().setLens(base.camLens)
        localAvatar.b_setGameState('LandRoam')
        self.show()

        if self.dirty:
            messenger.send('refresh-fixture', [self.id, self.pack()])
            self.dirty = False
            pass
        
        pass
    

class DistributedCamera(DistributedObject):
    def __init__(self, cr):
        DistributedObject.__init__(self, cr)
        self.parent = None
        self.fixtures = {}
        self.cameraId = base.config.GetInt('camera-id',0)

        pass

    def __getitem__(self, index):
        return self.fixtures.get(index)

    def __str__(self):
        out = ''
        for fixture in self.fixtures.itervalues():
            out = '%s\n%s' % (out, fixture)
        return out[1:]

    def pack(self):
        out = ''
        for fixture in self.fixtures.itervalues():
            out = '%s\n%s' % (out, fixture.pack())
        return out[1:]
            
    def disable(self):
        self.ignore('escape')
        
        self.parent = None
        
        for fixture in self.fixtures.itervalues():
            fixture.cleanup()
            fixture.detachNode()
            pass
        self.fixtures = {}
        
        DistributedObject.disable(self)

    def getOV(self):
        return self.cr.doId2ownerView.get(self.getDoId())

    def setCamParent(self, doId):
        if doId != self.parent:
            if not doId:
                self.parent = render
            else:
                self.parent = self.cr.getDo(doId)
                pass

            for fix in self.fixtures.itervalues():
                fix.reparentTo(self.parent)
                pass
            pass
        pass

    def getCamParent(self):
        return self.parent
    
    def setFixtures(self, fixtures):
        for x in xrange(len(fixtures), len(self.fixtures)):
            fixture = self.fixtures.pop(x)
            fixture.cleanup()
            fixture.detachNode()
            pass

        recordingInProgress = False
        for x,fixture in enumerate(fixtures):
            pos = Point3(*(fixture[:3]))
            hpr = Point3(*(fixture[3:6]))
            fov = VBase2(*(fixture[6:8]))
            state = fixture[8]

            if x not in self.fixtures:
                self.fixtures[x] = Fixture(x, self.parent, Point3(0), hpr = Point3(0), fov = VBase2(0))
                pass
            
            fix = self.fixtures.get(x)
            fix.setId(x)
            fix.setPosHpr(pos,hpr)
            fix.setState(state)
            fix.setFov(fov)
            recordingInProgress |= state == 'Recording'
            pass
        
        messenger.send('recordingInProgress', [recordingInProgress])

    def testFixture(self, index):
        fixture = self.fixtures.get(index)
        if fixture:
            fixture.request('Using', [True])
            self.accept('escape', self.stopTesting, [index])
            pass
        pass

    def stopTesting(self, index):
        fixture = self.fixtures.get(index)
        if fixture:
            self.ignore('escape')
            fixture.request('Standby')
            localAvatar.b_setGameState('LandRoam')
        pass
    
