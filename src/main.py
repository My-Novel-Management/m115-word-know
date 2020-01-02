# -*- coding: utf-8 -*-
"""Main story.
"""
import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append('storybuilder')
from storybuilder.builder.world import World
from storybuilder.assets import basic
from config import DAYS, ITEMS, LAYERS, PERSONS, RUBIS, STAGES, TIMES, WORDS
from src.demo.main import ep_demo
from src.herdead import ep_herdead
from src.herhome import ep_herhome
from src.truth import ep_truth


## defines
TITLE = "言葉の結び目"


## main
def ch_main(w: World):
    return w.chapter("main",
            ep_demo(w).omit(),
            ## NOTE
            ##      - SNSの親友
            ##      - 彼女が死んだ
            ##      - 彼女の実家に行く
            ##      - 彼女の本音を見つけ、もうひとりの自分だったと知る
            ep_herdead(w),
            ep_herhome(w),
            ep_truth(w),
            )

def world():
    """Create a world.
    """
    w = World(TITLE)
    w.setCommonData()
    w.setAssets(basic.ASSET)
    w.buildDB(PERSONS,
            STAGES, ITEMS, DAYS, TIMES, WORDS,
            RUBIS, LAYERS)
    w.entryBlock(
            )
    return w


def main(): # pragma: no cover
    w = world()
    return w.build(
            ch_main(w),
            )


if __name__ == '__main__':
    import sys
    sys.exit(main())

