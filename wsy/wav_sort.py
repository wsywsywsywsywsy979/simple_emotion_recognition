"""
target：用于将数据集中的数据根据配置文件进行分类
    针对emodb:class_labels: ["angry", "boredom", "disgust", "fear", "happy", "neutral", "sad"]
    W：anger
    L:boredom
    E:disgust
    A:anxiety/fear
    F:happiness
    T:sadness
    N:neutral version
author:wsy
"""
wav_emo={'W':'angry','L':'boredom','E':"disgust",'A':"fear",'F':"happy",'T':"sad",'N':"neutral"}
import os
import shutil
file_path="/home/wangshiyao/wangshiyao_space/exp3/Speech-Emotion-Recognition-master/datasets/EMO-DB/wav"
new_file_path="/home/wangshiyao/wangshiyao_space/exp3/Speech-Emotion-Recognition-master/datasets/EMO-DB/sorted" # 变成绝对路径以及适应\\再试试
for root, dirs, files in os.walk(file_path): # 参考 files.py下的move函数
    for item in files:
        if item.endswith('.wav'):
            emotion_name=wav_emo[item[5]]
            old_path = os.path.join(file_path, item)
            # new_path = os.path.join(new_file_path, emotion_name, item)
            new_path = os.path.join(new_file_path, emotion_name,item) # wsy fix 
            try:
                print("old_path：",old_path)
                print("new_path：",new_path)
                shutil.move(old_path, new_path)
                # shutil.move(new_path, old_path)
                print("Move ", old_path, " to ", new_path)
            except Exception as E:
                print(E)
                continue