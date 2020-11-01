#!/usr/bin/env python
# coding: utf-8

# In[6]:


import pandas as pd
import os
import string
from pathlib import Path

import argparse

# datetime
import time
from datetime import timezone

# import helper package
from helper import to_UTC_ts, strip_punc

if __name__ == '__main__':
    
    # All of parameters are sent as arguments
    # when this script is executed
    
    # create a parse

    parser = argparse.ArgumentParser(description="transform files by type")
    parser.add_argument("--cwd", type=str, help="usually, type in Desktop", default=os.getcwd(), required=False)
    parser.add_argument("--input_csv_path", required=True, type=str, help="please type the absolute path to the csv file")
# default=os.getcwd()
    parser.add_argument("--type", required=True, type=str, help="the type of files to be tranformed, example, posts", default = 'posts')
    parser.add_argument("--output_csv_path", required=True, type=str, help="please type the absolute path to the transformed csv file")
    
    
    # args holds all passed-in arguments
    args = parser.parse_args()
    
    # check if data file exists
    if not '{}/{}.csv'.format(args.cwd, args.type):
        print('File type not found. Please double check and upload one')
       
    # FILE PATH
    INPUT_FILE_PATH = args.input_csv_path
    OUTPUT_FILE_PATH = args.output_csv_path
    
    # read in data
    data = pd.read_csv(INPUT_FILE_PATH, encoding = 'utf8')
    
    
    # convert object column to datetime 
    data['date_with_time_dt'] =  pd.to_datetime(data['date_with_time'], format='%Y-%m-%d %H:%M:%S')
    data.drop('date_with_time', axis=1, inplace=True)
    
    
    # datetime --> UTC timestamp
    data['date_with_time_UTC'] = data['date_with_time_dt'].apply(to_UTC_ts)
    data.drop('date_with_time_dt', axis=1, inplace=True)

    # lowercase USERNAME 
    data["username_lower"] = data["username"].str.lower()
    data.drop('username', axis=1, inplace=True)

    # truncate message column
    data['message'] = data['message'].apply(strip_punc)
    data['message_trunc'] = data['message'].str.slice(0, 100)
    data.drop('message', axis=1, inplace=True)


    # write transformed data to a new csv file
    data.to_csv(OUTPUT_FILE_PATH, index=False, header=True)
    
    print('\n')
    print('Data file transformed!')





