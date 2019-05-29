#!/usr/bin/env python
# _*_ coding:utf-8 _*_

class PREPROCESS(object):

    def __init__(self,point_remain,raw_matrix):
        self.point_remain = point_remain
        self.raw_matrix = raw_matrix

    def generate_path(self,start,end,new_line_file):
        new_matrix = [[float("inf") for i in range(len(self.raw_matrix))] for j in range(len(self.raw_matrix))]        # create new_matrix
        for i in range(len(self.raw_matrix)):
            for j in range(len(self.raw_matrix)):
                new_matrix[i][j] = self.raw_matrix[i][j]
        #new_matrix = copy.deepcopy(self.raw_matrix)
        # for i in range(len(self.point_remain)): # create a new matrix
        #     if self.point_remain[i]!=start and self.point_remain[i]!=end:
        #         for j in range(len(self.raw_matrix)):
        #             if j!=self.point_remain[i]:
        #                 new_matrix[self.point_remain[i]][j] = float("inf")
        #                 new_matrix[j][self.point_remain[i]] = float("inf")

        #print(new_matrix)
        visited = [0 for i in range(len(new_matrix))]           # set
        path = ["" for i in range(len(new_matrix))]             # path
        for i in range(len(path)):
            path[i] = str(start) + "->" + str(i)
        visited[start] = 1
        while visited[end] == 0:
            choose_index = -1                 # choose the nearest point
            min = float("inf")
            for i in range(len(new_matrix)):
                if visited[i]==0 and new_matrix[start][i] < min:
                    min = new_matrix[start][i]
                    choose_index = i

            visited[choose_index] = 1           # add it to the set

            for i in range(len(new_matrix)):        # release the road from the chosen point
                if visited[i]==0 and new_matrix[start][choose_index] + new_matrix[choose_index][i] < new_matrix[start][i]:
                    new_matrix[start][i] = new_matrix[start][choose_index] + new_matrix[choose_index][i]
                    path[i] = path[choose_index] + "->" + str(i)

        result = str(start) + " " + str(end) + " " + str(new_matrix[start][end]) + " " + path[end]

        f = open(new_line_file,'a')
        f.write(result+"\n")
        f.close()




