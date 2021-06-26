# -*- coding: utf-8 -*-
import os
import pandas as pd
import wordcloud
from imageio import imread
import matplotlib.pyplot as plt
# 解决matplotlib在windows电脑上中文乱码问题
plt.rcParams['font.sans-serif'] = 'SimHei.'
# 解决matplotlib负号无法显示的问题
plt.rcParams['axes.unicode_minus'] = False
# 让图形变成矢量形式，显示更清晰
# %config InlineBackend.figure_format='svg'

def summary_data(df):
    ans = list(df['remove_text_tags'])
    text = ans[0]
    for i in range(1, len(ans)):
        text += ans[i]
    # print(text)
    return  text

if __name__ == '__main__':
    df = pd.read_excel('comments_2.xlsx')
    text = summary_data(df)
    print(len(text))
    image_name = os.path.join("1.jpg")  # 背景图片路径
    coloring = imread(image_name)  # 读取背景图片
    font_name = os.path.join("msyh.ttc")  # 使用的是微软雅黑字体
    # print(font_name)
    wc = wordcloud.WordCloud(mask=coloring, font_path=font_name).generate(text)
    # plt.figure(figsize=(10, 10))
    # plt.imshow(wc)
    # plt.axis("off")
    # plt.show()
