import numpy as np


def run_simulation(new_iklan, new_diskon, model , baseline_pred):
    # Input baru dari user (Intervensi)
    intervention_input = np.array([[new_iklan, new_diskon]])

    # Prediksi hasil  intervensi
    prediction = model.predict(intervention_input)[0]

    # Menghitung Delta (Selisih)
    delta_y = prediction - baseline_pred

    return prediction, delta_y
