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
def sc_intrain(w: World):
    ito, asa = W(w.ito), W(w.asa)
    man, lady = W(w.work_man), W(w.work_woman)
    seat = W(w.seat)
    return w.scene("電車の中で",
            w.comment("彼女の住む街に行くまでの車内で考える"),
            w.load("in_train"),
            w.load("ito_private2"),
            ito.do("乗っている"),
            ito.do("つり革に掴まって"),
            ito.explain("これから$asaの家に行く"),
            ito.think("どうして彼女は何も言わずに突然死んだのだろう"),
            ito.think("自分が何かしてあげられなかったのだろうか"),
            camera=w.ito,
            stage=w.on_train,
            day=w.in_findher, time=w.at_midmorning,
            )

def sc_herhome(w: World):
    ito, asa = W(w.ito), W(w.asa)
    hatsu = W(w.hatsumi)
    door = W(w.door)
    entrance = W(w.entrance)
    exterior = W(w.exterior)
    return w.scene("彼女の家",
            w.comment("彼女の家を見て、印象との違い、違和感"),
            w.load("out_herhome"),
            ito.come(),
            w.load("ito_private2"),
            ito.do("家を見上げる"),
            exterior.look("二階建て戸建て住宅"),
            ito.do("インタフォンを押す"),
            hatsu.talk("はい。どちら様？"),
            ito.think("どう答えよう"),
            ito.talk("$asaさんの、その、友達……親友です"),
            hatsu.come("出てきて"),
            hatsu.look("若そうなのに白髪が目立つ"),
            ito.talk("お母様ですか？　はじめまして。$full_itoです"),
            stage=w.on_herhome,
            time=w.at_afternoon,
            )

def sc_hermother(w: World):
    ito, asa = W(w.ito), W(w.asa)
    hatsu = W(w.hatsumi)
    table = W(w.maru_table)
    tea = W(w.greentea)
    return w.scene("彼女の母親",
            w.comment("彼女の母親から説明を受ける"),
            w.load("herliving"),
            w.load("ito_private2"),
            w.load("hatsumi"),
            ito.do("座っている"),
            hatsu.come("お茶を持って"),
            hatsu.talk("お茶でよかったかしら"),
            ito.talk("ほんと、お構いなく"),
            hatsu.do("お茶を出して"),
            hatsu.talk("学校のお友達なんて、いないと思ってたのに"),
            ito.talk("学校の友達じゃ、ないんです"),
            hatsu.talk("そうなの？"),
            ito.do("スマホを見せて"),
            ito.talk("この一年くらいの付き合いなんです"),
            hatsu.talk("今の子は知らない間にそういう付き合いをしてしまうのね"),
            hatsu.talk("ちょっと見ても？"),
            ito.talk("はい"),
            ito.do("見せる"),
            hatsu.have(w.phone),
            hatsu.look("眉を寄せて", "スマホのやり取りを見ている"),
            hatsu.talk("あなたには随分と心を許していたんですね"),
            hatsu.talk("どうして$asaは死んだんでしょう？"),
            ito.think("$meもそれが知りたかった"),
            hatsu.talk("何も、あの子は残していかなかった"),
            ito.talk("それは$meも同じです。だから、ここまで来たんです"),
            hatsu.talk("部屋には何もありません"),
            ito.talk("お願いします"),
            ito.do("土下座"),
            stage=w.on_living,
            )

def sc_herroom(w: World):
    ito, asa = W(w.ito), W(w.asa)
    hatsu = W(w.hatsumi)
    interior = W(w.interior)
    bed, desk = W(w.bed), W(w.desk)
    book, shelf = W(w.book), W(w.bookshelf)
    return w.scene("彼女の部屋",
            w.comment("彼女の部屋を見せてもらうが"),
            w.load("herroom"),
            w.load("ito_private2"),
            w.load("hatsumi"),
            hatsu.come(),
            hatsu.talk("本当に何もないから"),
            ito.come(),
            hatsu.talk("ね？"),
            ito.talk("少し見ても？"),
            hatsu.talk("自由にして"),
            hatsu.go(),
            ito.do("机や棚を調べる"),
            ito.think("何も置いてない部屋"),
            ito.do("自分のスマホの記録を確かめて", "不一致に違和感"),
            ito.think("ここに本当にいたの？"),
            stage=w.on_herroom,
            )

def sc_knownbox(w: World):
    ito, asa = W(w.ito), W(w.asa)
    contract = W(w.contract)
    return w.scene("トランクルーム",
            w.comment("トランクルームの契約書を見つけて"),
            ito.be("探している"),
            ito.do("$contract見つけた"),
            ito.think("何をそこに仕舞っていたのだろう"),
            )

## episode
def ep_herhome(w: World):
    return w.episode("彼女の居場所",
            ## NOTE:
            ##  - 彼女の家にやってくる
            ##  - 母親から彼女の話を聞く
            ##  - 彼女の部屋で、ギャップに気づく
            ##  - 彼女の契約していたトランクルームがあると知る
            sc_intrain(w),
            sc_herhome(w),
            sc_hermother(w),
            sc_herroom(w),
            sc_knownbox(w),
            )
