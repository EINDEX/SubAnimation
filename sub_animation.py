#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
SubAnimation : Provide an animation ics subscription service
Copyright (C) 2016-2017 EINDEX Li

@Author        : EINDEX Li
@File          : sub_animation.py
@Created       : 2017/3/6
@Last Modified : 2017/3/6
"""
from ical_builder import ical_builder
from parser import BgmlistParser


def write(filename, parser):
    cal_file = ical_builder(parser.anime_list())
    with open(filename, 'wb') as file:
        file.write(cal_file.to_ical())


if __name__ == '__main__':
    write('test.ics', BgmlistParser())
