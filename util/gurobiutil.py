#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec  6 12:38:45 2023

@author: hughdeep
"""

def setGurobiParams(m, paramsDict):
    m.Params.MIPGap = paramsDict['Gurobi']['MIPGap']
    m.Params.TimeLimit = paramsDict['Gurobi']['TimeLimit']
    m.Params.Threads = paramsDict['Gurobi']['Threads']