#!/usr/bin/python
# -*- coding: UTF-8 -*-
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QDoubleValidator
import sys
class Transformer_Two(QTabWidget):
    def __init__(self):
        self.left_vb = 0
        self.right_vb = 0
        self.index = 0
        self.P0 = ''
        self.PK = ''
        self.UK = ''
        self.I0 = ''
        self.ratio = ''
        self.SN = ""

        self.Rt = 0
        self.Xt = 0
        self.Bm = 0
        self.Gm = 0

        self.Z = 0
        self.Y = 0
        self.Y_N = 0
        self.Z_N = 0
        self.K_N = 0
        self.Y1 = 0
        self.Y2 = 0
        self.Y3 = 0
        super(Transformer_Two, self).__init__()

        self.setWindowTitle(str(self.index))
        self.resize(400,250)
        self.tab1 = QWidget()
        self.tab2 = QWidget()

        #将三个选项卡添加到顶层窗口中
        self.addTab(self.tab1, "input")
        self.addTab(self.tab2, "result")

        #每个选项卡自定义的内容
        self.tab1UI()
        self.tab2UI()

    def tab1UI(self):

        self.Layout = QGridLayout(self)
        self.label_v_ratio = QLabel("ratio")
        self.label_PK = QLabel("PK")
        self.label_UK = QLabel("UK")
        self.label_P0 = QLabel("P0")
        self.label_I0 = QLabel("I0")
        self.label_standard = QLabel("SN")
        self.push_button = QPushButton("确认")
        self.fromlayout = QFormLayout()#窗体布局
        self.lineedit1 = QLineEdit()
        self.lineedit1.setText(self.PK)
        self.lineedit2 = QLineEdit()
        self.lineedit2.setText(self.UK)
        self.lineedit3 = QLineEdit()
        self.lineedit3.setText(self.P0)
        self.lineedit4 = QLineEdit()
        self.lineedit4.setText(self.I0)
        self.lineedit5 = QLineEdit()
        self.lineedit5.setText(self.ratio)
        self.lineedit5.setToolTip("xx/xx")
        self.lineedit6 = QLineEdit()
        self.lineedit6.setText(self.SN)
        self.Layout.addWidget(self.label_PK,0,0)#0行 0列
        self.Layout.addWidget(self.lineedit1,0,1,1,2)
        self.Layout.addWidget(self.label_UK,1,0)#0行 0列
        self.Layout.addWidget(self.lineedit2,1,1,1,2)
        self.Layout.addWidget(self.label_P0,2,0)#0行 0列
        self.Layout.addWidget(self.lineedit3,2,1,1,2)
        self.Layout.addWidget(self.label_I0,3,0)#0行 0列
        self.Layout.addWidget(self.lineedit4,3,1,1,2)
        self.Layout.addWidget(self.label_v_ratio,4,0)
        self.Layout.addWidget(self.lineedit5,4,1,1,2)
        self.Layout.addWidget(self.label_standard,5,0)
        self.Layout.addWidget(self.lineedit6,5,1,1,2)
        self.Layout.addWidget(self.push_button,6,2,1,1)
        #设置校验器
        double_validator = QDoubleValidator(self)
        double_validator.setRange(0, 10000)
        double_validator.setDecimals(4)#小数点后4位
        double_validator.setNotation(QDoubleValidator.StandardNotation)
        self.lineedit1.setValidator(double_validator)
        self.lineedit2.setValidator(double_validator)
        self.lineedit3.setValidator(double_validator)
        self.lineedit4.setValidator(double_validator)

        self.setWindowModality(Qt.ApplicationModal)#dialog出现后mainwindow控件不可用
        self.push_button.clicked.connect(self.button_task)
        self.tab1.setLayout(self.Layout)
    def tab2UI(self):
        Layout = QFormLayout(self)
        self.vb1_line = QLineEdit()
        self.vb2_line = QLineEdit()
        self.Y_N_line = QLineEdit()
        self.Z_N_line = QLineEdit()
        self.K_N_line = QLineEdit()

        self.Y1_line = QLineEdit()
        self.Y2_line = QLineEdit()
        self.Y3_line = QLineEdit()

        Layout.addRow("Vb1", self.vb1_line)
        Layout.addRow("Vb2", self.vb2_line)
        Layout.addRow("Y_N",  self.Y_N_line)
        Layout.addRow("Z_N", self.Z_N_line)
        Layout.addRow("K_N", self.K_N_line)
        Layout.addRow("Y1",self.Y1_line)
        Layout.addRow("Y2",self.Y2_line)
        Layout.addRow("Y3",self.Y3_line)


        self.tab2.setLayout(Layout)

    def update(self):
        self.vb1_line.setText("{:.5f}".format(self.left_vb))
        self.vb2_line.setText("{:.5f}".format(self.right_vb))
        self.Y_N_line.setText("{:.5f}".format(self.Y_N))
        self.Z_N_line.setText("{:.5f}".format(self.Z_N))
        self.K_N_line.setText("{:.5f}".format(self.K_N))
        self.Y1_line.setText(("{:.5f}".format(self.Y1)))
        self.Y2_line.setText(("{:.5f}".format(self.Y2)))
        self.Y3_line.setText(("{:.5f}".format(self.Y3)))

    def button_task(self):
        self.PK = self.lineedit1.text()
        self.UK = self.lineedit2.text()
        self.P0 = self.lineedit3.text()
        self.I0 = self.lineedit4.text()
        self.ratio = self.lineedit5.text()
        self.SN = self.lineedit6.text()
        self.close()

