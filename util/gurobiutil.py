#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec  6 12:38:45 2023

@author: hughdeep
"""
import sys
from gurobipy import GRB

def handleGurobiStatus(m):
    '''
    
    Parameters
    ----------
    m : Model
        Gurobi model.

    Returns
    -------
    None.

    '''
    status = m.Status
    print("status", status)
    if status == GRB.UNBOUNDED:
        print('The model cannot be solved because it is unbounded')
        sys.exit(0)
    if status == GRB.INFEASIBLE:
        print('Optimization was stopped with status infeasible')
        sys.exit(0)
        
def setGurobiParams(m, paramsDict):
    m.Params.MIPGap = paramsDict['Gurobi']['MIPGap']
    m.Params.TimeLimit = paramsDict['Gurobi']['TimeLimit']
    m.Params.Threads = paramsDict['Gurobi']['Threads']