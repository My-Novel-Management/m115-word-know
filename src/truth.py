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
def sc_trunkroom(w: World):
    ito,asa = W(w.ito), W(w.asa)
    building = W(w.building)
    return w.scene("トランクルーム",
            w.comment("$asaの契約していたトランクルームにやってくる"),
            w.load("out_trunkroom"),
            w.load("ito_private2"),
            ito.come(),
            ito.do("ビルを見上げて"),
            ito.talk("ここなの？"),
            ito.go("入っていく"),
            camera=w.ito,
            stage=w.on_rentalbox,
            day=w.in_findher, time=w.at_afternoon,
            )

def sc_herbox(w: World):
    ito,asa = W(w.ito), W(w.asa)
    wall, door = W(w.wall), W(w.door)
    return w.scene("彼女の箱",
            w.comment("寒々としたものを感じさせる", "彼女の心との距離感を"),
            w.load("in_trunkroom"),
            w.load("ito_private2"),
            ito.be(),
            ito.explain("フロアの外観の説明"),
            ito.do("簡素なコンテナが並ぶのを見て", "寒々とする"),
            door.look("金属製の冷たい扉", "窓もなく"),
            ito.talk("何を、ここに？"),
            ito.do("鍵を開けて中に"),
            )

def sc_wordknot(w: World):
    ito,asa = W(w.ito), W(w.asa)
    letter, book, shelf = W(w.letter), W(w.book), W(w.bookshelf)
    return w.scene("言葉の結び目",
            w.comment("$itoは彼女の本音を探した"),
            w.load("trunkroom"),
            w.load("ito_private2"),
            ito.come(),
            ito.think("こんな場所で何を？"),
            ito.do("見つける"),
            ito.think("その違和感は確信に変わった"),
            ito.think("ここが、彼女のほんとの居場所だったんだ"),
            ito.do("彼女の書きなぐりを見つける"),
            letter.be(),
            letter.look("乱雑で荒々しい文字で", "孤独や死にたい願望など書かれている"),
            ito.do("読む"),
            asa.voice("○月×日、$Sと出会った"),
            asa.voice("この子なら共有してくれると思った"),
            asa.voice("でも現実は違った。何も分かってくれない"),
            asa.voice("こっちの心まで踏み込んでこない。だからいつも苦笑い"),
            ito.talk("そんなつもりじゃ"),
            ito.think("いつも自分が笑顔マークや顔文字で誤魔化していたことに気づき"),
            ito.talk("$meは……"),
            asa.voice("ほんとは$me以外にもいっぱいその程度の付き合いのやつがいるって知ってた"),
            asa.voice("漫画やアニメや声優の話も好きだけど、でも大学とか進路とか、人生とか、そんなことに向き合いたかった"),
            asa.voice("親友になりたかった"),
            ito.look("はっとした顔"),
            ito.talk("ごめんね。分かってあげられなくて。自分のことばかりで、ごめん"),
            ito.do("彼女の本音を抱き締めた"),
            camera=w.ito,
            stage=w.on_rentalbox,
            day=w.in_findher, time=w.at_evening,
            )

## episode
def ep_truth(w: World):
    return w.episode("彼女の本音",
            ## NOTE:
            ##  - 彼女の本音を知る
            ##  - 彼女とすれ違っていた
            ##  - 自分の言葉と彼女の言葉の間に「ホンネ」があったと気づいた
            ##  - 言葉の結び目を解く
            ##  - 彼女の本音を抱き締める
            sc_trunkroom(w),
            sc_herbox(w),
            sc_wordknot(w),
            )
