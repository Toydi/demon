#!/usr/bin/env python
# _*_ coding:utf-8 _*_

import random
import math

INITIAL_TEMPERATURE = 120
FINAL_TEMPERATURE = 0.001
REJECT_NUM = 1500
ITERATION_NUM = 5000

class SA(object):

    def __init__(self,point_remain,matrix):
        self.matrix = matrix
        self.num_of_point = len(point_remain)
        self.point_remain = point_remain

    def length(self,path):  # path to length
        dis = 0.0
        for i in range(self.num_of_point - 1):
            dis = self.matrix[path[i]][path[i + 1]] + dis
        dis = self.matrix[path[self.num_of_point-1]][path[0]] + dis  # form a circle
        return dis

    def min_path(self,start_id):
        path = []
        path.append(start_id)
        for i in range(self.num_of_point):  # start_id - 0 - 1 - ... - start_id-1 - start_id+1 - ... - n-1 - start_id
            if i!=start_id:
                path.append(i)

        dis = self.length(path)
        current_temperature = INITIAL_TEMPERATURE

        while current_temperature>FINAL_TEMPERATURE:    # temperature loop
            count_reject = 0
            count_iteration = 0
            while count_reject<REJECT_NUM and count_iteration<ITERATION_NUM:    # reject loop
                point1 = 0
                point2 = 0
                judge = 0
                while point1==point2 and judge < 20:       # point1!=point2     perhaps num_of_point = 2
                    point1 = random.randint(1,self.num_of_point-1)
                    point2 = random.randint(1,self.num_of_point-1)
                    judge += 1
                temp = path[point1]     # swap and temp = point1
                path[point1] = path[point2]
                path[point2] = temp
                dis_new = self.length(path)
                dis_delta = dis_new - dis
                if dis_delta < 0:   # smaller
                    dis = dis_new   # accept
                else:               # larger
                    accept_rate = math.exp(-dis_delta/current_temperature)
                    rand = random.random()
                    if accept_rate > rand:  # accept
                        dis = dis_new
                    else:                   # reject
                        path[point2] = path[point1]
                        path[point1] = temp
                        count_reject += 1
                count_iteration += 1
            current_temperature *= 0.99         # change the temperature

        print(path)
        return[dis,path]

    def min_path_2(self,start_id):
        path = []
        path.append(start_id)
        for i in range(self.num_of_point):  # start_id - 0 - 1 - ... - start_id-1 - start_id+1 - ... - n-1 - start_id
            if self.point_remain[i]!=start_id:
                path.append(self.point_remain[i])

        dis = self.length(path)
        current_temperature = INITIAL_TEMPERATURE

        while current_temperature>FINAL_TEMPERATURE:    # temperature loop
            count_reject = 0
            count_iteration = 0
            while count_reject<REJECT_NUM and count_iteration<ITERATION_NUM:    # reject loop
                point1 = 0
                point2 = 0
                while point1==point2:       # point1!=point2
                    point1 = random.randint(1,self.num_of_point-1)
                    point2 = random.randint(1,self.num_of_point-1)
                temp = path[point1]     # swap and temp = point1
                path[point1] = path[point2]
                path[point2] = temp
                dis_new = self.length(path)
                dis_delta = dis_new - dis
                if dis_delta < 0:   # smaller
                    dis = dis_new   # accept
                else:               # larger
                    accept_rate = math.exp(-dis_delta/current_temperature)
                    rand = random.random()
                    if accept_rate > rand:  # accept
                        dis = dis_new
                    else:                   # reject
                        path[point2] = path[point1]
                        path[point1] = temp
                        count_reject += 1
                count_iteration += 1
            current_temperature *= 0.99         # change the temperature

        print(path)
        return[dis,path]





