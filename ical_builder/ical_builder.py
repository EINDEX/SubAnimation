#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
SubAnimation : Provide an animation ics subscription service
Copyright (C) 2016-2017 EINDEX Li

@Author        : EINDEX Li
@File          : ical_builder.py
@Created       : 2017/3/6
@Last Modified : 2017/3/6
"""
import datetime
from time import localtime

from icalendar import Calendar, Event


def ical_builder(dict_list, tz=datetime.timezone(datetime.timedelta(hours=8))):
    cal = Calendar()
    cal['version'] = '2.0'
    cal['prodid'] = '-//BGM ICS//EINDEX//ZH'
    for dic in dict_list:
        cal.add_component(event_builder(dic, tz))
    return cal


def event_builder(dic, tz):
    start = dic['datetime']['start']
    end = start + datetime.timedelta(seconds=30 * 60)

    if 'end' not in dic['datetime']:
        count = (datetime.datetime.now() - dic['datetime']['start'].replace(tzinfo=None)).days // 7
        count = ((count + 12) // 12) * 12
        print(dic)
    else:
        count = (dic['datetime']['end'] - start).days // 7

    event = Event()
    event.add('SUMMARY', dic['title'])
    event.add('DTSTART', start.astimezone(tz))
    event.add('DTEND', end.astimezone(tz))
    event['description'] = f'{dic["intro"]} \n {dic["info"]}'
    event.add('RRULE',
              {'FREQ': 'WEEKLY',
               'INTERVAL': 1,
               'COUNT': count})
    return event
