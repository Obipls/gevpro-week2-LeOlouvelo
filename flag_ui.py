# #!/usr/bin/env python
# flag_ui.py
# Olivier Louwaars s2814714 en Leonardo Losno Velozo s1668501
# 16-2-2015


from country import *

class Flag(QtGui.QWidget):
    def __init__(self):
        super(Flag,self).__init__()
        self.initUI()

    def initUI(self):

        self.box=QtGui.QComboBox(self)
        self.box.activated.connect(self.onActivated)

        self.hbox=QtGui.QHBoxLayout()
        self.hbox.addWidget(self.box)
        self.setLayout(self.hbox)

        self.fbox=QtGui.QFrame(self)
        self.fbox.setFrameShape(QtGui.QFrame.StyledPanel)
        self.hbox.addWidget(self.fbox)

        for self.i in readText():
            self.box.addItem(self.i.getName())

        self.resize(400, 100)
        self.center()
        self.setWindowTitle('Countries flag')
        self.show()


    def center(self):
        qr=self.frameGeometry()
        cp=QtGui.QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def onActivated(self, text):
        self.flag=Country.getFlag(self.i)
        self.fbox.setStyleSheet("QFrame{background-color:%s}"%self.flag.name())
