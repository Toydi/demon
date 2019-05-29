#!/usr/bin/env python
# _*_ coding:utf-8 _*_

# import matplotlib.pyplot as plt
from preprocess import PREPROCESS
from generator import GENERATOR
from sa import SA
from clustering import CLUSTERING

def initialize(point_file,line_file):
    generator = GENERATOR()
    generator.generate_point(point_file)
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

    # fig = plt.figure()
    # ax = fig.add_subplot(1,1,1)
    # ax.set_title('RAW_MAP')
    # ax.set_xlabel('x')
    # ax.set_ylabel('y')
    # for i in range(len(result_point)):
    #     if result_point[i][2] != 0:
    #         ax.plot(result_point[i][0],result_point[i][1],'o',color='green')
    #         ax.text(result_point[i][0],result_point[i][1],str(result_point[i][2]),color='green',fontsize = 10)
    #     elif result_point[i][3] != 0:
    #         ax.plot(result_point[i][0],result_point[i][1],'o',color='red')
    #         ax.text(result_point[i][0], result_point[i][1], str(result_point[i][3]), color='red',fontsize = 10)
    #     else:
    #         ax.plot(result_point[i][0], result_point[i][1], 'o', color='black')

    # for i in range(len(result_line)):
    #     x = []
    #     y = []
    #     x.append(result_point[result_line[i][0]][0])
    #     x.append(result_point[result_line[i][1]][0])
    #     y.append(result_point[result_line[i][0]][1])
    #     y.append(result_point[result_line[i][1]][1])
    #     ax.plot(x,y,color='black')
    #     ax.text((x[0]+x[1])/2,(y[0]+y[1])/2,'%.2f'%result_line[i][2],color='blue',fontsize = 5)

    # ax.axis([0,550,0,550])
    # plt.savefig("raw_graph.jpg")
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

    # fig = plt.figure()
    # ax = fig.add_subplot(1,1,1)
    # ax.set_title('NEW_MAP')
    # ax.set_xlabel('x')
    # ax.set_ylabel('y')
    # for i in range(len(point_remain)):
    #     if result_point[point_remain[i]][2] != 0:
    #         ax.plot(result_point[point_remain[i]][0],result_point[point_remain[i]][1],'o',color='green')
    #         ax.text(result_point[point_remain[i]][0],result_point[point_remain[i]][1],str(result_point[point_remain[i]][2]),color='green',fontsize = 10)
    #     elif result_point[point_remain[i]][3] != 0:
    #         ax.plot(result_point[point_remain[i]][0],result_point[point_remain[i]][1],'o',color='red')
    #         ax.text(result_point[point_remain[i]][0],result_point[point_remain[i]][1],str(result_point[point_remain[i]][3]),color='red',fontsize = 10)
    #     # else:
    #     #     ax.plot(result_point[i][0], result_point[i][1], 'o', color='black')

    # for i in range(len(result_line)):
    #     x = []
    #     y = []
    #     x.append(result_point[result_line[i][0]][0])
    #     x.append(result_point[result_line[i][1]][0])
    #     y.append(result_point[result_line[i][0]][1])
    #     y.append(result_point[result_line[i][1]][1])
    #     ax.plot(x,y,color='black')
    #     ax.text((x[0]+x[1])/2,(y[0]+y[1])/2,'%.2f'%result_line[i][2],color='blue',fontsize = 5)

    # ax.axis([0,550,0,550])
    # plt.savefig("new_graph.jpg")
    # print(point_remain)
    # print(raw_matrix)

