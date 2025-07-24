import pyaudio
import struct
import numpy as np
import matplotlib.pyplot as plt
import time
from tkinter import TclError

CHUNK = 1024 * 2
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 44100

fig, ax = plt.subplots(1, figsize=(15, 7))

p = pyaudio.PyAudio()

info = p.get_host_api_info_by_index(0)
numdevices = info.get('deviceCount')
for i in range(0, numdevices):
    if (p.get_device_info_by_host_api_device_index(0, i).get('maxInputChannels')) > 0:
        print("Input Device id", i, "-", p.get_device_info_by_host_api_device_index(0, i).get('name'))

audio_input = input("\nSelect input by Device id: ")

stream = p.open(
    input_device_index=int(audio_input),
    format=FORMAT,
    channels=CHANNELS,
    rate=RATE,
    input=True,
    output=False,
    frames_per_buffer=CHUNK
)

x = np.arange(0, CHUNK)
line, = ax.plot(x, np.random.rand(CHUNK), '-', lw=2)

ax.set_title('AUDIO WAVEFORM')
ax.set_xlabel('samples')
ax.set_ylabel('volume')
ax.set_ylim(-32768, 32767)
ax.set_xlim(0, CHUNK)
plt.setp(ax, xticks=[0, CHUNK // 2, CHUNK], yticks=[-32768, 0, 32767])
plt.show(block=False)

print('stream started')
frame_count = 0
start_time = time.time()

while True:
    data = stream.read(CHUNK, exception_on_overflow=False)
    data_int = struct.unpack(str(CHUNK) + 'h', data)
    data_np = np.array(data_int, dtype='h')

    line.set_ydata(data_np)

    try:
        fig.canvas.draw()
        fig.canvas.flush_events()
        frame_count += 1
    except TclError:
        frame_rate = frame_count / (time.time() - start_time)
        print('stream stopped')
        print('average frame rate = {:.0f} FPS'.format(frame_rate))
        break
