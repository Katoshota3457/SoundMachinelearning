import json
import scipy.io.wavfile
import time

def read_sound():
    #音声ファイル読み込み
    wav_filename = "./sample.wav"
    rate,data = scipy.io.wavfile.read(wav_filename)

    sound_data = []

    #0から絶対値を計算する
    for absolute_value in data:
        data = abs(absolute_value)
        data_int = int(data)
        sound_data.append(data_int)

    max_str = max(sound_data)
    max_value = str(max_str)
    print(max_value)

    myname = "神谷浩史"
    text = """,{}:{}"""

    #jsonを使ってMAX値と照合する
    #あとjsonファイルの音声データを撮り直し
    with open('./womanactor.json') as j:
        try:
            jsn = json.load(j)
            print(jsn[max_value])
            adddata = str(jsn[max_value])
            f = open('./data.txt','w')
            f.write(adddata + "\n")
            f.close()

            time.sleep(2)

            f = open('./data.txt','r')
            data = f.readline()
            if "name" in data:
                p_name = data[84:100]
                print(p_name)
            if "face" in data:
                p_face = data[9:38]
                print(p_face)
            if "charactorname" in data:
                p_charactorname = data[115:137]
            if "charactor" in data:
                p_charactor = data[53:77]
                print(p_charactor)
            else:
                print("nn")

            html = """
                <h3>あなたに似ている声の方はこの人です</h3>
                <div>
                    <h1>{}</h1>
                </div>
                <div>
                    <p><img src={} width=400/></p>
                    <h2>{}</h2>
                    <p><img src={} width=400/></p>
                </div>
                """.format(p_name,p_face,p_charactorname,p_charactor)

            html = "<!DOCTYPE html><html lang='ja'><head><meta charset='utf-8'/></head><body style=text-align:center;margin:0;padding:0;>" + html + "</body></html>"
            #ここのindex.htmlのファイルパスをFlaskのディレクトリパスに変える
            with open("index.html","w") as f:
                f.write(html)

        except:
            with open('./男性声優.json','a') as f:
                json.dump(text.format(max_value,myname),f,indent=4)
