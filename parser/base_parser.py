#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
SubAnimation : Provide an animation ics subscription service
Copyright (C) 2016-2017 EINDEX Li

@Author        : EINDEX Li
@File          : base_parser.py
@Created       : 2017/3/6
@Last Modified : 2017/3/6
"""
import requests


class BaseParser(object):
    """
    将无序的数据格式化为 iCal 支持的规范格式，方便批量转换。
    """

    def __init__(self, url):
        """

        :param url:  请求的 url
        """
        self.__url = url
        self.__anime_list = None
        self.__session = requests.session()

    def get_json(self):
        data = self.__session.get(self.__url)
        if data.ok:
            data.encoding = 'utf-8'
            return data.json()

    def parsing(self):
        """
        setting the __animes value.
        """
        raise NotImplementedError

    # @property
    def anime_list(self):
        if self.__anime_list is None:
           self.__anime_list = self.parsing()
        return self.__anime_list
