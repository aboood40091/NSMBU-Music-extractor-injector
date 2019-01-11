#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# NSMBU DX Music extractor/injector
# Version 0.1
# Copyright © 2019 AboodXD

# This file is part of NSMBU DX Music extractor/injector.

# NSMBU DX Music extractor/injector is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# NSMBU DX Music extractor/injector is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

import os
import struct
import sys

nums = {
    0: "WSD_BGM_SELECT_W8",
    1: "WSD_BGM_SELECT_W9",
    2: "WSD_BGM_MAP_DEMO_W8",
    3: "STRM_BGM_SWITCH",
    4: "STRM_BGM_MULTI_RESULT",
    5: "STRM_BGM_SHORT_RESULT",
    6: "WSD_BGM_STAR_DRC",
    7: "WSD_BGM_COIN_EDIT",
    8: "STRM_BGM_COURSE_CLEAR",
    9: "STRM_BGM_ALL_CMPLT_5STARS",
    10: "STRM_BGM_STORY_CREAR",
    11: "STRM_BGM_COURSE_OUT_ALL_BUBBLE",
    12: "WSD_BGM_BGM_LAST_BOSS_FANFARE_LR_RY_32",
    13: "STRM_BGM_LAST_CASTLE_APPEAR",
    14: "STRM_BGM_MINIGAME_FANFARE_BAD",
    15: "STRM_BGM_MINIGAME_FANFARE_GOOD",
    16: "STRM_BGM_STAR_COIN_CMPLT_ALL",
    17: "STRM_BGM_STAR_COIN_CMPLT_WORLD",
    18: "WSD_BGM_CHEEPFANFARE_LR_RY_32",
    19: "STRM_BGM_COURSE_CLEAR_ZORO",
    20: "__STRM_BGM_MULTI_FAIL",
    21: "STRM_BGM_GAMEOVER",
    22: "STRM_BGM_MULTI_FAIL",
    23: "STRM_BGM_DOWN",
    24: "STRM_BGM_SHADOW_START",
    25: "STRM_BGM_SHADOW_CATCH",
    26: "STRM_BGM_COIN_WIN",
    27: "STRM_BGM_ODAI_CLEAR",
    28: "WSD_BGM_SPEED_UP",
    29: "WSD_BGM_SPEED_UP_MAX",
    30: "WSD_BGM_ODAI_MEDAL_CMP",
    31: "WSD_BGM_ODAI_MEDALCMP_GOLD",
    32: "STRM_BGM_TITLE",
    33: "STRM_BGM_DEMO_OP",
    34: "STRM_BGM_DEMO_OP2",
    35: "STRM_BGM_DEMO_ED",
    36: "STRM_BGM_DEMO_ED2",
    37: "STRM_BGM_HIKOUSEN",
    38: "STRM_BGM_HIKOUSEN_FAST",
    39: "STRM_BGM_LAST_BOSS",
    40: "STRM_BGM_LAST_BOSS_FAST",
    41: "STRM_BGM_LAST_BOSS_CLEAR",
    42: "STRM_BGM_LAST_BOSS2",
    43: "STRM_BGM_LAST_BOSS2_FAST",
    44: "STRM_BGM_LAST_BOSS2_CLEAR",
    45: "STRM_BGM_LAST_BOSS2_HARP",
    46: "STRM_BGM_MG_BTL",
    47: "STRM_BGM_MG_BTL_END",
    48: "STRM_BGM_SHIRO_BOSS",
    49: "STRM_BGM_SHIRO_BOSS_FAST",
    50: "STRM_BGM_SHIRO_BOSS_CLEAR",
    51: "STRM_BGM_TORIDE_BOSS",
    52: "STRM_BGM_TORIDE_BOSS_FAST",
    53: "STRM_BGM_TORIDEBOSS_CREAR",
    54: "STRM_BGM_HIKOUSEN_ROUKA",
    55: "STRM_BGM_HIKOUSEN_ROUKA_FAST",
    56: "STRM_BGM_HIKOUSEN_BOSS",
    57: "STRM_BGM_HIKOUSEN_BOSS_FAST",
    58: "STRM_BGM_HIKOUSENBOSS_CREAR",
    59: "STRM_BGM_SHADOW",
    60: "BGM_NX_STAFF_CREDIT",
    61: "WSD_BGM_SHIRO_LAST",
    62: "WSD_BGM_SHIRO_LAST_FAST",
    63: "STRM_BGM_ROAD_TO_LAST",
    64: "STRM_BGM_ROAD_TO_LAST_FAST",
    65: "SE_BGM_CS_STAR",
    66: "STRM_BGM_SELECT_W1",
    67: "STRM_BGM_SELECT_W2",
    68: "STRM_BGM_SELECT_W3",
    69: "STRM_BGM_SELECT_W5 - Haunted",
    70: "STRM_BGM_SELECT_W4",
    71: "STRM_BGM_SELECT_W5",
    72: "STRM_BGM_SELECT_W6",
    73: "STRM_BGM_SELECT_W7",
    74: "STRM_BGM_MENU",
    75: "STRM_BGM_MENU - Track 2",
    76: "STRM_BGM_CHIJOU",
    77: "STRM_BGM_CHIJOU - Yoshi",
    78: "STRM_BGM_CHIJOU - Baby Yoshi",
    79: "STRM_BGM_CHIJOU_FAST",
    80: "STRM_BGM_CHIJOU_FAST - Yoshi",
    81: "STRM_BGM_CHIJOU_FAST - Baby Yoshi",
    82: "STRM_BGM_CHIKA",
    83: "STRM_BGM_CHIKA - Yoshi",
    84: "STRM_BGM_CHIKA - Baby Yoshi",
    85: "STRM_BGM_CHIKA_FAST",
    86: "STRM_BGM_CHIKA_FAST - Yoshi",
    87: "STRM_BGM_CHIKA_FAST - Baby Yoshi",
    88: "STRM_BGM_BONUS",
    89: "STRM_BGM_BONUS - Yoshi",
    90: "STRM_BGM_BONUS - Baby Yoshi",
    91: "STRM_BGM_BONUS_FAST",
    92: "STRM_BGM_BONUS_FAST - Yoshi",
    93: "STRM_BGM_BONUS_FAST - Baby Yoshi",
    94: "STRM_BGM_STAR",
    95: "STRM_BGM_STAR - Yoshi",
    96: "STRM_BGM_STAR - Baby Yoshi",
    97: "STRM_BGM_STAR_FAST",
    98: "STRM_BGM_STAR_FAST - Yoshi",
    99: "STRM_BGM_STAR_FAST - Baby Yoshi",
    100: "STRM_BGM_WATER",
    101: "STRM_BGM_WATER - Baby Yoshi",
    102: "STRM_BGM_WATER_FAST",
    103: "STRM_BGM_WATER_FAST - Baby Yoshi",
    104: "STRM_BGM_ATHLETIC",
    105: "STRM_BGM_ATHLETIC - Yoshi",
    106: "STRM_BGM_ATHLETIC - Baby Yoshi",
    107: "STRM_BGM_ATHLETIC_FAST",
    108: "STRM_BGM_ATHLETIC_FAST - Yoshi",
    109: "STRM_BGM_ATHLETIC_FAST - Baby Yoshi",
    110: "STRM_BGM_OBAKE",
    111: "STRM_BGM_OBAKE - Baby Yoshi",
    112: "STRM_BGM_OBAKE_FAST",
    113: "STRM_BGM_OBAKE_FAST - Baby Yoshi",
    114: "STRM_BGM_SABAKU",
    115: "STRM_BGM_SABAKU - Yoshi",
    116: "STRM_BGM_SABAKU - Baby Yoshi",
    117: "STRM_BGM_SABAKU_FAST",
    118: "STRM_BGM_SABAKU_FAST - Yoshi",
    119: "STRM_BGM_SABAKU_FAST - Baby Yoshi",
    120: "STRM_BGM_YUKI",
    121: "STRM_BGM_YUKI - Yoshi",
    122: "STRM_BGM_YUKI - Baby Yoshi",
    123: "STRM_BGM_YUKI_FAST",
    124: "STRM_BGM_YUKI_FAST - Yoshi",
    125: "STRM_BGM_YUKI_FAST - Baby Yoshi",
    126: "STRM_BGM_KAZAN",
    127: "STRM_BGM_KAZAN - Baby Yoshi",
    128: "STRM_BGM_KAZAN_FAST",
    129: "STRM_BGM_KAZAN_FAST - Baby Yoshi",
    130: "STRM_BGM_TORIDE",
    131: "STRM_BGM_TORIDE_FAST",
    132: "STRM_BGM_SHIRO",
    133: "STRM_BGM_SHIRO_FAST",
    134: "STRM_BGM_MINIGAME",
    135: "STRM_BGM_MINIGAME - Track 2",
    136: "STRM_BGM_MORI",
    137: "STRM_BGM_MORI - Yoshi",
    138: "STRM_BGM_MORI - Baby Yoshi",
    139: "STRM_BGM_MORI_FAST",
    140: "STRM_BGM_MORI_FAST - Yoshi",
    141: "STRM_BGM_MORI_FAST - Baby Yoshi",
    142: "STRM_BGM_SANBASHI",
    143: "STRM_BGM_SANBASHI - Yoshi",
    144: "STRM_BGM_SANBASHI - Baby Yoshi",
    145: "STRM_BGM_SANBASHI_FAST",
    146: "STRM_BGM_SANBASHI_FAST - Yoshi",
    147: "STRM_BGM_SANBASHI_FAST - Baby Yoshi",
    148: "STRM_BGM_KAZAN_TIKA",
    149: "STRM_BGM_KAZAN_TIKA - Baby Yoshi",
    150: "STRM_BGM_KAZAN_TIKA_FAST",
    151: "STRM_BGM_KAZAN_TIKA_FAST - Baby Yoshi",
    152: "STRM_BGM_STAFF_CREDIT",
}

