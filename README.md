# fx9750gii_pyutil
(micro)Python utilities for running code on the fx-9750GIII graphing calculator by Casio.

Here are some limitations of using micro Python on the platform that I've noticed:
- no raw input; you can get `input()` but this supresses graphics and requires `EXE` to confirm, and does not support the directional pad
- no time functionality at all, I've attempted to improve this with a very poor `sleep()` function that just iterates enough times based on me using a stopwatch
