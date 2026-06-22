import numpy as np

def run_simulation2(new_iklan, new_diskon, new_cabang, model, baseline_pred):
    # Input baru dari user (Intervensi)
    intervention_input = np.array([[new_iklan, new_diskon, new_cabang]])


    # Prediksi hasil intervensi
    prediction = model.predict(intervention_input)[0]

    # menghiitung delta (Selisih)
    delta_y = prediction - baseline_pred

    return prediction, delta_y
