from pandac.PandaModules import *
from direct.interval.IntervalGlobal import *
from direct.particles import ParticleEffect
from direct.particles import Particles
from direct.particles import ForceGroup
from EffectController import EffectController
from PooledEffect import PooledEffect
import random

class WitherStar(PooledEffect, EffectController):
    cardScale = 128.0
    
    def __init__(self):
        PooledEffect.__init__(self)
        EffectController.__init__(self)
        model = loader.loadModel('models/effects/sigils')
        self.card = model.find('**/effectSkull')
        self.setDepthWrite(0)
        self.setLightOff()
        self.effectColor = Vec4(1, 1, 1, 1)
        self.f = ParticleEffect.ParticleEffect('WitherStar')
        self.f.reparentTo(self)
        self.p0 = Particles.Particles('particles-1')
        self.p0.setFactory('ZSpinParticleFactory')
        self.p0.setRenderer('SpriteParticleRenderer')
        self.p0.setEmitter('SphereSurfaceEmitter')
        self.f.addParticles(self.p0)
        self.p0.setPoolSize(64)
        self.p0.setBirthRate(0.02)
        self.p0.setLitterSize(6)
        self.p0.setLitterSpread(0)
        self.p0.setSystemLifespan(0.0)
        self.p0.setLocalVelocityFlag(1)
        self.p0.setSystemGrowsOlderFlag(0)
        self.p0.factory.setLifespanBase(0.40000000000000002)
        self.p0.factory.setLifespanSpread(0.10000000000000001)
        self.p0.factory.setMassBase(1.0)
        self.p0.factory.setMassSpread(0.0)
        self.p0.factory.setTerminalVelocityBase(400.0)
        self.p0.factory.setTerminalVelocitySpread(0.0)
        self.p0.factory.setInitialAngle(0.0)
        self.p0.factory.setInitialAngleSpread(360.0)
        self.p0.factory.enableAngularVelocity(1)
        self.p0.factory.setAngularVelocity(0.0)
        self.p0.factory.setAngularVelocitySpread(0.0)
        self.p0.renderer.setAlphaMode(BaseParticleRenderer.PRALPHAINOUT)
        self.p0.renderer.setUserAlpha(1.0)
        self.p0.renderer.setFromNode(self.card)
        self.p0.renderer.setColor(Vec4(1.0, 1.0, 1.0, 1.0))
        self.p0.renderer.setXScaleFlag(1)
        self.p0.renderer.setYScaleFlag(1)
        self.p0.renderer.setAnimAngleFlag(1)
        self.p0.renderer.setInitialXScale(0.0001 * self.cardScale)
        self.p0.renderer.setFinalXScale(0.0025000000000000001 * self.cardScale)
        self.p0.renderer.setInitialYScale(0.00050000000000000001 * self.cardScale)
        self.p0.renderer.setFinalYScale(0.025000000000000001 * self.cardScale)
        self.p0.renderer.setNonanimatedTheta(0.0)
        self.p0.renderer.setAlphaBlendMethod(BaseParticleRenderer.PPBLENDLINEAR)
        self.p0.renderer.setAlphaDisable(0)
        self.p0.renderer.setColorBlendMode(ColorBlendAttrib.MAdd, ColorBlendAttrib.OOneMinusFbufferAlpha, ColorBlendAttrib.OOneMinusIncomingAlpha)
        self.p0.renderer.getColorInterpolationManager().addLinear(0.0, 1.0, Vec4(1.0, 1.0, 1.0, 1.0), Vec4(0.59999999999999998, 0.90000000000000002, 0.69999999999999996, 0.40000000000000002), 1)
        self.p0.emitter.setEmissionType(BaseParticleEmitter.ETRADIATE)
        self.p0.emitter.setAmplitude(1.0)
        self.p0.emitter.setAmplitudeSpread(0.0)
        self.p0.emitter.setOffsetForce(Vec3(0.0, 0.0, 0.10000000000000001))
        self.p0.emitter.setExplicitLaunchVector(Vec3(1.0, 0.0, 0.0))
        self.p0.emitter.setRadiateOrigin(Point3(0.0, 0.0, 0.0))
        self.p0.emitter.setRadius(0.01)

    
    def createTrack(self, lod = None):
        self.startEffect = Sequence(Func(self.p0.setBirthRate, 0.02), Func(self.p0.clearToInitial), Func(self.f.start, self, self), Func(self.f.reparentTo, self))
        self.endEffect = Sequence(Func(self.p0.setBirthRate, 100.0), Wait(1.5), Func(self.cleanUpEffect))
        self.track = Sequence(self.startEffect, Wait(0.5), self.endEffect)

    
    def setEffectColor(self, color):
        self.effectColor = Vec4(1, 1, 1, 1) - (Vec4(1, 1, 1, 1) - color) / 2.0
        self.p0.renderer.getColorInterpolationManager().clearToInitial()
        self.p0.renderer.getColorInterpolationManager().addLinear(0.0, 1.0, self.effectColor, Vec4(0.59999999999999998, 0.90000000000000002, 0.69999999999999996, 0.40000000000000002), 1)

    
    def changeEffectColor(self, color):
        self.effectColor = color
        self.p0.renderer.getColorInterpolationManager().clearToInitial()
        self.p0.renderer.getColorInterpolationManager().addLinear(0.0, 1.0, Vec4(0, 0, 0, 1), self.effectColor, 1)

    
    def cleanUpEffect(self):
        EffectController.cleanUpEffect(self)
        self.checkInEffect(self)

    
    def destroy(self):
        EffectController.destroy(self)
        PooledEffect.destroy(self)