class Gene(QTabWidget):
    def __init__(self):
        self.index = 0
        self.V = ''
        self.PN = ''

        super(Gene, self).__init__()
        self.resize(400,250)
        self.setWindowTitle(str(self.index))
        self.tab1 = QWidget()
        self.tab2 = QWidget()
        self.resize(400,250)
        self.addTab(self.tab1, "input")
        self.addTab(self.tab2, "result")
        self.tab1UI()
        self.tab2UI()


    def tab1UI(self):

        self.Layout = QGridLayout(self)
        self.V_label = QLabel("V")
        self.PN_label = QLabel("PN")


        self.push_button = QPushButton("确认")
        self.fromlayout = QFormLayout()#窗体布局
        self.lineedit1 = QLineEdit()
        self.lineedit1.setText(self.V)
        self.lineedit2 = QLineEdit()
        self.lineedit2.setText(self.PN)


        self.Layout.addWidget(self.V_label,0,0)#0行 0列
        self.Layout.addWidget(self.lineedit1,0,1,1,2)
        self.Layout.addWidget(self.PN_label,1,0)#0行 0列
        self.Layout.addWidget(self.lineedit2,1,1,1,2)

        self.Layout.addWidget(self.push_button,2,2,1,1)
        #设置校验器
        double_validator = QDoubleValidator(self)
        double_validator.setRange(0, 10000)
        double_validator.setDecimals(4)#小数点后4位
        double_validator.setNotation(QDoubleValidator.StandardNotation)
        self.lineedit1.setValidator(double_validator)
        self.lineedit2.setValidator(double_validator)

        self.setWindowModality(Qt.ApplicationModal)      #dialog出现后mainwindow控件不可用
        self.push_button.clicked.connect(self.button_task)
        self.tab1.setLayout(self.Layout)
    def button_task(self):
        self.V = self.lineedit1.text()
        self.PN = self.lineedit2.text()
        self.close()
    def tab2UI(self):
        pass
