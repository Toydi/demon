#!/usr/bin/env python
# _*_ coding:utf-8 _*_

class CLUSTERING(object):

    def __init__(self,position,weight,start_id,matrix):
        self.position = position                                        #(x,y)
        self.weight = weight                                            #content
        self.start_id = start_id                                        #no partition
        self.matrix = matrix                                            #get the initialization

    def initialize(self,ID):
        represent1 = -1
        represent2 = -1

        dis = 0
        for i in range(len(ID)):                            # the two clusters should stay as far as they can
            for j in range(i+1,len(ID)):
                if dis < self.matrix[ID[i]][ID[j]]:
                    dis = self.matrix[ID[i]][ID[j]]
                    represent1 = ID[i]
                    represent2 = ID[j]

        return represent1,represent2

    def partition(self,max_num):
        ID = []
        for i in range(len(self.matrix)):           # not contain start_id
            if i != self.start_id:
                ID.append(i)

        ID1 = []
        ID2 = []
        ID1_new = []
        ID2_new = []

        represent1,represent2 = self.initialize(ID)
        ID1_new.append(represent1)
        ID2_new.append(represent2)

        center1 = [0, 0]
        center2 = [0, 0]
        center1_new = [self.position[represent1][0],self.position[represent1][1]]       #basic (x,y)
        center2_new = [self.position[represent2][0],self.position[represent2][1]]

        while center1_new != center1 or center2_new != center2:     # not change
            ID1 = ID1_new
            ID2 = ID2_new
            center1 = center1_new
            center2 = center2_new

            ID1_new = []
            ID2_new = []
            for i in range(len(ID)):            # choose a cluster again
                dis1 = pow(self.position[ID[i]][0]-center1[0],2) + pow(self.position[ID[i]][1]-center1[1],2)
                dis2 = pow(self.position[ID[i]][0]-center2[0],2) + pow(self.position[ID[i]][1]-center2[1],2)
                if dis1 <= dis2:
                    ID1_new.append(ID[i])
                else:
                    ID2_new.append(ID[i])

            x_all = 0                       # cluster1 new (x,y) * maybe weight is better
            y_all = 0
            for i in range(len(ID1_new)):
                x_all += self.position[ID1_new[i]][0]
                y_all += self.position[ID1_new[i]][1]
            center1_new = [x_all/len(ID1_new),y_all/len(ID1_new)]

            x_all = 0                       # cluster2 new (x,y) * maybe weight is better
            y_all = 0
            for i in range(len(ID2_new)):
                x_all += self.position[ID2_new[i]][0]
                y_all += self.position[ID2_new[i]][1]
            center2_new = [x_all / len(ID2_new), y_all / len(ID2_new)]

        weight1 = 0
        weight2 = 0
        for i in range(len(ID1_new)):
            weight1 += self.weight[ID1_new[i]]

        for i in range(len(ID2_new)):
            weight2 += self.weight[ID2_new[i]]

        overweight = int(max_num * 1.1 / 2)

        if weight1 > overweight:            # need to adjust
            distance = {}
            for i in range(len(ID1_new)):           # far from cluster1 and close to cluster2
                distance[ID1_new[i]] = pow(self.position[ID1_new[i]][0] - center1_new[0], 2) + pow(self.position[ID1_new[i]][1] - center1_new[1], 2) - pow(self.position[ID1_new[i]][0] - center2_new[0], 2) - pow(self.position[ID1_new[i]][1] - center2_new[1], 2)
            reverse_distance = {value : key for key, value in distance.items()}
            new_distance = sorted(reverse_distance.items(),key=lambda item:item[0],reverse=True)
            #print(new_distance)
            num = 0
            while weight1 > overweight:
                get = new_distance[num][1]
                if weight2 + self.weight[get] > overweight:     # cannot change
                    num += 1
                    continue
                else:
                    weight1 -= self.weight[get]         # adjust it to cluster2
                    ID1_new.remove(get)
                    weight2 += self.weight[get]
                    ID2_new.append(get)
                    #print(get)
                num += 1

        if weight2 > overweight:                # the same
            distance = {}
            for i in range(len(ID2_new)):  # far from cluster1 and close to cluster2
                distance[ID2_new[i]] = pow(self.position[ID2_new[i]][0] - center2_new[0], 2) + pow(self.position[ID2_new[i]][1] - center2_new[1], 2) - pow(self.position[ID2_new[i]][0] - center1_new[0], 2) - pow(self.position[ID2_new[i]][1] - center1_new[1], 2)
            reverse_distance = {value: key for key, value in distance.items()}
            new_distance = sorted(reverse_distance.items(), key=lambda item: item[0], reverse=True)
            # print(new_distance)
            num = 0
            while weight2 > overweight:
                get = new_distance[num][1]
                if weight1 + self.weight[get] > overweight:  # cannot change
                    num += 1
                    continue
                else:
                    weight2 -= self.weight[get]  # adjust it to cluster2
                    ID2_new.remove(get)
                    weight1 += self.weight[get]
                    ID1_new.append(get)
                    # print(get)
                num += 1

        print(ID1_new)
        print(ID2_new)
        return [ID1_new,ID2_new]

        # print(center1_new)
        # print(center2_new)



