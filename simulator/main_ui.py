#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
import json
from PyQt5.QtWidgets import QApplication, QWidget, QGridLayout, QTextBrowser, QSlider, QLabel
from PyQt5.QtGui import QIcon, QFont
from PyQt5.QtCore import Qt

import button_sets
from map_box import MapBox
from map_slider import MapSlider, UVASlider


class MainWindow():
    def __init__(self):
        super().__init__()
        with open("./conf.json", "r+") as f:
            f.truncate()
            json.dump({}, f)

        self.main_window = QWidget()
        self.grid_1 = QGridLayout()
        self.message = QTextBrowser()
        self.button_map = QWidget()
        self.grid_2 = QGridLayout()
        self.buttons = QWidget()
        self.grid_3 = QGridLayout()
        self.map_box = MapBox(self.message)

        self.init_ui()

    def init_ui(self):
        # 主界面初始化
        self.main_window.resize(1024, 1024)  # 初始大小
        self.main_window.move(300, 10)  # 初始位置
        self.main_window.setWindowTitle('UVAProject')  # 标题
        self.main_window.setWindowIcon(QIcon('./source/uva_icon.jpg'))  # 图标

        # 页面布局-外 (button_map, message)
        self.main_window.setLayout(self.grid_1)
        self.grid_1.setRowStretch(0, 8)
        self.grid_1.setRowStretch(1, 2)

        # message
        self.grid_1.addWidget(self.message, *(1, 0))

        # (button, map)
        self.button_map.setLayout(self.grid_2)
        self.grid_2.setColumnStretch(0, 1)
        self.grid_2.setColumnStretch(1, 9)

        # map
        self.grid_2.addWidget(self.map_box, *(0, 1))

        # buttons
        self.buttons.setLayout(self.grid_3)
        self.grid_2.addWidget(self.buttons, *(0, 0))

        button_num = 0
        # load map button
        load_map_button = button_sets.LoadButton(self.message, self.map_box)
        self.grid_3.addWidget(load_map_button, *(button_num, 0))
        button_num += 1

        # show map button
        show_map_button = button_sets.ShowMapButton(self.message, self.map_box)
        self.grid_3.addWidget(show_map_button, *(button_num, 0))
        button_num += 1

        # hide map button
        hide_map_button = button_sets.HideMapButton(self.message, self.map_box)
        self.grid_3.addWidget(hide_map_button, *(button_num, 0))
        button_num += 1

        # start button
        start_button = button_sets.StartButton(self.message, self.map_box)
        self.grid_3.addWidget(start_button, *(button_num, 0))
        button_num += 1

        # end button
        end_button = button_sets.EndButton(self.message, self.map_box)
        self.grid_3.addWidget(end_button, *(button_num, 0))
        button_num += 1

        # pass button
        pass_button = button_sets.PassButton(self.message, self.map_box)
        self.grid_3.addWidget(pass_button, *(button_num, 0))
        button_num += 1

        # plan button
        plan_button = button_sets.PlanButton(self.message, self.map_box)
        self.grid_3.addWidget(plan_button, *(button_num, 0))
        button_num += 1

        # run button
        run_button = button_sets.RunButton(self.message, self.map_box)
        self.grid_3.addWidget(run_button, *(button_num, 0))
        button_num += 1

        # init button
        init_button = button_sets.InitButton(self.message, self.map_box)
        self.grid_3.addWidget(init_button, *(button_num, 0))
        button_num += 1

        # update button
        update_button = button_sets.UpdateButton(self.message, self.map_box)
        self.grid_3.addWidget(update_button, *(button_num, 0))
        button_num += 1

        # change map slider
        change_map_slider = MapSlider(self.message, self.map_box)
        self.grid_3.addWidget(change_map_slider, *(button_num, 0))
        button_num += 1

        # change uva slider
        change_uva_slider = UVASlider(self.message, self.map_box)
        self.grid_3.addWidget(change_uva_slider, *(button_num, 0))
        button_num += 1

        for i in range(10):
            self.grid_3.setRowMinimumHeight(i, 50)

        self.message.append("初始化")
        self.grid_1.addWidget(self.button_map, *(0, 0))

    def run(self):
        self.main_window.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    uva = MainWindow()
    uva.run()
    sys.exit(app.exec_())
