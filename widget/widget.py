#!/usr/bin/python
#-*- coding:utf-8 -*-


import sys
from PySide import QtGui, QtCore
import datetime
from csvFinder import csvName

def checkDate(cale):
        if len(cale) != 8:
            return False
        m = int(cale[4:6])
        d = int(cale[-2:])
        y = int(cale[:4])
        try:
            datetime.date(y,m,d)
            return True
        except:
            return False

class Example(QtGui.QWidget):
    
    def __init__(self):
        super(Example, self).__init__()
        
        self.initUI()
        
    def initUI(self):
        self.cdFlag = True
        self.ee = QtGui.QLabel('     EEEE\nSN[12:15]')
        self.errCode = QtGui.QLabel('  errCode\n Ex:29,25')
        self.sd = QtGui.QLabel(' Start Date\n (20151230)')
        self.ed = QtGui.QLabel('  End Date\n(20151231)')
        self.cfg = QtGui.QLabel('      Config')

        self.notice = QtGui.QLabel('', self)
        #self.notice.move(10, 257)
        pe = QtGui.QPalette() 
        pe.setColor(QtGui.QPalette.WindowText, QtGui.QColor(255,0,0))
        self.notice.setPalette(pe)
        
        #self.notice.setAlignment(QtCore.Qt.AlignLift)

        self.btn = QtGui.QPushButton('Submit', self)
        #self.btn.move(160, 270)

        self.btn.clicked.connect(self.showDialog)

        self.cb = QtGui.QCheckBox('CFG/Date', self)
        self.cb.move(20, 10)
        self.cb.toggle()
        self.cb.stateChanged.connect(self.changeItem)

        self.eeEdit = QtGui.QLineEdit()
        self.errCodeEdit = QtGui.QLineEdit()
        self.sdEdit = QtGui.QLineEdit()
        self.edEdit = QtGui.QLineEdit()
        self.cfgEdit = QtGui.QLineEdit()

        self.grid = QtGui.QGridLayout()
        self.grid.setSpacing(10)

        self.grid.addWidget(self.cb, 1, 0)

        self.grid.addWidget(self.ee, 2, 0)
        self.grid.addWidget(self.eeEdit, 2, 1)

        self.grid.addWidget(self.errCode, 3, 0)
        self.grid.addWidget(self.errCodeEdit, 3, 1)

        self.grid.addWidget(self.sd, 4, 0)
        self.grid.addWidget(self.sdEdit, 4, 1)

        self.grid.addWidget(self.ed, 5, 0)
        self.grid.addWidget(self.edEdit, 5, 1)

        self.grid.addWidget(self.cfg, 6, 0)
        self.grid.addWidget(self.cfgEdit, 6, 1)

        self.grid.addWidget(self.btn, 7, 0)
        self.grid.addWidget(self.notice, 7, 1)
        
        self.setLayout(self.grid) 

        self.cfg.setVisible(False)
        self.cfgEdit.setVisible(False)
        self.sd.setVisible(True)
        self.sdEdit.setVisible(True)
        self.ed.setVisible(True)
        self.edEdit.setVisible(True)

        self.setGeometry(300, 300, 350, 300)
        self.setWindowTitle('Big data Analysis')    
        self.show()
    
    def showDialog(self):
        eeBuf = self.eeEdit.displayText()
        ecBuf = self.errCodeEdit.displayText()
        sdBuf = self.sdEdit.displayText()
        edBuf = self.edEdit.displayText()
        cfgBuf = self.cfgEdit.displayText()
        if len(eeBuf) != 4:
            self.notice.setText('EEEE code must be 4.')
            self.notice.adjustSize()
        else :
            self.notice.setText('')
            if self.cdFlag: 
                if checkDate(str(sdBuf)) and checkDate(str(edBuf)):
                    if edBuf >= sdBuf:
                        csvName([eeBuf, ecBuf, sdBuf, edBuf])
                    else :
                        self.notice.setText('End time must be greater than or equal start time.')
                        self.notice.adjustSize()
                else:
                    self.notice.setText('Date format is incorrect.')
                    self.notice.adjustSize()
            else:
                if len(cfgBuf) != 3:
                    self.notice.setText('Config must be 3.')
                    self.notice.adjustSize()
                else :
                    csvName([eeBuf, ecBuf, cfgBuf])

    def changeItem(self, state):
      
        if state == QtCore.Qt.Checked:
            self.cdFlag = True
            self.cfg.setVisible(False)
            self.cfgEdit.setVisible(False)
            self.cfgEdit.setText('')
            self.sd.setVisible(True)
            self.sdEdit.setVisible(True)
            self.ed.setVisible(True)
            self.edEdit.setVisible(True)            

        else:
            self.cdFlag = False
            self.cfg.setVisible(True)
            self.cfgEdit.setVisible(True)
            self.sd.setVisible(False)
            self.sdEdit.setVisible(False)
            self.sdEdit.setText('')
            self.ed.setVisible(False)
            self.edEdit.setVisible(False)
            self.edEdit.setText('')
        
def main():
    
    app = QtGui.QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()