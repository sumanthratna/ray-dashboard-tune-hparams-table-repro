# ray-dashboard-tune-hparams-table-repro
https://github.com/ray-project/ray/issues/8667

## reproducing

to install dependencies:
1. `python3 -m pip install -r requirements.txt` (deps were installed as `"ray[tune]" pandas tensorboard tabulate`)

to create mock data:
1. `rm -rf ray_results`
2. `python3 repro.py`

to view the dashboard:

1. `ray start --head` and open the Tune tab of `localhost:8265`