class Loader(QTabWidget):
    def __init__(self):
        self.index = 0
        self.P = ''
        self.Q = ''

        super(Loader, self).__init__()
        self.setWindowTitle(str(self.index))
        self.resize(400,250)
        self.tab1 = QWidget()
        self.tab2 = QWidget()
        self.addTab(self.tab1, "input")
        self.addTab(self.tab2, "result")
        self.tab1UI()
        self.tab2UI()

    def tab1UI(self):

        self.Layout = QGridLayout(self)
        self.P_label = QLabel("P")
        self.Q_label = QLabel("Q")

        self.push_button = QPushButton("确认")
        self.fromlayout = QFormLayout()#窗体布局
        self.lineedit1 = QLineEdit()
        self.lineedit1.setText(self.P)
        self.lineedit2 = QLineEdit()
        self.lineedit2.setText(self.Q)

        self.Layout.addWidget(self.P_label,0,0)#0行 0列
        self.Layout.addWidget(self.lineedit1,0,1,1,2)
        self.Layout.addWidget(self.Q_label,1,0)#0行 0列
        self.Layout.addWidget(self.lineedit2,1,1,1,2)

        self.Layout.addWidget(self.push_button,2,2,1,1)
        #设置校验器
        double_validator = QDoubleValidator(self)
        double_validator.setRange(0, 10000)
        double_validator.setDecimals(4)#小数点后4位
        double_validator.setNotation(QDoubleValidator.StandardNotation)
        self.lineedit1.setValidator(double_validator)
        self.lineedit2.setValidator(double_validator)

        self.setWindowModality(Qt.ApplicationModal)#dialog出现后mainwindow控件不可用
        self.push_button.clicked.connect(self.button_task)
        self.tab1.setLayout(self.Layout)
    def button_task(self):
        self.close()
    def tab2UI(self):
        pass



