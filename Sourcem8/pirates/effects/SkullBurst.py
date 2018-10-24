# File: S (Python 2.4)

from pandac.PandaModules import *
from direct.showbase.DirectObject import *
from direct.interval.IntervalGlobal import *
from PooledEffect import PooledEffect
from EffectController import EffectController

class SkullBurst(PooledEffect, EffectController):

    def __init__(self):
        PooledEffect.__init__(self)
        EffectController.__init__(self)
        self.fadeTime = 1.5
        self.startDelay = 0.0
        self.effectScale = 1.0
        self.effectColor = Vec4(1, 1, 1, 1)
        model = loader.loadModel('models/effects/fireworkCards')
        self.effectModel = model.find('**/pir_t_efx_msc_skull')
        self.effectModel.reparentTo(self)
        self.effectModel.setColorScale(0, 0, 0, 0)
        self.setAttrib(ColorBlendAttrib.make(ColorBlendAttrib.MAdd, ColorBlendAttrib.OIncomingAlpha, ColorBlendAttrib.OOne))
        self.setBillboardPointWorld()
        self.setDepthWrite(0)
        self.setLightOff()
        self.setFogOff()


    def createTrack(self):
        self.effectModel.setColorScale(0, 0, 0, 0)
        self.effectModel.setScale(700 * self.effectScale)
        fadeIn = self.effectModel.colorScaleInterval(0.20000000000000001, Vec4(self.effectColor), startColorScale = Vec4(0, 0, 0, 0), blendType = 'easeIn')
        fadeBlast = self.effectModel.colorScaleInterval(self.fadeTime, Vec4(0, 0, 0, 0), startColorScale = Vec4(self.effectColor), blendType = 'easeIn')
        scaleBlast = self.effectModel.scaleInterval(self.fadeTime, 850 * self.effectScale, startScale = 750 * self.effectScale, blendType = 'easeOut')
        self.track = Sequence(Wait(self.startDelay), fadeIn, Parallel(fadeBlast, scaleBlast), Func(self.cleanUpEffect))


    def setEffectColor(self, color):
        self.effectColor = color


    def setEffectScale(self, scale):
        self.effectScale = scale


    def cleanUpEffect(self):
        EffectController.cleanUpEffect(self)
        self.checkInEffect(self)


    def destroy(self):
        EffectController.destroy(self)
        PooledEffect.destroy(self)
