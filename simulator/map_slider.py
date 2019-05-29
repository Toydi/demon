from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QWidget, QSlider, QLabel, QVBoxLayout


class MapSlider(QWidget):
    def __init__(self, message_box, map_box):
        super().__init__()
        self.setObjectName("NJU-001")
        self.layout = QVBoxLayout()
        self.setLayout(self.layout)

        self.message_box = message_box
        self.map_box = map_box

        self.slider = QSlider(Qt.Horizontal, self)
        self.slider.setRange(1, 5)
        self.slider.setValue(1)
        self.slider.valueChanged.connect(lambda: self.on_change_func(self.slider))

        self.label = QLabel('map_height', self)
        self.label.setText("地图高度水平：" + str(self.slider.value()))
        self.label.setFont(QFont('Arial Black', 10))

        self.layout.addWidget(self.label)
        self.layout.addWidget(self.slider)
        self.label.setAlignment(Qt.AlignCenter)

    def on_change_func(self, slider):
        try:
            h = str(slider.value())
            self.map_box.update_map(h)
            self.label.setText("地图高度水平：" + h)
            self.message_box.append("高度调整，当前高度水平为：" + h)
        except:
            self.message_box.append("高度调整出错，未加载地图！！")


class UVASlider(QWidget):
    def __init__(self, message_box, map_box):
        super().__init__()
        self.setObjectName("NJU-001")
        self.layout = QVBoxLayout()
        self.setLayout(self.layout)

        self.message_box = message_box
        self.map_box = map_box

        self.slider = QSlider(Qt.Horizontal, self)
        self.slider.setRange(1, 5)
        self.slider.setValue(1)
        self.slider.valueChanged.connect(lambda: self.on_change_func(self.slider))

        self.label = QLabel('uva_num', self)
        self.label.setText("无人机数量：" + str(self.slider.value()))
        self.label.setFont(QFont('Arial Black', 10))

        self.layout.addWidget(self.label)
        self.layout.addWidget(self.slider)
        self.label.setAlignment(Qt.AlignCenter)

    def on_change_func(self, slider):
        n = str(slider.value())
        self.label.setText("无人机数量：" + n)
        self.message_box.append("数量调整，当前无人机数量为：" + n)
        self.map_box.uva_num = int(n)
