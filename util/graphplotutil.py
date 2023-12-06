#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 31 17:50:36 2023

@author: hughdeep
"""

from matplotlib import pyplot as plt
import matplotlib as mpl
import networkx as nx
    
def getShapeAndYOff(unitType, isAttack):
    if unitType == 'g':
        return "s", 0
    elif unitType == 'aa':
        return "v", 0.2
    elif unitType == 'ad':
        return "o", -0.2
    elif unitType == 's':
        return "s", 0
    elif unitType == 'm':
        return "v", 0.0
    elif unitType == 'l':
        return "o", 0.0
    
def drawGraphWithUnitsAndInterdict(flowG, blueUnits, redUnits, blueNodes = [], redInterdict = {}, blueInterdict = [], blueMove = [], includeRadius = True, fileName = 'graph.jpg'):
    pos = nx.get_node_attributes(flowG, 'pos')
    #edge_labels = nx.get_edge_attributes(flowG,'capacity')
    nrows = flowG.graph['nrows']
    ncols = flowG.graph['ncols']
    plt.figure(figsize=(ncols*2, nrows*2 - 2))
    nx.draw_networkx_edges(flowG, pos, width=1.0, alpha=0.8, style="dashed", arrows = False)
    node_colors = ["white" for i in flowG.nodes()]
    #node_colors[1] = "blue"
    for i in blueNodes:
        node_colors[i+1] = "blue"
    options = {"edgecolors": "tab:gray", "node_size": 300, "alpha": 0.7}
    nodes = nx.draw_networkx_nodes(flowG, pos, node_color = node_colors, **options)
    nx.draw_networkx_labels(flowG, pos,font_color = "black")
    spacing = 0.12
    mult = 5
    multspacing = 0.015
    aasize = 350
    adsize = 175
    for j in redUnits:
        shape, yoff = getShapeAndYOff(j, True)
        for i in redUnits[j]:
            if redUnits[j][i] > 0:
                numUnits = redUnits[j][i]
                offset = spacing + numUnits*multspacing
                plt.plot(pos[i][0] - offset, pos[i][1] + yoff, marker = shape, c = 'r', linestyle = '', markersize = numUnits*mult)
                if j == 'aa' and includeRadius:
                    plt.plot(pos[i][0], pos[i][1], marker = 'o', c = 'r', alpha = 0.2, linestyle = '', markersize = aasize)
                elif j == 'ad' and includeRadius:
                    plt.plot(pos[i][0], pos[i][1], marker = 'o', c = 'r', alpha = 0.2, linestyle = '', markersize = adsize)
    for j in blueUnits:
        shape, yoff = getShapeAndYOff(j, True)
        for i in blueUnits[j]:
            if blueUnits[j][i] > 0:
                numUnits = blueUnits[j][i]
                offset = spacing + numUnits*multspacing
                plt.plot(pos[i][0] + offset, pos[i][1] + yoff, marker = shape, c = 'b', linestyle = '', markersize = numUnits*mult)
                if j == 'aa' and includeRadius:
                    plt.plot(pos[i][0], pos[i][1], marker = 'o', c = 'b', alpha = 0.2, linestyle = '', markersize = aasize)
                elif j == 'ad' and includeRadius:
                    plt.plot(pos[i][0], pos[i][1], marker = 'o', c = 'b', alpha = 0.2, linestyle = '', markersize = adsize)
    for i in redInterdict:
        e = redInterdict[i]
        x = 0.5*pos[e[0]][0] + 0.5*pos[e[1]][0]
        y = 0.5*pos[e[0]][1] + 0.5*pos[e[1]][1]
        plt.plot(x, y, marker = "x", c = 'r', linestyle = '', markersize = 10, markeredgewidth = 3)
        plt.annotate("",
        xy=(x, y), xycoords='data',
        xytext=(pos[i][0], pos[i][1]), textcoords='data',
        arrowprops=dict(arrowstyle="->", color="r",
                        shrinkA=5, shrinkB=5,
                        patchA=None, patchB=None,
                        connectionstyle="angle3,angleA=90,angleB=0",
                        ),
        )
    for i in blueInterdict:
        j = blueInterdict[i]
        plt.plot(pos[j][0] + spacing, pos[j][1], marker = "x", c = 'b', linestyle = '', markersize = 10, markeredgewidth = 3)
        plt.annotate("",
        xy=(pos[j][0] + spacing, pos[j][1]), xycoords='data',
        xytext=(pos[i][0], pos[i][1]), textcoords='data',
        arrowprops=dict(arrowstyle="->", color="b",
                        shrinkA=5, shrinkB=5,
                        patchA=None, patchB=None,
                        connectionstyle="angle3,angleA=90,angleB=0",
                        ),
        )
    for e in flowG.edges():
        widthVal = 3
        if e in blueMove:
            nx.draw_networkx_edges(
                flowG,
                pos,
                edgelist=[e],
                width=widthVal,
                edge_color="tab:blue",
                arrows = True,
            )
                
    plt.axis('off')
    plt.savefig(fileName, format="JPG")
    plt.show()
    
def drawGraphWithUnitsAndSupply(flowG, blueUnits, redUnits, blueNodes = [], redSupply = [], blueSupply = []):
    pos = nx.get_node_attributes(flowG, 'pos')
    #edge_labels = nx.get_edge_attributes(flowG,'capacity')
    nrows = flowG.graph['nrows']
    ncols = flowG.graph['ncols']
    plt.figure(figsize=(ncols*2, nrows*2))
    nx.draw_networkx_edges(flowG, pos, width=1.0, alpha=0.8, style="dashed", arrows = False)
    node_colors = ["white" for i in flowG.nodes()]
    node_colors[1] = "blue"
    for i in blueNodes:
        node_colors[i+1] = "blue"
    
    options = {"edgecolors": "tab:gray", "node_size": 300, "alpha": 0.7}
    nodes = nx.draw_networkx_nodes(flowG, pos, node_color = node_colors, **options)
    #nodes.set_edgecolor('black')
    nx.draw_networkx_labels(flowG, pos,font_color = "black")
    offset = 0.3
    mult = 6
    for i in redUnits:
        plt.plot(pos[i][0] - offset, pos[i][1], marker = "s", c = 'r', linestyle = '', markersize = redUnits[i]*mult)
    for i in blueUnits:
        plt.plot(pos[i][0] + offset, pos[i][1], marker = "s", c = 'b', linestyle = '', markersize = blueUnits[i]*mult)
    for e in flowG.edges():
        widthVal = 3
        if e in redSupply or e in blueSupply:
            if e in redSupply:
                nx.draw_networkx_edges(
                    flowG,
                    pos,
                    edgelist=[e],
                    width=widthVal,
                    edge_color="tab:red",
                    arrows = False,
                )
            if e in blueSupply:
                nx.draw_networkx_edges(
                    flowG,
                    pos,
                    edgelist=[e],
                    width=widthVal,
                    edge_color="tab:blue",
                    arrows = False,
                )
    plt.axis('off')
    plt.savefig("graph.jpg", format="JPG")
    plt.show()
    
def drawGraph(flowG, name, show = False):
    pos = nx.get_node_attributes(flowG, 'pos')
    edge_labels = nx.get_edge_attributes(flowG,'capacity')
    nrows = flowG.graph['nrows']
    ncols = flowG.graph['ncols']
    plt.figure(figsize=(ncols*2, nrows*2))
    nx.draw_networkx(flowG, pos)
    nx.draw_networkx_edge_labels(flowG,pos, edge_labels, label_pos=0.33)
    plt.axis('off')
    plt.savefig(name + ".jpg", format="JPG")
    if show:
        plt.show()

def drawFlows(flowG, f):
    nrows = flowG.graph['nrows']
    ncols = flowG.graph['ncols']
    pos = nx.get_node_attributes(flowG, 'pos')
    edge_labels = nx.get_edge_attributes(flowG,'capacity')
    plt.figure(figsize=(ncols*2 + 5, nrows*2))
    nx.draw_networkx_nodes(flowG, pos)
    node_labels = nx.get_node_attributes(flowG, 'nlabel')
    nx.draw_networkx_labels(flowG, pos)
    nx.draw_networkx_edges(flowG, pos, width=1.0, alpha=0.8)
    flow_dict = f.getLastFlowDict()
    edge_labels2 = {}
    for e in flowG.edges():
        flow = 0
        if e[1] in flow_dict[e[0]]:
            flow = flow_dict[e[0]][e[1]]
        edge_labels2[e] = str(flow) + "/" + str(edge_labels[e])
        if flow > 0:
            widthVal = 5 + flow
            nx.draw_networkx_edges(
                flowG,
                pos,
                edgelist=[e],
                width=widthVal,
                alpha=0.5,
                edge_color="tab:gray",
            )
    nx.draw_networkx_edge_labels(flowG,pos,edge_labels2, label_pos=0.35)
    plt.axis('off')
    plt.savefig("graphWithFlow.jpg", format="JPG")
    plt.show()

def drawGraphWithInterdict(flowG, flowMod, interdictions, graphName):
    nrows = flowG.graph['nrows']
    ncols = flowG.graph['ncols']
    pos = nx.get_node_attributes(flowG, 'pos')
    edge_labels = nx.get_edge_attributes(flowG,'capacity')
    plt.figure(figsize=(ncols*2 + 3, nrows*2))
    nx.draw_networkx_nodes(flowG, pos)
    node_labels = nx.get_node_attributes(flowG, 'nlabel')
    nx.draw_networkx_edges(flowG, pos, width=1.0, alpha=0.8)
    nx.draw_networkx_labels(flowG, pos)
    #nx.draw_networkx_edges(flowG, pos, width=1.0, alpha=0.8)
    interdictionIndices = [list(flowG.edges()).index((i,j)) for (i,j) in interdictions]
    print("interdictionIndices", interdictionIndices)
    flowVal = flowMod.getF(interdictionIndices)
    print("flowVal", flowVal)
    flow_dict = flowMod.getLastFlowDict()
    edge_labels2 = {}
    for e in flowG.edges():
        flow = 0
        if e[1] in flow_dict[e[0]]:
            flow = flow_dict[e[0]][e[1]]
        edge_labels2[e] = str(flow) + "/" + str(edge_labels[e])
        if e not in interdictions:
            if flow > 0:
                widthVal = 5 + flow
                nx.draw_networkx_edges(
                    flowG,
                    pos,
                    edgelist=[e],
                    width=widthVal,
                    alpha=0.5,
                    edge_color="tab:gray",
                )
        else:
            nx.draw_networkx_edges(
                flowG,
                pos,
                edgelist=[e],
                width=5,
                alpha=0.5,
                edge_color="tab:red",
            )
    nx.draw_networkx_edge_labels(flowG,pos,edge_labels2,label_pos=0.35)
    plt.axis('off')
    plt.savefig(graphName + "-WithInterdictAndFlow.jpg", format="JPG")
    plt.show()
    
def plotDefenseAndAttack(flowG, flowMod, defense1, attack1, defense2, attack2, figName = "graphWithDefenseAndAttack", showFlow = True):
    nrows = flowG.graph['nrows']
    ncols = flowG.graph['ncols']
    pos = nx.get_node_attributes(flowG, 'pos')
    edge_labels = nx.get_edge_attributes(flowG,'capacity')
    plt.figure(figsize=(ncols*2 + 3, nrows*2))
    nx.draw_networkx_nodes(flowG, pos)
    node_labels = nx.get_node_attributes(flowG, 'nlabel')
    nx.draw_networkx_edges(flowG, pos, width=1.0, alpha=0.8)
    nx.draw_networkx_labels(flowG, pos)
    #nx.draw_networkx_edges(flowG, pos, width=1.0, alpha=0.8)
    destructionState = set(attack1).union(set(attack2))
    interdictionIndices = [list(flowG.edges()).index((i,j)) for (i,j) in destructionState]
    #print("interdictions", interdictions)
    #print("interdictionIndices", interdictionIndices)
    if showFlow:
        flowVal = flowMod.getF(interdictionIndices)
        print("flowVal", flowVal)
        flow_dict = flowMod.getLastFlowDict()
        #print("flow_dict", flow_dict)
    edge_labels2 = {}
    for e in flowG.edges():
        if showFlow:
            flow = 0
            if e[1] in flow_dict[e[0]]:
                flow = flow_dict[e[0]][e[1]]
            edge_labels2[e] = str(flow) + "/" + str(edge_labels[e])
            widthVal = 1 + 2*flow
        else:
            edge_labels2[e] = edge_labels[e]
            widthVal = 1
        if e in attack1 or e in attack2 or e in defense1 or e in defense2:
            if e in attack1:
                nx.draw_networkx_edges(
                    flowG,
                    pos,
                    edgelist=[e],
                    width=widthVal + 5,
                    alpha=0.4,
                    edge_color="tab:red",
                )
            if e in attack2:
                nx.draw_networkx_edges(
                    flowG,
                    pos,
                    edgelist=[e],
                    width=widthVal + 5,
                    alpha=0.4,
                    edge_color="tab:red",
                )
            if e in defense1:
                nx.draw_networkx_edges(
                    flowG,
                    pos,
                    edgelist=[e],
                    width=widthVal + 5,
                    alpha=0.4,
                    edge_color="tab:blue",
                )
            if e in defense2:
                nx.draw_networkx_edges(
                    flowG,
                    pos,
                    edgelist=[e],
                    width=widthVal + 5,
                    alpha=0.4,
                    edge_color="tab:blue",
                )
        else:
            if showFlow:
                nx.draw_networkx_edges(
                    flowG,
                    pos,
                    edgelist=[e],
                    width=widthVal,
                    alpha=0.4,
                    edge_color="tab:gray",
                )
        
    nx.draw_networkx_edge_labels(flowG,pos,edge_labels2, label_pos=0.35)
    plt.axis('off')
    plt.savefig(figName + ".jpg", format="JPG")
    plt.show()

def plotDefenseAndAttackAmounts(flowG, defense, attack, 
                                defenseBudget, attackBudget, 
                                filename = 'graph.jpg', 
                                show = False):
    nrows = flowG.graph['nrows']
    ncols = flowG.graph['ncols']
    pos = nx.get_node_attributes(flowG, 'pos')
    edge_labels = nx.get_edge_attributes(flowG,'capacity')
    plt.figure(figsize=(ncols*2 + 3, nrows*1.5))
    nx.draw_networkx_nodes(flowG, pos, node_color = "black")
    #node_labels = nx.get_node_attributes(flowG, 'nlabel')
    nx.draw_networkx_edges(flowG, pos, width=1.0, alpha=0.8)
    nx.draw_networkx_labels(flowG, pos,font_color = "white")
    edge_labels2 = {}
    for e in flowG.edges():
        edge_labels2[e] = edge_labels[e]
        #widthVal = 1
            
        if e in attack:
            nx.draw_networkx_edges(
                flowG,
                pos,
                edgelist=[e],
                width=attack[e]*5,
                alpha=0.4,
                edge_color="tab:red",
            )
        if e in defense:
            nx.draw_networkx_edges(
                flowG,
                pos,
                edgelist=[e],
                width=defense[e]*5,
                alpha= 0.4,
                edge_color="tab:blue",
            )
        
    nx.draw_networkx_edge_labels(flowG,pos,edge_labels2, label_pos=0.35)
    plt.axis('off')
    plt.savefig(filename, format="JPG")
    if show:
        plt.show()
        
def plotDefenseAndAttackAmountsMultistage(flowG, defense1, attack1, defense2, attack2, 
                                defenseBudget, attackBudget, graphName = '', 
                                note = '', show = False, showFlow = False):
    nrows = flowG.graph['nrows']
    ncols = flowG.graph['ncols']
    pos = nx.get_node_attributes(flowG, 'pos')
    edge_labels = nx.get_edge_attributes(flowG,'capacity')
    plt.figure(figsize=(ncols*2 + 3, nrows*1.5))
    nx.draw_networkx_nodes(flowG, pos, node_color = "black")
    #node_labels = nx.get_node_attributes(flowG, 'nlabel')
    nx.draw_networkx_edges(flowG, pos, width=1.0, alpha=0.8)
    nx.draw_networkx_labels(flowG, pos,font_color = "white")
    edge_labels2 = {}
    for e in flowG.edges():
        if showFlow:
            flow = 0
            # if e[1] in flow_dict[e[0]]:
            #     flow = flow_dict[e[0]][e[1]]
            edge_labels2[e] = str(flow) + "/" + str(edge_labels[e])
            widthVal = 1 + 2*flow
        else:
            edge_labels2[e] = edge_labels[e]
            widthVal = 1
        if e in attack1 or e in attack2 or e in defense1 or e in defense2:
            
            if e in attack1:
                nx.draw_networkx_edges(
                    flowG,
                    pos,
                    edgelist=[e],
                    width=attack1[e]*5,
                    alpha=0.4,
                    edge_color="tab:red",
                )
            if e in attack2:
                nx.draw_networkx_edges(
                    flowG,
                    pos,
                    edgelist=[e],
                    width=attack2[e]*5,
                    alpha=0.4,
                    edge_color="tab:red",
                )
            if e in defense1:
                nx.draw_networkx_edges(
                    flowG,
                    pos,
                    edgelist=[e],
                    width=defense1[e]*5,
                    alpha= 0.4,
                    edge_color="tab:blue",
                )
                
            if e in defense2:
                nx.draw_networkx_edges(
                    flowG,
                    pos,
                    edgelist=[e],
                    width=defense2[e]*5,
                    alpha=0.4,
                    edge_color="tab:blue",
                )
        else:
            if showFlow:
                nx.draw_networkx_edges(
                    flowG,
                    pos,
                    edgelist=[e],
                    width=widthVal,
                    alpha=0.4,
                    edge_color="tab:gray",
                )
        
    nx.draw_networkx_edge_labels(flowG,pos,edge_labels2, label_pos=0.35)
    plt.axis('off')
    plt.savefig(graphName + "-" + note + "-withDefenseAndAttackAmounts.jpg", format="JPG")
    if show:
        plt.show()
    
def plotAttacks(flowG, flowMod, interdictions, figName = "graphWithAttacks", showFlow = True):
    return plotDefenseAndAttack(flowG, flowMod, interdictions, [], figName, showFlow)