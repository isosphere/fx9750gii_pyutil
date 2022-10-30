import casioplot as cp

# These are empirically determined from my fx-9750GIII v. 360_2b
SCREEN_WIDTH = 130 # pixels
SCREEN_HEIGHT = 64 # pixels
# MEDIUM is the default font size
MEDIUM_CHAR_HEIGHT = 5    # pixels
MEDIUM_CHAR_WIDTH = 4     # pixels
MIN_FRAME_TIME = 0.25 # let a frame last this long with sleep

def sleep(sec):
  # unreliable, likely non-linear. may depend on battery, temperature, background tasks
  iterations = sec/3.75e-5
  for _ in range(iterations):
    pass

def fill_screen():
  for x in range(SCREEN_WIDTH):
    for y in range(SCREEN_HEIGHT):
      cp.set_pixel(x, y)
  cp.show_screen()
