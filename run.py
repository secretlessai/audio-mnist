from os import listdir
import wave

# import pylab
import matplotlib.pyplot as plt
import numpy as np
import scipy
from numberMap import numberMap

wavDir = "./wavs/test/"

def graph_spectrogram(wav_file,counter):
    print(numberMap(wav_file))
    sound_info, frame_rate = get_wav_info(wavDir + wav_file)
    plt.figure(num=None, figsize=(19, 12))
    
    temp = plt.specgram(sound_info, Fs=frame_rate)
    print(temp)
    # return
    plt.axis('off')
    plt.savefig("./img/test/" + numberMap(wav_file) + "_" + str(counter) + '.spectrogram.png',  
                dpi=100,
                frameon='false',
                aspect='normal',
                bbox_inches='tight',
                pad_inches=0)


def get_wav_info(wav_file):
    wav = wave.open(wav_file, 'r')
    frames = wav.readframes(-1)
    sound_info = np.frombuffer(frames, 'int16')
    frame_rate = wav.getframerate()
    wav.close()
    return sound_info, frame_rate

files = listdir(wavDir)
print(files)

counter = 0

for item in files:
    # pass
    graph_spectrogram(item,counter)
    counter = counter + 1

    



