# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'example.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    
    def __init__(self):
        self.result = 0
        self.x1 = 0
        self.x2 = 0


    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(703, 502)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Form.sizePolicy().hasHeightForWidth())
        Form.setSizePolicy(sizePolicy)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label = QtWidgets.QLabel(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.horizontalLayout_2.addWidget(self.label)
        spacerItem = QtWidgets.QSpacerItem(100, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.aCoef = QtWidgets.QLineEdit(Form)
        self.aCoef.setMaximumSize(QtCore.QSize(30, 16777215))
        self.aCoef.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.aCoef.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.aCoef.setObjectName("aCoef")
        self.horizontalLayout.addWidget(self.aCoef)
        self.firstLabel = QtWidgets.QLabel(Form)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.firstLabel.setFont(font)
        self.firstLabel.setText("")
        self.firstLabel.setObjectName("firstLabel")
        self.horizontalLayout.addWidget(self.firstLabel)
        self.bCoef = QtWidgets.QLineEdit(Form)
        self.bCoef.setMaximumSize(QtCore.QSize(30, 16777215))
        self.bCoef.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.bCoef.setObjectName("bCoef")
        self.horizontalLayout.addWidget(self.bCoef)
        self.secondLabel = QtWidgets.QLabel(Form)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.secondLabel.setFont(font)
        self.secondLabel.setText("")
        self.secondLabel.setObjectName("secondLabel")
        self.horizontalLayout.addWidget(self.secondLabel)
        self.cCoef = QtWidgets.QLineEdit(Form)
        self.cCoef.setMaximumSize(QtCore.QSize(30, 16777215))
        self.cCoef.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.cCoef.setObjectName("cCoef")
        self.horizontalLayout.addWidget(self.cCoef)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        self.verticalLayout_3.addLayout(self.verticalLayout_2)
        spacerItem2 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout_3.addItem(spacerItem2)
        self.label_2 = QtWidgets.QLabel(Form)
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_3.addWidget(self.label_2)
        self.discriminantLabel = QtWidgets.QLabel(Form)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.discriminantLabel.setFont(font)
        self.discriminantLabel.setText("")
        self.discriminantLabel.setObjectName("discriminantLabel")
        self.verticalLayout_3.addWidget(self.discriminantLabel)
        self.discriminantLabel2 = QtWidgets.QLabel(Form)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.discriminantLabel2.setFont(font)
        self.discriminantLabel2.setText("")
        self.discriminantLabel2.setObjectName("discriminantLabel2")
        self.verticalLayout_3.addWidget(self.discriminantLabel2)
        self.label_3 = QtWidgets.QLabel(Form)
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_3.addWidget(self.label_3)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.solutionLabel = QtWidgets.QLabel(Form)
        self.solutionLabel.setMaximumSize(QtCore.QSize(120, 16777215))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.solutionLabel.setFont(font)
        self.solutionLabel.setText("")
        self.solutionLabel.setObjectName("solutionLabel")
        self.horizontalLayout_4.addWidget(self.solutionLabel)
        self.solutionLabel2 = QtWidgets.QLabel(Form)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.solutionLabel2.setFont(font)
        self.solutionLabel2.setText("")
        self.solutionLabel2.setObjectName("solutionLabel2")
        self.horizontalLayout_4.addWidget(self.solutionLabel2)
        self.verticalLayout_3.addLayout(self.horizontalLayout_4)
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem3)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.pushButton = QtWidgets.QPushButton(Form)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout_3.addWidget(self.pushButton)
        self.pushButton_2 = QtWidgets.QPushButton(Form)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout_3.addWidget(self.pushButton_2)
        self.verticalLayout_3.addLayout(self.horizontalLayout_3)
        self.showPlot = QtWidgets.QPushButton(Form)
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        self.showPlot.setFont(font)
        self.showPlot.setObjectName("showPlot")
        self.verticalLayout_3.addWidget(self.showPlot)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

        self.pushButton.clicked.connect(self.calculateSolutions)
        self.pushButton_2.clicked.connect(self.clearAll)
        self.showPlot.clicked.connect(self.showPlotFunction)


        self.myInitMethods()

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "Kvadratna jednacina"))
        self.label_2.setText(_translate("Form", "Diskriminanta"))
        self.label_3.setText(_translate("Form", "Resenja: <p>x<sub>1/2</sub> = <sup>-b &plusmn; &radic;(b<sup>2</sup> - 4ac)</sup> / <sub>2a</sub></p>"))
        self.pushButton.setText(_translate("Form", "Izracunaj"))
        self.pushButton_2.setText(_translate("Form", "Obrisi"))
        self.showPlot.setText(_translate("Form", "Prikazi grafik"))
        # self.pushButton.clicked.connect(self.showDiscrimiant)
        

    def showPlotFunction(self):
        # pass
        from matplotlib import pyplot as plt 
        import numpy as np
        solutionsRange = max(abs(self.x1), abs(self.x2))
        if self.x1 < self.x2: 
            xs = np.linspace(min(-5,-solutionsRange-5), max(solutionsRange+5,5), 50)
        else:
            xs = np.linspace(min(-5,self.x2-3), max(self.x1+3,5), 50)
        ys = []
        for x in xs:
            ys.append(float(self.aCoef.text()) * x * x + float(self.bCoef.text()) * x + float(self.cCoef.text()))
            
        # plt.plot(range(1,5), range(5, 9))
        plt.figure(figsize=(10, 10))
        plt.plot(xs, [0 for _ in range(len(xs))], color = "red", dashes = [1])
        plt.plot(xs, ys)
        plt.show()
    def myInitMethods(self):
        self.firstLabel.setText("x<sup>2</sup>+")
        self.secondLabel.setText("x+")
        self.discriminantLabel.setText("D = b<sup>2</sup> - 4ac = ")
        # self.solutionLabel.setText("x<sub>1/2</sub>=")


    def clearAll(self):
        self.firstLabel.setText("x<sup>2</sup>+")
        self.secondLabel.setText("x+")
        self.discriminantLabel.setText("D = b<sup>2</sup> - 4ac")
        self.discriminantLabel2.setText("")
        self.solutionLabel.setText("x<sub>1/2</sub>=")
        self.aCoef.setText("")
        self.bCoef.setText("")
        self.cCoef.setText("")
        self.solutionLabel2.setText("")


    def showDiscrimiant(self):
        # result = self.calculateDiscrimiant()
        # self.result
        # if self.result == -1 or self.result == 0:
            # return
        # else:
        if self.result < 0:
            popUp = QtWidgets.QMessageBox()
            popUp.setText("Diskriminanta je negativna")
            popUp.setIcon(QtWidgets.QMessageBox().Warning)
            popUp.setCheckBox(QtWidgets.QCheckBox())
            popUp.exec()
        else:
            self.discriminantLabel.setText("D = b<sup>2</sup> - 4ac ")
            self.discriminantLabel2.setText("D = " + str(self.result))

    def calculateSolutions(self):
        import math
        bCoef = 1
        aCoef = 1
        cCoef = 1
        if self.bCoef.text() != "":
            bCoef = float(self.bCoef.text())

        if self.aCoef.text() != "":
            aCoef = float(self.aCoef.text())
        
        if self.cCoef.text() != "":
            cCoef = float(self.cCoef.text())

        self.solutionLabel.setText("")
        self.solutionLabel2.setText("")

        self.result = self.calculateDiscrimiant()
        self.showDiscrimiant()
        print(self.result)
        if self.result == 0: 
            x1 = (-bCoef + math.sqrt(self.result))/(2 * aCoef)
            # x2 = (-bCoef- math.sqrt(self.result))/(2 * aCoef)
            # print(x1)
            self.solutionLabel.setText("x<sub>1</sub>=" + str(round(x1,3)))
            self.x1 = round(x1,3)
        elif self.result > 0:
            x1 = (-bCoef + math.sqrt(self.result))/(2 * aCoef)
            x2 = (-bCoef- math.sqrt(self.result))/(2 * aCoef)
            self.solutionLabel.setText("x<sub>1</sub>=" + str(round(x1, 3)))
            font = QtGui.QFont()
            font.setPointSize(15)
            self.solutionLabel2.setText("x<sub>2</sub>=" + str(round(x2, 3)))
            self.x1 = round(x1,3)
            self.x2 = round(x2,3)
        return self.result


    def calculateDiscrimiant(self):
        bCoef = 0
        aCoef = 0
        cCoef = 0
        if self.bCoef.text() != "":
            bCoef = float(self.bCoef.text())

        if self.aCoef.text() != "":
            aCoef = float(self.aCoef.text())
        
        if self.cCoef.text() != "":
            cCoef = float(self.cCoef.text())

        # self.aCoef.setText("2")
        # print(self.aCoef.text())
        if float(aCoef) == 0: 
            popUp = QtWidgets.QMessageBox()
            popUp.setText("Koeficijent uz x<sup>2</sup> je 0!")
            popUp.setIcon(QtWidgets.QMessageBox().Warning)
            popUp.setCheckBox(QtWidgets.QCheckBox())
            popUp.exec()
            # return 
            return -1

        return float(bCoef) * float(bCoef) - 4 * float(aCoef) * float(cCoef)
    


if __name__ == "__main__":
    import sys
    import numpy as np
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
    # from matplotlib import pyplot as plt
    # xs = []
    # # for x in range(-10, 10, 1):
    # #     xs.append(x)
    # xs = np.linspace(-10, 10, 100)
    # ys = []
    # # plt.plot(xs, ys)
    # def funkcija(x):
    #     return float(2 * x*x - 5*x + 1)
    #     # return 1
    # for x in xs:
    #     ys.append(funkcija(x))
    # plt.plot(xs, ys)
    # plt.show()