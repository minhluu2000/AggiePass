import sys
import pandas as pd
import encrypt_tools as enc
from ard_comm import arduino_wr
from registration import new_uid_to_db
from PyQt5 import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from threading import *
from database import mydb as database
from constant import database_name
from authentication import login
 
# global secret key
secret_key = ''
# timers = []
current_uid = ''

# Define the welcome page.
class welcome(QWidget):
   # EXIT_CODE_REBOOT = -123
   def __init__(self, parent=None):
      super(welcome, self).__init__(parent)
      self.db = database(database_name)
      self.db.connect()

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
      # self.button_reset = QPushButton("RESET")  # add the submit button

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
      
      # modify the stylesheet of reset button.
      # self.button_reset.clicked.connect(self.reset)
      # self.button_reset.setStyleSheet(
      #    "background-color: white; color: #800000; font: bold 12px")
      # self.button_reset.setFixedWidth(80)
      # self.button_reset.setFixedHeight(30)

      # The horizontal layout for the buttons.
      # layout_buttons = QHBoxLayout()
      # layout_buttons.addWidget(self.button_reset, alignment=Qt.AlignRight)
      # horizontalSpacer = QSpacerItem(290, 0, QSizePolicy.Minimum, QSizePolicy.Minimum)
      # layout_buttons.addItem(horizontalSpacer)
      # layout_buttons.addWidget(self.button_register, alignment=Qt.AlignLeft)

      # create a layout for the window, and then add the widgets to the layout.
      layout = QVBoxLayout(self)
      # layout.addLayout(layout_buttons)
      layout.addWidget(self.button_register, alignment = Qt.AlignRight)
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

      # global timers
      # timer = QTimer()
      # timer.start(1000)
      # timer.timeout.connect(self.scan)
      # timers.append(timer)

      t1=Thread(target=self.scan)
      t1.daemon = True
      t1.start()
      
      # no registration window yet.
      self.reg = None

      # no management window yet.
      self.manage = None
   
   # def reset(self):
   #    qApp.exit(welcome.EXIT_CODE_REBOOT)

   # This method is invoked by button click, it will be changed in the future.
   def submission(self):
      try:
         # print(f"Hello, {self.edit.text()}")
         auth = login(self.db, self.uid, self.edit.text())
         if auth:
            # Forge the secret key and pass it to the password manager screen
            self.rand_str = self.rfid_card_data[1]
            global secret_key, current_uid
            secret_key = enc.forge_secret_key(tag_random_str=self.rand_str, pin = self.edit.text())
            current_uid = self.uid
            
            if self.manage == None:
               self.manage = manager()
               self.manage.show()
               self.close()
               self = None
            else:
               self.manage.close()
               self.manage = None
         else:
            self.title2.setText('Incorrect PIN, please try again')
            self.edit.clear()
      except AttributeError:
         self.title2.setText("No RFID tag detected, please scan your tag")
      

      
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
   
   # This method asks the user to scan the RFID tag and extracts the value out of it.
   def scan(self):
      # Read tag to get UID, check if it is new
      self.rfid_card_data = arduino_wr(mode='r')
      self.uid = self.rfid_card_data[0]
      print(self.uid)
      self.uid_status = self.db.uid_exist(self.uid)
      print(self.uid_status)
      if (not self.uid_status):
         # print('New UID detected...')
         self.title2.setText('Could not find the user information, please REGISTER')
      else:
         self.title2.setText('RFID found, please enter PIN')
      
      # global timers
      # timers.clear()

         
