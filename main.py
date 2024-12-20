from joblib import load
import numpy as np

# Define the list of all 33 features
FEATURES = [
    'Ram_In_GB', 'Weight', 'ScreenResolutionWidth', 'ScreenResolutionHeight', 'Cpu_ClockSpeed', 'Total_Memory_MB',
    'Touchscreen', 'IPS_Panel', '4K_Display', 'MemoryType_SSD', 'MemoryType_HDD', 'MemoryType_Flash_Storage', 'GpuBrand_Nvidia',
    'GpuBrand_Intel', 'GpuBrand_AMD', 'OpSys_Windows', 'OpSys_Linux', 'OpSys_No OS',
    'CpuSeries_i7', 'CpuSeries_i5', 'CpuSeries_i3', 'CpuSeries_A9-Series', 'CpuSeries_Dual',
    'CpuSeries_Quad', 'TypeName_Gaming', 'TypeName_Notebook', 'TypeName_Ultrabook',
    'TypeName_Workstation', 'Company_Acer', 'Company_MSI', 'Company_Apple',
    'Company_Toshiba', 'Company_Lenovo'
]

def get_user_input():
    print("\n--- Laptop Price Predictor ---\n")

    # Inputs from the user
    user_inputs = {}

    for feature in FEATURES:
        if feature in ['Touchscreen', 'IPS_Panel', '4K_Display', 'MemoryType_SSD', 'MemoryType_HDD', 'MemoryType_Flash_Storage', 'GpuBrand_Nvidia',
                       'GpuBrand_Intel', 'GpuBrand_AMD', 'OpSys_Windows', 'OpSys_Linux', 'OpSys_No OS',
                       'CpuSeries_i7', 'CpuSeries_i5', 'CpuSeries_i3', 'CpuSeries_A9-Series', 'CpuSeries_Dual',
                       'CpuSeries_Quad', 'TypeName_Gaming', 'TypeName_Notebook', 'TypeName_Ultrabook',
                       'TypeName_Workstation', 'Company_Acer', 'Company_MSI', 'Company_Apple', 'Company_Toshiba',
                       'Company_Lenovo']:
            # Boolean inputs
            value = input(f"Does it have {feature}? (yes/no): ").strip().lower()
            user_inputs[feature] = 1 if value == "yes" else 0
        else:
            # Numeric inputs
            value = float(input(f"Enter {feature} (numeric): "))
            user_inputs[feature] = value

    # Ensure all features are included in the correct order
    input_data = [user_inputs.get(feature, 0) for feature in FEATURES]  # Fill missing features with 0
    return np.array(input_data).reshape(1, -1)

def main():
    model = load('random_forest_model.joblib')  # Load the trained model

    # Get user inputs
    user_input = get_user_input()

    # Predict price
    predicted_price = model.predict(user_input)[0]

    print(f"\nPredicted Laptop Price: €{predicted_price:.2f}\n")


if __name__ == "__main__":
    main()
