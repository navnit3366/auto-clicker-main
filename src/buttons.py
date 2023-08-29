from src.interval import getInterval


class Button():
    def __init__(self, clicker, textVariable, entries):
        self.text = textVariable
        self.clicker = clicker
        self.entries = entries
        self.active = False

    def startButton(self):
        if self.active:
            self.active = False
            self.text.set('Start (F6)')
            self.clicker.deactivate()
        else:
            self.active = True
            self.text.set('Stop (F6)')
            seconds = getInterval(self.entries)
            self.clicker.interval = seconds
            self.clicker.activate()
