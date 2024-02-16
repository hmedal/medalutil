#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec  6 12:38:45 2023

@author: hughdeep
"""
import sys
from gurobipy import GRB

def handleGurobiStatus(m : gp.Model):
    '''
    
    Parameters
    ----------
    m : Model
        Gurobi model.

    Returns
    -------
    None.

    '''

    status = m.status
    if status == GRB.Status.INFEASIBLE:
        print("The model is infeasible. Computing IIS.")
        m.computeIIS()
        m.write('iismodel.ilp')
        sys.exit(0)
    elif status == GRB.Status.UNBOUNDED:
        print("The model is unbounded.")
        sys.exit(0)
    elif status == GRB.Status.OPTIMAL:
        print("The model is optimal.")
    elif status == GRB.Status.INF_OR_UNBD:  
        print("The model status is infeasible or unbounded. Set DualReductions parameter to 0 and reoptimize.")
        sys.exit(0)
    else:
        print("The model status is neither infeasible nor unbounded.")
        sys.exit(0)
        
def setGurobiParams(m, paramsDict):
    m.Params.MIPGap = paramsDict['Gurobi']['MIPGap']
    m.Params.TimeLimit = paramsDict['Gurobi']['TimeLimit']
    m.Params.Threads = paramsDict['Gurobi']['Threads']