def sa(point_file,line_file):
    f = open(point_file)  # read point file
    content = f.read()
    lines = content.splitlines()
    point_remain = []  # ID
    start_id = -1
    point_id = 0
    for line in lines:
        line = line.split(" ")
        point_remain.append(int(line[0]))
        if int(line[3])!=0:             # get the start point ID
            start_id = point_id
        point_id += 1
    f.close()

    f = open(line_file)  # read line file
    content = f.read()
    lines = content.splitlines()
    line_cost = []      # cost of each line
    get_the_route = {}  # display the route
    for line in lines:
        line = line.split(" ")
        line_cost.append(float(line[2]))
        key1 = (int(line[0]),int(line[1]))  # small-big
        key2 = (int(line[1]),int(line[0]))  # big-small
        temp = line[3].split("->")
        value1 = []
        value2 = []
        for i in range(len(temp)):
            value1.append(int(temp[i]))
            value2.append(int(temp[len(temp)-1-i]))

        get_the_route[key1] = value1
        get_the_route[key2] = value2


    f.close()

    matrix = [[float(0.0) for i in range(len(point_remain))] for j in range(len(point_remain))] # initialize map
    num = 0
    for i in range(len(matrix)):
        for j in range(i+1,len(matrix)):
            matrix[i][j] = line_cost[num]
            matrix[j][i] = line_cost[num]
            num += 1

    sa = SA(point_remain,matrix)

    get_value = []

    for i in range(20): # 20 iteration
        get_value.append(sa.min_path(start_id))

    dis = float("inf")
    path = list(range(len(point_remain)))

    for i in range(len(get_value)):
        if dis>get_value[i][0]:
            dis = get_value[i][0]    # get the smallest
            for j in range(len(point_remain)):
                path[j] = point_remain[get_value[i][1][j]]  # path contains the nodes in the new graph

    result = []     # result contains the nodes in the raw graph
    for i in range(len(path)-1):
        key = (path[i],path[i+1])
        for j in range(len(get_the_route[key])-1):
            result.append(get_the_route[key][j])                # a-b
    for i in range(len(get_the_route[(path[len(path)-1],path[0])])):    # b-a
        result.append(get_the_route[(path[len(path)-1],path[0])][i])
    result_route = ""
    for i in range(len(result)):        # display the route
        result_route += str(result[i])
        if i!=len(result)-1:
            result_route += "->"
    print(result_route)
    print(dis)
    return result_route

def display_route(point_file,result):
    # fig = plt.figure()
    # ax = fig.add_subplot(1, 1, 1)
    # ax.set_title('ROUTE_MAP')
    # ax.set_xlabel('x')
    # ax.set_ylabel('y')

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

    # for i in range(len(result)-1):
    #     if result_point[result[i]][2] != 0:
    #         ax.plot(result_point[result[i]][0],result_point[result[i]][1],'o',color='green')
    #         ax.text(result_point[result[i]][0],result_point[result[i]][1],str(result_point[result[i]][2]),color='green',fontsize = 10)
    #     elif result_point[result[i]][3] != 0:
    #         ax.plot(result_point[result[i]][0],result_point[result[i]][1],'o',color='red')
    #         ax.text(result_point[result[i]][0],result_point[result[i]][1],str(result_point[result[i]][3]),color='red',fontsize = 10)
    #     else:
    #         ax.plot(result_point[result[i]][0],result_point[result[i]][1],'o',color='black')

    # for i in range(len(result)-1):
    #     x = []
    #     y = []
    #     x.append(result_point[result[i]][0])
    #     x.append(result_point[result[i+1]][0])
    #     y.append(result_point[result[i]][1])
    #     y.append(result_point[result[i+1]][1])
    #     ax.plot(x,y,color='blue')

    # ax.axis([0, 550, 0, 550])
    # plt.savefig("route_graph.jpg")

def multimission(point_file,line_file):
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

    clustering = CLUSTERING(position,weight,start_id,matrix)
    ID1,ID2 = clustering.partition(max_num)                    # partition 2
    ID1.append(start_id)
    ID2.append(start_id)

    sa1 = SA(ID1,matrix)
    get_value1 = []
    for i in range(20): # 20 iteration
        get_value1.append(sa1.min_path_2(start_id))
    dis1 = float("inf")
    path1 = list(range(len(ID1)))
    for i in range(len(get_value1)):
        if dis1 > get_value1[i][0]:
            dis1 = get_value1[i][0]  # get the smallest
            for j in range(len(ID1)):
                path1[j] = point_remain[get_value1[i][1][j]]  # path contains the nodes in the new graph
    result1 = []  # result contains the nodes in the raw graph
    for i in range(len(path1) - 1):
        key = (path1[i], path1[i + 1])
        for j in range(len(get_the_route[key]) - 1):
            result1.append(get_the_route[key][j])  # a-b
    for i in range(len(get_the_route[(path1[len(path1) - 1], path1[0])])):  # b-a
        result1.append(get_the_route[(path1[len(path1) - 1], path1[0])][i])
    result_route1 = ""
    for i in range(len(result1)):  # display the route
        result_route1 += str(result1[i])
        if i != len(result1) - 1:
            result_route1 += "->"
    print(result_route1)
    print(dis1)

    sa2 = SA(ID2, matrix)
    get_value2 = []
    for i in range(20):  # 20 iteration
        get_value2.append(sa2.min_path_2(start_id))
    dis2 = float("inf")
    path2 = list(range(len(ID2)))
    for i in range(len(get_value2)):
        if dis2 > get_value2[i][0]:
            dis2 = get_value2[i][0]  # get the smallest
            for j in range(len(ID2)):
                path2[j] = point_remain[get_value2[i][1][j]]  # path contains the nodes in the new graph
    result2 = []  # result contains the nodes in the raw graph
    for i in range(len(path2) - 1):
        key = (path2[i], path2[i + 1])
        for j in range(len(get_the_route[key]) - 1):
            result2.append(get_the_route[key][j])  # a-b
    for i in range(len(get_the_route[(path2[len(path2) - 1], path2[0])])):  # b-a
        result2.append(get_the_route[(path2[len(path2) - 1], path2[0])][i])
    result_route2 = ""
    for i in range(len(result2)):  # display the route
        result_route2 += str(result2[i])
        if i != len(result2) - 1:
            result_route2 += "->"
    print(result_route2)
    print(dis2)
    return result_route1,result_route2

