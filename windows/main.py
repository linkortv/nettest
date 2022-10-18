import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QFileDialog
from PySide6 import QtGui
from form import Ui_MainWindow
import windows
import sptest
import resources
# import pdb

class MainWindow(QMainWindow):
  def __init__(self, parent=None):
    super(MainWindow, self).__init__(parent)

    self.ui = Ui_MainWindow()
    self.ui.setupUi(self)
    self.ui.progressBar.setValue(0)
    self.ui.start_test.clicked.connect(self.start_test)
    self.ui.full_test.clicked.connect(self.full_test)

  def full_test(self):
    line_address = self.ui.lineEdit.text()
    if len(line_address) != 0:
      address = line_address
    elif len(self.ui.comboBox.currentText()) != 0:
      service = self.ui.comboBox.currentText()
      address = windows.getAddress(service)
    
    fname = _dirDialog(self)
    if len(fname) > 1:
      f = open(f'{fname}/nettest.txt', "w+")
      # pdb.set_trace()
      status = "Проверяется доступность dns-сервера(1/2)"
      self.ui.status_label.setText(status)
      self.ui.progressBar.setValue(1)
      f.write("DNS #1\n")
      f.write(_winEncode(windows.fping_dns1(10) + '\n'))
      
      status = "Проверяется доступность dns-сервера(2/2)"
      self.ui.status_label.setText(status)
      self.ui.progressBar.setValue(5)
      f.write("DNS #2\n")
      f.write(_winEncode(windows.fping_dns2(10) + '\n'))

      status = "Измеряем задержку до yandex"
      self.ui.status_label.setText(status)
      self.ui.progressBar.setValue(15)
      f.write(_winEncode(windows.fping_service("ya.ru", 10) + '\n'))

      status = "Измеряем задержку до google"
      self.ui.status_label.setText(status)
      self.ui.progressBar.setValue(20)
      f.write(_winEncode(windows.fping_service("google.com", 10) + '\n'))

      status = "Измеряем задержку до внешних сервисов(1/4)"
      self.ui.status_label.setText(status)
      self.ui.progressBar.setValue(25)
      f.write(_winEncode(windows.fping_service("store.steampowered.com", 10) + '\n'))

      status = "Измеряем задержку до внешних сервисов(2/4)"
      self.ui.status_label.setText(status)
      self.ui.progressBar.setValue(30)
      f.write(_winEncode(windows.fping_service("blizzard.com", 10) + '\n'))

      status = "Измеряем задержку до внешних сервисов(3/4)"
      self.ui.status_label.setText(status)
      self.ui.progressBar.setValue(35)
      f.write(_winEncode(windows.fping_service("store.playstation.com", 10) + '\n'))

      status = "Измеряем задержку до внешних сервисов(4/4)"
      self.ui.status_label.setText(status)
      self.ui.progressBar.setValue(40)
      f.write(_winEncode(windows.fping_service("vk.com", 10) + '\n'))

      status = "Проверяем скорость"
      self.ui.status_label.setText(status)
      self.ui.progressBar.setValue(45)
      f.write('Speedtest\n')
      f.write(sptest.sptest() + '\n')

      status = "Проверяем задержку до выбранного сервиса"
      self.ui.status_label.setText(status)
      self.ui.progressBar.setValue(60)
      f.write(f"\nping {service}\n")
      f.write(_winEncode(windows.fping_service(address) + '\n'))

      status = "Проводим трассировку до выбранного сервиса"
      self.ui.status_label.setText(status)
      self.ui.progressBar.setValue(70)
      f.write(f"tracert {service}\n")
      f.write(_winEncode(windows.trace_service(address) + '\n'))

      f.close()
      self.ui.progressBar.setValue(100)
      self.ui.status_label.setText("Проверка завершена")
      
      windows.dir_open(fname)
    else:
      return False

  def start_test(self):
    fname = _dirDialog(self)
    if len(fname) > 1:
      f = open(f'{fname}/nettest.txt', "w+")
      status = "ping dns1"
      self.ui.status_label.setText(status)
      self.ui.progressBar.setValue(1)
      f.write(f"ping DNS1\n")
      f.write(_winEncode(windows.fping_dns1() + '\n'))
      
      status = "ping dns2"
      self.ui.status_label.setText(status)
      self.ui.progressBar.setValue(15)
      f.write(f"ping DNS2\n")
      f.write(_winEncode(windows.fping_dns2() + '\n'))

      status = "ping yandex"
      self.ui.status_label.setText(status)
      self.ui.progressBar.setValue(30)
      f.write(_winEncode(windows.fping_service("ya.ru") + '\n'))
      

      status = "ping google"
      self.ui.status_label.setText(status)
      self.ui.progressBar.setValue(40)
      f.write(_winEncode(windows.fping_service("google.com") + '\n'))


      status = "ping steam"
      self.ui.status_label.setText(status)
      self.ui.progressBar.setValue(50)
      f.write(f"ping steam store\n")
      f.write(_winEncode(windows.fping_service("store.steampowered.com") + '\n'))

      status = "ping blizzard"
      self.ui.status_label.setText(status)
      self.ui.progressBar.setValue(60)
      f.write(f"ping blizzard\n")
      f.write(_winEncode(windows.fping_service("blizzard.com") + '\n'))

      status = "ping vk"
      self.ui.status_label.setText(status)
      self.ui.progressBar.setValue(70)
      f.write(_winEncode(windows.fping_service("vk.com") + '\n'))

      status = "ping playstation"
      self.ui.status_label.setText(status)
      self.ui.progressBar.setValue(80)
      f.write(f"ping playstation store\n")
      f.write(_winEncode(windows.fping_service("store.playstation.com") + '\n'))

      status = "проверка скорости"
      self.ui.status_label.setText(status)
      self.ui.progressBar.setValue(90)
      f.write(sptest.sptest_short() + '\n')

      f.close()

      self.ui.progressBar.setValue(100)
      self.ui.status_label.setText("complete")
      windows.dir_open(fname)
    else:
      return False
    
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
