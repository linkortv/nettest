import sys
from sys import platform
from PySide6.QtWidgets import QApplication, QMainWindow
from form import Ui_MainWindow

class MainWindow(QMainWindow):
  def __init__(self, parent=None):
    super(MainWindow, self).__init__(parent)
    self.ui = Ui_MainWindow()
    self.ui.setupUi(self)
    self.ui.progressBar.setValue(0)
    self.ui.start_test.clicked.connect(self.start_test)

  def start_test(self):
    text = self.ui.lineEdit.text()
    if text == "":
      text = "test"
    if platform == "linux" or platform == "linux2":
      import linux
      start = "started test"
      self.ui.status_label.setText(start)
      self.ui.progressBar.setValue(50)
      t = linux.test()
      self.ui.status_label.setText(t)
      
    elif platform == "darwin":
      import macos
      t = macos.test()
    elif platform == "win32":
      print("it's window")
    self.ui.progressBar.setValue(100)
    self.ui.status_label.setText("complete")
    # self.ui.status_label.setText(t)


if __name__ == '__main__':

  if platform == "linux" or platform == "linux2":
    print("it's linux")
  elif platform == "darwin":
    print("it's macos")
  elif platform == "win32":
    print("it's window")

  app = QApplication()
  window = MainWindow()
  window.show()
  sys.exit(app.exec_())
