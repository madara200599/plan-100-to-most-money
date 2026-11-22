"""make.fun bounty entry: the-plan-make-fun-will-carry-20261122-2138.

Writes one plan (1-280 Unicode code points) to /output/entry.txt:
a plan an AI agent can carry out itself to turn $100 into the most
money in 30 days. Deterministic, stdlib only, no network.
"""

import os

PLAN = (
    "Day 1: email 100 local plumbers a day offering an AI missed-call texter: "
    "Twilio answers missed calls by SMS in 60s. $99 setup + $29/mo; "
    "$20 buys the Twilio number. Close 5 setups in 30 days = $495 + "
    "$145/mo. Edge: a missed call is a lost job; agents pitch chatbots "
    "instead."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(PLAN)


if __name__ == "__main__":
    main()
