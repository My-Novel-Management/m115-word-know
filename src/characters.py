# -*- coding: utf-8 -*-
"""Design: characters
"""
import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append('storybuilder')
from storybuilder.builder.world import World
from storybuilder.builder.writer import Writer


## defines
W = Writer


## characters
def set_charas(w: World):
    ito = W(w.ito)
    hatsu = W(w.hatsumi)
    keizo, chiyo = W(w.keizo), W(w.chiyo)
    taka = W(w.takahashi)
    hair, face = W(w.hair), W(w.face)
    sailor, tie = W(w.sailorsuit), W(w.tie)
    glasses, contact = W(w.glasses), W(w.contactlens)
    boy, girl = W(w.student_boy), W(w.student_girl)
    return (
            w.block("ito_face",
                ito.have(w.hair),
                ito.have(w.contactlens),
                hair.look("襟足が肩にかかるくらいの長さ"),
                ),
            w.block("ito_school",
                ito.be(),
                ito.have(w.sailorsuit, w.tie),
                ),
            w.block("ito_room",
                ito.have(w.sweat),
                ito.have(w.glasses),
                ito.look("髪はヘアバンドで全部まとめて"),
                ),
            w.block("ito_private1",
                ito.be(),
                ito.have(w.sweater, w.jersey),
                ),
            w.block("ito_private2",
                ito.be(),
                ito.have(w.sweater, w.skirt, w.downjacket),
                ),
            w.block("keizo",
                keizo.be(),
                keizo.have(w.jersey),
                ),
            w.block("chiyo",
                chiyo.be(),
                chiyo.have(w.shirt, w.pants),
                ),
            w.block("hatsumi",
                hatsu.have(w.shirt, w.skirt),
                ),
            w.block("students",
                boy.be(15),
                girl.be(15),
                ),
            w.block("teacher",
                taka.be(),
                taka.have(w.suit, w.necktie),
                taka.look("寝癖っぽい髪"),
                ),
            )

