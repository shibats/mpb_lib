# 大砲ゲーム用モジュールで提供する関数をまとめたモジュール
# 
# Copyright (c) 2023 Atsush Shibata(shivata@m-info.co.jp)
#
# Released under the MIT license.

from .cannon import cannon_game, cannon_game2, cannon_game3, get_distance, load_script, calc_powder
from random import seed

seed(100)