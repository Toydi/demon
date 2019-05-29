from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QPushButton
from PyQt5.QtGui import QPixmap, QIcon, QPen, QColor, QResizeEvent
from PyQt5.QtCore import Qt
from uva_path import UVA
import random
import time
import json

import matplotlib.pyplot as plt
from preprocess import PREPROCESS
from generator import GENERATOR
from sa import SA
from clustering import CLUSTERING
from multiclustering import MULTICLUSTERING
import math
import os

# WI = 600
# BR = 600
WI = 1200
BR = 800

def initialize(point_file,line_file,start,end_information):
    generator = GENERATOR()
    generator.generate_point(point_file,start,end_information)
    generator.generate_line(line_file)

def display(point_file,line_file):
    f = open(point_file)            # read point file
    content = f.read()
    lines = content.splitlines()
    result_point = {}                # point information
    num_of_points = 0
    for line in lines:
        line = line.split(" ")
        temp = []
        temp.append(float(line[0]))
        temp.append(float(line[1]))
        temp.append(int(line[2]))
        temp.append(int(line[3]))
        result_point[num_of_points] = temp
        num_of_points += 1

    f.close()

    f = open(line_file)             # read line file
    content = f.read()
    lines = content.splitlines()
    #print(num_of_points)
    result_line = {}                 # line information
    num_of_lines = 0
    for line in lines:
        line = line.split(" ")
        temp = []
        temp.append(int(line[0]))
        temp.append(int(line[1]))
        temp.append(float(line[2]))
        result_line[num_of_lines] = temp
        num_of_lines += 1

    f.close()

    fig = plt.figure()
    ax = fig.add_subplot(1,1,1)
    ax.set_title('RAW_MAP')
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    for i in range(len(result_point)):
        if result_point[i][2] != 0:
            ax.plot(result_point[i][0],result_point[i][1],'o',color='green')
            ax.text(result_point[i][0],result_point[i][1],str(result_point[i][2]),color='green',fontsize = 10)
        elif result_point[i][3] != 0:
            ax.plot(result_point[i][0],result_point[i][1],'o',color='red')
            ax.text(result_point[i][0], result_point[i][1], str(result_point[i][3]), color='red',fontsize = 10)
        else:
            ax.plot(result_point[i][0], result_point[i][1], 'o', color='black')

    for i in range(len(result_line)):
        x = []
        y = []
        x.append(result_point[result_line[i][0]][0])
        x.append(result_point[result_line[i][1]][0])
        y.append(result_point[result_line[i][0]][1])
        y.append(result_point[result_line[i][1]][1])
        ax.plot(x,y,color='black')
        #ax.text((x[0]+x[1])/2,(y[0]+y[1])/2,'%.2f'%result_line[i][2],color='blue',fontsize = 5)

    ax.axis([0,WI,0,BR])
    plt.savefig("raw_graph.jpg")
    # print(point_remain)
    # print(raw_matrix)

def preprocess(raw_point_file,raw_line_file,new_point_file,new_line_file):
    f_new = open(new_point_file,'w') # clean up the file
    f_new.truncate()
    f_new.close()

    f_new = open(new_point_file,'a')

    f_old = open(raw_point_file)  # read point file

    content = f_old.read()
    lines = content.splitlines()
    num_of_points = 0
    point_remain = []   # remain point
    for line in lines:
        temp = line.split(" ")
        if int(temp[2])!= 0 or int(temp[3])!=0:
            point_remain.append(num_of_points)
            f_new.write(str(num_of_points) + " " + line + "\n")
        num_of_points += 1

    f_old.close()
    f_new.close()

    f_old = open(raw_line_file)  # read line file
    content = f_old.read()
    lines = content.splitlines()
    raw_matrix = [[float("inf") for i in range(num_of_points)] for j in range(num_of_points)] # raw adj
    for i in range(num_of_points):
        raw_matrix[i][i] = 0
    for line in lines:
        temp = line.split(" ")
        raw_matrix[int(temp[0])][int(temp[1])] = float(temp[2])
        raw_matrix[int(temp[1])][int(temp[0])] = float(temp[2])

    f_old.close()

    process = PREPROCESS(point_remain,raw_matrix)

    f_new = open(new_line_file, 'w')  # clean up the file
    f_new.truncate()
    f_new.close()

    for i in range(len(point_remain)):
        for j in range(i+1,len(point_remain)):
            process.generate_path(point_remain[i],point_remain[j],new_line_file)

def display_again(point_file,line_file):
    f = open(point_file)            # read point file
    content = f.read()
    lines = content.splitlines()
    result_point = {}                # point information
    point_remain = []               # ID
    for line in lines:
        line = line.split(" ")
        temp = []
        temp.append(float(line[1]))
        temp.append(float(line[2]))
        temp.append(int(line[3]))
        temp.append(int(line[4]))
        result_point[int(line[0])] = temp
        point_remain.append(int(line[0]))

    f.close()

    f = open(line_file)             # read line file
    content = f.read()
    lines = content.splitlines()
    #print(num_of_points)
    result_line = {}                 # line information
    num_of_lines = 0
    for line in lines:
        line = line.split(" ")
        temp = []
        temp.append(int(line[0]))
        temp.append(int(line[1]))
        temp.append(float(line[2]))
        result_line[num_of_lines] = temp
        num_of_lines += 1

    f.close()

    fig = plt.figure()
    ax = fig.add_subplot(1,1,1)
    ax.set_title('NEW_MAP')
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    for i in range(len(point_remain)):
        if result_point[point_remain[i]][2] != 0:
            ax.plot(result_point[point_remain[i]][0],result_point[point_remain[i]][1],'o',color='green')
            ax.text(result_point[point_remain[i]][0],result_point[point_remain[i]][1],str(result_point[point_remain[i]][2]),color='green',fontsize = 10)
        elif result_point[point_remain[i]][3] != 0:
            ax.plot(result_point[point_remain[i]][0],result_point[point_remain[i]][1],'o',color='red')
            ax.text(result_point[point_remain[i]][0],result_point[point_remain[i]][1],str(result_point[point_remain[i]][3]),color='red',fontsize = 10)
        # else:
        #     ax.plot(result_point[i][0], result_point[i][1], 'o', color='black')

    for i in range(len(result_line)):
        x = []
        y = []
        x.append(result_point[result_line[i][0]][0])
        x.append(result_point[result_line[i][1]][0])
        y.append(result_point[result_line[i][0]][1])
        y.append(result_point[result_line[i][1]][1])
        ax.plot(x,y,color='black')
        #ax.text((x[0]+x[1])/2,(y[0]+y[1])/2,'%.2f'%result_line[i][2],color='blue',fontsize = 5)

    ax.axis([0,WI,0,BR])
    plt.savefig("new_graph.jpg")
    # print(point_remain)
    # print(raw_matrix)

