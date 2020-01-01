# -*- coding: utf-8 -*-
"""Episode:
"""
import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append('storybuilder')
from storybuilder.builder.world import World
from storybuilder.builder.writer import Writer


## defines
W = Writer
_ = W.getWho()


## scenes

## episode
def ep_(w: World):
    return w.episode("EP",
            )
