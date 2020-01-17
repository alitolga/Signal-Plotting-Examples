import numpy as np
import matplotlib.pyplot as plt

pi = np.pi
j = complex(0,1)
Fs = 100 # Hertz
t = np.arange(0, 10, 1/Fs)

fig, axes = plt.subplots(nrows=3, ncols=3, figsize=(7, 7))

s1 = np.square(np.cos(2*pi*t))

axes[0,0].set_title("Signal: A")
axes[0,0].plot(t, s1)
axes[0,0].set_xlabel("Time")
axes[0,0].set_ylabel("Amplitude")

axes[1,0].set_title("Magnitude Spectrum")
axes[1,0].magnitude_spectrum(s1, Fs=Fs)

axes[2,0].set_title("Phase Spectrum ")
axes[2,0].phase_spectrum(s1, Fs=Fs)

s2 = np.exp(j*pi*t)

axes[0,1].set_title("Signal: B")
axes[0,1].plot(t, s2)
axes[0,1].set_xlabel("Time")
axes[0,1].set_ylabel("Amplitude")

axes[1,1].set_title("Magnitude Spectrum")
axes[1,1].magnitude_spectrum(s2, Fs=Fs)

axes[2,1].set_title("Phase Spectrum ")
axes[2,1].phase_spectrum(s2, Fs=Fs)

s3 =  1 + 5*np.cos(2257*pi*t + pi/4) + 2*np.cos(2440*pi*t + 3*pi/2)

axes[0,2].set_title("Signal: C")
axes[0,2].plot(t, s3)
axes[0,2].set_xlabel("Time")
axes[0,2].set_ylabel("Amplitude")

axes[1,2].set_title("Magnitude Spectrum")
axes[1,2].magnitude_spectrum(s3, Fs=Fs)

axes[2,2].set_title("Phase Spectrum ")
axes[2,2].phase_spectrum(s3, Fs=Fs)

fig.tight_layout()
plt.show()
