import sys
from PyQt5 import sip
from PyQt5.QtWidgets import (QWidget,QPushButton,QLineEdit,QLabel,QVBoxLayout,QHBoxLayout,QApplication)

import webbrowser
import time

class Example(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()
        self.text = ''
        self.num=0

    def initUI(self):

        # self.setFixedHeight(500)
        pre = QLabel("输入'攻元宵'价格")
        pre.setFixedWidth(100)

        jifen = QLabel("输入各元宵积分")
        jifen.setFixedWidth(100)
        jiage = QLabel("得到元宵价格")
        jiage.setFixedWidth(100)

        gongji = QLabel("攻击积分")
        gongji.setFixedWidth(50)
        gongji1 = QLabel("攻击价格")
        gongji1.setFixedWidth(50)

        sudu = QLabel('速度积分')
        sudu.setFixedWidth(50)
        sudu1 = QLabel('速度价格')
        sudu1.setFixedWidth(50)

        fali = QLabel('法力积分')
        fali.setFixedWidth(50)
        fali1 = QLabel('法力价格')
        fali1.setFixedWidth(50)

        tili = QLabel('体力积分')
        tili.setFixedWidth(50)
        tili1 = QLabel('体力价格')
        tili1.setFixedWidth(50)

        fangyu = QLabel('防御积分')
        fangyu.setFixedWidth(50)
        fangyu1 = QLabel('防御价格')
        fangyu1.setFixedWidth(50)

        duobi = QLabel('躲避积分')
        duobi.setFixedWidth(50)
        duobi1 = QLabel('躲避价格')
        duobi1.setFixedWidth(50)

        end = QLabel('           from 一只特立独行的猪')

        self.preEdit = QLineEdit()
        self.preEdit.setFixedWidth(50)

        self.gongjiEdit=QLineEdit()
        self.gongjiEdit.setFixedWidth(50)
        self.gongji1Edit = QLineEdit()
        self.gongji1Edit.setFixedWidth(50)
        self.gongji1Edit.setReadOnly(True)

        self.suduEdit = QLineEdit()
        self.suduEdit.setFixedWidth(50)
        self.sudu1Edit = QLineEdit()
        self.sudu1Edit.setFixedWidth(50)
        self.sudu1Edit.setReadOnly(True)

        self.faliEdit = QLineEdit()
        self.faliEdit.setFixedWidth(50)
        self.fali1Edit = QLineEdit()
        self.fali1Edit.setFixedWidth(50)
        self.fali1Edit.setReadOnly(True)

        self.tiliEdit = QLineEdit()
        self.tiliEdit.setFixedWidth(50)
        self.tili1Edit = QLineEdit()
        self.tili1Edit.setFixedWidth(50)
        self.tili1Edit.setReadOnly(True)

        self.fangyuEdit = QLineEdit()
        self.fangyuEdit.setFixedWidth(50)
        self.fangyu1Edit = QLineEdit()
        self.fangyu1Edit.setFixedWidth(50)
        self.fangyu1Edit.setReadOnly(True)

        self.duobiEdit = QLineEdit()
        self.duobiEdit.setFixedWidth(50)
        self.duobi1Edit = QLineEdit()
        self.duobi1Edit.setFixedWidth(50)
        self.duobi1Edit.setReadOnly(True)

        startBtn = QPushButton('计算')

        hboxLayout_7 = QHBoxLayout()
        hboxLayout_7.addWidget(pre)
        hboxLayout_7.addWidget(self.preEdit)

        hboxLayout_8 = QHBoxLayout()
        hboxLayout_8.addWidget(jifen)
        hboxLayout_8.addWidget(jiage)

        hboxLayout_1=QHBoxLayout()
        hboxLayout_1.addWidget(gongji)
        hboxLayout_1.addWidget(self.gongjiEdit)
        hboxLayout_1.addWidget(gongji1)
        hboxLayout_1.addWidget(self.gongji1Edit)

        hboxLayout_2 = QHBoxLayout()
        hboxLayout_2.addWidget(sudu)
        hboxLayout_2.addWidget(self.suduEdit)
        hboxLayout_2.addWidget(sudu1)
        hboxLayout_2.addWidget(self.sudu1Edit)

        hboxLayout_3 = QHBoxLayout()
        hboxLayout_3.addWidget(fali)
        hboxLayout_3.addWidget(self.faliEdit)
        hboxLayout_3.addWidget(fali1)
        hboxLayout_3.addWidget(self.fali1Edit)

        hboxLayout_4 = QHBoxLayout()
        hboxLayout_4.addWidget(tili)
        hboxLayout_4.addWidget(self.tiliEdit)
        hboxLayout_4.addWidget(tili1)
        hboxLayout_4.addWidget(self.tili1Edit)

        hboxLayout_5 = QHBoxLayout()
        hboxLayout_5.addWidget(fangyu)
        hboxLayout_5.addWidget(self.fangyuEdit)
        hboxLayout_5.addWidget(fangyu1)
        hboxLayout_5.addWidget(self.fangyu1Edit)

        hboxLayout_6 = QHBoxLayout()
        hboxLayout_6.addWidget(duobi)
        hboxLayout_6.addWidget(self.duobiEdit)
        hboxLayout_6.addWidget(duobi1)
        hboxLayout_6.addWidget(self.duobi1Edit)

        hboxLayout_9 = QHBoxLayout()
        hboxLayout_9.addWidget(end)

        mainLayout=QVBoxLayout(self)
        mainLayout.addLayout(hboxLayout_7)
        mainLayout.addLayout(hboxLayout_8)
        mainLayout.addLayout(hboxLayout_1)
        mainLayout.addLayout(hboxLayout_2)
        mainLayout.addLayout(hboxLayout_3)
        mainLayout.addLayout(hboxLayout_4)
        mainLayout.addLayout(hboxLayout_5)
        mainLayout.addLayout(hboxLayout_6)
        mainLayout.addLayout(hboxLayout_9)
        mainLayout.addWidget(startBtn)

        # self.lb1 = QLabel(self)
        #
        # self.lb1.move(60, 40)
        # self.lb1.setFixedWidth(20)
        # self.lb1.setFixedHeight(20)

        # mainLayout.addWidget(self.lb1)
        self.setWindowTitle('元宵计算')
        self.show()

        startBtn.clicked.connect(self.start)
     
    def toint(self,obj):
        if obj.text():
            return int(obj.text())
        return 0
    def start(self):

        pre=self.toint(self.preEdit)
        gongji = self.toint(self.gongjiEdit)
        sudu = self.toint(self.suduEdit)
        fali = self.toint(self.faliEdit)
        tili = self.toint(self.tiliEdit)
        fangyu = self.toint(self.fangyuEdit)
        duobi = self.toint(self.duobiEdit)

        if pre and gongji:
            gongjia = pre / gongji * gongji
            self.gongji1Edit.setText(str(gongjia))
            self.gongji1Edit.repaint()
        if pre and sudu and gongji:
            sujia = pre / gongji * sudu
            self.sudu1Edit.setText(str(sujia))
            self.sudu1Edit.repaint()
        if pre and fali and gongji:
            fajia = pre / gongji * fali
            self.fali1Edit.setText(str(fajia))
            self.fali1Edit.repaint()
        if pre and tili and gongji:
            tijia = pre / gongji * tili
            self.tili1Edit.setText(str(tijia))
            self.tili1Edit.repaint()
        if pre and fangyu and gongji:
            fangjia = pre / gongji * fangyu
            self.fangyu1Edit.setText(str(fangjia))
            self.fangyu1Edit.repaint()
        if pre and duobi and gongji:
            duojia = pre / gongji * duobi
            self.duobi1Edit.setText(str(duojia))
            self.duobi1Edit.repaint()




        # if 'http://' in url:
        #     pass
        # else:
        #     url='http://'+url
        # import requests
        # self.lb1.setText("开始登入....")
        # self.lb1.repaint()
        # while True:
        #     try:
        #         self.num += 1
        #         data = requests.get(url)
        #         if "密钥错误" in data.text:
        #             self.lb1.setText("输入错误，请重新输入")
        #
        #             break
        #         elif "在线人数超限" not in data.text:
        #             self.lb1.setText("登入成功，尝试登入次数:"+str(self.num))
        #
        #             webbrowser.open(url, new=0, autoraise=True)
        #             break
        #         self.lb1.repaint()
        #     except Exception as e:
        #         self.lb1.setText("输入错误，请重新输入(仅支持HTTP，不支持https)")
        #         break

app=QApplication(sys.argv)
start=Example()
sys.exit(app.exec_())
