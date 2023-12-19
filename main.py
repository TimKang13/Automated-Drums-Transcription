import matplotlib.pyplot as plt
from IPython.display import Audio
import librosa, librosa.display

# load in the audio file, first 30 seconds
samples, sr = librosa.load(AUDIO_FILE_PATH)
# get the timestamps of each hit or each beat
onset_times = librosa.onset.onset_detect(y=samples, sr=sr, units='time')
beat_times = librosa.beat.beat_track(y=samples, sr=sr, 
 start_bpm=bpm, units='time')[1]
# get the click tracks
clicks = librosa.clicks(onset_times, sr=sr, length=len(samples))
display(Audio((samples + clicks), rate=sr))
clicks = librosa.clicks(beat_times, sr=sr, length=len(samples))
display(Audio((samples + clicks), rate=sr))
fig, ax = plt.subplots(nrows=3, sharex=True, figsize=(10,5))
librosa.display.waveplot(samples, sr=sr, offset=10, ax=ax[0])
onset_times = librosa.onset.onset_detect(y=samples, sr=sr, units='time')
ax[1].vlines(onset_times+10,-1, 1)
beat_times = librosa.beat.beat_track(y=samples, sr=sr, 
 start_bpm=bpm, units='time')[1]
ax[2].vlines(beat_times+10,-1, 1)