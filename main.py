#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# NSMBU Music extractor/injector
# Version 0.1
# Copyright © 2017 Stella/AboodXD

# This file is part of NSMBU Music extractor/injector.

# NSMBU Music extractor/injector is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# NSMBU Music extractor/injector is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

import os
import struct
import sys

nums = {
    0: "SE_BGM_CS_STAR",
    1: "STRM_BGM_DEMO_OP",
    2: "STRM_BGM_DEMO_OP2",
    3: "STRM_BGM_DEMO_ED",
    4: "STRM_BGM_DEMO_ED2",
    5: "STRM_BGM_TITLE",
    6: "STRM_BGM_MENU",
    7: "STRM_BGM_MENU - Track 2",
    8: "WSD_BGM_SELECT_W8",
    9: "WSD_BGM_SELECT_W9",
    10: "WSD_BGM_MAP_DEMO_W8",
    11: "STRM_BGM_SELECT_W1",
    12: "STRM_BGM_SELECT_W2",
    13: "STRM_BGM_SELECT_W3",
    14: "STRM_BGM_SELECT_W5 - Haunted",
    15: "STRM_BGM_SELECT_W4",
    16: "STRM_BGM_SELECT_W5",
    17: "STRM_BGM_SELECT_W6",
    18: "STRM_BGM_SELECT_W7",
    19: "STRM_BGM_SWITCH",
    20: "STRM_BGM_MULTI_RESULT",
    21: "WSD_BGM_STAR_DRC",
    22: "WSD_BGM_COIN_EDIT",
    23: "STRM_BGM_COURSE_CLEAR",
    24: "STRM_BGM_ALL_CMPLT_5STARS",
    25: "STRM_BGM_COURSE_OUT_ALL_BUBBLE",
    26: "STRM_BGM_LAST_CASTLE_APPEAR",
    27: "STRM_BGM_MINIGAME_FANFARE_BAD",
    28: "STRM_BGM_MINIGAME_FANFARE_GOOD",
    29: "STRM_BGM_STAR_COIN_CMPLT_ALL",
    30: "STRM_BGM_STAR_COIN_CMPLT_WORLD",
    31: "WSD_BGM_CHEEPFANFARE_LR_RY_32",
    32: "STRM_BGM_COURSE_CLEAR_ZORO",
    33: "STRM_BGM_DOWN_MULTI",
    34: "STRM_BGM_GAMEOVER",
    35: "STRM_BGM_MULTI_FAIL",
    36: "STRM_BGM_DOWN",
    37: "STRM_BGM_SHADOW_START",
    38: "STRM_BGM_SHADOW_CATCH",
    39: "STRM_BGM_COIN_WIN",
    40: "STRM_BGM_ODAI_CLEAR",
    41: "STRM_BGM_STAR",
    42: "STRM_BGM_STAR - Yoshi",
    43: "STRM_BGM_STAR - Baby Yoshi",
    44: "STRM_BGM_STAR_FAST",
    45: "STRM_BGM_STAR_FAST - Yoshi",
    46: "STRM_BGM_STAR_FAST - Baby Yoshi",
    47: "STRM_BGM_CHIJOU",
    48: "STRM_BGM_CHIJOU - Yoshi",
    49: "STRM_BGM_CHIJOU - Baby Yoshi",
    50: "STRM_BGM_CHIJOU_FAST",
    51: "STRM_BGM_CHIJOU_FAST - Yoshi",
    52: "STRM_BGM_CHIJOU_FAST - Baby Yoshi",
    53: "STRM_BGM_CHIKA",
    54: "STRM_BGM_CHIKA - Yoshi",
    55: "STRM_BGM_CHIKA - Baby Yoshi",
    56: "STRM_BGM_CHIKA_FAST",
    57: "STRM_BGM_CHIKA_FAST - Yoshi",
    58: "STRM_BGM_CHIKA_FAST - Baby Yoshi",
    59: "STRM_BGM_WATER",
    60: "STRM_BGM_WATER - Baby Yoshi",
    61: "STRM_BGM_WATER_FAST",
    62: "STRM_BGM_WATER_FAST - Baby Yoshi",
    63: "STRM_BGM_ATHLETIC",
    64: "STRM_BGM_ATHLETIC - Yoshi",
    65: "STRM_BGM_ATHLETIC - Baby Yoshi",
    66: "STRM_BGM_ATHLETIC_FAST",
    67: "STRM_BGM_ATHLETIC_FAST - Yoshi",
    68: "STRM_BGM_ATHLETIC_FAST - Baby Yoshi",
    69: "STRM_BGM_OBAKE",
    70: "STRM_BGM_OBAKE - Baby Yoshi",
    71: "STRM_BGM_OBAKE_FAST",
    72: "STRM_BGM_OBAKE_FAST - Baby Yoshi",
    73: "STRM_BGM_SABAKU",
    74: "STRM_BGM_SABAKU - Yoshi",
    75: "STRM_BGM_SABAKU - Baby Yoshi",
    76: "STRM_BGM_SABAKU_FAST",
    77: "STRM_BGM_SABAKU_FAST - Yoshi",
    78: "STRM_BGM_SABAKU_FAST - Baby Yoshi",
    79: "STRM_BGM_YUKI",
    80: "STRM_BGM_YUKI - Yoshi",
    81: "STRM_BGM_YUKI - Baby Yoshi",
    82: "STRM_BGM_YUKI_FAST",
    83: "STRM_BGM_YUKI_FAST - Yoshi",
    84: "STRM_BGM_YUKI_FAST - Baby Yoshi",
    85: "STRM_BGM_KAZAN",
    86: "STRM_BGM_KAZAN - Baby Yoshi",
    87: "STRM_BGM_KAZAN_FAST",
    88: "STRM_BGM_KAZAN_FAST - Baby Yoshi",
    89: "STRM_BGM_TORIDE",
    90: "STRM_BGM_TORIDE_FAST",
    91: "STRM_BGM_SHIRO",
    92: "STRM_BGM_SHIRO_FAST",
    93: "STRM_BGM_HIKOUSEN",
    94: "STRM_BGM_HIKOUSEN_FAST",
    95: "STRM_BGM_HIKOUSEN_ROUKA",
    96: "STRM_BGM_HIKOUSEN_ROUKA_FAST",
    97: "STRM_BGM_BONUS",
    98: "STRM_BGM_BONUS - Yoshi",
    99: "STRM_BGM_BONUS - Baby Yoshi",
    100: "STRM_BGM_BONUS_FAST",
    101: "STRM_BGM_BONUS_FAST - Yoshi",
    102: "STRM_BGM_BONUS_FAST - Baby Yoshi",
    103: "STRM_BGM_ROAD_TO_LAST",
    104: "STRM_BGM_ROAD_TO_LAST_FAST",
    105: "STRM_BGM_TORIDE_BOSS",
    106: "STRM_BGM_TORIDE_BOSS_FAST",
    107: "STRM_BGM_TORIDEBOSS_CREAR",
    108: "STRM_BGM_SHIRO_BOSS",
    109: "STRM_BGM_SHIRO_BOSS_FAST",
    110: "STRM_BGM_SHIRO_BOSS_CLEAR",
    111: "STRM_BGM_MINIGAME",
    112: "STRM_BGM_MINIGAME - Track 2",
    113: "STRM_BGM_HIKOUSEN_BOSS",
    114: "STRM_BGM_HIKOUSEN_BOSS_FAST",
    115: "STRM_BGM_HIKOUSENBOSS_CREAR",
    116: "STRM_BGM_MORI",
    117: "STRM_BGM_MORI - Yoshi",
    118: "STRM_BGM_MORI - Baby Yoshi",
    119: "STRM_BGM_MORI_FAST",
    120: "STRM_BGM_MORI_FAST - Yoshi",
    121: "STRM_BGM_MORI_FAST - Baby Yoshi",
    122: "STRM_BGM_MG_BTL",
    123: "STRM_BGM_MG_BTL_END",
    124: "STRM_BGM_SANBASHI",
    125: "STRM_BGM_SANBASHI - Yoshi",
    126: "STRM_BGM_SANBASHI - Baby Yoshi",
    127: "STRM_BGM_SANBASHI_FAST",
    128: "STRM_BGM_SANBASHI_FAST - Yoshi",
    129: "STRM_BGM_SANBASHI_FAST - Baby Yoshi",
    130: "STRM_BGM_KAZAN_TIKA",
    131: "STRM_BGM_KAZAN_TIKA - Baby Yoshi",
    132: "STRM_BGM_KAZAN_TIKA_FAST",
    133: "STRM_BGM_KAZAN_TIKA_FAST - Baby Yoshi",
    134: "STRM_BGM_SHADOW",
    135: "STRM_BGM_STAFF_CREDIT",
    136: "STRM_BGM_LAST_BOSS",
    137: "STRM_BGM_LAST_BOSS_FAST",
    138: "STRM_BGM_LAST_BOSS_CLEAR",
    139: "STRM_BGM_LAST_BOSS2",
    140: "STRM_BGM_LAST_BOSS2_FAST",
    141: "STRM_BGM_LAST_BOSS2_CLEAR",
    142: "STRM_BGM_LAST_BOSS2_HARP",
    143: "WSD_BGM_SHIRO_LAST",
    144: "WSD_BGM_SHIRO_LAST_FAST"
}

