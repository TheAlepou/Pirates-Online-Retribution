# STUB
# NO BASE CLASS WAS FOUND!
# IT MEANS THAT THIS FILE HAD NO DEF
# IN PIRATES.DC WHEN AI-GEN WAS RUN!

from direct.directnotify import DirectNotifyGlobal
from direct.distributed.DistributedObjectAI import DistributedObjectAI

class DistributedBlackPearlSimpleShipAI(DistributedObjectAI):
    notify = DirectNotifyGlobal.directNotify.newCategory('DistributedBlackPearlSimpleShipAI')

    def __init__(self, air):
        DistributedObjectAI.__init__(self, air)