# Define the registration page.
class registration(QWidget):
   def __init__(self, parent=None):
      super(registration, self).__init__(parent)

      # Creating a new account
      # Connect to database
      self.db = database(database_name)
      self.db.connect()

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

      # global timers
      # timer = QTimer()
      # timer.start(1000)
      # timer.timeout.connect(self.scan)
      # timers.append(timer)

      t2=Thread(target=self.scan)
      t2.daemon = True
      t2.start()
     
      # no home window yet.
      self.hm = None

   # This method urges the user to scan the RFID tag
   def scan(self):
      # Read tag to get UID, check if it is new
      self.rfid_card_data = arduino_wr(mode='r')
      self.uid = self.rfid_card_data[0]
      # print(self.uid)
      self.uid_status = self.db.uid_exist(self.uid)
      # print(self.uid_status)
      if (not self.uid_status):
         # print('New UID detected...')
         self.title2.setText('New UID detected...')  
         # Generate a random string key
         self.rand_str = enc.random_str_gen()
         # Write it to rfid tag
         self.rfid_card_data = arduino_wr(mode='w', random_str=self.rand_str)
         self.written_rand_str = self.rfid_card_data[1]
         if self.rand_str == enc.hex_to_string(self.written_rand_str):
            print('Successfully written to the card!')
            self.title2.setText('Successfully written to the card!')
            # Generate a random string key
            self.rand_str = enc.random_str_gen()
      else:
         print('UID recognized! Please use log in screen instead!')
         self.title2.setText('UID recognized! Please use log in screen instead!')
         # exit()
      
      # global timers
      # timers.clear()

   # This method is invoked by button click, it will be changed in the future.
   def submission(self):
      # print(f"Hello, {self.edit.text()}")
      # Get a pin entry from user (Lide working on it)
      new_pin = self.edit.text()  # <-- placeholder

      # Generate a salt -> store it in DB
      rand_salt = enc.generate_pin_salt()
      
      try:
         if (not self.uid_status):
            hash = enc.pin_hash(new_pin, rand_salt)
            new_uid_to_db(db=self.db, uid=self.uid, salt=rand_salt, hash=hash)

         self.title2.setText("Registraion Successful, you may return to Home")
         self.edit.setText("")
      except AttributeError:
         self.title2.setText("No RFID tag detected, please scan your tag")

      
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

# Define the manager page.
class manager(QWidget):
   def __init__(self, parent = None):
      super(manager, self).__init__(parent)
      global secret_key, current_uid
      print(secret_key)
      print(current_uid)

      # Creating a new account
      # Connect to database
      self.db = database(database_name)
      self.db.connect()

      print(self.db.vault_exist(current_uid))
      if not self.db.vault_exist(current_uid):
         data = {
        'acc_description':[],
        'acc_username':[],
        'acc_password':[]
        }
         self.df = pd.DataFrame(data)
         self.pass_data = self.df.to_numpy()
      else:
         encryted_df = self.db.user_vault(current_uid)
         print(encryted_df)
         self.df = enc.decrypt_vault(secret_key, encryted_df)
         print(self.df)
         self.df = self.df.drop(columns = ['uid'])
         self.pass_data = self.df.to_numpy()

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
         global secret_key, current_uid
         
         self.df.insert(0, 'uid', [current_uid for i in range(len(self.df.acc_password))], True)
         encrypted_df = enc.encrypt_vault(secret_key, self.df)
         self.db.update_user_vault(current_uid, encrypted_df)

         secret_key = ''
         current_uid = ''
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
      self.tableWidget.setRowCount(len(self.df.acc_username))
      self.tableWidget.setColumnCount(3)

      # set the column headers.
      idx = 0
      for i in self.df.columns.values:
         new_header =  QTableWidgetItem(i)
         new_header.setForeground(QColor(255, 255, 255))
         self.tableWidget.setHorizontalHeaderItem(idx, new_header)
         idx += 1

      # set the cell values.
      for i in range(self.tableWidget.rowCount()):
         for j in range(self.tableWidget.columnCount()):
            new_item = QTableWidgetItem(self.pass_data[i][j])
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
         print(r[0].row())
         self.tableWidget.removeRow(r[0].row())     # Remove the selected Row
         self.df = self.df.drop([r[0].row()])
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

            # update the dataframe
            new_df = {'acc_description': des, 'acc_username': username, 'acc_password': password}
            self.df = self.df.append(new_df, ignore_index = True)

  
def main():
   # currentExitCode = welcome.EXIT_CODE_REBOOT
   # while currentExitCode == welcome.EXIT_CODE_REBOOT:
   app = QApplication(sys.argv)
   screen = app.primaryScreen()
   print('Screen: %s' % screen.name())
   rect = screen.availableGeometry()
   print('Available: %d x %d' % (rect.width(), rect.height()))
   ex = welcome()
   ex.show()
   # currentExitCode = app.exec_()
   sys.exit(app.exec_())
   # app = None


if __name__ == '__main__':
   main()