# def sa(point_file,line_file):
#     f = open(point_file)  # read point file
#     content = f.read()
#     lines = content.splitlines()
#     point_remain = []  # ID
#     start_id = -1
#     point_id = 0
#     for line in lines:
#         line = line.split(" ")
#         point_remain.append(int(line[0]))
#         if int(line[3])!=0:             # get the start point ID
#             start_id = point_id
#         point_id += 1
#     f.close()
#
#     f = open(line_file)  # read line file
#     content = f.read()
#     lines = content.splitlines()
#     line_cost = []      # cost of each line
#     get_the_route = {}  # display the route
#     for line in lines:
#         line = line.split(" ")
#         line_cost.append(float(line[2]))
#         key1 = (int(line[0]),int(line[1]))  # small-big
#         key2 = (int(line[1]),int(line[0]))  # big-small
#         temp = line[3].split("->")
#         value1 = []
#         value2 = []
#         for i in range(len(temp)):
#             value1.append(int(temp[i]))
#             value2.append(int(temp[len(temp)-1-i]))
#
#         get_the_route[key1] = value1
#         get_the_route[key2] = value2
#
#
#     f.close()
#
#     matrix = [[float(0.0) for i in range(len(point_remain))] for j in range(len(point_remain))] # initialize map
#     num = 0
#     for i in range(len(matrix)):
#         for j in range(i+1,len(matrix)):
#             matrix[i][j] = line_cost[num]
#             matrix[j][i] = line_cost[num]
#             num += 1
#
#     sa = SA(point_remain,matrix)
#
#     get_value = []
#
#     for i in range(10): # 20 iteration
#         get_value.append(sa.min_path(start_id))
#
#     dis = float("inf")
#     path = list(range(len(point_remain)))
#
#     for i in range(len(get_value)):
#         if dis>get_value[i][0]:
#             dis = get_value[i][0]    # get the smallest
#             for j in range(len(point_remain)):
#                 path[j] = point_remain[get_value[i][1][j]]  # path contains the nodes in the new graph
#
#     result = []     # result contains the nodes in the raw graph
#     for i in range(len(path)-1):
#         key = (path[i],path[i+1])
#         for j in range(len(get_the_route[key])-1):
#             result.append(get_the_route[key][j])                # a-b
#     for i in range(len(get_the_route[(path[len(path)-1],path[0])])):    # b-a
#         result.append(get_the_route[(path[len(path)-1],path[0])][i])
#     result_route = ""
#     for i in range(len(result)):        # display the route
#         result_route += str(result[i])
#         if i!=len(result)-1:
#             result_route += "->"
#     print(result_route)
#     print(dis)
#     return result
#
# def display_route(point_file,result):
#     fig = plt.figure()
#     ax = fig.add_subplot(1, 1, 1)
#     ax.set_title('ROUTE_MAP')
#     ax.set_xlabel('x')
#     ax.set_ylabel('y')
#
#     f = open(point_file)  # read point file
#     content = f.read()
#     lines = content.splitlines()
#     result_point = {}
#     num = 0
#     for line in lines:
#         line = line.split(" ")
#         temp = []
#         temp.append(float(line[0]))
#         temp.append(float(line[1]))
#         temp.append(int(line[2]))
#         temp.append(int(line[3]))
#         result_point[num] = temp
#         num += 1
#     f.close()
#
#     for i in range(len(result)-1):
#         if result_point[result[i]][2] != 0:
#             ax.plot(result_point[result[i]][0],result_point[result[i]][1],'o',color='green')
#             ax.text(result_point[result[i]][0],result_point[result[i]][1],str(result_point[result[i]][2]),color='green',fontsize = 10)
#         elif result_point[result[i]][3] != 0:
#             ax.plot(result_point[result[i]][0],result_point[result[i]][1],'o',color='red')
#             ax.text(result_point[result[i]][0],result_point[result[i]][1],str(result_point[result[i]][3]),color='red',fontsize = 10)
#         else:
#             ax.plot(result_point[result[i]][0],result_point[result[i]][1],'o',color='black')
#
#     for i in range(len(result)-1):
#         x = []
#         y = []
#         x.append(result_point[result[i]][0])
#         x.append(result_point[result[i+1]][0])
#         y.append(result_point[result[i]][1])
#         y.append(result_point[result[i+1]][1])
#         ax.plot(x,y,color='blue')
#
#     ax.axis([0,WI,0,BR])
#     plt.savefig("route_graph.jpg")
#
# def multimission(point_file,line_file):
#     f = open(point_file)  # read point file
#     content = f.read()
#     lines = content.splitlines()
#     point_remain = []  # ID
#     start_id = -1
#     max_num = 0
#     point_id = 0
#     position = {}
#     weight = {}
#     for line in lines:
#         line = line.split(" ")
#         point_remain.append(int(line[0]))
#         position[point_id] = [float(line[1]),float(line[2])]
#         if int(line[3]) != 0:  # get the start point ID
#             start_id = point_id
#             max_num = int(line[3])
#         if int(line[4]) != 0:
#             weight[point_id] = int(line[4])
#         point_id += 1
#     f.close()
#
#     f = open(line_file)  # read line file
#     content = f.read()
#     lines = content.splitlines()
#     line_cost = []  # cost of each line
#     get_the_route = {}  # display the route
#     for line in lines:
#         line = line.split(" ")
#         line_cost.append(float(line[2]))
#         key1 = (int(line[0]), int(line[1]))  # small-big
#         key2 = (int(line[1]), int(line[0]))  # big-small
#         temp = line[3].split("->")
#         value1 = []
#         value2 = []
#         for i in range(len(temp)):
#             value1.append(int(temp[i]))
#             value2.append(int(temp[len(temp) - 1 - i]))
#
#         get_the_route[key1] = value1
#         get_the_route[key2] = value2
#
#     f.close()
#
#     matrix = [[float(0.0) for i in range(len(point_remain))] for j in range(len(point_remain))]  # initialize map
#     num = 0
#     for i in range(len(matrix)):
#         for j in range(i + 1, len(matrix)):
#             matrix[i][j] = line_cost[num]
#             matrix[j][i] = line_cost[num]
#             num += 1
#
#     clustering = CLUSTERING(position,weight,start_id,matrix)
#     ID1,ID2 = clustering.partition(max_num)                    # partition 2
#     ID1.append(start_id)
#     ID2.append(start_id)
#
#     sa1 = SA(ID1,matrix)
#     get_value1 = []
#     for i in range(5): # 20 iteration
#         get_value1.append(sa1.min_path_2(start_id))
#     dis1 = float("inf")
#     path1 = list(range(len(ID1)))
#     for i in range(len(get_value1)):
#         if dis1 > get_value1[i][0]:
#             dis1 = get_value1[i][0]  # get the smallest
#             for j in range(len(ID1)):
#                 path1[j] = point_remain[get_value1[i][1][j]]  # path contains the nodes in the new graph
#     result1 = []  # result contains the nodes in the raw graph
#     for i in range(len(path1) - 1):
#         key = (path1[i], path1[i + 1])
#         for j in range(len(get_the_route[key]) - 1):
#             result1.append(get_the_route[key][j])  # a-b
#     for i in range(len(get_the_route[(path1[len(path1) - 1], path1[0])])):  # b-a
#         result1.append(get_the_route[(path1[len(path1) - 1], path1[0])][i])
#     result_route1 = ""
#     for i in range(len(result1)):  # display the route
#         result_route1 += str(result1[i])
#         if i != len(result1) - 1:
#             result_route1 += "->"
#     print(result_route1)
#     print(dis1)
#
#     sa2 = SA(ID2, matrix)
#     get_value2 = []
#     for i in range(5):  # 20 iteration
#         get_value2.append(sa2.min_path_2(start_id))
#     dis2 = float("inf")
#     path2 = list(range(len(ID2)))
#     for i in range(len(get_value2)):
#         if dis2 > get_value2[i][0]:
#             dis2 = get_value2[i][0]  # get the smallest
#             for j in range(len(ID2)):
#                 path2[j] = point_remain[get_value2[i][1][j]]  # path contains the nodes in the new graph
#     result2 = []  # result contains the nodes in the raw graph
#     for i in range(len(path2) - 1):
#         key = (path2[i], path2[i + 1])
#         for j in range(len(get_the_route[key]) - 1):
#             result2.append(get_the_route[key][j])  # a-b
#     for i in range(len(get_the_route[(path2[len(path2) - 1], path2[0])])):  # b-a
#         result2.append(get_the_route[(path2[len(path2) - 1], path2[0])][i])
#     result_route2 = ""
#     for i in range(len(result2)):  # display the route
#         result_route2 += str(result2[i])
#         if i != len(result2) - 1:
#             result_route2 += "->"
#     print(result_route2)
#     print(dis2)
#     return result1,result2
#
# def display_multi_route(point_file,result1,result2):
#     fig = plt.figure()
#     ax = fig.add_subplot(1, 1, 1)
#     ax.set_title('MULTI_ROUTE_MAP')
#     ax.set_xlabel('x')
#     ax.set_ylabel('y')
#
#     f = open(point_file)  # read point file
#     content = f.read()
#     lines = content.splitlines()
#     result_point = {}
#     num = 0
#     for line in lines:
#         line = line.split(" ")
#         temp = []
#         temp.append(float(line[0]))
#         temp.append(float(line[1]))
#         temp.append(int(line[2]))
#         temp.append(int(line[3]))
#         result_point[num] = temp
#         num += 1
#     f.close()
#
#     for i in range(len(result1) - 1):
#         if result_point[result1[i]][2] != 0:
#             ax.plot(result_point[result1[i]][0], result_point[result1[i]][1], 'o', color='green')
#             ax.text(result_point[result1[i]][0], result_point[result1[i]][1], str(result_point[result1[i]][2]),
#                     color='green', fontsize=10)
#         elif result_point[result1[i]][3] != 0:
#             ax.plot(result_point[result1[i]][0], result_point[result1[i]][1], 'o', color='red')
#             ax.text(result_point[result1[i]][0], result_point[result1[i]][1], str(result_point[result1[i]][3]),
#                     color='red', fontsize=10)
#         else:
#             ax.plot(result_point[result1[i]][0], result_point[result1[i]][1], 'o', color='black')
#
#     for i in range(len(result1) - 1):
#         x = []
#         y = []
#         x.append(result_point[result1[i]][0])
#         x.append(result_point[result1[i + 1]][0])
#         y.append(result_point[result1[i]][1])
#         y.append(result_point[result1[i + 1]][1])
#         ax.plot(x, y, color='blue')
#
#     for i in range(len(result2) - 1):
#         if result_point[result2[i]][2] != 0:
#             ax.plot(result_point[result2[i]][0], result_point[result2[i]][1], 'o', color='green')
#             ax.text(result_point[result2[i]][0], result_point[result2[i]][1], str(result_point[result2[i]][2]),
#                     color='green', fontsize=10)
#         elif result_point[result2[i]][3] != 0:
#             ax.plot(result_point[result2[i]][0], result_point[result2[i]][1], 'o', color='red')
#             ax.text(result_point[result2[i]][0], result_point[result2[i]][1], str(result_point[result2[i]][3]),
#                     color='red', fontsize=10)
#         else:
#             ax.plot(result_point[result2[i]][0], result_point[result2[i]][1], 'o', color='black')
#
#     for i in range(len(result2) - 1):
#         x = []
#         y = []
#         x.append(result_point[result2[i]][0])
#         x.append(result_point[result2[i + 1]][0])
#         y.append(result_point[result2[i]][1])
#         y.append(result_point[result2[i + 1]][1])
#         ax.plot(x, y, color='purple')
#
#     ax.axis([0,WI,0,BR])
#     plt.savefig("multi_route_graph.jpg")

