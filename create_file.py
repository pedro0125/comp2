import pandas as pd

# Input CSV path
input_path = "input.csv"

# Output CSV path
output_path = "clientes_prediction_1.csv"

# Read input CSV
df = pd.read_csv(input_path)

# Filter only prediction == 1
filtered = df[df["Predicted"] == 1][["numero_de_cliente"]]

# Write result (without index, no header)
filtered.to_csv(output_path, index=False, header=False)

print("Archivo generado:", output_path)