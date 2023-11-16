from scipy.io import wavfile
import noisereduce as nr
import glob

for file in glob.glob("./asset/test/*.wav"):
    rate, data = wavfile.read(file)
    print(rate, data)

    reduced_noise = nr.reduce_noise(y=data, sr=rate, device='metal', stationary=False)
    wavfile.write("./result/" + file.split("/")[-1], rate, reduced_noise)