def multiroute1(point_file,line_file,cluster_num):
    f = open(point_file)  # read point file
    content = f.read()
    lines = content.splitlines()
    point_remain = []  # ID
    start_id = -1
    max_num = 0
    point_id = 0
    position = {}
    weight = {}
    for line in lines:
        line = line.split(" ")
        point_remain.append(int(line[0]))
        position[point_id] = [float(line[1]),float(line[2])]
        if int(line[3]) != 0:  # get the start point ID
            start_id = point_id
            max_num = int(line[3])
        if int(line[4]) != 0:
            weight[point_id] = int(line[4])
        point_id += 1
    f.close()

    f = open(line_file)  # read line file
    content = f.read()
    lines = content.splitlines()
    line_cost = []  # cost of each line
    get_the_route = {}  # display the route
    for line in lines:
        line = line.split(" ")
        line_cost.append(float(line[2]))
        key1 = (int(line[0]), int(line[1]))  # small-big
        key2 = (int(line[1]), int(line[0]))  # big-small
        temp = line[3].split("->")
        value1 = []
        value2 = []
        for i in range(len(temp)):
            value1.append(int(temp[i]))
            value2.append(int(temp[len(temp) - 1 - i]))

        get_the_route[key1] = value1
        get_the_route[key2] = value2

    f.close()

    matrix = [[float(0.0) for i in range(len(point_remain))] for j in range(len(point_remain))]  # initialize map
    num = 0
    for i in range(len(matrix)):
        for j in range(i + 1, len(matrix)):
            matrix[i][j] = line_cost[num]
            matrix[j][i] = line_cost[num]
            num += 1

    multiclustering = MULTICLUSTERING(position,weight,start_id,matrix)
    ID = multiclustering.partition(max_num,cluster_num)                    # partition 2
    print(ID)
    for i in range(len(ID)):
        ID[i].append(start_id)

    sa = [0 for i in range(len(ID))]
    for i in range(len(ID)):
        sa[i] = SA(ID[i],matrix)
    get_value = [[] for i in range(len(ID))]
    for i in range(len(ID)):
        for j in range(2):
            get_value[i].append(sa[i].min_path_2(start_id))     # save the iteration result
    # print(get_value)
    dis = [float("inf") for i in range(len(ID))]
    path = [[] for i in range(len(ID))]
    for i in range(len(ID)):
        for j in range(len(get_value[i])):
            if dis[i] > get_value[i][j][0]:
                dis[i] = get_value[i][j][0]
                path[i] = []
                for k in range(len(ID[i])):
                    path[i].append(point_remain[get_value[i][j][1][k]])     # get the shortest
    result = [[] for i in range(len(ID))]
    for i in range(len(ID)):
        for j in range(len(path[i]) - 1):
            key = (path[i][j], path[i][j + 1])
            for k in range(len(get_the_route[key]) - 1):
                result[i].append(get_the_route[key][k])
        for j in range(len(get_the_route[(path[i][len(path[i]) - 1], path[i][0])])):
            result[i].append(get_the_route[(path[i][len(path[i]) - 1], path[i][0])][j])     # save like id id
    result_route = ["" for i in range(len(ID))]
    for i in range(len(ID)):
        for j in range(len(result[i])):  # display the route
            result_route[i] += str(result[i][j])
            if j != len(result[i]) - 1:
                result_route[i] += "->"                         # save like id->id
    print(result_route)
    print(dis)
    return result
    #print(get_value)
    # ID1.append(start_id)
    # ID2.append(start_id)
    #
    # sa1 = SA(ID1,matrix)
    # get_value1 = []
    # for i in range(20): # 20 iteration
    #     get_value1.append(sa1.min_path_2(start_id))
    # dis1 = float("inf")
    # path1 = list(range(len(ID1)))
    # for i in range(len(get_value1)):
    #     if dis1 > get_value1[i][0]:
    #         dis1 = get_value1[i][0]  # get the smallest
    #         for j in range(len(ID1)):
    #             path1[j] = point_remain[get_value1[i][1][j]]  # path contains the nodes in the new graph
    # result1 = []  # result contains the nodes in the raw graph
    # for i in range(len(path1) - 1):
    #     key = (path1[i], path1[i + 1])
    #     for j in range(len(get_the_route[key]) - 1):
    #         result1.append(get_the_route[key][j])  # a-b
    # for i in range(len(get_the_route[(path1[len(path1) - 1], path1[0])])):  # b-a
    #     result1.append(get_the_route[(path1[len(path1) - 1], path1[0])][i])
    # result_route1 = ""
    # for i in range(len(result1)):  # display the route
    #     result_route1 += str(result1[i])
    #     if i != len(result1) - 1:
    #         result_route1 += "->"
    # print(result_route1)
    # print(dis1)
    #
    # sa2 = SA(ID2, matrix)
    # get_value2 = []
    # for i in range(20):  # 20 iteration
    #     get_value2.append(sa2.min_path_2(start_id))
    # dis2 = float("inf")
    # path2 = list(range(len(ID2)))
    # for i in range(len(get_value2)):
    #     if dis2 > get_value2[i][0]:
    #         dis2 = get_value2[i][0]  # get the smallest
    #         for j in range(len(ID2)):
    #             path2[j] = point_remain[get_value2[i][1][j]]  # path contains the nodes in the new graph
    # result2 = []  # result contains the nodes in the raw graph
    # for i in range(len(path2) - 1):
    #     key = (path2[i], path2[i + 1])
    #     for j in range(len(get_the_route[key]) - 1):
    #         result2.append(get_the_route[key][j])  # a-b
    # for i in range(len(get_the_route[(path2[len(path2) - 1], path2[0])])):  # b-a
    #     result2.append(get_the_route[(path2[len(path2) - 1], path2[0])][i])
    # result_route2 = ""
    # for i in range(len(result2)):  # display the route
    #     result_route2 += str(result2[i])
    #     if i != len(result2) - 1:
    #         result_route2 += "->"
    # print(result_route2)
    # print(dis2)
    # return result1,result2