class Transformer_Three(QTabWidget):
    def __init__(self):
        self.node_type = 1
        self.node_p = 0
        self.node_q = 0
        self.node_v = 0
        self.node_angle = 0
        self.flag = 0


        self.index = 0
        self.left_vb = 0
        self.right_vb = 0
        self.down_vb = 0
        self.V1B = 0
        self.V2B = 0
        self.V3B = 0
        self.Y1 = 0
        self.Y2 = 0
        self.Y3 = 0
        self.Y4 = 0
        self.Y5 = 0
        self.Y6 = 0
        self.Y7 = 0
        self.Y8 = 0

        self.P12 = ''
        self.P23 = ''
        self.P31 = ''
        self.I0 = ''
        self.P0 = ''
        self.SN1 = ""
        self.SN2 = ""
        self.SN3 = ""
        self.ratio = ""
        self.V12 =''
        self.V23 =''
        self.V31 =''
        super(Transformer_Three, self).__init__()
        self.setWindowTitle(str(self.index))
        self.resize(400 ,800)
        self.tab1 = QWidget()
        self.tab2 = QWidget()
        self.tab3 = QWidget()
        self.addTab(self.tab1, "input")
        self.addTab(self.tab2, "result")
        self.addTab(self.tab3, "node")
        self.tab1UI()
        self.tab2UI()
        self.tab3UI()
    def tab1UI(self):

        self.Layout = QGridLayout(self)
        self.label_P12 = QLabel("P12")
        self.label_P23 = QLabel("P23")
        self.label_P31 = QLabel("P31")
        self.label_I0 = QLabel("I0")
        self.label_P0 = QLabel("P0")
        self.label_standard1 = QLabel("SN1")
        self.label_standard2 = QLabel("SN2")
        self.label_standard3 = QLabel("SN3")
        self.label_ratio = QLabel("Ratio")
        self.label_v12 = QLabel("V12")
        self.label_v23 = QLabel("V23")
        self.label_v31 = QLabel("V31")
        self.label_V1B = QLabel("V1B")
        self.label_V2B = QLabel("V2B")
        self.label_V3B = QLabel("V3B")

        self.push_button = QPushButton("确认")
        self.fromlayout = QFormLayout()#窗体布局
        self.lineedit1 = QLineEdit()
        self.lineedit1.setText(self.P12)
        self.lineedit2 = QLineEdit()
        self.lineedit2.setText(self.P23)
        self.lineedit3 = QLineEdit()
        self.lineedit3.setText(self.P31)
        self.lineedit4 = QLineEdit()
        self.lineedit4.setText(self.I0)
        self.lineedit5 = QLineEdit()
        self.lineedit5.setText(self.P0)
        self.lineedit6 = QLineEdit()
        self.lineedit6.setText(self.SN1)
        self.lineedit7 = QLineEdit()
        self.lineedit7.setText(self.SN2)
        self.lineedit8 = QLineEdit()
        self.lineedit8.setText(self.SN3)
        self.lineedit9 = QLineEdit()
        self.lineedit9.setText(self.ratio)
        self.lineedit9.setToolTip("xx/xx/xx")
        self.lineedit10 = QLineEdit()
        self.lineedit11 = QLineEdit()
        self.lineedit12 = QLineEdit()

        self.lineedit13 = QLineEdit()
        self.lineedit14 = QLineEdit()
        self.lineedit15 = QLineEdit()

        self.Layout.addWidget(self.label_P12,0,0)#0行 0列
        self.Layout.addWidget(self.lineedit1,0,1,1,2)
        self.Layout.addWidget(self.label_P23,1,0)#0行 0列
        self.Layout.addWidget(self.lineedit2,1,1,1,2)
        self.Layout.addWidget(self.label_P31,2,0)#0行 0列
        self.Layout.addWidget(self.lineedit3,2,1,1,2)
        self.Layout.addWidget(self.label_I0,3,0)#0行 0列
        self.Layout.addWidget(self.lineedit4,3,1,1,2)
        self.Layout.addWidget(self.label_P0,4,0)
        self.Layout.addWidget(self.lineedit5,4,1,1,2)
        self.Layout.addWidget(self.label_standard1,5,0)
        self.Layout.addWidget(self.lineedit6,5,1,1,2)
        self.Layout.addWidget(self.label_standard2,6,0)
        self.Layout.addWidget(self.lineedit7,6,1,1,2)
        self.Layout.addWidget(self.label_standard3,7,0)
        self.Layout.addWidget(self.lineedit8, 7, 1, 1, 2)
        self.Layout.addWidget(self.lineedit9, 8, 1, 1, 2)
        self.Layout.addWidget(self.label_ratio, 8, 0)
        self.Layout.addWidget(self.lineedit10, 9, 1, 1, 2)
        self.Layout.addWidget(self.label_v12, 9, 0)
        self.Layout.addWidget(self.lineedit11, 10, 1, 1, 2)
        self.Layout.addWidget(self.label_v23, 10, 0)
        self.Layout.addWidget(self.lineedit12, 11, 1, 1, 2)
        self.Layout.addWidget(self.label_v31, 11, 0)
        self.Layout.addWidget(self.lineedit13, 12, 1, 1, 2)
        self.Layout.addWidget(self.label_V1B, 12, 0)
        self.Layout.addWidget(self.lineedit14, 13, 1, 1, 2)
        self.Layout.addWidget(self.label_V2B, 13, 0)
        self.Layout.addWidget(self.lineedit15, 14, 1, 1, 2)
        self.Layout.addWidget(self.label_V3B, 14, 0)

        self.Layout.addWidget(self.push_button, 15, 2, 1, 1)
        #设置校验器
        double_validator = QDoubleValidator(self)
        double_validator.setRange(0, 10000)
        double_validator.setDecimals(4)#小数点后4位
        double_validator.setNotation(QDoubleValidator.StandardNotation)
        self.lineedit1.setValidator(double_validator)
        self.lineedit2.setValidator(double_validator)
        self.lineedit3.setValidator(double_validator)
        self.lineedit4.setValidator(double_validator)
        self.lineedit5.setValidator(double_validator)
        self.lineedit6.setValidator(double_validator)
        self.lineedit7.setValidator(double_validator)
        self.lineedit8.setValidator(double_validator)

        self.setWindowModality(Qt.ApplicationModal)#dialog出现后mainwindow控件不可用
        self.push_button.clicked.connect(self.button_task)
        self.tab1.setLayout(self.Layout)
    def button_task(self):
        self.P12 = self.lineedit1.text()
        self.P23 = self.lineedit2.text()
        self.P31 = self.lineedit3.text()
        self.I0 = self.lineedit4.text()
        self.P0 = self.lineedit5.text()
        self.SN1 = self.lineedit6.text()
        self.SN2 = self.lineedit7.text()
        self.SN3 = self.lineedit8.text()
        self.ratio = self.lineedit9.text()
        self.V12 = self.lineedit10.text()
        self.V23 = self.lineedit11.text()
        self.V31 = self.lineedit12.text()
        self.node_p = self.node_lineP.text()
        self.node_q =self.node_lineQ.text()
        self.node_v =self.node_lineV.text()
        self.node_angle =self.node_lineA.text()
        self.V1B = self.lineedit13.text()
        self.V2B = self.lineedit14.text()
        self.V3B = self.lineedit15.text()

        if self.combobox.currentIndex() == 0:
            self.node_tpye = 1
        elif self.combobox.currentIndex() == 1:
            self.node_tpye = 2
        else:
            self.node_tpye = 3
        self.flag =1
        self.close()
    def tab2UI(self):
        Layout = QFormLayout(self)
        self.vb1_line = QLineEdit()
        self.vb2_line = QLineEdit()
        self.vb3_line = QLineEdit()
        self.y1_line = QLineEdit()
        self.y2_line = QLineEdit()
        self.y3_line = QLineEdit()
        self.y4_line = QLineEdit()
        self.y5_line = QLineEdit()
        self.y6_line = QLineEdit()
        self.y7_line = QLineEdit()
        self.y8_line = QLineEdit()
        Layout.addRow("Vb1", self.vb1_line)
        Layout.addRow("Vb2", self.vb2_line)
        Layout.addRow("Vb3", self.vb3_line)
        Layout.addRow("Y1", self.y1_line)
        Layout.addRow("Y2", self.y2_line)
        Layout.addRow("Y3", self.y3_line)
        Layout.addRow("Y4", self.y4_line)
        Layout.addRow("Y5", self.y5_line)
        Layout.addRow("Y6", self.y6_line)
        Layout.addRow("Y7", self.y7_line)
        Layout.addRow("Y8", self.y8_line)
        self.tab2.setLayout(Layout)

    def tab3UI(self):
        Layout = QFormLayout(self)
        self.combobox = QComboBox()
        self.combobox.addItems(["PQ", "PV", "BALANCE"])
        self.node_lineP = QLineEdit()
        self.node_lineQ= QLineEdit()
        self.node_lineV = QLineEdit()
        self.node_lineA = QLineEdit()
        Layout.addRow("type", self.combobox)
        Layout.addRow("P", self.node_lineP)
        Layout.addRow("Q", self.node_lineQ)
        Layout.addRow("V", self.node_lineV)
        Layout.addRow("angel", self.node_lineA)
        self.tab3.setLayout(Layout)

    def update(self):

        self.vb1_line.setText("{:.4f}".format(self.left_vb))
        self.vb2_line.setText("{:.4f}".format(self.down_vb))
        self.vb3_line.setText("{:.4f}".format(self.right_vb))
        self.y1_line.setText("{:.10f}".format(self.Y1))
        self.y2_line.setText("{:.10f}".format(self.Y2))
        self.y3_line.setText("{:.10f}".format(self.Y3))
        self.y4_line.setText("{:.10f}".format(self.Y4))
        self.y5_line.setText("{:.10f}".format(self.Y5))
        self.y6_line.setText("{:.10f}".format(self.Y6))
        self.y7_line.setText("{:.10f}".format(self.Y7))
        self.y8_line.setText("{:.10f}".format(self.Y8))
        if self.flag == 1:
            if self.node_p!="": self.node_lineP.setText("{:.4f}".format(eval(self.node_p)))
            if self.node_q!="": self.node_lineQ.setText("{:.4f}".format(eval(self.node_q)))
            if self.node_v!="": self.node_lineV.setText("{:.4f}".format(float(self.node_v)))
            if self.node_angle!="": self.node_lineA.setText("{:.4f}".format(float(self.node_angle)))


