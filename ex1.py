import numpy as np
import scipy.io.wavfile as wav
import matplotlib.pyplot as plt
import librosa
import librosa.display
from memory_profiler import profile

def read_wav(filename):
    rate, data = wav.read(filename)
    return rate, data

@profile
def analyze_and_plot(filename, block_size=1024, hop_length=512):
    rate, data = read_wav(filename)
    if len(data.shape) > 1:
        data = data.mean(axis=1)  # Convert to mono by averaging channels

    # Normalize data
    data = data / np.max(np.abs(data))

    # Compute STFT using librosa
    stft_result = librosa.stft(data, n_fft=block_size, hop_length=hop_length)
    spectrogram = np.abs(stft_result)

    # Create a spectrogram plot
    plt.figure(figsize=(10, 6))
    librosa.display.specshow(librosa.amplitude_to_db(spectrogram, ref=np.max), sr=rate, hop_length=hop_length, x_axis='time', y_axis='log')
    plt.colorbar(format='%+2.0f dB')
    plt.title('Spectrogram')
    plt.xlabel('Time (s)')
    plt.ylabel('Frequency (Hz)')
    plt.show()

if __name__ == "__main__":
    filename = r'D:\\Master Trier\\HC\\nicht_zu_laut_abspielen.wav'  # Replace with your WAV file path
    analyze_and_plot(filename, block_size=1024, hop_length=512)
