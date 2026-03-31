
---

# 🧠 ثانيًا: MelFilterBank.py

هذا ملف بسيط وعملي لتوليد mel-spectrogram 👇

```python
import numpy as np
import scipy.signal as signal


def hz_to_mel(hz):
    return 2595 * np.log10(1 + hz / 700)


def mel_to_hz(mel):
    return 700 * (10**(mel / 2595) - 1)


def mel_filterbank(sr, n_fft, n_mels=80, fmin=0, fmax=None):
    if fmax is None:
        fmax = sr / 2

    # Convert Hz to Mel
    mel_min = hz_to_mel(fmin)
    mel_max = hz_to_mel(fmax)

    mel_points = np.linspace(mel_min, mel_max, n_mels + 2)
    hz_points = mel_to_hz(mel_points)

    bins = np.floor((n_fft + 1) * hz_points / sr).astype(int)

    filterbank = np.zeros((n_mels, int(n_fft // 2 + 1)))

    for i in range(1, n_mels + 1):
        left = bins[i - 1]
        center = bins[i]
        right = bins[i + 1]

        for j in range(left, center):
            filterbank[i - 1, j] = (j - left) / (center - left)

        for j in range(center, right):
            filterbank[i - 1, j] = (right - j) / (right - center)

    return filterbank


def compute_mel_spectrogram(signal_input, sr=16000, n_fft=512, hop_length=160, n_mels=80):
    # STFT
    _, _, Zxx = signal.stft(signal_input, fs=sr, nperseg=n_fft, noverlap=n_fft - hop_length)

    spectrogram = np.abs(Zxx) ** 2

    # Mel filter
    mel_fb = mel_filterbank(sr, n_fft, n_mels)

    mel_spec = np.dot(mel_fb, spectrogram)

    # Log scale
    mel_spec = np.log(mel_spec + 1e-9)

    return mel_spec