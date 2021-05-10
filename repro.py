from ray import tune
from random import random


hparam_keys = frozenset({"loss1", "loss2", "really_long_key_that_has_many_words", "loss3", "inference_time (s)", "accuracy"})
def trainable(config):
    results = {key: random() for key in hparam_keys}
    tune.report(results)

tune.run(trainable, local_dir="./ray_results")