def display_multi_route(point_file,result1,result2):
    # fig = plt.figure()
    # ax = fig.add_subplot(1, 1, 1)
    # ax.set_title('MULTI_ROUTE_MAP')
    # ax.set_xlabel('x')
    # ax.set_ylabel('y')

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

    # for i in range(len(result1) - 1):
    #     if result_point[result1[i]][2] != 0:
    #         ax.plot(result_point[result1[i]][0], result_point[result1[i]][1], 'o', color='green')
    #         ax.text(result_point[result1[i]][0], result_point[result1[i]][1], str(result_point[result1[i]][2]),
    #                 color='green', fontsize=10)
    #     elif result_point[result1[i]][3] != 0:
    #         ax.plot(result_point[result1[i]][0], result_point[result1[i]][1], 'o', color='red')
    #         ax.text(result_point[result1[i]][0], result_point[result1[i]][1], str(result_point[result1[i]][3]),
    #                 color='red', fontsize=10)
    #     else:
    #         ax.plot(result_point[result1[i]][0], result_point[result1[i]][1], 'o', color='black')

    # for i in range(len(result1) - 1):
    #     x = []
    #     y = []
    #     x.append(result_point[result1[i]][0])
    #     x.append(result_point[result1[i + 1]][0])
    #     y.append(result_point[result1[i]][1])
    #     y.append(result_point[result1[i + 1]][1])
    #     ax.plot(x, y, color='blue')

    # for i in range(len(result2) - 1):
    #     if result_point[result2[i]][2] != 0:
    #         ax.plot(result_point[result2[i]][0], result_point[result2[i]][1], 'o', color='green')
    #         ax.text(result_point[result2[i]][0], result_point[result2[i]][1], str(result_point[result2[i]][2]),
    #                 color='green', fontsize=10)
    #     elif result_point[result2[i]][3] != 0:
    #         ax.plot(result_point[result2[i]][0], result_point[result2[i]][1], 'o', color='red')
    #         ax.text(result_point[result2[i]][0], result_point[result2[i]][1], str(result_point[result2[i]][3]),
    #                 color='red', fontsize=10)
    #     else:
    #         ax.plot(result_point[result2[i]][0], result_point[result2[i]][1], 'o', color='black')

    # for i in range(len(result2) - 1):
    #     x = []
    #     y = []
    #     x.append(result_point[result2[i]][0])
    #     x.append(result_point[result2[i + 1]][0])
    #     y.append(result_point[result2[i]][1])
    #     y.append(result_point[result2[i + 1]][1])
    #     ax.plot(x, y, color='purple')

    # ax.axis([0, 550, 0, 550])
    # plt.savefig("multi_route_graph.jpg")
    
def display(event,context):
    initialize("raw_point.txt","raw_line.txt")
    # display("raw_point.txt","raw_line.txt")
    preprocess("raw_point.txt","raw_line.txt","new_point.txt","new_line.txt")
    # display_again("new_point.txt","new_line.txt")
    result = sa("new_point.txt","new_line.txt")
    # display_route("raw_point.txt",result)
    result1,result2 = multimission("new_point.txt","new_line.txt")
    return result


if __name__ == '__main__':
    initialize("raw_point.txt","raw_line.txt")
    # display("raw_point.txt","raw_line.txt")
    preprocess("raw_point.txt","raw_line.txt","new_point.txt","new_line.txt")
    # display_again("new_point.txt","new_line.txt")
    result = sa("new_point.txt","new_line.txt")
    # display_route("raw_point.txt",result)
    result1,result2 = multimission("new_point.txt","new_line.txt")
    # display_multi_route("raw_point.txt",result1,result2)

