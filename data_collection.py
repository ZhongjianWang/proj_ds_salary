#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug 26 14:45:40 2020

@author: jason
"""
import glassdoor_scraper as gs
import pandas as pd 
path = '/Users/jason/Python/proj_ds_salary/chromedriver'



df = gs.get_jobs('data scientist', 800, False, path, 30 )