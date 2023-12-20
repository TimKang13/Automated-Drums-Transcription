import matplotlib.pyplot as plt
from IPython.display import Audio
import librosa, librosa.display
import numpy as np

# load in the audio file, first 30 seconds
samples, sr = librosa.load("drum1.mp3")
print(sr)

S = np.abs(librosa.stft(samples, hop_length = 1024)) #Fourier Transform 
#librosa.display.specshow(librosa.amplitude_to_db(S, ref=np.max), y_axis='log', x_axis='time')
# get the timestamps of each hit or each beat


sgram_mag, _ = librosa.magphase(S)
mel_scale_sgram = librosa.feature.melspectrogram(S=sgram_mag, sr=sr)
print(mel_scale_sgram.shape)
difference = np.diff(mel_scale_sgram, axis=1) #difference in energy levels between back to back timeframes
print(mel_scale_sgram[50, 50])
print(difference[:,50])
librosa.display.specshow(librosa.amplitude_to_db(mel_scale_sgram, ref=np.min), sr=sr, y_axis= 'mel', x_axis='time')

onset_env = librosa.onset.onset_strength(y=samples, sr=sr)
onset_times = librosa.onset.onset_detect(y=samples, onset_envelope=onset_env,  sr=sr, units='time')
#look before and after, detect which frequencies were included 
# (db of each frequencies after onset) - (db of each frequencies before onset)
#    gives the addeed sounds...
#    make a 1D array of size (0~1000) Hz  that has each frequency added thing
#      make a function that takes in this (with parameters inputted by initial hitting of the drums)   and produces which drum has been hit 
#   combine with ML? 

print(onset_times)
print(samples.shape)
# Plot the waveform and onsets
plt.figure(figsize=(12, 8))

librosa.display.waveshow(y=samples, sr=sr, alpha=0.6)
# Plot onset times
plt.vlines(onset_times, ymin=min(samples), ymax=max(samples), color='r', linestyle='--', label='Onsets')

plt.title('Waveform with Onsets')
plt.xlabel('Time (s)')
plt.ylabel('Amplitude')
plt.legend()

plt.figure(figsize=(12,8))
plt.plot(mel_scale_sgram[50, :])

plt.show()




"""
# Plot the waveform
plt.subplot(2, 1, 1)
plt.title('Waveform')
librosa.display.waveshow(y=samples, sr=sr)


# Plot the onset envelope

# Mark detected onsets
plt.subplot(2, 1, 2)
plt.vlines(librosa.frames_to_time(onset_times), 0, 1, color='r', alpha=0.8, linestyle='--', label='Onsets')
plt.legend()

plt.show()

"""


    
# 1d array with element being short time fourier transforms (close to sample rate? enough to pick up timing of the hits) -> musescore
def transcribe():
    return 0

#differece array -> array of time
def detect_practice(bins, frames, cor_times, difference): #will need threshold parameters for actual functions
    threshold = 0.07   #have to change
    hits = []
    for timeframe in range(frames-1):
        diff = difference[50, timeframe]
        if threshold < diff:
            hits.append(cor_times[timeframe])
        
    print(hits)
    return hits

# stft, frequency profile for kick -> array of time 
def detect_kick():
    return 0


def detect_kick():
    return 0


def detect_kick():
    return 0


def detect_kick():
    return 0


def detect_kick():
    return 0


def detect_kick():
    return 0


def detect_kick():
    return 0


def detect_kick():
    return 0


def detect_kick():
    return 0


def detect_kick():
    return 0



rows, cols = difference.shape
cor_times = librosa.times_like(difference.shape[1], sr=sr, hop_length = 1024)
hits = detect_practice(rows, cols, cor_times, difference)
plt.figure(figsize=(12, 8))

librosa.display.waveshow(y=samples, sr=sr, alpha=0.6)
# Plot onset times
plt.vlines(hits, ymin=min(samples), ymax=max(samples), color='r', linestyle='--', label='Onsets')
plt.show()