import sys
from PyQt5.QtWidgets import QDialog, QLineEdit
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QComboBox, QPushButton, QTableWidget, QTableWidgetItem
import psycopg2

class DatabaseManager:
    def __init__(self, host, port, database, user, password):
        self.conn = psycopg2.connect(host=host, port=port, database=database, user=user, password=password)
        self.cur = self.conn.cursor()
        
    def get_primary_key_column(self, table_name):
        try:
            with self.conn:
                with self.conn.cursor() as cur:
                    # Fetch the primary key column using the table_constraints and key_column_usage
                    cur.execute("""
                        SELECT column_name
                        FROM information_schema.key_column_usage
                        WHERE table_name = %s
                    """, (table_name,))

                    # Check if any primary key columns are found
                    columns_info = cur.fetchall()

                    if columns_info:
                        return columns_info[0][0]  # Return the first primary key column found
                    else:
                        print(f"Primary key column not found for table '{table_name}'.")
                        return None
        except Exception as e:
            print(f"Error fetching primary key column: {e}")
            return None
        
    def execute_query(self, query, values=None):
        try:
            self.cur.execute(query, values)
            self.conn.commit()  # Commit changes explicitly
        except Exception as e:
            print(f"Error executing query: {e}")
            self.conn.rollback()  # Rollback in case of an error

    def read_table(self, table_name):
        sql_query = f"SELECT * FROM {table_name};"
        self.cur.execute(sql_query)
        return self.cur.fetchall()
    def fetch_data(self, query, values=None):
        try:
            if values is not None:
                self.cur.execute(query, values)
            else:
                self.cur.execute(query)

            result = self.cur.fetchall()
            return result[0] if result else None
        except Exception as e:
            print(f"Error fetching data: {e}")
            return None

    def close_connection(self):
        self.conn.close()