class Wire(QTabWidget):
    def __init__(self):
        self.vb = 0
        self.index = 0
        self.Y1N = 0
        self.Y2N = 0
        self.Y3N = 0
        self.length = ""
        self.x1 = ""
        self.r1 = ""
        self.b1 = ""
        super(Wire, self).__init__()
        self.resize(400, 200)
        self.setWindowTitle(str(self.index))
        self.tab1 = QWidget()
        self.tab2 = QWidget()
        self.addTab(self.tab1, "input")
        self.addTab(self.tab2, "result")
        self.tab1UI()
        self.tab2UI()
    def tab1UI(self):

        self.Layout = QGridLayout(self)
        self.length_label = QLabel("lenth")
        self.x1_label = QLabel("X1")
        self.r1_label = QLabel("R1")
        self.b1_label = QLabel("B1")
        self.push_button = QPushButton("确认")
        self.fromlayout = QFormLayout()#窗体布局
        self.lineedit1 = QLineEdit()
        self.lineedit1.setText(self.x1)
        self.lineedit2 = QLineEdit()
        self.lineedit2.setText(self.r1)
        self.lineedit3 = QLineEdit()
        self.lineedit3.setText(self.b1)
        self.lineedit4 = QLineEdit()


        self.Layout.addWidget(self.x1_label,0,0)#0行 0列
        self.Layout.addWidget(self.lineedit1,0,1,1,2)
        self.Layout.addWidget(self.r1_label,1,0)#0行 0列
        self.Layout.addWidget(self.lineedit2,1,1,1,2)
        self.Layout.addWidget(self.b1_label,2,0)#0行 0列
        self.Layout.addWidget(self.lineedit3,2,1,1,2)
        self.Layout.addWidget(self.length_label,3,0)
        self.Layout.addWidget(self.lineedit4,3,1,1,2)
        self.Layout.addWidget(self.push_button,4,2,1,1)

        #设置校验器
        double_validator = QDoubleValidator(self)
        double_validator.setRange(0, 10000)
        double_validator.setDecimals(10)#小数点后4位
        double_validator.setNotation(QDoubleValidator.StandardNotation)

        self.lineedit1.setValidator(double_validator)
        self.lineedit2.setValidator(double_validator)
        self.lineedit3.setValidator(double_validator)

        self.setWindowModality(Qt.ApplicationModal)#dialog出现后mainwindow控件不可用
        self.push_button.clicked.connect(self.button_task)
        self.tab1.setLayout(self.Layout)
    def button_task(self):
        self.length = self.lineedit4.text()
        self.r1 = self.lineedit2.text()
        self.x1 = self.lineedit1.text()
        self.b1 = self.lineedit3.text()
        self.close()
    def tab2UI(self):
        Layout = QFormLayout(self)
        self.vb1_line = QLineEdit()
        self.y1_line = QLineEdit()
        self.y2_line = QLineEdit()
        self.y3_line = QLineEdit()
        Layout.addRow("Vb", self.vb1_line)
        Layout.addRow("Y1N", self.y1_line)
        Layout.addRow("Y2N", self.y2_line)
        Layout.addRow("Y3N", self.y3_line)

        self.tab2.setLayout(Layout)

    def update(self):
        self.vb1_line.setText("{:.4f}".format(self.vb))
        self.y1_line.setText("{:.4f}".format(self.Y1N))
        self.y2_line.setText("{:.4f}".format(self.Y2N))
        self.y3_line.setText("{:.4f}".format(self.Y3N))

