# -*- coding: utf-8 -*-
"""Demo: story
"""
import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../..'))
sys.path.append('storybuilder')
from storybuilder.builder.world import World
from storybuilder.builder.writer import Writer


## defines
W = Writer
_ = W.getWho()


## scenes
def sc_ourmistake(w: World):
    ito, asa = W(w.ito), W(w.asa)
    letter = W(w.letter)
    return w.scene("私たちの失敗", w.comment("SNSに本音を吐き出せず、都合の良い自分たちを見せあっていただけだった"),
            ito.be(),
            ito.do("ちらかっているゴミを解いていく"),
            ito.do("手紙を読む"),
            asa.explain("自分の本音を書き綴ったもの"),
            letter.be(),
            letter.look("乱雑な字で書き綴られたもの"),
            ito.think("$meは何も分かってなかった"),
            asa.think("ずっと死ぬ相手を探していた"),
            asa.think("でもあの日、$itoはそれを断った",
                "同じ気持ちじゃなかったと分かった"),
            ito.do("言葉の結び目を見つける", "すれ違っていたやり取り"),
            _.talk("嘘だ。こんなの、違う"),
            _.think("全てを否定したかった。けどもう戻らない"),
            _.do("泣いた"),
            camera=w.ito,
            stage=w.on_rentalbox,
            day=w.in_findher, time=w.at_evening,
            )


## episode
def ep_demo(w: World):
    return w.episode("Demo", "SNSで仲良くなったと思いこんでいた相手は、本音を全然言ってなかったと知る",
            sc_ourmistake(w),
            )