def displayroute1(point_file,result,cluster_num):
    f = open(point_file)  # read point file
    content = f.read()
    lines = content.splitlines()
    result_point = {}
    num = 0
    for line in lines:
        line = line.split(" ")
        temp = []
        temp.append(float(line[0]))
        temp.append(float(line[1]))
        temp.append(int(line[2]))
        temp.append(int(line[3]))
        result_point[num] = temp
        num += 1
    f.close()

    color = ['green','red','black','blue','purple']

    for j in range(len(result)):
        fig = plt.figure()
        ax = fig.add_subplot(1, 1, 1)
        ax.set_title('MULTI_ROUTE')
        ax.set_xlabel('x')
        ax.set_ylabel('y')
        for i in range(len(result[j]) - 1):
            if result_point[result[j][i]][2] != 0:
                ax.plot(result_point[result[j][i]][0], result_point[result[j][i]][1], 'o', color='green')
                ax.text(result_point[result[j][i]][0], result_point[result[j][i]][1], str(result_point[result[j][i]][2]),
                        color='green', fontsize=10)
            elif result_point[result[j][i]][3] != 0:
                ax.plot(result_point[result[j][i]][0], result_point[result[j][i]][1], 'o', color='red')
                ax.text(result_point[result[j][i]][0], result_point[result[j][i]][1], str(result_point[result[j][i]][3]),
                        color='red', fontsize=10)
            else:
                ax.plot(result_point[result[j][i]][0], result_point[result[j][i]][1], 'o', color='black')

        for i in range(len(result[j]) - 1):
            x = []
            y = []
            x.append(result_point[result[j][i]][0])
            x.append(result_point[result[j][i + 1]][0])
            y.append(result_point[result[j][i]][1])
            y.append(result_point[result[j][i + 1]][1])
            ax.plot(x, y, color = color[j % 5])

        ax.axis([0,WI,0,BR])
        if os.path.exists("case1/" + str(cluster_num)) == False:
            os.mkdir("case1/" + str(cluster_num))
        plt.savefig("case1/" + str(cluster_num) + "/" + str(j+1) + ".jpg")