tracks = {
    "WSD_BGM_SELECT_W8": (0x41ad80, 0x1313b8),
    "WSD_BGM_SELECT_W9": (0x54c140, 0x1313b8),
    "WSD_BGM_MAP_DEMO_W8": (0x67d500, 0x7bf90),
    "STRM_BGM_SWITCH": (0x6f9580, 0x14aa08),
    "STRM_BGM_MULTI_RESULT": (0x843fc0, 0x10dca0),
    "STRM_BGM_SHORT_RESULT": (0x951c80, 0xc3ca0),
    "WSD_BGM_STAR_DRC": (0xa15940, 0xb80a0),
    "WSD_BGM_COIN_EDIT": (0xacda00, 0x15dca8),
    "STRM_BGM_COURSE_CLEAR": (0xc2b880, 0xa3c9c),
    "STRM_BGM_ALL_CMPLT_5STARS": (0xccf540, 0x28ec0),
    "STRM_BGM_STORY_CREAR": (0xcf8400, 0x26398),
    "STRM_BGM_COURSE_OUT_ALL_BUBBLE": (0xd1e7c0, 0x1dd18),
    "WSD_BGM_BGM_LAST_BOSS_FANFARE_LR_RY_32": (0xd3c500, 0x22888),
    "STRM_BGM_LAST_CASTLE_APPEAR": (0xd5edc0, 0x7ec28),
    "STRM_BGM_MINIGAME_FANFARE_BAD": (0xddda00, 0x22698),
    "STRM_BGM_MINIGAME_FANFARE_GOOD": (0xe000c0, 0x1e3b8),
    "STRM_BGM_STAR_COIN_CMPLT_ALL": (0xe1e480, 0x27ac0),
    "STRM_BGM_STAR_COIN_CMPLT_WORLD": (0xe45f40, 0x25f18),
    "WSD_BGM_CHEEPFANFARE_LR_RY_32": (0xe6be80, 0x16140),
    "STRM_BGM_COURSE_CLEAR_ZORO": (0xe81fc0, 0x59db8),
    "__STRM_BGM_MULTI_FAIL": (0xedbd80, 0x19618),
    "STRM_BGM_GAMEOVER": (0xef53c0, 0x4a890),
    "STRM_BGM_MULTI_FAIL": (0xf3fc80, 0x24318),
    "STRM_BGM_DOWN": (0xf63fc0, 0x1ffb8),
    "STRM_BGM_SHADOW_START": (0xf83f80, 0x3eaa0),
    "STRM_BGM_SHADOW_CATCH": (0xfc2a40, 0x1ea30),
    "STRM_BGM_COIN_WIN": (0xfe1480, 0x13108),
    "STRM_BGM_ODAI_CLEAR": (0xff45c0, 0x25a90),
    "WSD_BGM_SPEED_UP": (0x101a080, 0xce98),
    "WSD_BGM_SPEED_UP_MAX": (0x1026f40, 0xfcb8),
    "WSD_BGM_ODAI_MEDAL_CMP": (0x1036c00, 0x19f40),
    "WSD_BGM_ODAI_MEDALCMP_GOLD": (0x1050b40, 0x1cc20),
    "STRM_BGM_TITLE": (0x106d800, 0x28c0a8),
    "STRM_BGM_DEMO_OP": (0x12f9980, 0x1ff830),
    "STRM_BGM_DEMO_OP2": (0x14f91c0, 0xd9810),
    "STRM_BGM_DEMO_ED": (0x15d2ac0, 0xd0438),
    "STRM_BGM_DEMO_ED2": (0x16a2f00, 0x15b230),
    "STRM_BGM_HIKOUSEN": (0x17fe200, 0x456ca0),
    "STRM_BGM_HIKOUSEN_FAST": (0x1c54ec0, 0x3b7a90),
    "STRM_BGM_LAST_BOSS": (0x200ca40, 0x284fb8),
    "STRM_BGM_LAST_BOSS_FAST": (0x2291a00, 0x219810),
    "STRM_BGM_LAST_BOSS_CLEAR": (0x24ab240, 0x43540),
    "STRM_BGM_LAST_BOSS2": (0x24ee840, 0x2b1390),
    "STRM_BGM_LAST_BOSS2_FAST": (0x279fc00, 0x24a0b0),
    "STRM_BGM_LAST_BOSS2_CLEAR": (0x29e9cc0, 0xac4a0),
    "STRM_BGM_LAST_BOSS2_HARP": (0x2a96180, 0xe41b8),
    "STRM_BGM_MG_BTL": (0x2b7a400, 0x25e488),
    "STRM_BGM_MG_BTL_END": (0x2dd88c0, 0x1e3b8),
    "STRM_BGM_SHIRO_BOSS": (0x2df6d40, 0x39aab0),
    "STRM_BGM_SHIRO_BOSS_FAST": (0x3191800, 0x329418),
    "STRM_BGM_SHIRO_BOSS_CLEAR": (0x34bac40, 0x3b9a0),
    "STRM_BGM_TORIDE_BOSS": (0x34f66c0, 0x236bb0),
    "STRM_BGM_TORIDE_BOSS_FAST": (0x372d280, 0x1dfda8),
    "STRM_BGM_TORIDEBOSS_CREAR": (0x390d040, 0x3ae40),
    "STRM_BGM_HIKOUSEN_ROUKA": (0x3947f40, 0x100e08),
    "STRM_BGM_HIKOUSEN_ROUKA_FAST": (0x3a48d80, 0xc0b28),
    "STRM_BGM_HIKOUSEN_BOSS": (0x3b09980, 0x1ffa18),
    "STRM_BGM_HIKOUSEN_BOSS_FAST": (0x3d093c0, 0x1aaa98),
    "STRM_BGM_HIKOUSENBOSS_CREAR": (0x3eb3e80, 0x3bdc0),
    "STRM_BGM_SHADOW": (0x3eefd00, 0x1546b8),
    "BGM_NX_STAFF_CREDIT": (0x40443c0, 0x6563b8),
    "WSD_BGM_SHIRO_LAST": (0x469a840, 0x193eb0),
    "WSD_BGM_SHIRO_LAST_FAST": (0x482e700, 0x155b88),
    "STRM_BGM_ROAD_TO_LAST": (0x4984380, 0x82d40),
    "STRM_BGM_ROAD_TO_LAST_FAST": (0x4a070c0, 0x66e38),
    "SE_BGM_CS_STAR": (0x6ec0380, 0xf0e0),
    "STRM_BGM_SELECT_W1": (0x74ff800, 0x1757c0),
    "STRM_BGM_SELECT_W2": (0x7674fc0, 0x131588),
    "STRM_BGM_SELECT_W3": (0x77a6580, 0x130fb0),
    "STRM_BGM_SELECT_W5 - Haunted": (0x78d7540, 0x169b30),
    "STRM_BGM_SELECT_W4": (0x7a41080, 0x1487b0),
    "STRM_BGM_SELECT_W5": (0x7b89840, 0x130fb8),
    "STRM_BGM_SELECT_W6": (0x7cba800, 0x130fb8),
    "STRM_BGM_SELECT_W7": (0x7deb7c0, 0x130fb8),
    "STRM_BGM_MENU": (0x7f1c840, 0x159d08),
    "STRM_BGM_MENU - Track 2": (0x8076580, 0x159d08),
    "STRM_BGM_CHIJOU": (0x81d0380, 0x265b98),
    "STRM_BGM_CHIJOU - Yoshi": (0x8435f40, 0x265b98),
    "STRM_BGM_CHIJOU - Baby Yoshi": (0x869bb00, 0x265b98),
    "STRM_BGM_CHIJOU_FAST": (0x89016c0, 0x2103a8),
    "STRM_BGM_CHIJOU_FAST - Yoshi": (0x8b11a80, 0x210030),
    "STRM_BGM_CHIJOU_FAST - Baby Yoshi": (0x8d21ac0, 0x215f20),
    "STRM_BGM_CHIKA": (0x8f37ac0, 0x32bf40),
    "STRM_BGM_CHIKA - Yoshi": (0x9263a00, 0x32bf08),
    "STRM_BGM_CHIKA - Baby Yoshi": (0x958f940, 0x349a38),
    "STRM_BGM_CHIKA_FAST": (0x98d9380, 0x2a7020),
    "STRM_BGM_CHIKA_FAST - Yoshi": (0x9b803c0, 0x2a6f40),
    "STRM_BGM_CHIKA_FAST - Baby Yoshi": (0x9e27300, 0x2b3b08),
    "STRM_BGM_BONUS": (0xa0daf00, 0x1bb5c0),
    "STRM_BGM_BONUS - Yoshi": (0xa2964c0, 0x1bb5a0),
    "STRM_BGM_BONUS - Baby Yoshi": (0xa451a80, 0x19ee90),
    "STRM_BGM_BONUS_FAST": (0xa5f0940, 0x176028),
    "STRM_BGM_BONUS_FAST - Yoshi": (0xa766980, 0x176018),
    "STRM_BGM_BONUS_FAST - Baby Yoshi": (0xa8dc9c0, 0x173718),
    "STRM_BGM_STAR": (0xaa501c0, 0xe0ec0),
    "STRM_BGM_STAR - Yoshi": (0xab31080, 0x86fa0),
    "STRM_BGM_STAR - Baby Yoshi": (0xabb8040, 0x86fa0),
    "STRM_BGM_STAR_FAST": (0xac3f000, 0xc6a88),
    "STRM_BGM_STAR_FAST - Yoshi": (0xad05ac0, 0x77310),
    "STRM_BGM_STAR_FAST - Baby Yoshi": (0xad7ce00, 0x77310),
    "STRM_BGM_WATER": (0xadf4200, 0x29e730),
    "STRM_BGM_WATER - Baby Yoshi": (0xb092940, 0x29e730),
    "STRM_BGM_WATER_FAST": (0xb331080, 0x234928),
    "STRM_BGM_WATER_FAST - Baby Yoshi": (0xb5659c0, 0x234928),
    "STRM_BGM_ATHLETIC": (0xb79a3c0, 0x220718),
    "STRM_BGM_ATHLETIC - Yoshi": (0xb9bab00, 0x254498),
    "STRM_BGM_ATHLETIC - Baby Yoshi": (0xbc0efc0, 0x220720),
    "STRM_BGM_ATHLETIC_FAST": (0xbe2f700, 0x1c51b8),
    "STRM_BGM_ATHLETIC_FAST - Yoshi": (0xbff48c0, 0x1ca840),
    "STRM_BGM_ATHLETIC_FAST - Baby Yoshi": (0xc1bf100, 0x1c51b8),
    "STRM_BGM_OBAKE": (0xc384380, 0x36a7b0),
    "STRM_BGM_OBAKE - Baby Yoshi": (0xc6eeb40, 0x303838),
    "STRM_BGM_OBAKE_FAST": (0xc9f2380, 0x2d8640),
    "STRM_BGM_OBAKE_FAST - Baby Yoshi": (0xccca9c0, 0x30e690),
    "STRM_BGM_SABAKU": (0xcfd9140, 0x361c90),
    "STRM_BGM_SABAKU - Yoshi": (0xd33ae00, 0x361c90),
    "STRM_BGM_SABAKU - Baby Yoshi": (0xd69cac0, 0x361c90),
    "STRM_BGM_SABAKU_FAST": (0xd9fe780, 0x31a920),
    "STRM_BGM_SABAKU_FAST - Yoshi": (0xdd190c0, 0x31a920),
    "STRM_BGM_SABAKU_FAST - Baby Yoshi": (0xe033a00, 0x31a920),
    "STRM_BGM_YUKI": (0xe34e400, 0x265ba0),
    "STRM_BGM_YUKI - Yoshi": (0xe5b3fc0, 0x265b98),
    "STRM_BGM_YUKI - Baby Yoshi": (0xe819b80, 0x265ba0),
    "STRM_BGM_YUKI_FAST": (0xea7f740, 0x1ff730),
    "STRM_BGM_YUKI_FAST - Yoshi": (0xec7ee80, 0x210030),
    "STRM_BGM_YUKI_FAST - Baby Yoshi": (0xee8eec0, 0x1ff0b8),
    "STRM_BGM_KAZAN": (0xf08e040, 0x4d0420),
    "STRM_BGM_KAZAN - Baby Yoshi": (0xf55e480, 0x4d0420),
    "STRM_BGM_KAZAN_FAST": (0xfa2e8c0, 0x402d10),
    "STRM_BGM_KAZAN_FAST - Baby Yoshi": (0xfe31600, 0x402d28),
    "STRM_BGM_TORIDE": (0x10234400, 0x26a2a0),
    "STRM_BGM_TORIDE_FAST": (0x1049e6c0, 0x1ff3a8),
    "STRM_BGM_SHIRO": (0x1069db40, 0x3fa508),
    "STRM_BGM_SHIRO_FAST": (0x10a98080, 0x417d40),
    "STRM_BGM_MINIGAME": (0x10eafe80, 0x2708b8),
    "STRM_BGM_MINIGAME - Track 2": (0x11120740, 0x2708b8),
    "STRM_BGM_MORI": (0x113910c0, 0x323a98),
    "STRM_BGM_MORI - Yoshi": (0x116b4b80, 0x323a98),
    "STRM_BGM_MORI - Baby Yoshi": (0x119d8640, 0x323a98),
    "STRM_BGM_MORI_FAST": (0x11cfc100, 0x29dba8),
    "STRM_BGM_MORI_FAST - Yoshi": (0x11f99cc0, 0x29dba8),
    "STRM_BGM_MORI_FAST - Baby Yoshi": (0x12237880, 0x29dba8),
    "STRM_BGM_SANBASHI": (0x124d5500, 0x2d4e38),
    "STRM_BGM_SANBASHI - Yoshi": (0x127aa340, 0x2d4e38),
    "STRM_BGM_SANBASHI - Baby Yoshi": (0x12a7f180, 0x259488),
    "STRM_BGM_SANBASHI_FAST": (0x12cd8640, 0x29b130),
    "STRM_BGM_SANBASHI_FAST - Yoshi": (0x12f73780, 0x29b130),
    "STRM_BGM_SANBASHI_FAST - Baby Yoshi": (0x1320e8c0, 0x21d298),
    "STRM_BGM_KAZAN_TIKA": (0x1342bc40, 0x27de38),
    "STRM_BGM_KAZAN_TIKA - Baby Yoshi": (0x136a9a80, 0x27de38),
    "STRM_BGM_KAZAN_TIKA_FAST": (0x139278c0, 0x1db838),
    "STRM_BGM_KAZAN_TIKA_FAST - Baby Yoshi": (0x13b03100, 0x1e2e38),
    "STRM_BGM_STAFF_CREDIT": (0x13ce5fc0, 0xc69830),
}


