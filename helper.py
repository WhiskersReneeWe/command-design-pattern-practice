#!/usr/bin/env python
# coding: utf-8

import time
from datetime import timezone

import string

def to_UTC_ts(dt):
    '''input - a datetime value
       output - a UTC timestamp'''
    
    utc_time = dt.replace(tzinfo = timezone.utc) 
    utc_timestamp = utc_time.timestamp()
    
    return(utc_timestamp)
    
# dt = data.loc[1, 'date_with_time_dt']
# to_UTC_ts(dt)

def strip_punc(message):
    '''input - a string of any length'''
    
    return message.translate(str.maketrans('', '', string.punctuation))

