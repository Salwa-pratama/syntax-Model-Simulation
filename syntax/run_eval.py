import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

np.random.seed(42)
n_samples = 300

x = pd.DataFrame({
    "usia_bangunan": np.random.randint(1, 30, n_samples),
    "anggota_keluarga": np.random.randint(2, 7, n_samples),
    "paparan_matahari": np.random.uniform(3, 8, n_samples),
    "index_isolasi_panas": np.random.uniform(0.3, 0.9, n_samples)
})

y = (
    100000 +  # biaya dasar (Rp)
    150000 * x["anggota_keluarga"] +
    5000 * x["usia_bangunan"] +
    -20000 * x["paparan_matahari"] +
    -80000 * x["index_isolasi_panas"] +
    np.random.normal(0, 20000, n_samples)
)

x_train, x_test, y_train,y_test = train_test_split(x, y, test_size=0.2, random_state=42)

model = RandomForestRegressor(n_estimators=100, random_state=42)
model.fit(x_train, y_train)
y_pred = model.predict(x_test)
mae = mean_absolute_error(y_test, y_pred)
mse = mean_squared_error(y_test, y_pred)
rmse = np.sqrt(mse)
r2 = r2_score(y_test, y_pred)

print(f"MAE : {mae}")
print(f"RMSE: {rmse}")
print(f"R2  : {r2}")
