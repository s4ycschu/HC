Einen speziellen Frequenzmix konnte ich leider nicht finden. Es sind unterschiedliche Frequenzen zu erkennen, aber um hier eine genauere Analyse durchführen zu können fehlt mir leider die Fachkompetenz.


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

    
Line #    Mem usage    Increment  Occurrences   Line Contents
=============================================================
    12     70.3 MiB     70.3 MiB           1   @profile
    13                                         def analyze_and_plot(filename, block_size=1024, hop_length=512):
    14     90.5 MiB     20.2 MiB           1       rate, data = read_wav(filename)
    15     90.5 MiB      0.0 MiB           1       if len(data.shape) > 1:
    16    130.9 MiB     40.4 MiB           1           data = data.mean(axis=1)  # Convert to mono by averaging channels
    17                                         
    18                                             # Normalize data
    19    171.3 MiB     40.4 MiB           1       data = data / np.max(np.abs(data))
    20                                         
    21                                             # Compute STFT using librosa
    22    394.7 MiB    223.4 MiB           1       stft_result = librosa.stft(data, n_fft=block_size, hop_length=hop_length)
    23    435.2 MiB     40.5 MiB           1       spectrogram = np.abs(stft_result)
    24                                         
    25                                             # Create a spectrogram plot
    26    459.8 MiB     24.6 MiB           1       plt.figure(figsize=(10, 6))
    27    931.0 MiB    471.2 MiB           1       librosa.display.specshow(librosa.amplitude_to_db(spectrogram, ref=np.max), sr=rate, hop_length=hop_length, x_axis='time', y_axis='log')
    28    931.0 MiB      0.0 MiB           1       plt.colorbar(format='%+2.0f dB')
    29    931.0 MiB      0.0 MiB           1       plt.title('Spectrogram')
    30    931.0 MiB      0.0 MiB           1       plt.xlabel('Time (s)')
    31    931.0 MiB      0.0 MiB           1       plt.ylabel('Frequency (Hz)')
    32   1467.8 MiB    536.8 MiB           1       plt.show()
    
This is the memory usage from my M1 Macbook Pro
Man kann einen deutlichen Unterschied bei dem Speicherverbrauch feststellen. Dies liegt offensichtlich an der geänderten Hardware, sowie an dem anderen Betriebssystem. 


Line #    Mem usage    Increment  Occurrences   Line Contents
=============================================================
    12     66.2 MiB     66.2 MiB           1   @profile
    13                                         def analyze_and_plot(filename, block_size=1024, hop_length=512):
    14     86.4 MiB     20.2 MiB           1       rate, data = read_wav(filename)        
    15     86.4 MiB      0.0 MiB           1       if len(data.shape) > 1:
    16    106.7 MiB     20.3 MiB           1           data = data.mean(axis=1)  # Convert to mono by averaging channels
    17
    18                                             # Normalize data
    19    106.7 MiB      0.0 MiB           1       data = data / np.max(np.abs(data))     
    20
    21                                             # Compute STFT using librosa
    22    309.3 MiB    202.6 MiB           1       stft_result = librosa.stft(data, n_fft=block_size, hop_length=hop_length)
    23    349.7 MiB     40.5 MiB           1       spectrogram = np.abs(stft_result)      
    24
    25                                             # Create a spectrogram plot
    26    361.9 MiB     12.1 MiB           1       plt.figure(figsize=(10, 6))
    27    483.7 MiB    121.8 MiB           1       librosa.display.specshow(librosa.amplitude_to_db(spectrogram, ref=np.max), sr=rate, hop_length=hop_length, x_axis='time', y_axis='log')
    28    483.8 MiB      0.1 MiB           1       plt.colorbar(format='%+2.0f dB')       
    29    483.8 MiB      0.0 MiB           1       plt.title('Spectrogram')
    30    483.8 MiB      0.0 MiB           1       plt.xlabel('Time (s)')
    31    483.8 MiB      0.0 MiB           1       plt.ylabel('Frequency (Hz)')
    32    646.7 MiB    162.9 MiB           1       plt.show()
Old Windows Laptop

Der Speicherverbauch auf meinen beiden Windows-Geräten ist änhlich. Den größten Unterschied scheint somit wohl das Betriebssystem zu machen. Ich würde gerne noch ein anderes Aplle-Gerät testen, habe aber leider nicht die Möglichkeit.