class Node(QTabWidget):
    def __init__(self):
        self.flag = 0
        self.vb = 0
        self.index = 0
        self.node_tpye = 1# 1 pq 2 pv 3 balance
        self.node_p = 0
        self.node_q = 0
        self.node_v =0
        self.node_angle = 0

        super(Node, self).__init__()

        self.resize(400,250)
        self.tab1 = QWidget()
        self.tab2 = QWidget()
        self.addTab(self.tab1, "input")
        self.addTab(self.tab2, "result")
        self.tab1UI()
        self.tab2UI()

    def tab1UI(self):

        self.setWindowTitle(str(self.index))
        self.Layout = QGridLayout(self)

        self.type_label = QLabel("tpye")

        self.push_button = QPushButton("确认")

        self.combobox = QComboBox()
        self.combobox.addItems(["PQ", "PV", "BALANCE"])
        self.p_label =QLabel("P")
        self.q_label =QLabel("Q")
        self.v_label =QLabel("V")
        self.a_label =QLabel("Angel")
        self.node_lineP = QLineEdit()
        self.node_lineQ= QLineEdit()
        self.node_lineV = QLineEdit()
        self.node_lineA = QLineEdit()

        self.Layout.addWidget(self.type_label,0,0)#0行 0列
        self.Layout.addWidget(self.combobox,0,1,1,2)
        self.Layout.addWidget(self.p_label,1,0)#0行 0列
        self.Layout.addWidget(self.node_lineP,1,1,1,2)
        self.Layout.addWidget(self.q_label,2,0)#0行 0列
        self.Layout.addWidget(self.node_lineQ,2,1,1,2)
        self.Layout.addWidget(self.v_label,3,0)#0行 0列
        self.Layout.addWidget(self.node_lineV,3,1,1,2)
        self.Layout.addWidget(self.a_label,4,0)#0行 0列
        self.Layout.addWidget(self.node_lineA,4,1,1,2)
        self.Layout.addWidget(self.push_button,5,2,1,1)


        self.setWindowModality(Qt.ApplicationModal)#dialog出现后mainwindow控件不可用
        self.push_button.clicked.connect(self.button_task)
        self.tab1.setLayout(self.Layout)
    def button_task(self):
        if self.combobox.currentIndex() == 0:
            self.node_tpye = 1
        elif self.combobox.currentIndex() == 1:
            self.node_tpye = 2
        else:
            self.node_tpye = 3
        self.node_p = self.node_lineP.text()
        self.node_q =self.node_lineQ.text()
        self.node_v =self.node_lineV.text()
        self.node_angle =self.node_lineA.text()
        self.flag = 1

        self.close()
    def tab2UI(self):
        Layout = QFormLayout(self)
        self.vb1_line = QLineEdit()

        Layout.addRow("Vb", self.vb1_line)

        self.tab2.setLayout(Layout)

    def update(self):
        self.vb1_line.setText("{:.2f}".format(self.vb))
        if self.flag == 1:
            if self.node_p != "" :self.node_lineP.setText("{:.4f}".format(eval(self.node_p)))
            if self.node_q != "" :self.node_lineQ.setText("{:.4f}".format(eval(self.node_q)))
            if self.node_v != "" :self.node_lineV.setText("{:.4f}".format(float(self.node_v)))
            if self.node_angle != "" :self.node_lineA.setText("{:.4f}".format(float(self.node_angle)))










# if __name__ == '__main__':
#     app = QApplication(sys.argv)
#     w = Transformer_Two()
#     w.setup("1")
#     w.show()
#     sys.exit(app.exec_())#退出显示
