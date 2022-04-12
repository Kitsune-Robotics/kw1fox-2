from PIL import Image

from pysstv.color import Robot36

from tools.pyaudio import PyAudioSSTV


class kw1fox2:
    def __init__(self, sim=False):
        # Lets us automate more testing locally by having a program-wide sim mode.
        self.sim = sim

        img = Image.open("../../Resources/KW1FOX-1_320x240.png")
        self.sstv = Robot36(img, 44100, 16)
        self.sstv.vox_enabled = True

        self.sstv.write_wav("Mysstv.wav")

    def run(self):
        PyAudioSSTV(self.sstv).execute()

    def take_snapshot(self):
        if not self.sim:
            raise NotImplementedError


if __name__ == "__main__":
    station = kw1fox2()
    station.run()
