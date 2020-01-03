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
def sc_alonelife(w: World):
    ito, asa = W(w.ito), W(w.asa)
    taka = W(w.takahashi)
    board, desk = W(w.blackboard), W(w.desk)
    return w.scene("つまらない学生生活",
            w.comment("糸にとって学校はただ義務の為に通うだけの場所"),
            w.load("in_classroom"),
            ito.be("勉強している"),
            taka.be("板書中"),
            taka.talk("えー、お前ら来年は受験生だから、今のうちからしっかりとやっておくように"),
            ito.do("前から回ってきたプリントを後ろに"),
            ito.think("つまらない"),
            ito.hear("チャイム"),
            taka.go(),
            ito.hear("生徒の声でざわつく"),
            ito.do("一人でこっそりスマホを触っている"),
            camera=w.ito,
            stage=w.on_highschool,
            day=w.in_everyday, time=w.at_afternoon,
            )

def sc_myfriend(w: World):
    ito, asa = W(w.ito), W(w.asa)
    bed = W(w.bed)
    phone = W(w.phone)
    return w.scene("親友",
            w.comment("SNSの親友と話せる家が一番幸せだった"),
            w.load("in_myroom"),
            ito.be("寝転がり"),
            ito.have(w.phone),
            ito.talk("えー、そんなことないよ"),
            phone.look("画面にはLINEのやり取り"),
            phone.look("相手は$asa"),
            asa.voice("今季のアニメはさ"),
            ito.explain("いつも自分たちの好きな話で盛り上がる"),
            ito.think("$asaさえいればいい"),
            ito.think("クラスのグループLINEを思い出して"),
            ito.talk("あんなやつら、いらないし"),
            stage=w.on_myroom,
            time=w.at_night,
            )

def sc_herletter(w: World):
    ito, asa = W(w.ito), W(w.asa)
    chiyo = W(w.chiyo)
    return w.scene("彼女の手紙",
            w.comment("彼女から手紙をもらって、綺麗な字にどんな子だろうと",
                "いつか会おうと書いてあった"),
            w.load("myliving"),
            ito.be(),
            chiyo.come("手紙を持って"),
            chiyo.talk("これ、あんたに"),
            ito.talk("誰？"),
            chiyo.talk("$full_asaって子"),
            ito.think("本当にきた！"),
            ito.do("手紙を受け取る"),
            ito.go(),
            stage=w.on_living,
            day=w.in_herletter
            )

def sc_herwish(w: World):
    ito, asa = W(w.ito), W(w.asa)
    letter = W(w.letter)
    return w.scene("手紙の中身",
            w.load("in_myroom"),
            ito.come(),
            ito.have(w.letter),
            ito.do("手紙を読む"),
            letter.look("綺麗で線の細い字で書かれて"),
            asa.voice("はじめまして$full_itoさん、というのも変かな"),
            asa.voice("来年は一度くらい実際に会いたいね"),
            ito.talk("$meも"),
            ito.do("手紙を抱き締める"),
            stage=w.on_myroom,
            )

## episode
def ep_myfriend(w: World):
    return w.episode("友達",
            ## NOTE:
            ##  - 学校では適当な付き合い、でも友達はいない
            ##  - でもSNSでは親友がいる
            ##  - 好きな趣味（アニメとか）を共有し、彼女だけいればいいと思える
            ##  - 手紙も交換したりしている
            ##  - それだけで充分だと思っていた
            sc_alonelife(w),
            sc_myfriend(w),
            sc_herletter(w),
            sc_herwish(w),
            )
