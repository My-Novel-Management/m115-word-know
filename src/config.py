# -*- coding: utf-8 -*-
"""Story config.
"""
################################################################
#
# Sample:
#
# 1) PERSONS
#       人物簡易設定
# 2) STAGES
#       舞台基本設定
# 3) DAYS
#       年月日設定
# 4) TIMES
#       時間帯基本設定
# 5) ITEMS
#       小道具設定
# 6) WORDS
#       辞書設定
# 7) RUBIS
#       ルビ設定
# 8) LAYERS
#       レイヤ設定
#
################################################################


PERSONS = (
        # Tag / 氏,名 / 歳 / 性別 / 職業 / 呼称 / 紹介
        ("ito", "糸", "", 17, "female", "高校生", "me:私"),
        ("asa", "麻美", "", 17, "female", "高校生", "me:ワタシ"),
        ("chiyo", "千代", "", 40, "female", "介護職", "me:わたし"),
        ("keizo", "恵三", "", 20, "male", "大学生", "me:俺"),
        ("hatsumi", "初美", "", 38, "female", "看護師", "me:私"),
        ("takahashi", "高橋", "", 49, "male", "数学教師", "me:僕"),
        ("announcer", "アナウンサー", "", 30, "male", "アナウンサー", "me:私"),
        )

STAGES = (
        # Tag / 名前 / 紹介
        ("rentalbox", "トランクルーム"),
        ("myroom", "糸の部屋"),
        ("myhome", "糸の家", "マンション三階"),
        ("herhome", "彼女の家"),
        ("herroom", "彼女の部屋"),
        )

DAYS = (
        # Tag / 名前 / 月 / 日 / 年
        ("parted", "連絡を取らなかった", 1,14, 2020),
        ("term3test", "三学期期末試験", 1,27, 2020),
        ("news", "彼女の死のニュース", 2,1, 2020),
        ("findher", "彼女の残骸を発見した", 2,2, 2020),
        )

TIMES = (
        # Tag / 名前 / 時 / 分
        )

ITEMS = (
        # Tag / 名前 / 紹介
        ("letter", "彼女の手紙"),
        ("table", "テーブル"),
        ("tv", "ＴＶ"),
        ("bag", "鞄"),
        ("sky", "空"),
        ("desk", "机"),
        ("blackboard", "黒板"),
        ("contract", "契約書"),
        ("floor", "床"),
        ("wall","壁"),
        ("door", "扉"),
        ("entrance", "玄関"),
        ("interior", "内装"),
        ("exterior", "外装"),
        ("seat", "シート"),
        ("bed", "ベッド"),
        ("bookshelf", "本棚"),
        ("book", "本"),
        ("greentea", "お茶"),
        ("maru_table", "丸テーブル"),
        ("phone", "スマートフォン"),
        )

WORDS = (
        # Tag / 名前 / 紹介
        )

RUBIS = (
        # Base / Rubi / Type
        )

LAYERS = (
        )

