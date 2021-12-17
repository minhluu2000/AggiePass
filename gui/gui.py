import sys
from PyQt5 import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import pandas as pd
# from database import mydb as database
# from constant import database_name, authentication_tab, password_vault_tab
# import encrypt_tools as enc
# from ard_comm import arduino_wr

# Define the welcome page.


class welcome(QWidget):

   def __init__(self, parent=None):
      super(welcome, self).__init__(parent)

      # create the widgets.
      # the title of the window.
      self.title = QLabel("Aggie Pass")
      # the second line of title
      self.title2 = QLabel("Please Scan Your RFID")
      # the third line of title
      self.title3 = QLabel("Please Enter Your PIN")
      # add the text edit bar, this will serve as the input box of PIN.
      self.edit = QLineEdit()
      self.button_submit = QPushButton("LOG IN")      # add the submit button
      self.button_register = QPushButton("REGISTER")  # add the submit button

      # modify the stylesheets of the titles.
      self.title.setStyleSheet("color: white; font: bold 25px")
      self.title2.setStyleSheet("color: white; font: bold 15px")
      self.title3.setStyleSheet("color: white; font: bold 15px")

      # modify the stylesheet of the edit bar.
      self.edit.setFixedWidth(400)
      self.edit.setFixedHeight(40)
      self.edit.setStyleSheet(
         "background-color: white; color: #800000; font: 14px; border-color: white")
      self.edit.setAlignment(Qt.AlignCenter)
      # Selects all the texts currently in the text box, so the new values will immediately replace the default.
      self.edit.selectAll()

      # modify the stylesheet of submission button.
      self.button_submit.clicked.connect(self.submission)
      self.button_submit.setStyleSheet(
         "background-color: white; color: #800000; font: bold 14px")
      self.button_submit.setFixedWidth(170)
      self.button_submit.setFixedHeight(60)

      # modify the stylesheet of registration button.
      self.button_register.clicked.connect(self.registration)
      self.button_register.setStyleSheet(
         "background-color: white; color: #800000; font: bold 12px")
      self.button_register.setFixedWidth(80)
      self.button_register.setFixedHeight(30)

      # create a layout fot he window, and then add the widgets to the layout.
      layout = QVBoxLayout(self)
      layout.addWidget(self.button_register, alignment=Qt.AlignRight)
      layout.addWidget(self.title, alignment=Qt.AlignCenter)
      layout.addWidget(self.title2, alignment=Qt.AlignCenter)
      layout.addWidget(self.title3, alignment=Qt.AlignCenter)
      layout.addWidget(self.edit, alignment=Qt.AlignCenter)
      layout.addWidget(self.button_submit, alignment=Qt.AlignCenter)

      # set the layout for the window
      self.setLayout(layout)

      # modify the stylesheet of the window
      self.setStyleSheet("background-color: #800000")
      self.setWindowFlag(Qt.FramelessWindowHint)
      self.showMaximized()

      # no registration window yet.
      self.reg = None

      # no management window yet.
      self.manage = None

   # This method is invoked by button click, it will be changed in the future.
   def submission(self):
      print(f"Hello, {self.edit.text()}")
      if self.manage == None:
         self.manage = manager()
         self.manage.show()
         self.close()
         self = None
      else:
         self.manage.close()
         self.manage = None

   # This method is invoked by button click, it will be changed in the future.
   def registration(self):
      if self.reg == None:
         self.reg = registration()
         self.reg.show()
         self.close()
         self = None
      else:
         self.reg.close()
         self.reg = None


