#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
SubAnimation : Provide an animation ics subscription service
Copyright (C) 2016-2017 EINDEX Li

@Author        : EINDEX Li
@File          : bgmlist_parser.py
@Created       : 2017/3/6
@Last Modified : 2017/3/6
"""
import datetime
from pprint import pprint

import dateutil.parser

from parser.base_parser import BaseParser


class BgmlistParser(BaseParser):
    """Parser for bgmlist data"""

    def __init__(self):
        self.url = 'https://raw.githubusercontent.com/bangumi-data/bangumi-data/master/dist/data.json'
        super().__init__(self.url)

    def parsing(self):
        self.__anime_list = []
        data = self.get_json()
        sites = data['sites']
        for anime in data['items']:
            if not len(anime['begin']):
                continue
            date = {'start': dateutil.parser.parse(anime['begin'])}
            if len(anime['end']):
                date['end'] = dateutil.parser.parse(anime['end'])

            title = anime['title']
            if 'zh-Hans' in anime['titleTranslate']:
                title = anime['titleTranslate']['zh-Hans'][0]
            elif 'zh-Hant' in anime['titleTranslate']:
                title = anime['titleTranslate']['zh-Hant'][0]

            info = ''
            for site in anime['sites']:
                s = sites[site['site']]
                if 'id' in site:
                    url = s["urlTemplate"].replace('{{id}}', site['id'])  # type:str
                    info += f'{s["title"]}:{url} \n'
                if 'begin' in site:
                    date['start'] = dateutil.parser.parse(anime['begin'])
            if len(anime['sites']) <2:
                info = '无时间安排'

            bgm_dict = {
                'uid': f'anime_{anime["id"]}',
                'title': title,
                'datetime': date,
                'info': info,
                'intro': anime['title']
            }
            self.__anime_list.append(bgm_dict)
        return self.__anime_list
