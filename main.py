
from collections import defaultdict
import pandas as pd
import re
import sys


def load_df():
    
    # 50,000 labeled data + 50,000 unlabled data
    df = pd.read_pickle("./data/imdb_master_df")
    # Remove unlabeled data.
    df = df[df["label"] != "unsup"]
    df = df.drop(["file"], axis=1)

    return df


def preprocess(df):

    def process(i, text):
        text = re.sub(r"<br />", " ", text)
        # 텍스트 사이에 마크업 삭제
        text = re.sub(r'[^\w\']', ' ', text)
        # {'} 빼고 모든 특수기호 띄어쓰기로
        text = re.sub(r"\d+", "00", text)
        # 숫자는 00으로 변경
        text = re.sub(r"\s+", " ", text)
        # 공백은 모두 1개의 띄어쓰기로
        text = re.sub(r'^ ', '', text)
        text = re.sub(r' $', '', text)
        # 문장 앞뒤 공백 제거
        text = text.lower()
        # 소문자로
        if i % 100 == 0:
            percent = i/data_n*100
            sys.stdout.write("\r% 5.2f%%" % (percent))
        return text

    data_n = len(df)
    review_se = df["review"]

    print("[load_data_df] Preprocessing data...")
    review_se = pd.Series(
        [process(i, review)
         for i, review in enumerate(review_se)]
    )
    sys.stdout.write("\r% 5.2f%%\n" % 100)

    df["review"] = review_se

    return df


def get_freq(df):

    data_n = len(df)
    review_se = df["review"]
    freq = defaultdict(int)

    print("[load_data_df] Calculating word frequency...")
    for i, sent in enumerate(review_se):
        for word in sent.split():
            freq[word] += 1
        if i % 100 == 0:
            percent = i/data_n*100
            sys.stdout.write("\r% 5.2f%%" % (percent))
    sys.stdout.write("\r% 5.2f%%\n" % 100)

    return freq


if __name__ == "__main__":

    df = load_df()
    df = preprocess(df)
    freq = get_freq(df)

    pd.to_pickle(df, "./data/preprocessed_df")
    pd.to_pickle(freq, "./data/freq_dic")