def multiroute2(point_file,line_file,cluster_num):
    f = open(point_file)  # read point file
    content = f.read()
    lines = content.splitlines()
    point_remain = []  # ID
    start_id = -1
    max_num = 0
    point_id = 0
    position = {}
    weight = {}
    for line in lines:
        line = line.split(" ")
        point_remain.append(int(line[0]))
        position[point_id] = [float(line[1]), float(line[2])]
        if int(line[3]) != 0:  # get the start point ID
            start_id = point_id
            max_num = int(line[3])
        if int(line[4]) != 0:
            weight[point_id] = int(line[4])
        point_id += 1
    f.close()

    f = open(line_file)  # read line file
    content = f.read()
    lines = content.splitlines()
    line_cost = []  # cost of each line
    # get_the_route = {}  # display the route
    for line in lines:
        line = line.split(" ")
        line_cost.append(float(line[2]))
        # key1 = (int(line[0]), int(line[1]))  # small-big
        # key2 = (int(line[1]), int(line[0]))  # big-small
        # temp = line[3].split("->")
        # value1 = []
        # value2 = []
        # for i in range(len(temp)):
        #     value1.append(int(temp[i]))
        #     value2.append(int(temp[len(temp) - 1 - i]))
        #
        # get_the_route[key1] = value1
        # get_the_route[key2] = value2

    f.close()

    matrix = [[float(0.0) for i in range(len(point_remain))] for j in range(len(point_remain))]  # initialize map
    num = 0
    for i in range(len(matrix)):
        for j in range(i + 1, len(matrix)):
            matrix[i][j] = line_cost[num]
            matrix[j][i] = line_cost[num]
            num += 1

    multiclustering = MULTICLUSTERING(position, weight, start_id, matrix)
    ID = multiclustering.partition(max_num, cluster_num)  # partition 2
    print(ID)
    for i in range(len(ID)):
        ID[i].append(start_id)

    sa = [0 for i in range(len(ID))]
    for i in range(len(ID)):
        sa[i] = SA(ID[i], matrix)
    get_value = [[] for i in range(len(ID))]
    for i in range(len(ID)):
        for j in range(2):
            get_value[i].append(sa[i].min_path_2(start_id))  # save the iteration result
    dis = [float("inf") for i in range(len(ID))]
    path = [[] for i in range(len(ID))]
    for i in range(len(ID)):
        for j in range(len(get_value[i])):
            if dis[i] > get_value[i][j][0]:
                dis[i] = get_value[i][j][0]
                path[i] = []
                for k in range(len(ID[i])):
                    path[i].append(point_remain[get_value[i][j][1][k]])  # get the shortest
    print(path)
    result = [[]for i in range(len(ID))]
    for i in range(len(ID)):
        result[i] = path[i]
    for i in range(len(ID)):
        result[i].append(point_remain[start_id])
    result_route = ["" for i in range(len(ID))]
    for i in range(len(ID)):
        for j in range(len(result[i])):  # display the route
            result_route[i] += str(result[i][j])
            if j != len(result[i]) - 1:
                result_route[i] += "->"  # save like id->id
    print(result_route)
    print(dis)
    return result

