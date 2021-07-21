# -*- coding: utf-8 -*-
"""
Created on Tue Jul 20 09:38:12 2021

@author: s21030
"""
import os
import openpyxl
from openpyxl import Workbook
from openpyxl import load_workbook
from openpyxl.utils.dataframe import dataframe_to_rows
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import requests

dfsemirawdata = pd.DataFrame()
finalDF = pd.DataFrame()

#there are nine degree levels in the files we'll be using...
degree_lvls = [1,2,3,4,5,6,7,8,9]

#these are the educational groups defined in the files we'll be using
edu_groups =  {'Total':1,
               'LessThan9th': 2,
                    'SomeHighSchool':3,
                    'HighSchool':4,
                    'SomeCollege':5,
                    'Associates':6,
                    'Bachelors':7,
                    'Masters':8,
                    'Professional':9,
                    'Doctorate':10}

# Create two tuples to contain info about the files we'll be fetching
# tuple format is source file, target file, sex (M/F)
FileTuple1 = ('https://www2.census.gov/programs-surveys/cps/tables/pinc-03/2020/pinc03_2_1_2_1.xlsx',
              'C:\\Users\\s21030\\Desktop\\python stuff\\labor\\data_in\\male_data.xlsx',
              'M' )
FileTuple2 = ('https://www2.census.gov/programs-surveys/cps/tables/pinc-03/2020/pinc03_3_1_2_1.xlsx',
              'C:\\Users\\s21030\\Desktop\\python stuff\\labor\\data_in\\female_data.xlsx',
              'F' )
FileList = (FileTuple1,FileTuple2)

def get_data(flist):
    
    #There are 40 salary ranges in the file, in $2500 increments
    salary_levels = np.arange(start=2500, stop=102501, step=2500)

   
    for fline in flist:
        
        global dfsemirawdata

        r = requests.get(fline[0])
        with open(fline[1], 'wb') as f:
            f.write(r.content)  
            f.close()
        dfxl = pd.read_excel(fline[1], engine="openpyxl")  #don't try to use pyxlsb -- these aren't binary files and it will fail with an inscrutable error
        dfxl = dfxl.drop(range(0,15))   #these rows are superfluous -- they don't have useful data, so drop them
        dfxl = dfxl.drop(range(56,62))  #same as above
        dfxl = dfxl.drop(columns=['Unnamed: 7','Table with row headers in column A and column headers in rows 11 through 13']) #useless columns
        dfxl.columns = edu_groups   #rename columns to our liking
        dfxl['Salary level'] = salary_levels  #this replaces the out of the box labels with the range we built
        dfxl['Sex'] = fline[2]  #assign the value for sex as an element in our df (it's not in the data otherwise)
        dfsemirawdata = dfsemirawdata.append(dfxl,ignore_index=True) #append to the global DF we'll use later
#main

#this function call gets us the raw data
get_data(FileList)

# now we need to transform it to work with our plan to histogram it
# this means modifying it so that each record is (education level | # of peopple | salarly level | sex)
for row in dfsemirawdata.itertuples():
       for key, value in edu_groups.items():       # edu groups are just the columns we want to normalize
            
            print(key, "|", row[value],"|",row[11],"|",row[12])  #columns 11 & 12 are salar level and sex
            newDFRow = {'EduLvl': key, 'NumObs':row[value],'SalaryLvl':row[11], 'Sex':row[12]}
            finalDF = finalDF.append(newDFRow,ignore_index=True)
            # the above append operation is slow, but the dataset is small, so... <shrug>

# now for the graphing
for key, value in edu_groups.items():
    # for clarity, we'll split our main DF into two frames: male and female, and graph them both on the same charts
    dfM = finalDF[(finalDF.Sex=='M')&(finalDF.EduLvl==key)]
    dfF = finalDF[(finalDF.Sex=='F')&(finalDF.EduLvl==key)]
    #ladies first
    plt.hist(dfF['SalaryLvl'],alpha=.5,weights=dfF['NumObs'], histtype='bar', label='F',density=True,color='green',edgecolor='black')
    #then the dudes
    plt.hist(dfM['SalaryLvl'],alpha=.5,weights=dfM['NumObs'], histtype='bar', label='M',density=True,color='blue',edgecolor='black')
    # formatting
    plt.xlabel('salary')
    plt.ylabel('frequency')
    plt.legend(loc='upper left')
    plt.xlim(0,120000)
    plt.title(key)
    # do it
    plt.show()