def extract(fsar):
    with open(fsar, "rb") as inf:
        inb = inf.read()

    if inb[:4] != b'FSAR':
        print('')
        print("Invalid BFSAR file!")
        sys.exit(1)

    print('')
    print("Extracting: " + fsar)

    for track in tracks:
        folder = os.path.dirname(fsar)
        if folder: folder += '/'

        pos, size = tracks[track]

        if inb[pos:pos+4] != b'FWAV':
            print('')
            print("Could not read " + track + " from BFSAR!")
            sys.exit(1)

        endianness = ">" if inb[pos+4:pos+6] == b'\xFE\xFF' else "<"

        size2 = struct.unpack(endianness + "I", inb[pos+12:pos+16])[0]

        if size2 > size:
            size2 = size

        with open(folder + track + '.bfwav', "wb+") as output:
            output.write(inb[pos:pos+size2])


def inject(fsar, num, fwav):
    with open(fsar, "rb") as inf:
        inb = inf.read()

    with open(fwav, "rb") as inf:
        inb2 = inf.read()

    if inb[:4] != b'FSAR':
        print('')
        print("Invalid BFSAR file!")
        sys.exit(1)

    if inb2[:4] != b'FWAV':
        print('')
        print("Invalid BFWAV file!")
        sys.exit(1)

    name = nums[num]

    pos, size = tracks[name]

    endianness = ">" if inb2[4:6] == b'\xFE\xFF' else "<"

    size2 = len(inb2)

    size3 = struct.unpack(endianness + "I", inb2[12:16])[0]

    if size2 > size or size3 > size:
        print('')
        print("Size of the BFWAV file exceeds the original!")
        sys.exit(1)

    print('')
    print("Injecting: " + fwav)

    inb = bytearray(inb)
    inb[pos:pos+size2] = inb2

    with open(fsar, "wb+") as outf:
        outf.write(inb)