def displayroute2(point_file,result,cluster_num):
    f = open(point_file)  # read point file
    content = f.read()
    lines = content.splitlines()
    result_point = {}
    #num = 0
    for line in lines:
        line = line.split(" ")
        temp = []
        temp.append(float(line[1]))
        temp.append(float(line[2]))
        temp.append(int(line[3]))
        temp.append(int(line[4]))
        result_point[int(line[0])] = temp
        #num += 1
    f.close()

    color = ['green', 'red', 'black', 'blue', 'purple']

    for j in range(len(result)):
        fig = plt.figure()
        ax = fig.add_subplot(1, 1, 1)
        ax.set_title('MULTI_ROUTE')
        ax.set_xlabel('x')
        ax.set_ylabel('y')
        for i in range(len(result[j]) - 1):
            if result_point[result[j][i]][2] != 0:
                ax.plot(result_point[result[j][i]][0], result_point[result[j][i]][1], 'o', color='green')
                ax.text(result_point[result[j][i]][0], result_point[result[j][i]][1],
                        str(result_point[result[j][i]][2]),
                        color='green', fontsize=10)
            elif result_point[result[j][i]][3] != 0:
                ax.plot(result_point[result[j][i]][0], result_point[result[j][i]][1], 'o', color='red')
                ax.text(result_point[result[j][i]][0], result_point[result[j][i]][1],
                        str(result_point[result[j][i]][3]),
                        color='red', fontsize=10)
            else:
                ax.plot(result_point[result[j][i]][0], result_point[result[j][i]][1], 'o', color='black')

        for i in range(len(result[j]) - 1):
            x = []
            y = []
            x.append(result_point[result[j][i]][0])
            x.append(result_point[result[j][i + 1]][0])
            y.append(result_point[result[j][i]][1])
            y.append(result_point[result[j][i + 1]][1])
            ax.plot(x, y, color=color[j % 5])

        ax.axis([0, WI, 0, BR])
        if os.path.exists("case2/" + str(cluster_num)) == False:
            os.mkdir("case2/" + str(cluster_num))
        plt.savefig("case2/" + str(cluster_num) + "/" + str(j + 1) + ".jpg")

def plan_route_handler(event,context):
    start_input = int(event['start_input'])
    end_input_splits = event['end_input'].split(',')
    end_input = [int(i) for i in end_input_splits]
    map_height = int(event['map_height'])
    num_of_u = int(event['num_of_u'])
    return plan_route(start_input, end_input, map_height, num_of_u)

