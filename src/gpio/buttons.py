from gpiozero import Button
from signal import pause
import time

import threading

RIGHT_PIN = 3
LEFT_PIN = 27
CENTER_PIN = 10
# BOTH = -1

# THRESH_DOUBLE = 0.5  # time between presses from two distinct buttons to be registered as simultaneous, in seconds
THRESH_NOISE = 0.1  # minimum time between two presses from the same button, in seconds

right_button = Button(RIGHT_PIN)
left_button = Button(LEFT_PIN)
center_button = Button(CENTER_PIN)

# start_time = time.time()
blocking = {RIGHT_PIN : False, LEFT_PIN : False, CENTER_PIN: False}
# last = {RIGHT_PIN : start_time, LEFT_PIN : start_time}

def ignore_noise(pin):
  if blocking[pin]:
    return True
  def revert():
    blocking[pin] = False
  blocking[pin] = True
  threading.Timer(THRESH_NOISE, revert).start()
  return False

# def ignore_release(pin):
#   return time.time() - last[pin] < THRESH_DOUBLE

def bind_buttons(window):

  def handle_release(pin):
    def handle():
      if ignore_noise(pin): # or ignore_release(pin):
        return
      if pin == RIGHT_PIN:
        window.get_child().move_right()
        print("RIGHT RELEASED")
      elif pin == LEFT_PIN:
        window.get_child().move_left()
        print("LEFT RELEASED")
      else:
        window.get_child().select()
        print("CENTER RELEASED")
    return handle
    
  right_button.when_released = handle_release(RIGHT_PIN)
  left_button.when_released = handle_release(LEFT_PIN)
  center_button.when_released = handle_release(CENTER_PIN)

  # def check_other(other_button):
  #   def handle():
  #     if other_button.is_pressed:
  #       now = time.time()
  #       last[RIGHT_PIN] = now
  #       last[LEFT_PIN] = now
  #       # window.get_child().select()
  #       print("BOTH PRESSED")
  #   return handle

  # handle simultaneous activation
  # right_button.when_pressed = check_other(left_button)
  # left_button.when_pressed = check_other(right_button)
  
def bind(view):
  def handle_release(pin):
    def handle():
      if ignore_noise(pin): # or ignore_release(pin):
        return
      if pin == RIGHT_PIN:
        view.move_right()
        print("RIGHT RELEASED")
      elif pin == LEFT_PIN:
        view.move_left()
        print("LEFT RELEASED")
      else:
        view.select()
        print("CENTER RELEASED")
    return handle

  right_button.when_released = handle_release(RIGHT_PIN)
  left_button.when_released = handle_release(LEFT_PIN)
  center_button.when_released = handle_release(CENTER_PIN)
  