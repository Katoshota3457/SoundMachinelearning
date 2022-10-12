import sys
import scipy.io.wavfile
import numpy as np
import matplotlib.pyplot as plt
 
 
#音声ファイル読み込み
wav_filename = "./cat.wav"
rate, data = scipy.io.wavfile.read(wav_filename)
 
##### 周波数成分を表示する #####
#縦軸：dataを高速フーリエ変換する（時間領域から周波数領域に変換する）
fft_data = np.abs(np.fft.fft(data))
#横軸：周波数の取得　　#np.fft.fftfreq(データ点数, サンプリング周期)
time = np.arange(0, data.shape[0]/rate, 1/rate)
#データプロット
plt.plot(time, fft_data)
plt.savefig('./cat_freq.png')