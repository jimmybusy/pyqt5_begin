from PyQt5 import QtCore, QtGui, QtWidgets
import dialog_drawBackground
import GraphicVeiw

class Dialog_simulate(QtWidgets.QDialog):
     def __init__(self,trans2,trans3,wire,loader,node,generator,parent = None):
        super().__init__(parent)
        self.sortlist1 = []
        self.sortlist2 = []
        self.sortlist3 = []
        self.list1 = trans2
        self.list2 = trans3
        self.list3 = wire
        self.list4 = loader
        self.list5 = node
        self.list6 = generator
        self.setWindowTitle("jimmy_simulate")
        self.desktop = QtWidgets.QDesktopWidget().availableGeometry()
        self.resize(self.desktop.width(),self.desktop.height())
        self.secene = QtWidgets.QGraphicsScene(self)
        self.view = dialog_drawBackground.GraphicView(self.secene,self)
        self.view.setDragMode(self.view.RubberBandDrag)
        self.view.setGeometry(10,10,self.desktop.width(),self.desktop.height())


     def sortlist(self):
        self.sortlist1 = self.list1+self.list2+self.list3+self.list5
        for i in range(len(self.sortlist1)):
            for j in range(len(self.sortlist1)-1-i):
                if(self.sortlist1[j].x()>self.sortlist1[j+1].x()):
                    a = self.sortlist1[j]
                    self.sortlist1[j] = self.sortlist1[j+1]
                    self.sortlist1[j+1] = a
        for i in range(len(self.sortlist1)):
            if (self.sortlist1[i-len(self.sortlist2)-len(self.sortlist3)].y()-self.sortlist1[0].y()) >=64 and (self.sortlist1[i-len(self.sortlist2)-len(self.sortlist3)].y()-self.sortlist1[0].y())<=256:
                self.sortlist2.append(self.sortlist1.pop(i-len(self.sortlist2)-len(self.sortlist3)))
            elif (self.sortlist1[i-len(self.sortlist2)-len(self.sortlist3)].y()-self.sortlist1[0].y()) >256 and (self.sortlist1[i-len(self.sortlist2)-len(self.sortlist3)].y()-self.sortlist1[0].y())<=512:
                self.sortlist3.append(self.sortlist1.pop(i-len(self.sortlist2)-len(self.sortlist3)))
     def create_gory(self):
        for i in range(len(self.sortlist1)):
            if isinstance(self.sortlist1[i], GraphicVeiw.GraphicItem_trans2):
                a = dialog_drawBackground.Mode_trans2(self.sortlist1[i])
                pos = self.view.mapToScene(QtCore.QPoint(0-100*i,0-100*i))
                a.setPos(pos.x(),pos.y())
                self.secene.addItem(a)
                print(self.sortlist1[i].x(), self.sortlist1[i].y())
                print(a.pos())

            # elif isinstance(self.sortlist1[i], GraphicVeiw.GraphicItem_trans3):
            #      a = dialog_drawBackground.Mode_trans2
            #      a.setpos(self.sortlist1[i].x(), self.sortlist1[i].y())
            #      self.secene.addItem(a)
            # elif isinstance(self.sortlist1[i], GraphicVeiw.GraphicItem_node):
            #      a = dialog_drawBackground.Mode_trans2
            #      a.setpos(self.sortlist1[i].x(), self.sortlist1[i].y())
            #      self.secene.addItem(a)
            # elif isinstance(self.sortlist1[i], GraphicVeiw.GraphicItem_wire):
            #     a = dialog_drawBackground.Mode_trans2
            #     a.setpos(self.sortlist1[i].x(), self.sortlist1[i].y())
            #     self.secene.addItem(a)






# def demo_run():
#     app = QtWidgets.QApplication(sys.argv)
#     demo = Dialog_simulate()
#     demo.show()
#     sys.exit(app.exec_())
# if __name__ == "__main__" :
#     demo_run()