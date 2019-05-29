#!/usr/bin/env python
# _*_ coding:utf-8 _*_

import random
import math

# LINE_OF_POINTS = 10
# NUM_OF_POINTS = 100
# MAP_SIZE = 50.0
# RECEIVE_POINT_NUM = 15
# RECEIVE_THING_NUM = 10

NUM_OF_POINTS = 114

class GENERATOR(object):

    def __init__(self):
        self.x = []
        self.y = []
        self.send = []
        self.receive = []

    def generate_point(self,point_file,start,end_information):

        f = open(point_file,'w') # clean up the file
        f.truncate()
        f.close()

        f = open(point_file,'a')

        for i in range(NUM_OF_POINTS):
            if i in end_information.keys():
                self.receive.append(end_information[i])
            else:
                self.receive.append(0)

        send = sum(self.receive)

        for i in range(NUM_OF_POINTS):
            if i == start:
                self.send.append(send)
            else:
                self.send.append(0)

        # example = random.sample(range(NUM_OF_POINTS),RECEIVE_POINT_NUM+1) # random send/receive point ID
        #
        # for i in range(NUM_OF_POINTS): # random send num
        #     if i in example[1:RECEIVE_POINT_NUM+1]:
        #         receive = random.randint(1,RECEIVE_THING_NUM)
        #         self.receive.append(receive)
        #     else:
        #         self.receive.append(0)
        #
        # send = sum(self.receive) # calculate receive num
        # for i in range(NUM_OF_POINTS):
        #     if i==example[0]:
        #         self.send.append(send)
        #     else:
        #         self.send.append(0)



        # for i in range(NUM_OF_POINTS):
        #     x_sand = i % LINE_OF_POINTS + 1 # x
        #     x = random.uniform(x_sand * MAP_SIZE - 5.0, x_sand * MAP_SIZE + 5.0)
        #     y_sand = i // LINE_OF_POINTS + 1 # y
        #     y = random.uniform(y_sand * MAP_SIZE - 5.0, y_sand * MAP_SIZE + 5.0)
        #     self.x.append(x)
        #     self.y.append(y)
        #
        #     result = str(x) + " " + str(y) + " " + str(self.send[i]) + " " + str(self.receive[i])
        #     f.write(result+"\n")

        self.x.append(41) #0
        self.y.append(690)
        self.x.append(61)
        self.y.append(696)
        self.x.append(166)
        self.y.append(731)
        self.x.append(240)
        self.y.append(767)
        self.x.append(111)
        self.y.append(533)
        self.x.append(123)
        self.y.append(534)
        self.x.append(226)
        self.y.append(585)
        self.x.append(269)
        self.y.append(656)
        self.x.append(303)
        self.y.append(616)
        self.x.append(202)
        self.y.append(524)
        self.x.append(240)  #10
        self.y.append(541)
        self.x.append(289)
        self.y.append(545)
        self.x.append(330)
        self.y.append(602)
        self.x.append(268)
        self.y.append(481)
        self.x.append(316)
        self.y.append(505)
        self.x.append(380)
        self.y.append(575)
        self.x.append(240)
        self.y.append(427)
        self.x.append(282)
        self.y.append(450)
        self.x.append(297)
        self.y.append(420)
        self.x.append(363)
        self.y.append(466)
        self.x.append(384)  #20
        self.y.append(487)
        self.x.append(428)
        self.y.append(550)
        self.x.append(312)
        self.y.append(393)
        self.x.append(356)
        self.y.append(427)
        self.x.append(472)
        self.y.append(526)
        self.x.append(347)
        self.y.append(396)
        self.x.append(393)
        self.y.append(417)
        self.x.append(486)
        self.y.append(524)
        self.x.append(191)
        self.y.append(346)
        self.x.append(205)
        self.y.append(355)
        self.x.append(330)  #30
        self.y.append(338)
        self.x.append(297)
        self.y.append(325)
        self.x.append(288)
        self.y.append(302)
        self.x.append(259)
        self.y.append(288)
        self.x.append(339)
        self.y.append(322)
        self.x.append(397)
        self.y.append(342)
        self.x.append(430)
        self.y.append(372)
        self.x.append(139)
        self.y.append(108)
        self.x.append(249)
        self.y.append(154)
        self.x.append(274)
        self.y.append(164)
        self.x.append(288)  #40
        self.y.append(173)
        self.x.append(164)
        self.y.append(67)
        self.x.append(272)
        self.y.append(110)
        self.x.append(306)
        self.y.append(76)
        self.x.append(364)
        self.y.append(78)
        self.x.append(372)
        self.y.append(88)
        self.x.append(397)
        self.y.append(136)
        self.x.append(342)
        self.y.append(189)
        self.x.append(375)
        self.y.append(33)
        self.x.append(400)
        self.y.append(73)
        self.x.append(405)  #50
        self.y.append(75)
        self.x.append(439)
        self.y.append(116)
        self.x.append(534)
        self.y.append(99)
        self.x.append(566)
        self.y.append(131)
        self.x.append(555)
        self.y.append(90)
        self.x.append(540)
        self.y.append(32)
        self.x.append(539)
        self.y.append(13)
        self.x.append(597)
        self.y.append(214)
        self.x.append(517)
        self.y.append(229)
        self.x.append(435)
        self.y.append(308)
        self.x.append(366)  #60
        self.y.append(248)
        self.x.append(492)
        self.y.append(356)
        self.x.append(610)
        self.y.append(322)
        self.x.append(642)
        self.y.append(213)
        self.x.append(649)
        self.y.append(107)
        self.x.append(601)
        self.y.append(475)
        self.x.append(523)
        self.y.append(504)
        self.x.append(496)
        self.y.append(469)
        self.x.append(751)
        self.y.append(56)
        self.x.append(780)
        self.y.append(61)
        self.x.append(784)  #70
        self.y.append(43)
        self.x.append(818)
        self.y.append(66)
        self.x.append(824)
        self.y.append(50)
        self.x.append(743)
        self.y.append(119)
        self.x.append(829)
        self.y.append(133)
        self.x.append(842)
        self.y.append(69)
        self.x.append(881)
        self.y.append(147)
        self.x.append(853)
        self.y.append(327)
        self.x.append(812)
        self.y.append(326)
        self.x.append(807)
        self.y.append(345)
        self.x.append(873)  #80
        self.y.append(360)
        self.x.append(872)
        self.y.append(426)
        self.x.append(656)
        self.y.append(393)
        self.x.append(917)
        self.y.append(369)
        self.x.append(871)
        self.y.append(479)
        self.x.append(802)
        self.y.append(469)
        self.x.append(722)
        self.y.append(458)
        self.x.append(1062)
        self.y.append(88)
        self.x.append(1056)
        self.y.append(108)
        self.x.append(982)
        self.y.append(252)
        self.x.append(1127)  #90
        self.y.append(288)
        self.x.append(1113)
        self.y.append(403)
        self.x.append(1037)
        self.y.append(401)
        self.x.append(1008)
        self.y.append(400)
        self.x.append(938)
        self.y.append(337)
        self.x.append(1031)
        self.y.append(499)
        self.x.append(865)
        self.y.append(496)
        self.x.append(969)
        self.y.append(527)
        self.x.append(958)
        self.y.append(601)
        self.x.append(898)
        self.y.append(642)
        self.x.append(830)  #100
        self.y.append(744)
        self.x.append(728)
        self.y.append(624)
        self.x.append(676)
        self.y.append(667)
        self.x.append(676)
        self.y.append(575)
        self.x.append(804)
        self.y.append(554)
        self.x.append(801)
        self.y.append(494)
        self.x.append(713)
        self.y.append(481)
        self.x.append(663)
        self.y.append(527)
        self.x.append(677)
        self.y.append(552)
        self.x.append(636)
        self.y.append(530)
        self.x.append(534) #110
        self.y.append(608)
        self.x.append(430)
        self.y.append(602)
        self.x.append(632)
        self.y.append(706)
        self.x.append(673)
        self.y.append(725)

        for i in range(NUM_OF_POINTS):
            f.write(str(self.x[i]) + " " + str(self.y[i]) + " " + str(self.send[i]) + " " + str(self.receive[i]) + "\n")

        f.close()

    def generate_line(self,line_file):
        f = open(line_file, 'w') # clean up the file
        f.truncate()
        f.close()

        f = open(line_file,'a')

        # for i in range(NUM_OF_POINTS):
        #     if i % LINE_OF_POINTS != (LINE_OF_POINTS-1): # start and end in row
        #         start = i
        #         end = start + 1
        #         distance = math.sqrt((self.x[start]-self.x[end])**2+(self.y[start]-self.y[end])**2)
        #         cost = random.uniform(distance-5.0,distance+5.0)
        #         f.write(str(start) + " " + str(end) + " " + str(cost) + "\n")
        #     if i // LINE_OF_POINTS != (LINE_OF_POINTS-1): # start and end in col
        #         start = i
        #         end = start + LINE_OF_POINTS
        #         distance = math.sqrt((self.x[start] - self.x[end]) ** 2 + (self.y[start] - self.y[end]) ** 2)
        #         cost = random.uniform(distance-5.0,distance+5.0)
        #         f.write(str(start) + " " + str(end) + " " + str(cost) + "\n")

        f.write(str(0) + " " + str(1) + " " + str(
            math.sqrt(pow(self.x[0] - self.x[1], 2) + pow(self.y[0] - self.y[1], 2))) + "\n")
        f.write(str(0) + " " + str(4) + " " + str(
            math.sqrt(pow(self.x[0] - self.x[4], 2) + pow(self.y[0] - self.y[4], 2))) + "\n")
        f.write(str(1) + " " + str(2) + " " + str(
            math.sqrt(pow(self.x[1] - self.x[2], 2) + pow(self.y[1] - self.y[2], 2))) + "\n")
        f.write(str(1) + " " + str(5) + " " + str(
            math.sqrt(pow(self.x[1] - self.x[5], 2) + pow(self.y[1] - self.y[5], 2))) + "\n")
        f.write(str(2) + " " + str(3) + " " + str(
            math.sqrt(pow(self.x[2] - self.x[3], 2) + pow(self.y[2] - self.y[3], 2))) + "\n")
        f.write(str(2) + " " + str(6) + " " + str(
            math.sqrt(pow(self.x[2] - self.x[6], 2) + pow(self.y[2] - self.y[6], 2))) + "\n")
        f.write(str(3) + " " + str(7) + " " + str(
            math.sqrt(pow(self.x[3] - self.x[7], 2) + pow(self.y[3] - self.y[7], 2))) + "\n")
        f.write(str(4) + " " + str(5) + " " + str(
            math.sqrt(pow(self.x[4] - self.x[5], 2) + pow(self.y[4] - self.y[5], 2))) + "\n")
        f.write(str(4) + " " + str(28) + " " + str(
            math.sqrt(pow(self.x[4] - self.x[28], 2) + pow(self.y[4] - self.y[28], 2))) + "\n")
        f.write(str(5) + " " + str(6) + " " + str(
            math.sqrt(pow(self.x[5] - self.x[6], 2) + pow(self.y[5] - self.y[6], 2))) + "\n")
        f.write(str(5) + " " + str(29) + " " + str(
            math.sqrt(pow(self.x[5] - self.x[29], 2) + pow(self.y[5] - self.y[29], 2))) + "\n")
        f.write(str(6) + " " + str(8) + " " + str(
            math.sqrt(pow(self.x[6] - self.x[8], 2) + pow(self.y[6] - self.y[8], 2))) + "\n")
        f.write(str(6) + " " + str(10) + " " + str(
            math.sqrt(pow(self.x[6] - self.x[10], 2) + pow(self.y[6] - self.y[10], 2))) + "\n")
        f.write(str(7) + " " + str(8) + " " + str(
            math.sqrt(pow(self.x[7] - self.x[8], 2) + pow(self.y[7] - self.y[8], 2))) + "\n")
        f.write(str(8) + " " + str(12) + " " + str(
            math.sqrt(pow(self.x[8] - self.x[12], 2) + pow(self.y[8] - self.y[12], 2))) + "\n")
        f.write(str(9) + " " + str(10) + " " + str(
            math.sqrt(pow(self.x[9] - self.x[10], 2) + pow(self.y[9] - self.y[10], 2))) + "\n")
        f.write(str(10) + " " + str(13) + " " + str(
            math.sqrt(pow(self.x[10] - self.x[13], 2) + pow(self.y[10] - self.y[13], 2))) + "\n")
        f.write(str(11) + " " + str(12) + " " + str(
            math.sqrt(pow(self.x[11] - self.x[12], 2) + pow(self.y[11] - self.y[12], 2))) + "\n")
        f.write(str(12) + " " + str(15) + " " + str(
            math.sqrt(pow(self.x[12] - self.x[15], 2) + pow(self.y[12] - self.y[15], 2))) + "\n")
        f.write(str(13) + " " + str(14) + " " + str(
            math.sqrt(pow(self.x[13] - self.x[14], 2) + pow(self.y[13] - self.y[14], 2))) + "\n")
        f.write(str(13) + " " + str(17) + " " + str(
            math.sqrt(pow(self.x[13] - self.x[17], 2) + pow(self.y[13] - self.y[17], 2))) + "\n")
        f.write(str(14) + " " + str(15) + " " + str(
            math.sqrt(pow(self.x[14] - self.x[15], 2) + pow(self.y[14] - self.y[15], 2))) + "\n")
        f.write(str(15) + " " + str(21) + " " + str(
            math.sqrt(pow(self.x[15] - self.x[21], 2) + pow(self.y[15] - self.y[21], 2))) + "\n")
        f.write(str(15) + " " + str(111) + " " + str(
            math.sqrt(pow(self.x[15] - self.x[111], 2) + pow(self.y[15] - self.y[111], 2))) + "\n")
        f.write(str(16) + " " + str(17) + " " + str(
            math.sqrt(pow(self.x[16] - self.x[17], 2) + pow(self.y[16] - self.y[17], 2))) + "\n")
        f.write(str(17) + " " + str(18) + " " + str(
            math.sqrt(pow(self.x[17] - self.x[18], 2) + pow(self.y[17] - self.y[18], 2))) + "\n")
        f.write(str(18) + " " + str(19) + " " + str(
            math.sqrt(pow(self.x[18] - self.x[19], 2) + pow(self.y[18] - self.y[19], 2))) + "\n")
        f.write(str(18) + " " + str(22) + " " + str(
            math.sqrt(pow(self.x[18] - self.x[22], 2) + pow(self.y[18] - self.y[22], 2))) + "\n")
        f.write(str(20) + " " + str(21) + " " + str(
            math.sqrt(pow(self.x[20] - self.x[21], 2) + pow(self.y[20] - self.y[21], 2))) + "\n")
        f.write(str(21) + " " + str(24) + " " + str(
            math.sqrt(pow(self.x[21] - self.x[24], 2) + pow(self.y[21] - self.y[24], 2))) + "\n")
        f.write(str(22) + " " + str(23) + " " + str(
            math.sqrt(pow(self.x[22] - self.x[23], 2) + pow(self.y[22] - self.y[23], 2))) + "\n")
        f.write(str(22) + " " + str(25) + " " + str(
            math.sqrt(pow(self.x[22] - self.x[25], 2) + pow(self.y[22] - self.y[25], 2))) + "\n")
        f.write(str(22) + " " + str(29) + " " + str(
            math.sqrt(pow(self.x[22] - self.x[29], 2) + pow(self.y[22] - self.y[29], 2))) + "\n")
        f.write(str(22) + " " + str(30) + " " + str(
            math.sqrt(pow(self.x[22] - self.x[30], 2) + pow(self.y[22] - self.y[30], 2))) + "\n")
        f.write(str(23) + " " + str(24) + " " + str(
            math.sqrt(pow(self.x[23] - self.x[24], 2) + pow(self.y[23] - self.y[24], 2))) + "\n")
        f.write(str(24) + " " + str(27) + " " + str(
            math.sqrt(pow(self.x[24] - self.x[27], 2) + pow(self.y[24] - self.y[27], 2))) + "\n")
        f.write(str(25) + " " + str(26) + " " + str(
            math.sqrt(pow(self.x[25] - self.x[26], 2) + pow(self.y[25] - self.y[26], 2))) + "\n")
        f.write(str(26) + " " + str(27) + " " + str(
            math.sqrt(pow(self.x[26] - self.x[27], 2) + pow(self.y[26] - self.y[27], 2))) + "\n")
        f.write(str(27) + " " + str(66) + " " + str(
            math.sqrt(pow(self.x[27] - self.x[66], 2) + pow(self.y[27] - self.y[66], 2))) + "\n")
        f.write(str(28) + " " + str(29) + " " + str(
            math.sqrt(pow(self.x[28] - self.x[29], 2) + pow(self.y[28] - self.y[29], 2))) + "\n")
        f.write(str(28) + " " + str(39) + " " + str(
            math.sqrt(pow(self.x[28] - self.x[39], 2) + pow(self.y[28] - self.y[39], 2))) + "\n")
        f.write(str(29) + " " + str(40) + " " + str(
            math.sqrt(pow(self.x[29] - self.x[40], 2) + pow(self.y[29] - self.y[40], 2))) + "\n")
        f.write(str(30) + " " + str(31) + " " + str(
            math.sqrt(pow(self.x[30] - self.x[31], 2) + pow(self.y[30] - self.y[31], 2))) + "\n")
        f.write(str(30) + " " + str(34) + " " + str(
            math.sqrt(pow(self.x[30] - self.x[34], 2) + pow(self.y[30] - self.y[34], 2))) + "\n")
        f.write(str(31) + " " + str(32) + " " + str(
            math.sqrt(pow(self.x[31] - self.x[32], 2) + pow(self.y[31] - self.y[32], 2))) + "\n")
        f.write(str(32) + " " + str(33) + " " + str(
            math.sqrt(pow(self.x[32] - self.x[33], 2) + pow(self.y[32] - self.y[33], 2))) + "\n")
        f.write(str(34) + " " + str(35) + " " + str(
            math.sqrt(pow(self.x[34] - self.x[35], 2) + pow(self.y[34] - self.y[35], 2))) + "\n")
        f.write(str(34) + " " + str(60) + " " + str(
            math.sqrt(pow(self.x[34] - self.x[60], 2) + pow(self.y[34] - self.y[60], 2))) + "\n")
        f.write(str(35) + " " + str(36) + " " + str(
            math.sqrt(pow(self.x[35] - self.x[36], 2) + pow(self.y[35] - self.y[36], 2))) + "\n")
        f.write(str(37) + " " + str(38) + " " + str(
            math.sqrt(pow(self.x[37] - self.x[38], 2) + pow(self.y[37] - self.y[38], 2))) + "\n")
        f.write(str(37) + " " + str(41) + " " + str(
            math.sqrt(pow(self.x[37] - self.x[41], 2) + pow(self.y[37] - self.y[41], 2))) + "\n")
        f.write(str(38) + " " + str(39) + " " + str(
            math.sqrt(pow(self.x[38] - self.x[39], 2) + pow(self.y[38] - self.y[39], 2))) + "\n")
        f.write(str(38) + " " + str(42) + " " + str(
            math.sqrt(pow(self.x[38] - self.x[42], 2) + pow(self.y[38] - self.y[42], 2))) + "\n")
        f.write(str(39) + " " + str(40) + " " + str(
            math.sqrt(pow(self.x[39] - self.x[40], 2) + pow(self.y[39] - self.y[40], 2))) + "\n")
        f.write(str(39) + " " + str(44) + " " + str(
            math.sqrt(pow(self.x[39] - self.x[44], 2) + pow(self.y[39] - self.y[44], 2))) + "\n")
        f.write(str(40) + " " + str(45) + " " + str(
            math.sqrt(pow(self.x[40] - self.x[45], 2) + pow(self.y[40] - self.y[45], 2))) + "\n")
        f.write(str(40) + " " + str(60) + " " + str(
            math.sqrt(pow(self.x[40] - self.x[60], 2) + pow(self.y[40] - self.y[60], 2))) + "\n")
        f.write(str(41) + " " + str(42) + " " + str(
            math.sqrt(pow(self.x[41] - self.x[42], 2) + pow(self.y[41] - self.y[42], 2))) + "\n")
        f.write(str(42) + " " + str(43) + " " + str(
            math.sqrt(pow(self.x[42] - self.x[43], 2) + pow(self.y[42] - self.y[43], 2))) + "\n")
        f.write(str(43) + " " + str(48) + " " + str(
            math.sqrt(pow(self.x[43] - self.x[48], 2) + pow(self.y[43] - self.y[48], 2))) + "\n")
        f.write(str(44) + " " + str(45) + " " + str(
            math.sqrt(pow(self.x[44] - self.x[45], 2) + pow(self.y[44] - self.y[45], 2))) + "\n")
        f.write(str(44) + " " + str(49) + " " + str(
            math.sqrt(pow(self.x[44] - self.x[49], 2) + pow(self.y[44] - self.y[49], 2))) + "\n")
        f.write(str(45) + " " + str(46) + " " + str(
            math.sqrt(pow(self.x[45] - self.x[46], 2) + pow(self.y[45] - self.y[46], 2))) + "\n")
        f.write(str(45) + " " + str(50) + " " + str(
            math.sqrt(pow(self.x[45] - self.x[50], 2) + pow(self.y[45] - self.y[50], 2))) + "\n")
        f.write(str(46) + " " + str(47) + " " + str(
            math.sqrt(pow(self.x[46] - self.x[47], 2) + pow(self.y[46] - self.y[47], 2))) + "\n")
        f.write(str(48) + " " + str(49) + " " + str(
            math.sqrt(pow(self.x[48] - self.x[49], 2) + pow(self.y[48] - self.y[49], 2))) + "\n")
        f.write(str(49) + " " + str(50) + " " + str(
            math.sqrt(pow(self.x[49] - self.x[50], 2) + pow(self.y[49] - self.y[50], 2))) + "\n")
        f.write(str(49) + " " + str(56) + " " + str(
            math.sqrt(pow(self.x[49] - self.x[56], 2) + pow(self.y[49] - self.y[56], 2))) + "\n")
        f.write(str(50) + " " + str(51) + " " + str(
            math.sqrt(pow(self.x[50] - self.x[51], 2) + pow(self.y[50] - self.y[51], 2))) + "\n")
        f.write(str(50) + " " + str(55) + " " + str(
            math.sqrt(pow(self.x[50] - self.x[55], 2) + pow(self.y[50] - self.y[55], 2))) + "\n")
        f.write(str(51) + " " + str(52) + " " + str(
            math.sqrt(pow(self.x[51] - self.x[52], 2) + pow(self.y[51] - self.y[52], 2))) + "\n")
        f.write(str(52) + " " + str(53) + " " + str(
            math.sqrt(pow(self.x[52] - self.x[53], 2) + pow(self.y[52] - self.y[53], 2))) + "\n")
        f.write(str(52) + " " + str(54) + " " + str(
            math.sqrt(pow(self.x[52] - self.x[54], 2) + pow(self.y[52] - self.y[54], 2))) + "\n")
        f.write(str(53) + " " + str(57) + " " + str(
            math.sqrt(pow(self.x[53] - self.x[57], 2) + pow(self.y[53] - self.y[57], 2))) + "\n")
        f.write(str(54) + " " + str(55) + " " + str(
            math.sqrt(pow(self.x[54] - self.x[55], 2) + pow(self.y[54] - self.y[55], 2))) + "\n")
        f.write(str(54) + " " + str(64) + " " + str(
            math.sqrt(pow(self.x[54] - self.x[64], 2) + pow(self.y[54] - self.y[64], 2))) + "\n")
        f.write(str(55) + " " + str(56) + " " + str(
            math.sqrt(pow(self.x[55] - self.x[56], 2) + pow(self.y[55] - self.y[56], 2))) + "\n")
        f.write(str(55) + " " + str(68) + " " + str(
            math.sqrt(pow(self.x[55] - self.x[68], 2) + pow(self.y[55] - self.y[68], 2))) + "\n")
        f.write(str(56) + " " + str(70) + " " + str(
            math.sqrt(pow(self.x[56] - self.x[70], 2) + pow(self.y[56] - self.y[70], 2))) + "\n")
        f.write(str(57) + " " + str(58) + " " + str(
            math.sqrt(pow(self.x[57] - self.x[58], 2) + pow(self.y[57] - self.y[58], 2))) + "\n")
        f.write(str(57) + " " + str(63) + " " + str(
            math.sqrt(pow(self.x[57] - self.x[63], 2) + pow(self.y[57] - self.y[63], 2))) + "\n")
        f.write(str(58) + " " + str(59) + " " + str(
            math.sqrt(pow(self.x[58] - self.x[59], 2) + pow(self.y[58] - self.y[59], 2))) + "\n")
        f.write(str(59) + " " + str(60) + " " + str(
            math.sqrt(pow(self.x[59] - self.x[60], 2) + pow(self.y[59] - self.y[60], 2))) + "\n")
        f.write(str(59) + " " + str(61) + " " + str(
            math.sqrt(pow(self.x[59] - self.x[61], 2) + pow(self.y[59] - self.y[61], 2))) + "\n")
        f.write(str(61) + " " + str(62) + " " + str(
            math.sqrt(pow(self.x[61] - self.x[62], 2) + pow(self.y[61] - self.y[62], 2))) + "\n")
        f.write(str(61) + " " + str(65) + " " + str(
            math.sqrt(pow(self.x[61] - self.x[65], 2) + pow(self.y[61] - self.y[65], 2))) + "\n")
        f.write(str(62) + " " + str(63) + " " + str(
            math.sqrt(pow(self.x[62] - self.x[63], 2) + pow(self.y[62] - self.y[63], 2))) + "\n")
        f.write(str(62) + " " + str(79) + " " + str(
            math.sqrt(pow(self.x[62] - self.x[79], 2) + pow(self.y[62] - self.y[79], 2))) + "\n")
        f.write(str(63) + " " + str(64) + " " + str(
            math.sqrt(pow(self.x[63] - self.x[64], 2) + pow(self.y[63] - self.y[64], 2))) + "\n")
        f.write(str(64) + " " + str(73) + " " + str(
            math.sqrt(pow(self.x[64] - self.x[73], 2) + pow(self.y[64] - self.y[73], 2))) + "\n")
        f.write(str(65) + " " + str(66) + " " + str(
            math.sqrt(pow(self.x[65] - self.x[66], 2) + pow(self.y[65] - self.y[66], 2))) + "\n")
        f.write(str(65) + " " + str(86) + " " + str(
            math.sqrt(pow(self.x[65] - self.x[86], 2) + pow(self.y[65] - self.y[86], 2))) + "\n")
        f.write(str(65) + " " + str(109) + " " + str(
            math.sqrt(pow(self.x[65] - self.x[109], 2) + pow(self.y[65] - self.y[109], 2))) + "\n")
        f.write(str(66) + " " + str(67) + " " + str(
            math.sqrt(pow(self.x[66] - self.x[67], 2) + pow(self.y[66] - self.y[67], 2))) + "\n")
        f.write(str(68) + " " + str(69) + " " + str(
            math.sqrt(pow(self.x[68] - self.x[69], 2) + pow(self.y[68] - self.y[69], 2))) + "\n")
        f.write(str(68) + " " + str(73) + " " + str(
            math.sqrt(pow(self.x[68] - self.x[73], 2) + pow(self.y[68] - self.y[73], 2))) + "\n")
        f.write(str(69) + " " + str(70) + " " + str(
            math.sqrt(pow(self.x[69] - self.x[70], 2) + pow(self.y[69] - self.y[70], 2))) + "\n")
        f.write(str(69) + " " + str(71) + " " + str(
            math.sqrt(pow(self.x[69] - self.x[71], 2) + pow(self.y[69] - self.y[71], 2))) + "\n")
        f.write(str(70) + " " + str(72) + " " + str(
            math.sqrt(pow(self.x[70] - self.x[72], 2) + pow(self.y[70] - self.y[72], 2))) + "\n")
        f.write(str(71) + " " + str(72) + " " + str(
            math.sqrt(pow(self.x[71] - self.x[72], 2) + pow(self.y[71] - self.y[72], 2))) + "\n")
        f.write(str(71) + " " + str(75) + " " + str(
            math.sqrt(pow(self.x[71] - self.x[75], 2) + pow(self.y[71] - self.y[75], 2))) + "\n")
        f.write(str(72) + " " + str(87) + " " + str(
            math.sqrt(pow(self.x[72] - self.x[87], 2) + pow(self.y[72] - self.y[87], 2))) + "\n")
        f.write(str(73) + " " + str(74) + " " + str(
            math.sqrt(pow(self.x[73] - self.x[74], 2) + pow(self.y[73] - self.y[74], 2))) + "\n")
        f.write(str(74) + " " + str(75) + " " + str(
            math.sqrt(pow(self.x[74] - self.x[75], 2) + pow(self.y[74] - self.y[75], 2))) + "\n")
        f.write(str(74) + " " + str(76) + " " + str(
            math.sqrt(pow(self.x[74] - self.x[76], 2) + pow(self.y[74] - self.y[76], 2))) + "\n")
        f.write(str(75) + " " + str(88) + " " + str(
            math.sqrt(pow(self.x[75] - self.x[88], 2) + pow(self.y[75] - self.y[88], 2))) + "\n")
        f.write(str(76) + " " + str(77) + " " + str(
            math.sqrt(pow(self.x[76] - self.x[77], 2) + pow(self.y[76] - self.y[77], 2))) + "\n")
        f.write(str(77) + " " + str(78) + " " + str(
            math.sqrt(pow(self.x[77] - self.x[78], 2) + pow(self.y[77] - self.y[78], 2))) + "\n")
        f.write(str(78) + " " + str(79) + " " + str(
            math.sqrt(pow(self.x[78] - self.x[79], 2) + pow(self.y[78] - self.y[79], 2))) + "\n")
        f.write(str(79) + " " + str(80) + " " + str(
            math.sqrt(pow(self.x[79] - self.x[80], 2) + pow(self.y[79] - self.y[80], 2))) + "\n")
        f.write(str(80) + " " + str(81) + " " + str(
            math.sqrt(pow(self.x[80] - self.x[81], 2) + pow(self.y[80] - self.y[81], 2))) + "\n")
        f.write(str(80) + " " + str(83) + " " + str(
            math.sqrt(pow(self.x[80] - self.x[83], 2) + pow(self.y[80] - self.y[83], 2))) + "\n")
        f.write(str(81) + " " + str(82) + " " + str(
            math.sqrt(pow(self.x[81] - self.x[82], 2) + pow(self.y[81] - self.y[82], 2))) + "\n")
        f.write(str(81) + " " + str(83) + " " + str(
            math.sqrt(pow(self.x[81] - self.x[83], 2) + pow(self.y[81] - self.y[83], 2))) + "\n")
        f.write(str(81) + " " + str(84) + " " + str(
            math.sqrt(pow(self.x[81] - self.x[84], 2) + pow(self.y[81] - self.y[84], 2))) + "\n")
        f.write(str(83) + " " + str(94) + " " + str(
            math.sqrt(pow(self.x[83] - self.x[94], 2) + pow(self.y[83] - self.y[94], 2))) + "\n")
        f.write(str(84) + " " + str(85) + " " + str(
            math.sqrt(pow(self.x[84] - self.x[85], 2) + pow(self.y[84] - self.y[85], 2))) + "\n")
        f.write(str(84) + " " + str(95) + " " + str(
            math.sqrt(pow(self.x[84] - self.x[95], 2) + pow(self.y[84] - self.y[95], 2))) + "\n")
        f.write(str(84) + " " + str(96) + " " + str(
            math.sqrt(pow(self.x[84] - self.x[96], 2) + pow(self.y[84] - self.y[96], 2))) + "\n")
        f.write(str(85) + " " + str(86) + " " + str(
            math.sqrt(pow(self.x[85] - self.x[86], 2) + pow(self.y[85] - self.y[86], 2))) + "\n")
        f.write(str(85) + " " + str(105) + " " + str(
            math.sqrt(pow(self.x[85] - self.x[105], 2) + pow(self.y[85] - self.y[105], 2))) + "\n")
        f.write(str(87) + " " + str(88) + " " + str(
            math.sqrt(pow(self.x[87] - self.x[88], 2) + pow(self.y[87] - self.y[88], 2))) + "\n")
        f.write(str(88) + " " + str(89) + " " + str(
            math.sqrt(pow(self.x[88] - self.x[89], 2) + pow(self.y[88] - self.y[89], 2))) + "\n")
        f.write(str(89) + " " + str(90) + " " + str(
            math.sqrt(pow(self.x[89] - self.x[90], 2) + pow(self.y[89] - self.y[90], 2))) + "\n")
        f.write(str(89) + " " + str(94) + " " + str(
            math.sqrt(pow(self.x[89] - self.x[94], 2) + pow(self.y[89] - self.y[94], 2))) + "\n")
        f.write(str(90) + " " + str(91) + " " + str(
            math.sqrt(pow(self.x[90] - self.x[91], 2) + pow(self.y[90] - self.y[91], 2))) + "\n")
        f.write(str(91) + " " + str(92) + " " + str(
            math.sqrt(pow(self.x[91] - self.x[92], 2) + pow(self.y[91] - self.y[92], 2))) + "\n")
        f.write(str(91) + " " + str(94) + " " + str(
            math.sqrt(pow(self.x[91] - self.x[94], 2) + pow(self.y[91] - self.y[94], 2))) + "\n")
        f.write(str(92) + " " + str(93) + " " + str(
            math.sqrt(pow(self.x[92] - self.x[93], 2) + pow(self.y[92] - self.y[93], 2))) + "\n")
        f.write(str(92) + " " + str(95) + " " + str(
            math.sqrt(pow(self.x[92] - self.x[95], 2) + pow(self.y[92] - self.y[95], 2))) + "\n")
        f.write(str(96) + " " + str(97) + " " + str(
            math.sqrt(pow(self.x[96] - self.x[97], 2) + pow(self.y[96] - self.y[97], 2))) + "\n")
        f.write(str(96) + " " + str(104) + " " + str(
            math.sqrt(pow(self.x[96] - self.x[104], 2) + pow(self.y[96] - self.y[104], 2))) + "\n")
        f.write(str(97) + " " + str(98) + " " + str(
            math.sqrt(pow(self.x[97] - self.x[98], 2) + pow(self.y[97] - self.y[98], 2))) + "\n")
        f.write(str(98) + " " + str(99) + " " + str(
            math.sqrt(pow(self.x[98] - self.x[99], 2) + pow(self.y[98] - self.y[99], 2))) + "\n")
        f.write(str(99) + " " + str(100) + " " + str(
            math.sqrt(pow(self.x[99] - self.x[100], 2) + pow(self.y[99] - self.y[100], 2))) + "\n")
        f.write(str(99) + " " + str(104) + " " + str(
            math.sqrt(pow(self.x[99] - self.x[104], 2) + pow(self.y[99] - self.y[104], 2))) + "\n")
        f.write(str(100) + " " + str(101) + " " + str(
            math.sqrt(pow(self.x[100] - self.x[101], 2) + pow(self.y[100] - self.y[101], 2))) + "\n")
        f.write(str(101) + " " + str(102) + " " + str(
            math.sqrt(pow(self.x[101] - self.x[102], 2) + pow(self.y[101] - self.y[102], 2))) + "\n")
        f.write(str(101) + " " + str(104) + " " + str(
            math.sqrt(pow(self.x[101] - self.x[104], 2) + pow(self.y[101] - self.y[104], 2))) + "\n")
        f.write(str(102) + " " + str(103) + " " + str(
            math.sqrt(pow(self.x[102] - self.x[103], 2) + pow(self.y[102] - self.y[103], 2))) + "\n")
        f.write(str(102) + " " + str(113) + " " + str(
            math.sqrt(pow(self.x[102] - self.x[113], 2) + pow(self.y[102] - self.y[113], 2))) + "\n")
        f.write(str(103) + " " + str(108) + " " + str(
            math.sqrt(pow(self.x[103] - self.x[108], 2) + pow(self.y[103] - self.y[108], 2))) + "\n")
        f.write(str(103) + " " + str(109) + " " + str(
            math.sqrt(pow(self.x[103] - self.x[109], 2) + pow(self.y[103] - self.y[109], 2))) + "\n")
        f.write(str(104) + " " + str(105) + " " + str(
            math.sqrt(pow(self.x[104] - self.x[105], 2) + pow(self.y[104] - self.y[105], 2))) + "\n")
        f.write(str(105) + " " + str(106) + " " + str(
            math.sqrt(pow(self.x[105] - self.x[106], 2) + pow(self.y[105] - self.y[106], 2))) + "\n")
        f.write(str(106) + " " + str(107) + " " + str(
            math.sqrt(pow(self.x[106] - self.x[107], 2) + pow(self.y[106] - self.y[107], 2))) + "\n")
        f.write(str(107) + " " + str(108) + " " + str(
            math.sqrt(pow(self.x[107] - self.x[108], 2) + pow(self.y[107] - self.y[108], 2))) + "\n")
        f.write(str(109) + " " + str(110) + " " + str(
            math.sqrt(pow(self.x[109] - self.x[110], 2) + pow(self.y[109] - self.y[110], 2))) + "\n")
        f.write(str(110) + " " + str(111) + " " + str(
            math.sqrt(pow(self.x[110] - self.x[111], 2) + pow(self.y[110] - self.y[111], 2))) + "\n")
        f.write(str(110) + " " + str(112) + " " + str(
            math.sqrt(pow(self.x[110] - self.x[112], 2) + pow(self.y[110] - self.y[112], 2))) + "\n")
        f.write(str(112) + " " + str(113) + " " + str(
            math.sqrt(pow(self.x[112] - self.x[113], 2) + pow(self.y[112] - self.y[113], 2))) + "\n")

        f.close()