def printInfo():
    print('')
    print("Usage:")
    print("  Extracting:")
    print("    main bfsar")
    print('')
    print("  Injecting:")
    print("    main bfsar num bfwav")
    print('')
    print("  bfsar             NSMBU BFSAR file")
    print("  num               Track number")
    print("  bfwav             BFWAV file")
    print('')
    print("Track numbers:")
    for num in nums:
        print("  " + str(num) + " = " + nums[num])
    sys.exit(1)


def main():
    print("NSMBU DX Music extractor/injector v0.1")
    print("(C) 2019 AboodXD")
    
    if not len(sys.argv) in [2, 4]:
        printInfo()

    elif len(sys.argv) == 2:
        if not os.path.isfile(sys.argv[1]):
            print('')
            print("BFSAR file not found!")
            printInfo()

        extract(sys.argv[1])

    else:
        if not os.path.isfile(sys.argv[1]):
            print('')
            print("BFSAR file not found!")
            printInfo()

        try:
            num = int(sys.argv[2], 0)
        except ValueError:
            print('')
            print("Invalid track number!")
            printInfo()

        if not num in nums:
            print('')
            print("Invalid track number!")
            printInfo()

        if not os.path.isfile(sys.argv[3]):
            print('')
            print("BFWAV file not found!")
            printInfo()

        inject(sys.argv[1], num, sys.argv[3])


if __name__ == '__main__': main()