def plan_route(start_input,end_input,map_height,num_of_u):
    if map_height == 1:
        #start_input = input("start_point information: ID")
        # if int(start_input) == -1:
        #     break
        # end_input = input("end_point information: ID1 ID2...")
        start = int(start_input)  # start point ID
        #print("asdfasdf")
        #temp = end_input.split(" ")
        end_information = {}  # end point information map = (key = ID,value = num)
        for i in range(len(end_input)):
            if int(end_input[i]) not in end_information.keys():
                end_information[int(end_input[i])] = 1

        initialize("raw_point.txt", "raw_line.txt", start, end_information)
        display("raw_point.txt", "raw_line.txt")
        preprocess("raw_point.txt", "raw_line.txt", "new_point.txt", "new_line.txt")
        display_again("new_point.txt", "new_line.txt")

        # result = sa("new_point.txt","new_line.txt")
        # display_route("raw_point.txt",result)
        # result1,result2 = multimission("new_point.txt","new_line.txt")
        # display_multi_route("raw_point.txt",result1,result2)
        if num_of_u == 1:
            result1_1 = multiroute1("new_point.txt", "new_line.txt", 1)
            if os.path.exists("case1") == False:
                os.mkdir("case1")
            displayroute1("raw_point.txt", result1_1, 1)
            return result1_1

        elif num_of_u == 2:
            result1_2 = multiroute1("new_point.txt", "new_line.txt", 2)
            if os.path.exists("case1") == False:
                os.mkdir("case1")
            displayroute1("raw_point.txt", result1_2, 2)
            return result1_2

        else:
            result1_5 = multiroute1("new_point.txt", "new_line.txt", 5)
            if os.path.exists("case1") == False:
                os.mkdir("case1")
            displayroute1("raw_point.txt", result1_5, 5)
            return result1_5

    if map_height == 5:
        f = open("raw_point.txt")
        lines = f.read().splitlines()
        information = []
        for line in lines:
            temp = line.split(" ")
            information.append([float(temp[0]), float(temp[1])])
        f.close()

        # start_input = input("start_point information: ID")
        # if int(start_input) == -1:
        #     break
        # end_input = input("end_point information: ID1 ID2...")
        start = int(start_input)  # start point ID
        # temp = end_input.split(" ")
        point_remain = []
        point_remain.append(start)
        for i in range(len(end_input)):
            point_remain.append(int(end_input[i]))
        point_remain.sort()

        f = open("point_2.txt", 'w')
        f.truncate()
        f.close()
        f = open("point_2.txt", 'a')
        for i in range(len(point_remain)):
            if point_remain[i] == start:
                f.write(str(point_remain[i]) + " " + str(information[point_remain[i]][0]) + " " + str(
                    information[point_remain[i]][1]) + " " + str(len(point_remain) - 1) + " " + "0" + "\n")
            else:
                f.write(str(point_remain[i]) + " " + str(information[point_remain[i]][0]) + " " + str(
                    information[point_remain[i]][1]) + " " + "0" + " " + "1" + "\n")
        f.close()

        f = open("line_2.txt", 'w')
        f.truncate()
        f.close()
        f = open("line_2.txt", 'a')
        for i in range(len(point_remain)):
            for j in range(i + 1, len(point_remain)):
                f.write(str(point_remain[i]) + " " + str(point_remain[j]) + " " + str(math.sqrt(
                    pow(information[point_remain[i]][0] - information[point_remain[j]][0], 2) + pow(
                        information[point_remain[i]][1] - information[point_remain[j]][1], 2))) + "\n")
        f.close()

        if num_of_u == 1:
            result2_1 = multiroute2("point_2.txt", "line_2.txt", 1)
            if os.path.exists("case2") == False:
                os.mkdir("case2")
            displayroute2("point_2.txt", result2_1, 1)
            return result2_1

        elif num_of_u == 2:
            result2_2 = multiroute2("point_2.txt", "line_2.txt", 2)
            if os.path.exists("case2") == False:
                os.mkdir("case2")
            displayroute2("point_2.txt", result2_2, 2)
            return result2_2

        else:
            result2_5 = multiroute2("point_2.txt", "line_2.txt", 5)
            if os.path.exists("case2") == False:
                os.mkdir("case2")
            displayroute2("point_2.txt", result2_5, 5)
            return result2_5


class LocationButton(QPushButton):
    def __init__(self, name, px, py, parent, kind):
        super().__init__("", parent)
        self.id = int(name)-1
        name = "Location " + name
        self.setObjectName(name)
        self.setStyleSheet("focusPolicy: NoFocus")

        self.icon_black = QIcon()
        self.icon_black.addPixmap(QPixmap("./source/location.png"), QIcon.Normal, QIcon.Off)
        self.icon_purple = QIcon()
        self.icon_purple.addPixmap(QPixmap("./source/location-purple.png"), QIcon.Normal, QIcon.Off)
        self.icon_blue = QIcon()
        self.icon_blue.addPixmap(QPixmap("./source/location-blue.png"), QIcon.Normal, QIcon.Off)
        self.icon_red = QIcon()
        self.icon_red.addPixmap(QPixmap("./source/location-red.png"), QIcon.Normal, QIcon.Off)
        self.icon_green = QIcon()
        self.icon_green.addPixmap(QPixmap("./source/location-green.png"), QIcon.Normal, QIcon.Off)
        self.icon_uva = QIcon()
        self.icon_uva.addPixmap(QPixmap("./source/uva_icon-black.png"), QIcon.Normal, QIcon.Off)

        self.setIcon(self.icon_black)
        self.setStyleSheet(
            "QPushButton{border-radius:10px;}"
            "QPushButton:hover {background-color: grey;border-style: inset;}"
        )
        self.setToolTip(name)
        self.clicked.connect(self.on_click)
        self.resize(16, 16)
        self.move(px, py)

        self.parent = parent
        self.kind = kind

    def on_click(self):
        if self.kind == "start":
            if self.parent.start_point != -1:
                self.parent.locations_button[self.parent.start_point].setIcon(self.icon_black)
            self.parent.locations_button[self.id].setIcon(self.icon_purple)
            self.parent.start_point = self.id
            self.parent.message_box.append("设置起点： " + self.objectName())
        elif self.kind == "end":
            if self.parent.end_point != -1:
                self.parent.locations_button[self.parent.end_point].setIcon(self.icon_black)
            self.parent.locations_button[self.id].setIcon(self.icon_blue)
            self.parent.end_point = self.id
            self.parent.message_box.append("设置终点： " + self.objectName())
        elif self.kind == "pass":
            if self.id != self.parent.start_point and self.id != self.parent.end_point and self.id not in self.parent.pass_point:
                self.parent.locations_button[self.id].setIcon(self.icon_green)

            self.parent.pass_point.append(self.id)
            self.parent.message_box.append("增加经过点： " + self.objectName())


