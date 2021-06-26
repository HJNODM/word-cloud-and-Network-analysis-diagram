# -*- coding: utf-8 -*-
import jieba
import jieba.analyse as ana
import pandas as pd
import xlsxwriter


def nan_judge(df, path):
    df.dropna(inplace=True)
    print(df)
    print(df.isnull().sum())
    df.to_excel(path, index=False)


def jieba_process(df: pd.DataFrame):
    remove_text_tags = []
    normal_text_tags = []
    text_list = list(df['comment'])
    text_list = [str(it) for it in text_list]
    for i in range(len(text_list)):
        its = jieba.lcut(text_list[i])
        its = [it for it in its if it not in ['”', '？', '。', '，', '.', '！', '#', '—', '】', '【', '####', '##', '...']]
        normal_text_tags.append(its)
        it = ana.extract_tags(text_list[i].replace('#', ''), topK=10)
        remove_text_tags.append(it)
    print(normal_text_tags)
    for i in range(len(normal_text_tags)):
        strr = ''
        for j in range(len(normal_text_tags[i])):
            if not normal_text_tags[i][j].isascii():
                strr += normal_text_tags[i][j]
                if j != len(normal_text_tags) - 1:
                    strr += ' '
        normal_text_tags[i] = strr
    df['normal_tags'] = normal_text_tags
    for i in range(len(remove_text_tags)):
        strr = ''
        for j in range(len(remove_text_tags[i])):
            if not remove_text_tags[i][j].isascii():
                strr += remove_text_tags[i][j]
                if j != len(remove_text_tags) - 1:
                    strr += ' '
        remove_text_tags[i] = strr
    print(remove_text_tags)
    df['remove_text_tags'] = remove_text_tags
    print(df)
    df.to_excel("comments_2.xlsx", index=False, engine='xlsxwriter')


if __name__ == '__main__':
    df = pd.read_excel('comments_data.xlsx')
    jieba_process(df)

    df = pd.read_excel('comments_2.xlsx')
    nan_judge(df, 'comments_2.xlsx')
