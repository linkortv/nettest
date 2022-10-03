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
      status = "ping dns1"
      self.ui.status_label.setText(status)
      self.ui.progressBar.setValue(1)
      linux.fping_dns1()
      
      status = "ping dns2"
      self.ui.status_label.setText(status)
      self.ui.progressBar.setValue(15)
      linux.fping_dns2()
      

      status = "ping yandex"
      self.ui.status_label.setText(status)
      self.ui.progressBar.setValue(30)
      linux.fping_yandex()
      

      status = "ping google"
      self.ui.status_label.setText(status)
      self.ui.progressBar.setValue(45)
      linux.fping_google()
      

      status = "traceroute service"
      self.ui.status_label.setText(status)
      self.ui.progressBar.setValue(60)
      linux.trace_service()
      
    elif platform == "darwin":
      import macos
      t = macos.test()
    elif platform == "win32":
      print("it's window")
    self.ui.progressBar.setValue(100)
    self.ui.status_label.setText("complete")
    # self.ui.status_label.setText(t)


if __name__ == '__main__':
  app = QApplication()
  window = MainWindow()
  window.show()
  sys.exit(app.exec_())
