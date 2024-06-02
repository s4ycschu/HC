Line #    Mem usage    Increment  Occurrences   Line Contents
=============================================================
    12     67.4 MiB     67.4 MiB           1   @profile
    13                                         def analyze_and_plot(filename, block_size=1024, hop_length=512):
    14     87.7 MiB     20.2 MiB           1       rate, data = read_wav(filename)
    15     87.7 MiB      0.0 MiB           1       if len(data.shape) > 1:
    16    107.9 MiB     20.3 MiB           1           data = data.mean(axis=1)  # Convert to mono by averaging channels
    17
    18                                             # Normalize data
    19    107.9 MiB      0.0 MiB           1       data = data / np.max(np.abs(data))
    20
    21                                             # Compute STFT using librosa
    22    275.9 MiB    168.0 MiB           1       stft_result = librosa.stft(data, n_fft=block_size, hop_length=hop_length)
    23    316.4 MiB     40.5 MiB           1       spectrogram = np.abs(stft_result)
    24
    25                                             # Create a spectrogram plot
    26    329.2 MiB     12.8 MiB           1       plt.figure(figsize=(10, 6))
    27    451.7 MiB    122.5 MiB           1       librosa.display.specshow(librosa.amplitude_to_db(spectrogram, ref=np.max), sr=rate, hop_length=hop_length, x_axis='time', y_axis='log')
    28    452.1 MiB      0.3 MiB           1       plt.colorbar(format='%+2.0f dB')
    29    452.1 MiB      0.0 MiB           1       plt.title('Spectrogram')
    30    452.1 MiB      0.0 MiB           1       plt.xlabel('Time (s)')
    31    452.1 MiB      0.0 MiB           1       plt.ylabel('Frequency (Hz)')
    32    616.6 MiB    164.5 MiB           1       plt.show()

    Memory usage from my Desktop PC Hardware
