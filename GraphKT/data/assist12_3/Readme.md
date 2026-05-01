
## Environment
requirements.txt
```bash
pip install -r requirements.txt
```
## Test GPU

```bash
python - <<'PY'
import tensorflow as tf
print(tf.__version__)
print(tf.config.list_physical_devices('GPU'))
PY
```

## Run

```bash
python -u main.py --dataset assist12_3
```
