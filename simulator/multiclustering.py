#!/usr/bin/env python
# _*_ coding:utf-8 _*_

from sklearn.cluster import KMeans
import numpy as np

class MULTICLUSTERING(object):

    def __init__(self,position,weight,start_id,matrix):
        self.position = position                                        #(x,y)
        self.weight = weight                                            #content
        self.start_id = start_id                                        #no partition
        self.matrix = matrix                                            #get the initialization

    def partition(self, max_num, cluster_num):
        ID = []
        for i in range(len(self.matrix)):  # not contain start_id
            if i != self.start_id:
                ID.append(i)
        data = np.zeros((len(ID),2))
        for i in range(len(ID)):
            data[i][0] = self.position[ID[i]][0]
            data[i][1] = self.position[ID[i]][1]
        estimator = KMeans(n_clusters=cluster_num)
        res = estimator.fit_predict(data)
        lable_pred = estimator.labels_
        centroids = estimator.cluster_centers_
        result = [[]for i in range(cluster_num)]
        for i in range(len(ID)):
            result[lable_pred[i]].append(ID[i])                                 #clustering
        #print(result)

        weight = [0 for i in range(cluster_num)]
        for i in range(cluster_num):
            for j in range(len(result[i])):
                weight[i] += self.weight[result[i][j]]
        overweight = int(max_num * 1.2 / cluster_num)                          #get weight

        for i in range(cluster_num):
            if weight[i] <= overweight:                                         #currently not change
                continue
            distance = {}
            for j in range(len(result[i])):
                for k in range(cluster_num):
                    if k==i:
                        continue
                    inner = pow(self.position[result[i][j]][0] - centroids[i][0],2) + pow(self.position[result[i][j]][1] - centroids[i][1],2)
                    outer = pow(self.position[result[i][j]][0] - centroids[k][0],2) + pow(self.position[result[i][j]][1] - centroids[k][1],2)
                    distance[(result[i][j],k)] = inner - outer                      #{(id,cluster_id),distance}
            reverse_distance = {value: key for key, value in distance.items()}
            new_distance = sorted(reverse_distance.items(),key=lambda item:item[0],reverse=True)
            num = 0
            not_there = []
            while weight[i] > overweight:
                get_id = new_distance[num][1][0]                                #(...(distance,(id,cluster_id))...)
                get_cluster = new_distance[num][1][1]
                if get_id in not_there:                                         # remove yet
                    num += 1
                    continue
                if weight[get_cluster] + self.weight[get_id] > overweight:      # cannot change
                    num += 1
                    continue
                else:
                    weight[i] -= self.weight[get_id]
                    weight[get_cluster] += self.weight[get_id]
                    result[i].remove(get_id)
                    result[get_cluster].append(get_id)
                    not_there.append(get_id)                                    # remove yet
                    num += 1

        return result






