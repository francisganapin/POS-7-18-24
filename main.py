import sys
from PyQt6 import QtWidgets, uic
import os
import csv
from datetime import datetime
from PyQt6.QtGui import QStandardItemModel, QStandardItem

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()

        uic.loadUi('main.ui', self)

        # Initialize the price
        self.price = 0

        # Set fixed size based on loaded UI
        self.setFixedSize(self.size())

        # Find and connect the button
        self.caramel_bt.clicked.connect(self.caramel)
        self.melon_bt.clicked.connect(self.melon)
        self.chocolate_bt.clicked.connect(self.chocoalte)
        self.straberry_bt.clicked.connect(self.straberry)
        self.vanilla_bt.clicked.connect(self.vanilla)
        self.avocado_bt.clicked.connect(self.avocado)   
        self.okinawa_bt.clicked.connect(self.okinawa)
        self.mango_bt.clicked.connect(self.mango)
        self.mocha_bt.clicked.connect(self.mocha)
        self.hazelnut_bt.clicked.connect(self.hazelnut)
        self.red_velvet_bt.clicked.connect(self.red_velvet)
        self.java_bt.clicked.connect(self.java)

        self.check_out_bt.clicked.connect(self.create_pdf)
        #self.check_out_bt.clicked.connect(self.clear_order)


        # Find the label for displaying the total price
        self.label_total = self.findChild(QtWidgets.QLabel, 'label_total')

        # Find the text edit widget
        self.text_edit = self.findChild(QtWidgets.QTextEdit, 'textEdit')
        self.display_login_records()


    def okinawa(self):
        # Increment the price
        self.price += 130
        self.text_edit.append('Okinawa                130PHP')
        self.text_edit.append(f'')
        self.label_total.setText(f'Total Price: {self.price}')

    def mango(self):
        # Increment the price
        self.price += 120
        self.text_edit.append('Mango                   120PHP')
        self.text_edit.append(f'')
        self.label_total.setText(f'Total Price: {self.price}')

    def mocha(self):
        # Increment the price
        self.price += 140
        self.text_edit.append('Mocha                   140PHP')
        self.text_edit.append(f'')
        self.label_total.setText(f'Total Price: {self.price}')


    def hazelnut(self):
        # Increment the price
        self.price += 150
        self.text_edit.append('Hazelnut                150PHP')
        self.text_edit.append(f'')
        self.label_total.setText(f'Total Price: {self.price}')

    def red_velvet(self):
        # Increment the price
        self.price += 160
        self.text_edit.append('Red Velvet              160PHP')
        self.text_edit.append(f'')
        self.label_total.setText(f'Total Price: {self.price}')

    def java(self):
        # Increment the price
        self.price += 170
        self.text_edit.append('Java                    170PHP')
        self.text_edit.append(f'')
        self.label_total.setText(f'Total Price: {self.price}')


    def caramel(self):
        # Increment the price
        self.price += 130
        # Print the updated price to the console
        print(f'Price:{self.price}')
        # Display the updated price in the text edit widget
        self.text_edit.append(f'Caramel                130PHP')
        self.text_edit.append(f'')
        # Update the label with the total price
        self.label_total.setText(f'Total Price: {self.price}')

    def melon(self):
        # Increment the price
        self.price += 90
        # Print the updated price to the console
        print(f'Price: {self.price}')
        # Display the updated price in the text edit widget
        self.text_edit.append(f'Melon                  90PHP ')
        self.text_edit.append(f'')
        # Update the label with the total price
        self.label_total.setText(f'Total Price: {self.price}')
    def chocoalte(self):
        # Increment the price
        self.price += 100
        # Print the updated price to the console
        print(f'Price: {self.price}')
        # Display the updated price in the text edit widget
        self.text_edit.append(f'Chocolate             100PHP')
        self.text_edit.append(f'')
        # Update the label with the total price
        self.label_total.setText(f'Total Price: {self.price}')
    def avocado(self):
        # Increment the price
        self.price += 100
        # Print the updated price to the console
        print(f'Price: {self.price}')
        # Display the updated price in the text edit widget
        self.text_edit.append(f'avocado             100PHP')
        self.text_edit.append(f'')
        # Update the label with the total price
        self.label_total.setText(f'Total Price: {self.price}')
    def vanilla(self):
        # Increment the price
        self.price += 120
        # Print the updated price to the console
        print(f'Price: {self.price}')
        # Display the updated price in the text edit widget
        self.text_edit.append(f'Vanilla               120PHP')
        self.text_edit.append(f'')
        # Update the label with the total price
        self.label_total.setText(f'Total Price: {self.price}')
    def straberry(self):
        # Increment the price
        self.price += 90
        # Print the updated price to the console
        print(f'Price: {self.price}')
        # Display the updated price in the text edit widget
        self.text_edit.append(f'Straberry             90PHP ')
        self.text_edit.append(f'')
        # Update the label with the total price
        self.label_total.setText(f'Total Price: {self.price}')


    def create_pdf(self):
        """
        this code if the person was login it would save at login_records.csv
        """
        try:
            current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            orderdetails = self.text_edit.toPlainText()
            record = [ orderdetails, current_time]

            current_directory = os.path.dirname(os.path.abspath(__file__))
            file_path = os.path.join(current_directory, 'login_records.csv')

            file_exists = os.path.isfile(file_path)
            with open(file_path, 'a', newline='',encoding='utf-8') as file:
                writer = csv.writer(file)
                if not file_exists:
                    writer.writerow(["Name", "Login Time"])
                writer.writerow(record)
            print("Record saved successfully.")
        except FileNotFoundError :
            print(f"Error: File '{file_path}' not found.")
        except IOError as e:
            print(f"Error writing to file '{file_path}': {e}")
        except Exception as e:
            print(f"Unexpected error saving record: {e}")

    def display_login_records(self):
       
        current_directory = os.path.dirname(os.path.abspath(__file__))
        file_path = os.path.join(current_directory, 'login_records.csv')

        try:
            with open(file_path, 'r', newline='', encoding='utf-8') as file:
                        reader = csv.reader(file)
                        data = list(reader)

                    # Initialize a new model if it doesn't exist
            if not hasattr(self, 'tableView_3_model'):
                        self.tableView_3_model = QStandardItemModel()

                    # Set headers
            if data:
                        self.tableView_3_model.setHorizontalHeaderLabels(data[0])

                    # Populate data rows
            for row in data[1:]:
                    items = [QStandardItem(field) for field in row]
                    self.tableView_3_model.appendRow(items)

            print('Login Records Displayed Successfully')

                    # Ensure tableView_3 updates with the new model
            self.tableView_3.setModel(self.tableView_3_model)
            self.tableView_3.repaint()  # Or self.tableView_3.update()

        except FileNotFoundError:
            print(f"Error: File '{file_path}' not found.")
        except IOError as e:
            print(f"Error reading file '{file_path}': {e}")
        except csv.Error as e:
            print(f"CSV error while reading file '{file_path}': {e}")
        except Exception as e:
            print(f"Unexpected error displaying login records: {e}")
    

# Entry point for the application
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())


