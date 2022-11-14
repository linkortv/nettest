import sys
import resources #import icon
from PySide6.QtWidgets import QApplication, QMainWindow, QFileDialog
from PySide6 import QtGui
from form import Ui_MainWindow
import net
import sptest
# import pdb
import asyncio

class MainWindow(QMainWindow):
  def __init__(self, parent=None):
    super(MainWindow, self).__init__(parent)

    self.ui = Ui_MainWindow()
    self.ui.setupUi(self)
    self.ui.progressBar.setValue(0)
    self.ui.start_test.clicked.connect(self.ltest)
    self.ui.full_test.clicked.connect(self.ftest)

    self.DNS1 = "213.234.0.2"
    self.DNS2 = "213.234.2.6"

  def test(self, type_test, count_packages = 1):
    fname = _dirDialog(self)

    if len(fname) > 1:
      f = open(f'{fname}/nettest.txt', "w+")
      status = "ping dns1"
      self.ui.status_label.setText(status)
      self.ui.progressBar.setValue(1)
      f.write(f"ping DNS1\n")
      f.write(_winEncode(net.fping_service(self.DNS1, count_packages) + '\n'))
      
      status = "ping dns2"
      self.ui.status_label.setText(status)
      self.ui.progressBar.setValue(5)
      f.write(f"ping DNS2\n")
      f.write(_winEncode(net.fping_service(self.DNS2, count_packages) + '\n'))

      status = "ping yandex"
      self.ui.status_label.setText(status)
      self.ui.progressBar.setValue(10)
      f.write(_winEncode(net.fping_service("ya.ru", count_packages) + '\n'))
      

      status = "ping google"
      self.ui.status_label.setText(status)
      self.ui.progressBar.setValue(20)
      f.write(_winEncode(net.fping_service("google.com", count_packages) + '\n'))


      status = "ping steam"
      self.ui.status_label.setText(status)
      self.ui.progressBar.setValue(30)
      f.write(f"ping steam store\n")
      f.write(_winEncode(net.fping_service("store.steampowered.com", count_packages) + '\n'))

      status = "ping blizzard"
      self.ui.status_label.setText(status)
      self.ui.progressBar.setValue(40)
      f.write(f"ping blizzard\n")
      f.write(_winEncode(net.fping_service("blizzard.com", count_packages) + '\n'))

      status = "ping vk"
      self.ui.status_label.setText(status)
      self.ui.progressBar.setValue(50)
      f.write(_winEncode(net.fping_service("vk.com", count_packages) + '\n'))

      status = "ping playstation"
      self.ui.status_label.setText(status)
      self.ui.progressBar.setValue(60)
      f.write(f"ping playstation store\n")
      f.write(_winEncode(net.fping_service("store.playstation.com", count_packages) + '\n'))

      status = "Проверяем скорость"
      self.ui.status_label.setText(status)
      self.ui.progressBar.setValue(70)
      f.write('Speedtest\n')
      f.write(sptest.sptest() + '\n')

      if type_test == 'full':
        line_address = self.ui.lineEdit.text()
        if len(line_address) != 0:
          address = line_address
        elif len(self.ui.comboBox.currentText()) != 0:
          service = self.ui.comboBox.currentText()
          address = net.getAddress(service)
        else:
          address = None
        print(address)
        if address != None:
          status = "Проверяем задержку до выбранного сервиса"
          self.ui.status_label.setText(status)
          self.ui.progressBar.setValue(80)
          f.write(f"\nping {service}\n")
          f.write(_winEncode(net.fping_service(address, count_packages) + '\n'))

          status = "Проводим трассировку до выбранного сервиса"
          self.ui.status_label.setText(status)
          self.ui.progressBar.setValue(90)
          f.write(f"tracert {service}\n")
          f.write(_winEncode(net.trace_service(address) + '\n'))
        
      else:
        print('here end light test')
      f.close()
      self.ui.progressBar.setValue(100)
      self.ui.status_label.setText("complete")
      net.dir_open(fname)
    else:
      return False


  def ftest(self):
    self.test('full', 10)

  def ltest(self):
    self.test('light')
    

def _dirDialog(self):
    return QFileDialog.getExistingDirectory(self, "Куда сохранить результат?", options = QFileDialog.ShowDirsOnly)
    
def _winEncode(s):
  return str(bytes(s,"cp1251"),"cp866")

if __name__ == '__main__':
  try:
    from ctypes import windll  # Only exists on Windows.
    myappid = 'mycompany.myproduct.subproduct.version'
    windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)
  except ImportError:
      pass

  app = QApplication()
  window = MainWindow()
  window.show()
  app.setWindowIcon(QtGui.QIcon(QtGui.QPixmap(':/icons/icon.ico')))
  window.setWindowIcon(QtGui.QIcon(QtGui.QPixmap(':/icons/icon.ico')))
  sys.exit(app.exec())
