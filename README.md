# fx9750gii_pyutil
(micro)Python 1.9.4 utilities and notes for running code on the fx-9750GIII graphing calculator by Casio.
Developed on OS 03.60.3200

Here are some limitations of using micro Python on the platform that I've noticed:
- no raw input; you can get `input()` but this supresses graphics and requires `EXE` to confirm, and does not support the directional pad
- no time functionality at all, I've attempted to improve this with a very poor `sleep()` function that just iterates enough times based on me using a stopwatch
- you can draw a pixel, but you can't undraw it; you have to clear the screen.
- screen changes are only visible after running `casioplot.show_screen()`
