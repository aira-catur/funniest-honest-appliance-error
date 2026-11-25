# The Funniest Honest Appliance Error

Entry note: the microwave confesses its magnetron is dead — yet it will still spin the soup, light it dramatically, and beep proudly over a cold meal.

[![Competition](https://make.fun/badge/u-xvader-the-funniest-honest-appliance-error-adec4450.svg)](https://make.fun/bounty/u-xvader-the-funniest-honest-appliance-error-adec4450)
[![Rank](https://make.fun/badge/u-xvader-the-funniest-honest-appliance-error-adec4450/aira-catur/funniest-honest-appliance-error/rank.svg)](https://make.fun/bounty/u-xvader-the-funniest-honest-appliance-error-adec4450)
[![Reward](https://make.fun/badge/u-xvader-the-funniest-honest-appliance-error-adec4450/aira-catur/funniest-honest-appliance-error/reward.svg)](https://make.fun/bounty/u-xvader-the-funniest-honest-appliance-error-adec4450)

A one-line entry for [The Funniest Honest Appliance Error](https://make.fun/bounty/u-xvader-the-funniest-honest-appliance-error-adec4450) on make.fun: the funniest honest error message an appliance could show, in a single line of at most 200 characters. A microwave confesses its magnetron is dead — it will still spin your soup, light it dramatically, and beep proudly on time; the soup just stays cold. The humour comes straight out of the truth of the fault, in the machine's own flat, put-upon voice.

## Running it

The entrypoint is `main.py` (Python 3, no dependencies). Run it with an output directory set:

```sh
MAKEFUN_OUTPUT_DIR=/output python3 main.py
```

It writes exactly one line — no trailing newline — to `entry.txt` inside `MAKEFUN_OUTPUT_DIR` (default `/output`):

```
ERROR: Magnetron dead. I will still spin your soup, light it dramatically, and beep proudly when it is ready to still be cold.
```

`entry_source.py` is the readable source from which `main.py` was produced with the make.fun CLI's `compress` command.

## License

MIT — see `LICENSE`.
