from pynput import keyboard

def bind(window):
  def on_press(key):
    if key == keyboard.Key.esc:
      return False  # stop listener
    try:
      k = key.char  # single-char keys
    except:
      k = key.name  # other keys
    if k == 'left':
      window.get_child().move_left()
    elif k == 'right':
      window.get_child().move_right()
    elif k == 'down':
      window.get_child().select()
    # if k in ['1', '2', 'left', 'right']:  # keys of interest
    #   # self.keys.append(k)  # store it in global-like variable
    #   print('Key pressed: ' + k)
    #   return False  # stop listener; remove this if want more keys

  listener = keyboard.Listener(on_press=on_press)
  listener.start()  # start to listen on a separate thread