class CRUDApp(QWidget):
    def __init__(self):
        super().__init__()

        self.init_ui()

    def init_ui(self):
        self.db_manager = DatabaseManager(host='localhost', port="5433", database='lab5', user='postgres', password='123qwerty')

        self.table_names = ['col1', 'col2', 'col3']  # Replace with your table names

        self.table_label = QLabel('Select Table:')
        self.table_combobox = QComboBox()
        self.load_table_names()

        self.data_table = QTableWidget()

        self.load_data_button = QPushButton('Load Data')
        self.add_button = QPushButton('Add Row')
        self.update_button = QPushButton('Update Row')
        self.delete_button = QPushButton('Delete Row')

        self.load_data_button.clicked.connect(self.load_data)
        self.add_button.clicked.connect(self.add_row)
        self.update_button.clicked.connect(self.update_row)
        self.delete_button.clicked.connect(self.delete_row)

        vbox = QVBoxLayout()
        hbox = QHBoxLayout()

        hbox.addWidget(self.table_label)
        hbox.addWidget(self.table_combobox)
        hbox.addWidget(self.load_data_button)

        vbox.addLayout(hbox)
        vbox.addWidget(self.data_table)
        vbox.addWidget(self.add_button)
        vbox.addWidget(self.update_button)
        vbox.addWidget(self.delete_button)

        self.setLayout(vbox)

        self.setGeometry(100, 100, 800, 600)
        self.setWindowTitle('CRUD App')
        self.show()

    def load_data(self):
        table_name = self.table_combobox.currentText()
        print(f"Table name: {table_name}")  # Add this line to see the table name

        if table_name in self.table_names:
            query = f"SELECT * FROM {table_name};"
            data = self.db_manager.fetch_data(query)

            if data:
                self.populate_table(data)
            else:
                self.data_table.setRowCount(0)
        else:
            print(f"Table '{table_name}' does not exist.")

    def populate_table(self, data, column_names):
        self.data_table.clearContents()
        self.data_table.setRowCount(len(data))
        self.data_table.setColumnCount(len(data[0]))

        for col_index, col_name in enumerate(column_names):
            header_item = QTableWidgetItem(str(col_name))
            self.data_table.setHorizontalHeaderItem(col_index, header_item)

        for row_index, row_data in enumerate(data):
            for col_index, col_data in enumerate(row_data):
                item = QTableWidgetItem(str(col_data))
                self.data_table.setItem(row_index, col_index, item)

    # Add this method to your CRUDApp class
    def load_table_names(self):
        # Replace the following line with the logic to fetch the table names from the database
        # For example, you can query the PostgreSQL catalog for table names
        self.table_names = ['col1', 'col2', 'col3']

        self.table_combobox.clear()
        self.table_combobox.addItems(self.table_names)

    def load_data(self):
        table_name = self.table_combobox.currentText()
        print(f"Table name: {table_name}")

        if table_name in self.table_names:
            data = self.db_manager.read_table(table_name)

            if data:
                # Fetch the column names separately
                columns_query = f"SELECT column_name FROM information_schema.columns WHERE table_name = %s;"
                column_names = [column[0] for column in self.db_manager.fetch_data(columns_query, (table_name,))]

                # Fetch the primary key column
                primary_key_column = self.db_manager.get_primary_key_column(table_name)

                if primary_key_column is not None:
                    print(f"Primary key column for table '{table_name}': {primary_key_column}")

                    # Ensure the primary key column is included in the list of column names
                    if primary_key_column not in column_names:
                        column_names.insert(0, primary_key_column)

                    self.populate_table(data, column_names)
                else:
                    print(f"Primary key column not found for table '{table_name}'.")
            else:
                self.data_table.setRowCount(0)
        else:
            print(f"Table '{table_name}' does not exist.")

    def add_row(self):
        table_name = self.table_combobox.currentText()

        # Fetch the column names from the table
        columns_query = f"SELECT column_name FROM information_schema.columns WHERE table_name = %s;"
        column_names = [column[0] for column in self.db_manager.fetch_data(columns_query, (table_name,))]

        if not column_names:
            print(f"Column names not available for table '{table_name}'. Unable to add row.")
            return

        # Update the column_names list to match the actual columns in your "col1" table
        column_names = ["col1_id", "col1_name", "col1_values"]

        # Ask the user to input values for a new row
        new_values, ok = self.get_new_values(column_names)

        if ok:
            # Prepare the INSERT query
            columns = ', '.join(column_names)
            placeholders = ', '.join(['%s' for _ in new_values])
            query = f"INSERT INTO {table_name} ({columns}) VALUES ({placeholders});"

            try:
                # Execute the INSERT query with parameters
                self.db_manager.execute_query(query, tuple(new_values))

                print("Row added successfully.")
            except Exception as e:
                print(f"Error adding row: {e}")
            finally:
                # Refresh the displayed data in the table
                self.load_data()

    def get_new_values(self, column_names):
        # Create a dialog to get new values from the user
        dialog = QDialog(self)
        dialog.setWindowTitle("Add New Row")

        # Create layout and widgets
        layout = QVBoxLayout()

        input_widgets = []
        for col_name in column_names:
            label = QLabel(f"Enter value for {col_name}:")
            line_edit = QLineEdit()
            input_widgets.append(line_edit)
            layout.addWidget(label)
            layout.addWidget(line_edit)

        ok_button = QPushButton("OK")
        ok_button.clicked.connect(dialog.accept)

        cancel_button = QPushButton("Cancel")
        cancel_button.clicked.connect(dialog.reject)

        layout.addWidget(ok_button)
        layout.addWidget(cancel_button)

        dialog.setLayout(layout)

        # Show the dialog
        result = dialog.exec_()

        # Check if the user clicked OK
        if result == QDialog.Accepted:
            new_values = [widget.text() for widget in input_widgets]
            return new_values, True
        else:
            return None, False

    def update_row(self, new_col1_id=None, new_col1_name=None, new_col1_values=None):
        table_name = "col1"  # Update with your actual table name

        # Fetch the primary key column
        primary_key_column = self.db_manager.get_primary_key_column(table_name)

        if primary_key_column is None:
            print(f"Primary key column not found for table '{table_name}'. Unable to update row.")
            return

        # Fetch the current values for the selected row
        current_row = self.data_table.currentRow()

        # If new values are not provided, prompt the user to enter them
        if new_col1_name is None or new_col1_values is None:
            current_values = [
                self.data_table.item(current_row, col).text()
                for col in range(self.data_table.columnCount())
            ]

            updated_values, ok = self.get_updated_values(current_values)

            if not ok:
                print("Update canceled by the user.")
                return

            # Assign the updated values
            new_col1_id, new_col1_name, new_col1_values = updated_values

        # Prepare the SET clause for the UPDATE query
        set_clause_parts = [
            f'"{primary_key_column}" = %s',
            f'"col1_name" = %s',
            f'"col1_values" = %s'  # Replace with your actual column name
        ]
        values = [new_col1_id, new_col1_name, new_col1_values]

        # Build the complete SET clause
        set_clause = ', '.join(set_clause_parts)

        # Build the WHERE clause for the UPDATE query
        where_clause = f'"{primary_key_column}" = %s'
        values.append(new_col1_id)

        # Combine both clauses to form the complete UPDATE query
        query = f'UPDATE "{table_name}" SET {set_clause} WHERE {where_clause} RETURNING "{primary_key_column}";'

        try:
            # Execute the UPDATE query with parameters
            self.db_manager.execute_query(query, tuple(values))

            print("Row updated successfully.")
        except Exception as e:
            print(f"Error updating row: {e}")
        finally:
            # Refresh the displayed data in the table
            self.load_data()

    def get_updated_values(self, current_values):
        # Create a dialog to get updated values from the user
        dialog = QDialog(self)
        dialog.setWindowTitle("Update Row")

        # Create layout and widgets
        layout = QVBoxLayout()

        input_widgets = []
        for col_index, col_value in enumerate(current_values):
            label = QLabel(f"Update value for column {col_index + 1}:")
            line_edit = QLineEdit()
            line_edit.setText(col_value)
            input_widgets.append(line_edit)
            layout.addWidget(label)
            layout.addWidget(line_edit)

        ok_button = QPushButton("OK")
        ok_button.clicked.connect(dialog.accept)

        cancel_button = QPushButton("Cancel")
        cancel_button.clicked.connect(dialog.reject)

        layout.addWidget(ok_button)
        layout.addWidget(cancel_button)

        dialog.setLayout(layout)

        # Show the dialog
        result = dialog.exec_()

        # Check if the user clicked OK
        if result == QDialog.Accepted:
            updated_values = [widget.text() for widget in input_widgets]
            return updated_values, True  # Return a single list of updated values
        else:
            return current_values, False  # Return the original values and indicate update cancellation

    def get_primary_key_column(self, table_name):
        # Fetch the column information from the PostgreSQL catalog
        self.cur.execute("""
            SELECT column_name
            FROM information_schema.columns
            WHERE table_name = %s AND column_default LIKE 'nextval(%%'
        """, (table_name,))

        # Check if any serial columns are found
        columns_info = self.cur.fetchall()

        if columns_info:
            return columns_info[0][0]  # Return the first serial column found
        else:
            print(f"Serial primary key column not found for table '{table_name}'.")
            return None

    def get_column_index(self, column_name):
        header_items = [self.data_table.horizontalHeaderItem(i) for i in range(self.data_table.columnCount())]
        column_names = [item.text() if item is not None else '' for item in header_items]
        
        try:
            index = column_names.index(column_name)
            return index
        except ValueError:
            print(f"Column '{column_name}' not found in the table header.")
            print("Column Names:", column_names)
            return -1  # Return a sentinel value to indicate column not found

    def delete_row(self):
        table_name = self.table_combobox.currentText()

        current_row = self.data_table.currentRow()
        if current_row >= 0 and current_row < self.data_table.rowCount():
            primary_key_column = self.db_manager.get_primary_key_column(table_name)

            if primary_key_column is not None:
                print(f"Primary key column for table '{table_name}': {primary_key_column}")

                # Get the primary key value of the selected row
                primary_key_index = self.get_column_index(primary_key_column)
                if primary_key_index != -1:
                    # Get the primary key value of the selected row
                    primary_key_value = self.data_table.item(current_row, primary_key_index).text()

                    query = f"DELETE FROM {table_name} WHERE {primary_key_column} = %s RETURNING {primary_key_column};"
                    deleted_primary_key_result = self.db_manager.fetch_data(query, (primary_key_value,))

                    if deleted_primary_key_result:
                        deleted_primary_key = deleted_primary_key_result[0]
                        print(f"Row deleted with primary key: {deleted_primary_key}")
                    else:
                        print("Failed to delete row.")

                    self.load_data()
                else:
                    print(f"Primary key column '{primary_key_column}' not found in the table header.")
            else:
                print(f"Primary key column not found for table '{table_name}'.")
        else:
            print("No row selected.")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = CRUDApp()
    sys.exit(app.exec_())