tracks = {
    "STRM_BGM_SELECT_W1": (0x2F63120, 0x100958),
    "STRM_BGM_HIKOUSEN_FAST": (0x982FA00, 0x2B28E0),
    "STRM_BGM_HIKOUSENBOSS_CREAR": (0xB51F720, 0x2E150),
    "STRM_BGM_HIKOUSEN": (0x956B9A0, 0x2C4060),
    "STRM_BGM_ATHLETIC_FAST": (0x5EE4CE0, 0x131B18),
    "STRM_BGM_ATHLETIC_FAST - Baby Yoshi": (0x6148320, 0x12E160),
    "STRM_BGM_ATHLETIC - Baby Yoshi": (0x5D79D40, 0x16AFA0),
    "STRM_BGM_ATHLETIC_FAST - Yoshi": (0x6016800, 0x131B18),
    "STRM_BGM_ATHLETIC - Yoshi": (0x5BEC4A0, 0x18D8A0),
    "STRM_BGM_ATHLETIC": (0x5A5EC00, 0x18D8A0),
    "STRM_BGM_MG_BTL": (0xC0F5220, 0x194348),
    "STRM_BGM_MG_BTL_END": (0xC289580, 0x12A58),
    "STRM_BGM_SANBASHI_FAST": (0xC7F8A60, 0x1BCBC8),
    "STRM_BGM_SANBASHI_FAST - Baby Yoshi": (0xCB72220, 0x168C98),
    "STRM_BGM_SANBASHI - Baby Yoshi": (0xC667C80, 0x190DE0),
    "STRM_BGM_SANBASHI_FAST - Yoshi": (0xC9B5640, 0x1BCBC8),
    "STRM_BGM_SANBASHI - Yoshi": (0xC4847E0, 0x1E3490),
    "STRM_BGM_SANBASHI": (0xC2A1340, 0x1E3488),
    "STRM_BGM_BONUS_FAST": (0x9F8F800, 0xF95A0),
    "STRM_BGM_BONUS_FAST - Baby Yoshi": (0xA182340, 0xF7A48),
    "STRM_BGM_BONUS - Baby Yoshi": (0x9E7CEA0, 0x112950),
    "STRM_BGM_BONUS_FAST - Yoshi": (0xA088DA0, 0xF95A0),
    "STRM_BGM_BONUS - Yoshi": (0x9D55540, 0x127958),
    "STRM_BGM_BONUS": (0x9C2DBA0, 0x127990),
    "STRM_BGM_LAST_BOSS_FAST": (0xDEC0B40, 0x166598), # 0xA428100
    "STRM_BGM_LAST_BOSS": (0xDD12B20, 0x1AE018), # 0xA27A0E0
    "STRM_BGM_LAST_BOSS2_CLEAR": (0xE3AA500, 0x76EE0),
    "WSD_BGM_MAP_DEMO_W8": (0x2DF9D00, 0x59F88),
    "STRM_BGM_LAST_CASTLE_APPEAR": (0x3AB5BA0, 0x7EC08),
    "STRM_BGM_HIKOUSEN_BOSS_FAST": (0xB3E9D80, 0x1359A0),
    "STRM_BGM_HIKOUSEN_BOSS": (0xB271FA0, 0x177DC8),
    "STRM_BGM_SHIRO_FAST": (0x92B6BA0, 0x2B4AD8),
    "STRM_BGM_SHIRO_BOSS_CLEAR": (0xAEB4B20, 0x2D858),
    "STRM_BGM_SHIRO": (0x8FBB240, 0x2FB958),
    "STRM_BGM_SHADOW_START": (0x3C68340, 0x24BD8),
    "WSD_BGM_COIN_EDIT": (0x38D2A40, 0xE9360),
    "STRM_BGM_STAFF_CREDIT": (0xD399D40, 0x832388),
    "STRM_BGM_DOWN": (0x3C50FA0, 0x17388),
    "STRM_BGM_SABAKU_FAST": (0x717CF00, 0x211BA0),
    "STRM_BGM_SABAKU_FAST - Baby Yoshi": (0x75A0640, 0x211BA0),
    "STRM_BGM_SABAKU - Baby Yoshi": (0x6F3BBA0, 0x241350),
    "STRM_BGM_SABAKU_FAST - Yoshi": (0x738EAA0, 0x211BA0),
    "STRM_BGM_SABAKU - Yoshi": (0x6CFA840, 0x241350),
    "STRM_BGM_SABAKU": (0x6AB94E0, 0x241350),
    "STRM_BGM_ROAD_TO_LAST_FAST": (0xA642060, 0x66E18),
    "STRM_BGM_ROAD_TO_LAST": (0xA5BF340, 0x82D20),
    "STRM_BGM_LAST_BOSS2_HARP": (0xE4213E0, 0x98188),
    "STRM_BGM_DEMO_ED": (0x169B340, 0x97248),
    "STRM_BGM_DEMO_ED2": (0x17325A0, 0xFBE88),
    "STRM_BGM_LAST_BOSS_CLEAR": (0xE0270E0, 0x30C98), # 0xA58E6A0
    "STRM_BGM_ALL_CMPLT_5STARS": (0x3A463A0, 0x1DD88),
    "STRM_BGM_DOWN_MULTI": (0x3BE2900, 0x195D8),
    "STRM_BGM_ODAI_CLEAR": (0x3CA7460, 0x191E0),
    "WSD_BGM_CHEEPFANFARE_LR_RY_32": (0x3B8AB40, 0x16120),
    "STRM_BGM_COURSE_OUT_ALL_BUBBLE": (0x3A7D960, 0x159D0),
    "STRM_BGM_MINIGAME_FANFARE_BAD": (0x3B347C0, 0x1A520),
    "STRM_BGM_MINIGAME_FANFARE_GOOD": (0x3B4ECE0, 0x12A58),
    "STRM_BGM_STAR_COIN_CMPLT_ALL": (0x3B61740, 0x18008),
    "STRM_BGM_STAR_COIN_CMPLT_WORLD": (0x3B79760, 0x113D8),
    "STRM_BGM_COIN_WIN": (0x3C9A8C0, 0xCB90),
    "STRM_BGM_SELECT_W4": (0x32EBB60, 0xDB010),
    "STRM_BGM_GAMEOVER": (0x3BFBEE0, 0x30DD8),
    "STRM_BGM_OBAKE_FAST": (0x66C4D20, 0x1E5A08),
    "STRM_BGM_OBAKE_FAST - Baby Yoshi": (0x68AA740, 0x209A08),
    "STRM_BGM_OBAKE - Baby Yoshi": (0x64C2740, 0x2025D0),
    "STRM_BGM_OBAKE": (0x627B720, 0x247020),
    "STRM_BGM_DEMO_OP2": (0x14080C0, 0x9DD58),
    "STRM_BGM_DEMO_OP": (0x1294DE0, 0x1732D8),
    "STRM_BGM_MORI_FAST": (0xBBB9700, 0x1BE808),
    "STRM_BGM_MORI_FAST - Baby Yoshi": (0xBF36700, 0x1BE808),
    "STRM_BGM_MORI - Baby Yoshi": (0xB9825A0, 0x237150),
    "STRM_BGM_MORI_FAST - Yoshi": (0xBD77F20, 0x1BE7D0),
    "STRM_BGM_MORI - Yoshi": (0xB76A8C0, 0x217CC8),
    "STRM_BGM_MORI": (0xB552BE0, 0x217CD8),
    "STRM_BGM_TORIDE_BOSS_FAST": (0xA844820, 0x15C358),
    "STRM_BGM_TORIDE_BOSS": (0xA6A9440, 0x19B3E0),
    "STRM_BGM_SHIRO_BOSS_FAST": (0xAC766C0, 0x23E448),
    "STRM_BGM_SHIRO_BOSS": (0xA9CF120, 0x2A75A0),
    "STRM_BGM_SELECT_W2": (0x3063A80, 0xCB920),
    "STRM_BGM_COURSE_CLEAR": (0x39BBDA0, 0x8A5F6),
    "STRM_BGM_MENU - Track 2": (0x1C70EA0, 0xE68E0),
    "STRM_BGM_MENU": (0x1B8A5C0, 0xE68E0),
    "STRM_BGM_LAST_BOSS2_FAST": (0xE223960, 0x186B88),
    "STRM_BGM_LAST_BOSS2": (0xE058180, 0x1CB7E0),
    "STRM_BGM_SELECT_W7": (0x355D680, 0xCB560),
    "STRM_BGM_KAZAN_FAST": (0x8724380, 0x2AC918),
    "STRM_BGM_KAZAN_FAST - Baby Yoshi": (0x89D0CA0, 0x2AC918),
    "STRM_BGM_KAZAN - Baby Yoshi": (0x83EEB20, 0x335858),
    "STRM_BGM_KAZAN": (0x80B92C0, 0x335860),
    "STRM_BGM_KAZAN_TIKA_FAST": (0xD032AA0, 0x13D060),
    "STRM_BGM_KAZAN_TIKA_FAST - Baby Yoshi": (0xD16FB00, 0x141F18),
    "STRM_BGM_KAZAN_TIKA - Baby Yoshi": (0xCE89600, 0x1A9488),
    "STRM_BGM_KAZAN_TIKA": (0xCCE0160, 0x1A9488),
    "STRM_BGM_HIKOUSEN_ROUKA_FAST": (0x9B9C940, 0x8BD60), # 0xDC86A40
    "STRM_BGM_HIKOUSEN_ROUKA": (0x9AE22E0, 0xBA660), # 0xDBCC3E0
    "STRM_BGM_CHIJOU_FAST": (0x43F9D40, 0x1602A0),
    "STRM_BGM_CHIJOU_FAST - Baby Yoshi": (0x46BA040, 0x163FA0),
    "STRM_BGM_CHIJOU - Baby Yoshi": (0x4260AA0, 0x1992A0),
    "STRM_BGM_CHIJOU_FAST - Yoshi": (0x4559FE0, 0x160060),
    "STRM_BGM_CHIJOU - Yoshi": (0x40A00C0, 0x1C09E0),
    "STRM_BGM_CHIJOU": (0x3F06E20, 0x1992A0),
    "WSD_BGM_SELECT_W8": (0x2C62CC0, 0xCB810),
    "WSD_BGM_SHIRO_LAST_FAST": (0xE5C6BE0, 0xE3D20),
    "WSD_BGM_SHIRO_LAST": (0xE4B9700, 0x10D4C8),
    "STRM_BGM_COURSE_CLEAR_ZORO": (0x3BA0C60, 0x41C98),
    "STRM_BGM_SELECT_W6": (0x3492120, 0xCB560),
    "STRM_BGM_SHADOW": (0xD2B1C60, 0xE2F88),
    "STRM_BGM_YUKI_FAST": (0x7CAA480, 0x154FC8),
    "STRM_BGM_YUKI_FAST - Baby Yoshi": (0x7F5F4C0, 0x154B60),
    "STRM_BGM_YUKI - Baby Yoshi": (0x7B111E0, 0x1992A0),
    "STRM_BGM_YUKI_FAST - Yoshi": (0x7DFF460, 0x160060),
    "STRM_BGM_YUKI - Yoshi": (0x7950800, 0x1C09E0),
    "STRM_BGM_YUKI": (0x77B7560, 0x1992A0),
    "STRM_BGM_SELECT_W5 - Haunted": (0x31FA900, 0xF1260),
    "STRM_BGM_SELECT_W5": (0x33C6B80, 0xCB588),
    "STRM_BGM_SELECT_W3": (0x312F3A0, 0xCB560),
    "WSD_BGM_STAR_DRC": (0x3857EE0, 0x7AB58),
    "STRM_BGM_STAR_FAST": (0x3E121E0, 0x4F798),
    "SE_BGM_CS_STAR": (0xE24260, 0xF0C0),
    "STRM_BGM_STAR_FAST - Baby Yoshi": (0x3EB1120, 0x4F798),
    "STRM_BGM_STAR - Baby Yoshi": (0x3DB81C0, 0x5A010),
    "STRM_BGM_STAR_FAST - Yoshi": (0x3E61980, 0x4F798),
    "STRM_BGM_STAR - Yoshi": (0x3D5E1A0, 0x5A010),
    "STRM_BGM_STAR": (0x3D04180, 0x5A010),
    "WSD_BGM_SELECT_W9": (0x2D2E4E0, 0xCB810),
    "STRM_BGM_SWITCH": (0x3714320, 0x7FF60),
    "STRM_BGM_TITLE": (0x19D7720, 0x1B2B60),
    "STRM_BGM_MINIGAME - Track 2": (0xB0AC8A0, 0x1C5348),
    "STRM_BGM_MINIGAME": (0xAEE7540, 0x1C5348),
    "STRM_BGM_TORIDE_FAST": (0x8E430C0, 0x172F90),
    "STRM_BGM_TORIDEBOSS_CREAR": (0xA9A0B80, 0x2E208),
    "STRM_BGM_TORIDE": (0x8C827A0, 0x1C0910),
    "STRM_BGM_CHIKA_FAST": (0x4E8EF00, 0x1C4A98),
    "STRM_BGM_CHIKA_FAST - Baby Yoshi": (0x5218440, 0x1CD548),
    "STRM_BGM_CHIKA - Baby Yoshi": (0x4C5DD20, 0x2311D8),
    "STRM_BGM_CHIKA_FAST - Yoshi": (0x50539A0, 0x1C4A90),
    "STRM_BGM_CHIKA - Yoshi": (0x4A40840, 0x21D4E0),
    "STRM_BGM_CHIKA": (0x4823360, 0x21D4E0),
    "STRM_BGM_WATER_FAST": (0x5768BC0, 0x178658),
    "STRM_BGM_WATER_FAST - Baby Yoshi": (0x58E1220, 0x178658),
    "STRM_BGM_WATER - Baby Yoshi": (0x55A9C20, 0x1BEFA0),
    "STRM_BGM_WATER": (0x53EAC40, 0x1BEFD0),
    "STRM_BGM_MULTI_RESULT": (0x3794280, 0xC3C60),
    "STRM_BGM_SHADOW_CATCH": (0x3C8CF20, 0xD9A0),
    "STRM_BGM_MULTI_FAIL": (0x3C2CCC0, 0x242D8)
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

        pos = tracks[track][0]

        endianness = "big" if inb[pos+4:pos+6] == b'\xFE\xFF' else "little"
        endianness2 = ">" if inb[pos+4:pos+6] == b'\xFE\xFF' else "<"

        size = struct.unpack(endianness2 + "I", inb[pos+12:pos+16])[0]

        if inb[pos:pos+4] != b'FWAV':
            print('')
            print("Could not read " + track + " from BFSAR!")
            sys.exit(1)

        with open(folder + track + '.bfwav', "wb+") as output:
            output.write(inb[pos:pos+size])


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

    endianness = "big" if inb[pos+4:pos+6] == b'\xFE\xFF' else "little"

    size2 = len(inb2)

    if size2 > size:
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
    print("NSMBU Music extractor/injector v0.1")
    print("(C) 2017 Stella/AboodXD")
    
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
