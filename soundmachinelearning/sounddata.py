import sys
import scipy.io.wavfile
import numpy as np
import matplotlib.pyplot as plt
 
 
#音声ファイル読み込み
wav_filename = "./sample.wav"
rate, data = scipy.io.wavfile.read(wav_filename)
 
##### 音声データをそのまま表示する #####
#縦軸（振幅）の配列を作成   #16bitの音声ファイルのデータを-1から1に正規化
#for i in data:
#    with open('./frequency.csv','a') as f:
#        frequency_str = str(i)
#        f.write(frequency_str + '\n')
#f.close()
#横軸（時間）の配列を作成　　#np.arange(初項, 等差数列の終点, 等差)
time = np.arange(0, data.shape[0]/rate, 1/rate)
#データプロット
plt.plot(time, data)
plt.savefig('fure.png')