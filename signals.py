import numpy as np
import matplotlib.pyplot as plt
import scipy.io.wavfile

pi = np.pi
j = complex(0,1)
t = np.arange(0, 10, 1/5000)

f1 = 1100
f2 = 1099

s1 = np.cos(2*f1*pi*t)
s2 = np.cos(2*f2*pi*t)
s3 = s1 + s2

plt.title("Signal 1")
plt.xlabel("Time")
plt.ylabel("Amplitude")
plt.plot(t, s3)
plt.show()

scipy.io.wavfile.write(filename="signal1.wav", rate=5000, data=s3)

f1 = 1100
f2 = 1094

s1 = np.cos(2*f1*pi*t)
s2 = np.cos(2*f2*pi*t)
s3 = s1 + s2

plt.title("Signal 2")
plt.xlabel("Time")
plt.ylabel("Amplitude")
plt.plot(t, s3)
plt.show()

scipy.io.wavfile.write("signal2.wav", 5000, s3)
