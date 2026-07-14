# electricity-bill-prediction-

### FastAPI Endpoint

```python
from fastapi import FastAPI
import numpy as np

app = FastAPI()

@app.post("/predict")
def predict_bill(consumption_kwh: float, rate: float):
    bill = consumption_kwh * rate

    return {
        "predicted_bill": round(bill, 2),
        "consumption": consumption_kwh
    }
