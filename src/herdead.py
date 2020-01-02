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
def sc_days(w: World):
    ito, asa = W(w.ito), W(w.asa)
    taka = W(w.takahashi)
    desk, blackboard = W(w.desk), W(w.blackboard)
    return w.scene("忙しい日々",
            w.comment("試験や受験のことで忙しい日々"),
            desk.be(), blackboard.be(),
            ito.be(),
            taka.be(),
            taka.do("しゃべりながら板書"),
            ito.do("黒板の文字を写している"),
            ito.do("スマホにＬＩＮＥが入っていたことに気づく"),
            ito.talk("何なんだろ"),
            ito.think("そこの謎の言葉の意味を考えていた"),
            ito.do("試験勉強に集中する"),
            camera=w.ito,
            stage=w.on_highschool,
            day=w.in_parted, time=w.at_afternoon,
            )

def sc_news(w: World):
    ito, asa = W(w.ito), W(w.asa)
    keizo, chiyo = W(w.keizo), W(w.chiyo)
    ana = W(w.announcer)
    table = W(w.table)
    tv = W(w.tv)
    return w.scene("彼女の死",
            w.comment("ニュースで流れてきた同姓同名"),
            table.be(), tv.be(),
            ito.be("席について"),
            keizo.be(), chiyo.be(),
            ito.talk("おかわり"),
            keizo.talk("そんな食う奴だったか？"),
            ito.talk("試験終わるまで我慢してたのよ"),
            table.look("唐揚げや天ぷらの惣菜"),
            ito.do("満足そうに食べる", "好物ばかり"),
            tv.look("ニュースが流れて"),
            ana.talk("本日未明に埼玉県内の高校生が転落死しました。自殺とみられ"),
            ana.talk("亡くなったのは高校二年の$full_asaさんで"),
            ito.talk("え？"),
            stage=w.on_dining,
            day=w.in_news, time=w.at_evening,
            )

def sc_checksrc(w: World):
    ito, asa = W(w.ito), W(w.asa)
    hatsu = W(w.hatsumi)
    phone = W(w.phone)
    return w.scene("確認",
            w.comment("いくら確かめてもそこに彼女の遺言も何もなかった"),
            ito.be("慌てて連絡を取ろうとしている"),
            ito.have(w.phone),
            phone.look("返事がないLINE"),
            ito.talk("嘘だ"),
            ito.talk("どっか出かけてるだけだ。そうだ"),
            ito.explain("じっと待ったけれど返信がなかった"),
            ito.do("初めて電話してみる"),
            ito.explain("通話にならない"),
            ito.talk("もう一度"),
            hatsu.talk("はい？"),
            ito.think("大人の女性の疲れた声だ"),
            ito.talk("えっと、そちら$full_asaさんの携帯ですよね？"),
            hatsu.talk("娘はもう死にました。あなたは？"),
            ito.talk("ご、ごめんなさい"),
            ito.do("電話を切ってしまう"),
            ito.think("嘘じゃなかった"),
            ito.do("呆然と"),
            stage=w.on_myroom,
            time=w.at_night,
            )

def sc_gotoherhome(w: World):
    ito, asa = W(w.ito), W(w.asa)
    entrance = W(w.entrance)
    sky = W(w.sky)
    return w.scene("彼女の家に",
            w.comment("手紙の住所を見て、そこに向かう"),
            entrance.be(),
            ito.be("立っている"),
            ito.have(w.bag),
            ito.have(w.letter),
            ito.think("彼女が何故死んだのかを突き止めたい"),
            ito.go("力強く"),
            sky.look("雪がちらつき"),
            day=w.in_findher, time=w.at_morning,
            )

## episode
def ep_herdead(w: World):
    return w.episode("彼女の死",
            ## NOTE:
            ##  - しばらく互いに忙しかった（糸は別の付き合いを継続）
            ##  - 彼女の死を知る（ニュースで／本名は知っていた）
            ##  - 彼女は何も残さなかった
            ##  - 彼女の住所を手に入れて、そこに向かう
            sc_days(w),
            sc_news(w),
            sc_checksrc(w),
            sc_gotoherhome(w),
            )
