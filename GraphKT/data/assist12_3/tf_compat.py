# encoding: utf-8
import os
os.environ.setdefault("TF_CPP_MIN_LOG_LEVEL", "2")
import tensorflow.compat.v1 as tf
tf.disable_v2_behavior()
try:
    tf.logging.set_verbosity(tf.logging.ERROR)
except Exception:
    pass
