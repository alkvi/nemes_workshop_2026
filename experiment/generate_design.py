import csv
import random

SEED = 42
random.seed(SEED)

BLOCK_DURATION = 10.0
REST_RANGE = (10.0, 20.0)
N_REPEATS = {"left": 10, "right": 10, "control": 5}

MARKERS = {"rest": 0, "control": 1, "left": 2, "right": 3}

blocks = [cond for cond, n in N_REPEATS.items() for _ in range(n)]
random.shuffle(blocks)

rows = []
trial_counter = 0

for block_idx, condition in enumerate(blocks):
    rows.append(
        {
            "trial": trial_counter,
            "condition": condition,
            "duration": BLOCK_DURATION,
            "marker": MARKERS[condition],
        }
    )
    trial_counter += 1

    if block_idx < len(blocks) - 1:
        rest_dur = round(random.uniform(*REST_RANGE), 3)
        rows.append(
            {
                "trial": trial_counter,
                "condition": "rest",
                "duration": rest_dur,
                "marker": MARKERS["rest"],
            }
        )
        trial_counter += 1

out_path = "experiment_design.csv"

with open(out_path, "w", newline="") as f:
    writer = csv.DictWriter(f, fieldnames=["trial", "condition", "duration", "marker"])
    writer.writeheader()
    writer.writerows(rows)

print(f"CSV saved to {out_path}")
print(f"Total rows: {len(rows)}")
print(f"Total condition blocks: {len(blocks)}")