# Define the registration page.
class registration(QWidget):
   def __init__(self, parent=None):
      super(registration, self).__init__(parent)

      # Creating a new account
      # Connect to database
      # db = database(database_name)
      # db.connect()

      # create the widgets.
      # the title of the window.
      self.title = QLabel("Registration")
      # the second line of title
      self.title2 = QLabel("Please Scan Your RFID")
      # the third line of title
      self.title3 = QLabel("Please Enter Your PIN")
      # add the text edit bar, this will serve as the input box of PIN.
      self.edit = QLineEdit()
      self.button_submit = QPushButton("SUBMIT")      # add the submit button
      self.button_home = QPushButton("HOME")  # add the submit button

      # modify the stylesheets of the titles.
      self.title.setStyleSheet("color: white; font: bold 25px")
      self.title2.setStyleSheet("color: white; font: bold 15px")
      self.title3.setStyleSheet("color: white; font: bold 15px")

      # modify the stylesheet of the edit bar.
      self.edit.setFixedWidth(400)
      self.edit.setFixedHeight(40)
      self.edit.setStyleSheet(
         "background-color: white; color: #800000; font: 14px; border-color: white")
      self.edit.setAlignment(Qt.AlignCenter)
      # Selects all the texts currently in the text box, so the new values will immediately replace the default.
      self.edit.selectAll()

      # modify the stylesheet of submission button.
      self.button_submit.clicked.connect(self.submission)
      self.button_submit.setStyleSheet(
         "background-color: white; color: #800000; font: bold 14px")
      self.button_submit.setFixedWidth(170)
      self.button_submit.setFixedHeight(60)

      # modify the stylesheet of registration button.
      self.button_home.clicked.connect(self.home)
      self.button_home.setStyleSheet(
         "background-color: white; color: #800000; font: bold 12px")
      self.button_home.setFixedWidth(80)
      self.button_home.setFixedHeight(30)

      # create a layout fot he window, and then add the widgets to the layout.
      layout = QVBoxLayout(self)
      layout.addWidget(self.button_home, alignment=Qt.AlignRight)
      layout.addWidget(self.title, alignment=Qt.AlignCenter)
      layout.addWidget(self.title2, alignment=Qt.AlignCenter)
      layout.addWidget(self.title3, alignment=Qt.AlignCenter)
      layout.addWidget(self.edit, alignment=Qt.AlignCenter)
      layout.addWidget(self.button_submit, alignment=Qt.AlignCenter)

      # set the layout for the window
      self.setLayout(layout)

      # modify the stylesheet of the window

      self.setStyleSheet("background-color: #800000")
      self.setWindowFlag(Qt.FramelessWindowHint)
      self.showMaximized()

      # Read tag to get UID, check if it is new
      # rfid_card_data = arduino_wr(mode='r')
      # uid = rfid_card_data[0]
      # uid_status = db.uid_exist(uid)
      # if (not uid_status):
      #    print('New UID detected...')
      #    self.title2.setText('New UID detected...')
      # else:
      #    print('UID recognized! Please use log in screen instead!')
      #    exit()


      # no home window yet.
      self.hm = None

   # This method is invoked by button click, it will be changed in the future.
   def submission(self):
      print(f"Hello, {self.edit.text()}")
      self.home()

   # This method is invoked by button click, it will be changed in the future.
   def home(self):
      if self.hm == None:
         self.hm = welcome()
         self.hm.show()
         self.close()
         self = None
      else:
         self.hm.close()
         self.hm = None


data = {
        'acc_description':['dafergdsgagdadsa1234', 'dsa4dsa32dgsat4', '2fdsat4eadfa454', '2efdsa4ty5yhts', 'dsa234gdfsa4ytqa'],
        'acc_username':['sa2rfdsa32gsa', 'a32t2dsa4tf', '2rgdfsaaw34gra', 'as32fdsa4ygfdsa', 'q2fdsa32ytgfdas'],
        'acc_password':['2esda32tdsa3tgrsae312sa3', 'as4esagesa32afdsafdsa', '1ea43wadasf43ag4a4', '2gsa33at4afdsa', '23ta4a4ygs4ay4afds'] 
        }
df = pd.DataFrame(data)
pass_data = df.to_numpy()