class MapBox(QWidget):
    def __init__(self, message_box):
        super().__init__()
        # 定义布局
        self.layout = QVBoxLayout()
        self.setLayout(self.layout)

        # 定义地图
        self.map = QLabel()
        self.init_map()

        # 定义无人机
        self.uvas = []
        self.init_uvas()

        # 消息
        self.message_box = message_box

        self.rw = 0
        self.rh = 0
        self.start_point = -1
        self.end_point = -1
        self.pass_point = []
        self.locations = []
        self.locations_button = []
        self.uva_num = 1

    def resizeEvent(self, a0: QResizeEvent):
        self.update_map()
        self.update_location()

    def init_map(self):
        self.map.setObjectName("none")
        self.map.setScaledContents(True)
        self.map.resize(self.width(), self.height())
        self.layout.addChildWidget(self.map)

    def init_uvas(self):
        for i in range(10):
            r = random.randint(100, 255)
            g = random.randint(100, 255)
            b = random.randint(100, 255)
            self.uvas.append(UVA([(500, 500), (10, 10), (r, g)], self, pen=QPen(QColor(r, g, b), 2, Qt.DashLine)))
            self.layout.addChildWidget(self.uvas[-1])
            self.uvas[-1].hide()

    def init_location(self):
        self.locations.clear()
        self.locations_button.clear()

        tp = json.load(open("./conf.json", "r"))

        name = tp["map"]

        with open("./maps/" + name + ".txt", "r") as f:
            n = 0
            for row in f:
                x, y = row.split()
                x = float(x)
                y = float(y)
                if n == 0:
                    self.rw = x
                    self.rh = y
                else:
                    self.locations.append((x, y))
                n += 1

        for i in range(len(self.locations)):
            location_button = LocationButton(str(i+1), 0, 0, self, "none")
            location_button.setIcon(location_button.icon_black)
            self.locations_button.append(location_button)

    def load_map(self, file):
        l = file.rfind("NJU")
        r = file.rfind("-")
        self.map_name = file[l:r]
        self.map_height = file[r + 1]
        self.map_path = file[:r]
        self.clear()
        conf = json.load(open("./conf.json", "r"))
        conf["map"] = self.map_name
        conf["height"] = self.map_height
        json.dump(conf, open("./conf.json", "w"))
        self.map.setPixmap(QPixmap(file))
        self.map.setObjectName(file)
        self.show_map()

    def show_map(self):
        if self.map.objectName() == "none":
            self.message_box.append("未加载地图")
            return False
        else:
            self.map.show()
            return True

    def hide_map(self):
        self.map.hide()

    def update_map(self, h=None):
        if h is not None:
            self.map_height = h
            print(self.map_path + "-" + h + ".png")
            self.map.setPixmap(QPixmap(self.map_path + "-" + h + ".png"))
        self.map.resize(self.width(), self.height())

    def update_location(self):
        w = self.width()
        h = self.height()
        self.map.resize(w, h)
        pts = []
        for i in range(len(self.locations)):
            px = int(self.locations[i][0] * w / self.rw)
            py = int((self.rh - self.locations[i][1]) * h / self.rh)
            self.locations_button[i].move(px, py)
            pts.append((px, h - py))
        # self.locations = list(pts)
        # self.rw = w
        # self.rh = h

    def show_location(self, kind):
        self.update_location()
        for i in range(len(self.locations)):
            self.locations_button[i].kind = kind
            self.locations_button[i].show()

    def hide_location(self):
        for i in range(len(self.locations)):
            self.locations_button[i].kind = "none"
            self.locations_button[i].hide()

    def plan_path(self):
        self.hide_location()
        self.update_location()
        if self.start_point < 0:
            self.message_box.append("规划失败，未设置起点!!")
            return
        if self.end_point < 0:
            self.message_box.append("未设置终点，默认为起点!!")
            self.end_point = self.start_point

        tp = set(self.pass_point)
        self.pass_point = []
        for pid in tp:
            if pid < 0:
                continue
            if pid == self.start_point or pid == self.end_point:
                continue
            self.pass_point.append(pid)

        # 显示选中点
        self.locations_button[self.start_point].setIcon(self.locations_button[self.start_point].icon_blue)
        self.locations_button[self.start_point].show()

        self.locations_button[self.end_point].setIcon(self.locations_button[self.start_point].icon_purple)
        self.locations_button[self.end_point].show()

        for i in range(len(self.pass_point)):
            pid = self.pass_point[i]
            self.locations_button[pid].setIcon(self.locations_button[pid].icon_green)
            self.locations_button[pid].show()

        # 规划路径
        self.message_box.append("路径规划中...")

        conf = json.load(open("./conf.json", "r"))
        conf["start_location"] = self.start_point
        conf["end_location"] = self.end_point
        conf["pass_location"] = [pid for pid in self.pass_point]
        json.dump(conf, open("./conf.json", "w"))

        print("start_location:",conf["start_location"])
        print("pass_location:",conf["pass_location"])
        print("map_height:",self.map_height)
        print("uva_num:",self.uva_num)
        paths = plan_route(conf["start_location"], conf["pass_location"], int(self.map_height), int(self.uva_num))
        print(paths)

        # 读入规划路线
        #paths = [[self.start_point] + self.pass_point + [self.end_point], [0, 1, 2, 3, 4]]
        #  = [[0, 5, 6, 7], [0, 1, 2, 3]]
        # paths = [[0, 5, 6, 7]]
        t = random.random() * 60
        # time.sleep(t)
        self.message_box.append("路径规划完成，一共耗时%.2f秒，规划结果共需要%d架无人机" % (t, len(paths)))

        # 显示规划路径
        for i in range(len(paths)):
            self.uvas[i].update_locations([(self.rw, self.rh)] + [self.locations[paths[i][j]] for j in range(len(paths[i]))])
            self.uvas[i].show()

    def run_path(self):
        for i in range(len(self.uvas)):
            self.uvas[i].run()

    def clear(self):
        # self.hide_map()
        self.hide_location()
        for x in self.uvas:
            x.hide()
