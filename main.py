import sys
from PyQt5.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, QPushButton, QMessageBox, QRadioButton, QGroupBox
)
from joblib import load
import numpy as np


class LaptopPricePredictorApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.model = load('random_forest_model.joblib')  # Load the saved model

    def initUI(self):
        # Window setup
        self.setWindowTitle('Laptop Price Predictor')
        self.setGeometry(100, 100, 1200, 800)  # Adjusted size for better horizontal layout

        # Layouts
        self.main_layout = QVBoxLayout()
        self.input_layout = QVBoxLayout()

        # Define feature fields
        self.inputs = {}
        self.numeric_fields = [
            'Ram_In_GB', 'Weight', 'ScreenResolutionWidth', 'ScreenResolutionHeight', 'Cpu_ClockSpeed', 'Total_Memory_MB'
        ]
        self.boolean_fields = [
            'Touchscreen', 'IPS_Panel', '4K_Display', 'MemoryType_SSD', 'MemoryType_HDD', 'GpuBrand_Nvidia',
            'GpuBrand_Intel', 'GpuBrand_AMD', 'OpSys_Windows', 'OpSys_Linux', 'OpSys_No OS',
            'CpuSeries_i7', 'CpuSeries_i5', 'CpuSeries_i3', 'CpuSeries_A9-Series', 'CpuSeries_Dual',
            'CpuSeries_Quad'
        ]
        self.categorical_fields = [
            'TypeName_Gaming', 'TypeName_Notebook', 'TypeName_Ultrabook', 'TypeName_Workstation',
            'Company_Acer', 'Company_MSI', 'Company_Apple', 'Company_Toshiba', 'Company_Lenovo'
        ]

        # Add numeric inputs horizontally
        for field in self.numeric_fields:
            row_layout = QHBoxLayout()
            row_layout.addWidget(QLabel(f"{field}:"))
            self.inputs[field] = QLineEdit()
            row_layout.addWidget(self.inputs[field])
            self.input_layout.addLayout(row_layout)

        # Add boolean inputs horizontally
        for field in self.boolean_fields:
            row_layout = QHBoxLayout()
            row_layout.addWidget(QLabel(f"{field}:"))
            yes_button = QRadioButton("Yes")
            no_button = QRadioButton("No")
            no_button.setChecked(True)  # Default value
            row_layout.addWidget(yes_button)
            row_layout.addWidget(no_button)

            self.inputs[field] = {"Yes": yes_button, "No": no_button}
            self.input_layout.addLayout(row_layout)

        # Add categorical inputs horizontally (treated as boolean here for simplicity)
        for field in self.categorical_fields:
            row_layout = QHBoxLayout()
            row_layout.addWidget(QLabel(f"{field}:"))
            yes_button = QRadioButton("Yes")
            no_button = QRadioButton("No")
            no_button.setChecked(True)  # Default value
            row_layout.addWidget(yes_button)
            row_layout.addWidget(no_button)

            self.inputs[field] = {"Yes": yes_button, "No": no_button}
            self.input_layout.addLayout(row_layout)

        # Add input layout to main layout
        self.main_layout.addLayout(self.input_layout)

        # Predict button
        self.predict_button = QPushButton('Predict Price')
        self.predict_button.clicked.connect(self.predict_price)
        self.main_layout.addWidget(self.predict_button)

        # Result label
        self.result_label = QLabel('')
        self.main_layout.addWidget(self.result_label)

        # Set main layout
        self.setLayout(self.main_layout)

    def predict_price(self):
        try:
            # Collect inputs
            input_data = []
            for field, widget in self.inputs.items():
                if isinstance(widget, dict):  # Boolean field
                    input_data.append(1 if widget["Yes"].isChecked() else 0)
                else:  # Numeric field
                    value = float(widget.text())
                    input_data.append(value)

            input_array = np.array(input_data).reshape(1, -1)

            # Make prediction
            prediction = self.model.predict(input_array)[0]
            self.result_label.setText(f"Predicted Price: €{prediction:.2f}")
        except Exception as e:
            QMessageBox.critical(self, 'Error', f'Invalid input: {e}')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = LaptopPricePredictorApp()
    ex.show()
    sys.exit(app.exec_())
