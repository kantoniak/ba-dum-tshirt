"""
Sound player main app. Plays "Ba-Dum-Tss" as separate sounds.
"""
import board
from adafruit_debouncer import Button
from adafruit_mpr121 import MPR121, MPR121_Channel
from audiobusio import I2SOut
from audiocore import WaveFile
from audiomixer import Mixer
from busio import I2C


# Set up buttons
i2c = I2C(board.GP5, board.GP4)
touchpad = MPR121(i2c)
buttons = []

for pad_num in [10, 8, 6]:
  # Lower sensitivity of the touch buttons
  channel = MPR121_Channel(touchpad, pad_num)
  channel.threshold = 7
  channel.release_threshold = 3

for pad in touchpad:
  buttons.append(Button(pad, value_when_pressed=True))


# Set up audio
audio = I2SOut(board.GP10, board.GP11, board.GP9)
mixer = Mixer(voice_count=3, sample_rate=16000, channel_count=1, bits_per_sample=16, samples_signed=True)
audio.play(mixer)

sound_ba = WaveFile("sounds/ba.wav")
sound_dum = WaveFile("sounds/dum.wav")
sound_tss = WaveFile("sounds/tss.wav")

def play_sound_on_voice(voice: int, sound: WaveFile):
  if mixer.voice[voice].playing:
    return
  mixer.voice[voice].play(sound)


# Wait for pad presses
while True:
  for i in range(12):
    buttons[i].update()
    if buttons[i].pressed:
      print(f"Pad #{i} touched!")
      if i == 10:
        play_sound_on_voice(0, sound_ba)
      if i == 8:
        play_sound_on_voice(1, sound_dum)
      if i == 6:
        play_sound_on_voice(2, sound_tss)