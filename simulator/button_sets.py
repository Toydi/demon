from PyQt5.QtWidgets import QPushButton, QFileDialog
import json


class LoadButton(QPushButton):
    def __init__(self, message_box, map_box):
        super().__init__()
        self.setText("加载地图")
        self.setDefault(False)
        self.map_path = ""
        self.clicked.connect(self.on_click)
        self.message_box = message_box
        self.map_box = map_box

    def on_click(self):
        try:
            self.message_box.append("正在加载地图")
            self.map_path, _ = QFileDialog.getOpenFileName(self, '选择地图', './maps/', 'Image files(*.jpg *.gif *.png)')
            self.map_box.load_map(self.map_path)
            """
            conf = json.load(open("./conf.json", "r"))
            conf["map_path"] = self.map_path
            l = self.map_path.rfind("/")
            r = self.map_path.rfind(".")
            conf["map"] = self.map_path[l+1:r]
            json.dump(conf, open("./conf.json", "w"))
            """
            self.map_box.init_location()

            self.message_box.append("成功加载地图：" + self.map_path)
        except:
            self.message_box.append("无法加载地图")
        self.toggle()


class InitButton(QPushButton):
    def __init__(self, message_box, map_box):
        super().__init__()
        self.setText("初始化")
        self.setDefault(False)
        self.clicked.connect(self.on_click)
        self.message_box = message_box
        self.map_box = map_box

    def on_click(self):
        try:
            self.map_box.clear()
            self.message_box.append("初始化")
        except:
            self.message_box.append("初始化失败")
        self.toggle()


class EndButton(QPushButton):
    def __init__(self, message_box, map_box):
        super().__init__()
        self.setText("设置终点")
        self.setDefault(False)
        self.map_path = ""
        self.clicked.connect(self.on_click)
        self.message_box = message_box
        self.map_box = map_box

    def on_click(self):
        self.map_box.show_location("end")
        self.toggle()


class PassButton(QPushButton):
    def __init__(self, message_box, map_box):
        super().__init__()
        self.setText("设置送货地点")
        self.setDefault(False)
        self.map_path = ""
        self.clicked.connect(self.on_click)
        self.message_box = message_box
        self.map_box = map_box

    def on_click(self):
        self.map_box.show_location("pass")
        self.toggle()


class PlanButton(QPushButton):
    def __init__(self, message_box, map_box):
        super().__init__()
        self.setText("规划路径")
        self.setDefault(False)
        self.clicked.connect(self.on_click)
        self.message_box = message_box
        self.map_box = map_box

    def on_click(self):
        self.message_box.append("开始规划路径")
        self.map_box.plan_path()
        self.toggle()


class RunButton(QPushButton):
    def __init__(self, message_box, map_box):
        super().__init__()
        self.setText("运行")
        self.setDefault(False)
        self.map_path = ""
        self.clicked.connect(self.on_click)
        self.message_box = message_box
        self.map_box = map_box

    def on_click(self):
        self.message_box.append("开始执行")
        self.map_box.run_path()
        self.toggle()


class StartButton(QPushButton):
    def __init__(self, message_box, map_box):
        super().__init__()
        self.setText("设置发货地点")
        self.setDefault(False)
        self.map_path = ""
        self.clicked.connect(self.on_click)
        self.message_box = message_box
        self.map_box = map_box

    def on_click(self):
        self.map_box.show_location("start")
        self.toggle()


class UpdateButton(QPushButton):
    def __init__(self, message_box, map_box):
        super().__init__()
        self.setText("校正地图")
        self.setDefault(False)
        self.clicked.connect(self.on_click)
        self.message_box = message_box
        self.map_box = map_box

    def on_click(self):
        try:
            # self.map_box.update_map()
            self.map_box.update_location()
            self.message_box.append("地图校正")
        except:
            self.message_box.append("地图校正失败")
        self.toggle()


class ShowMapButton(QPushButton):
    def __init__(self, message_box, map_box):
        super().__init__()
        self.setText("显示地图")
        self.setDefault(False)
        self.clicked.connect(self.on_click)
        self.message_box = message_box
        self.map_box = map_box

    def on_click(self):
        try:
            if self.map_box.show_map() is True:
                self.message_box.append("显示地图")
        except:
            self.message_box.append("显示地图出错")
        self.toggle()


class HideMapButton(QPushButton):
    def __init__(self, message_box, map_box):
        super().__init__()
        self.setText("隐藏地图")
        self.setDefault(False)
        self.clicked.connect(self.on_click)
        self.message_box = message_box
        self.map_box = map_box

    def on_click(self):
        try:
            if self.map_box.hide_map() is True:
                self.message_box.append("隐藏地图")
        except:
            self.message_box.append("隐藏地图出错")
        self.toggle()