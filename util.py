# These are empirically determined from my fx-9750GIII v. 360_2b
SCREEN_WIDTH = 130 # pixels
SCREEN_HEIGHT = 64 # pixels
CHAR_HEIGHT = 5    # pixels
CHAR_WIDTH = 4     # pixels

def sleep(sec):
  # unreliable, likely non-linear. may depend on battery, temperature, background tasks
  iterations = sec/3.75e-5
  for _ in range(iterations):
    pass
