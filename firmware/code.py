"""
Sound player main app. Plays "Ba-Dum-Tss" as separate sounds.
"""
import time
import board
import audiomixer
import audiocore
import audiobusio

# Set up audiomixer
audio = audiobusio.I2SOut(board.GP10, board.GP11, board.GP9)
mixer = audiomixer.Mixer(voice_count=3, sample_rate=16000, channel_count=1, bits_per_sample=16, samples_signed=True)
audio.play(mixer)

# Play sample sounds
mixer.voice[0].play(audiocore.WaveFile("sounds/ba.wav"))
time.sleep(0.05)
mixer.voice[1].play(audiocore.WaveFile("sounds/dum.wav"))
time.sleep(0.05)
mixer.voice[2].play(audiocore.WaveFile("sounds/tss.wav"))
time.sleep(1)