# Define the manager page.
class manager(QWidget):
   def __init__(self, parent=None):
      super(manager, self).__init__(parent)

      self.button_export = QPushButton("SELECT")
      self.button_add = QPushButton("ADD")        # add the add button
      self.button_delete = QPushButton("DELETE")  # add the delete button
      self.button_home = QPushButton("LOG OUT")      # add the home button

      # modify the stylesheet of buttonS.
      self.button_home.clicked.connect(self.home)
      self.button_home.setStyleSheet("background-color: white; color: #800000; font: bold 12px")
      self.button_home.setFixedWidth(80)
      self.button_home.setFixedHeight(30)
      
      self.button_add.clicked.connect(self.add)
      self.button_add.setStyleSheet("background-color: white; color: #800000; font: bold 12px")
      self.button_add.setFixedWidth(80)
      self.button_add.setFixedHeight(30)

      self.button_delete.clicked.connect(self.delete)
      self.button_delete.setStyleSheet("background-color: white; color: #800000; font: bold 12px")
      self.button_delete.setFixedWidth(80)
      self.button_delete.setFixedHeight(30)
      
      self.button_export.clicked.connect(self.export)
      self.button_export.setStyleSheet("background-color: white; color: #800000; font: bold 12px")
      self.button_export.setFixedWidth(80)
      self.button_export.setFixedHeight(30)

      # create a horizontal layout to contain the table.
      layout_h = QHBoxLayout()
      layout_h.addWidget(self.createTable(), stretch = 1, alignment=Qt.AlignCenter)

      # create a horizontal layout to contain the buttons.
      layout_buttons = QHBoxLayout()
      layout_buttons.addWidget(self.button_export)
      layout_buttons.addWidget(self.button_add)
      layout_buttons.addWidget(self.button_delete)
      layout_buttons.addWidget(self.button_home)

      # create a layout fot he window, and then add the widgets to the layout.
      layout = QVBoxLayout(self)
      layout.addLayout(layout_buttons)
      layout.addLayout(layout_h)
   
      # set the layout for the window
      self.setLayout(layout)

      # modify the stylesheet of the window
      self.setStyleSheet("background-color: #800000; QInputDialog{background-color:white}")
      self.setWindowFlag(Qt.FramelessWindowHint)
      self.showMaximized()

      # no home window yet.
      self.hm = None

   # This method is invoked by button click, it will be changed in the future.
   def home(self):
      if self.hm == None:
         self.hm = welcome()
         self.hm.show()
         self.close()
         self = None
      else:
         self.hm.close()
         self.hm = None
   
   # This method is to create a table for passwords, and user names, etc.
   def createTable(self):
      # initailize a table object.
      self.tableWidget = QTableWidget()
      
      # this line prevents triggering edit once clicked on the cell.
      self.tableWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)

      # sets the size of the table, we need to manually change the width and height to make it fill the window.
      self.tableWidget.setFixedWidth(460)
      self.tableWidget.setFixedHeight(240)

      # row and column count.
      self.tableWidget.setRowCount(len(df.acc_username))
      self.tableWidget.setColumnCount(3)

      # set the column headers.
      idx = 0
      for i in df.columns.values:
         new_header =  QTableWidgetItem(i)
         new_header.setForeground(QColor(255, 255, 255))
         self.tableWidget.setHorizontalHeaderItem(idx, new_header)
         idx += 1

      # set the cell values.
      for i in range(self.tableWidget.rowCount()):
         for j in range(self.tableWidget.columnCount()):
            new_item = QTableWidgetItem(pass_data[i][j])
            new_item.setForeground(QColor(255, 255, 255))
            self.tableWidget.setItem(i,j, new_item)
      
      # stretch the header view to fill the window. 
      # still need to set the size of table, this line only makes the table fill the rectangle with fixed size.
      self.tableWidget.horizontalHeader().setStretchLastSection(True)
      self.tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
      self.tableWidget.setSelectionBehavior(QTableView.SelectRows)
      # self.tableWidget.selectionModel().selectionChanged.connect(self.selectionFunction)
      return self.tableWidget
   
   # Obtain the password on the selected row
   def export(self):
      try:
         r = self.tableWidget.selectionModel().selectedRows()
         password = self.tableWidget.item(r[0].row(),2).text() # get the passowrd value based on the row number obtained above.
         print(password)
      except IndexError:
         pass

   def delete(self):
      try:
         r = self.tableWidget.selectionModel().selectedRows()
         self.tableWidget.removeRow(r[0].row())     # Remove the selected Row
      except IndexError:
         pass

   def add(self):
      userInput = QInputDialog(self)
      userInput.setStyleSheet("background-color: white")
      # userInput.setBackground(QColor(255, 255, 255))

      des, done1 = userInput.getText(
         self, 'Add Password', 'Enter Description:')

      username, done2 = userInput.getText(
         self, 'Add Password', 'Enter Username:')

      password, done3 = userInput.getText(
         self, 'Add Password', 'Enter Passoword:')
      
      if done1 and done2 and done3:
         if (des != "" or username != "" or password != ""):
            # insert a new empty row at the bottom of the table
            rowPosition = self.tableWidget.rowCount()
            self.tableWidget.insertRow(rowPosition)

            # create new values for the row
            new_des = QTableWidgetItem(des)
            new_username = QTableWidgetItem(username)
            new_pass = QTableWidgetItem(password)

            # set up text colors for new description, username and password
            new_des.setForeground(QColor(255, 255, 255))
            new_username.setForeground(QColor(255, 255, 255))
            new_pass.setForeground(QColor(255, 255, 255))

            self.tableWidget.setItem(rowPosition , 0, new_des)
            self.tableWidget.setItem(rowPosition , 1, new_username)
            self.tableWidget.setItem(rowPosition , 2, new_pass)
  
def main():
   app = QApplication(sys.argv)
   screen = app.primaryScreen()
   print('Screen: %s' % screen.name())
   rect = screen.availableGeometry()
   print('Available: %d x %d' % (rect.width(), rect.height()))
   ex = welcome()
   ex.show()
   sys.exit(app.exec_())


if __name__ == '__main__':
   main()
