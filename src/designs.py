# -*- coding: utf-8 -*-
"""Design: stage, items and more
"""
import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append('storybuilder')
from storybuilder.builder.world import World
from storybuilder.builder.writer import Writer


## defines
W = Writer


## stages
def set_stages(w: World):
    door, wall, window, ceil = W(w.door), W(w.wall), W(w.window), W(w.ceil)
    floor = W(w.floor)
    boxroom = W(w.boxroom)
    shelf, book = W(w.bookshelf), W(w.book)
    building = W(w.building)
    road = W(w.road)
    entrance, gate = W(w.entrance), W(w.gate)
    house = W(w.house)
    table = W(w.table)
    tv = W(w.tv)
    interior = W(w.interior)
    bed, desk = W(w.bed), W(w.desk)
    seat = W(w.seat)
    man, lady = W(w.work_man), W(w.work_woman)
    sofa, chair = W(w.sofa), W(w.chair)
    blackboard = W(w.blackboard)
    return (
            w.block("in_classroom",
                blackboard.be(),
                desk.be(30),
                desk.be("先生の"),
                ),
            w.block("myliving",
                wall.be(),ceil.be(),floor.be(),
                tv.be(),shelf.be(),
                table.be(),
                sofa.be(),
                ),
            w.block("mydining",
                wall.be(),ceil.be(),floor.be(),
                table.be(),tv.be(),
                chair.be(),
                ),
            w.block("in_myroom",
                wall.be(), ceil.be(), door.be(),
                desk.be(),
                bed.be(),
                shelf.be(), book.be("参考書に漫画、同人誌も"),
                ),
            w.block("in_train",
                seat.be(30),
                interior.be(),
                man.be(10),lady.be(10),
                ),
            w.block("out_herhome",
                house.be(),
                entrance.be(), gate.be(),
                door.be(),
                house.look("一戸建て、二階"),
                entrance.look("小奇麗にされている"),
                entrance.look("小さなしめ縄が落ちている"),
                door.look("黒っぽい玄関扉"),
                ),
            w.block("herliving",
                floor.be(), wall.be(), table.be(),
                tv.be(),
                ),
            w.block("herroom",
                door.be(),wall.be(),ceil.be(),
                interior.be(),
                bed.be(), desk.be(),
                shelf.be(), book.be(10),
                door.look("木製"),
                interior.look("ほとんど何も置かれていない、質素"),
                ),
            w.block("out_trunkroom",
                building.be(), road.be(),
                building.look("十階建て"),
                ),
            w.block("in_trunkroom",
                door.be(), wall.be(), floor.be(),
                boxroom.be("沢山"),
                floor.look("リノリウムの冷たい床"),
                door.look("黄色のドア"),
                wall.look("クリーム色の塗装がされた壁"),
                boxroom.look("同じ長方形の箱が並ぶ"),
                ),
            w.block("trunkroom",
                door.be(), wall.be(), window.be(), ceil.be(),
                shelf.be(), book.be(),
                bed.be(),
                window.look("小さな窓が一つだけ"),
                window.look("カーテンもかかっていない"),
                wall.look("白い壁"),
                wall.look("冷暖房設備はない"),
                door.look("金属製の薄い扉"),
                bed.look("シーツが乱れたベッド"),
                ),
            )

## items
def set_items(w: World):
    return (
            )
