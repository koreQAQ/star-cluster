import argparse
import os
from itertools import combinations

import pandas as pd

from src import config


def to_question_1(data_dict: dict) -> pd.DataFrame:
    time_list = ['c_' + str(i).zfill(4) for i in range(0, 1900, 100)]
    original_final_time_list = list(combinations(time_list, 2))
    question_1_data = []
    for pair_time in original_final_time_list:
        original = pair_time[0]
        final = pair_time[1]
        df = pd.merge(data_dict[original], data_dict[final], on='id', suffixes=('_original', '_final'))
        df['duration'] = int(final[-4:]) - int(original[-4:])
        question_1_data.append(df)
    print(f'question_1_data 共计: {len(question_1_data)}')
    return pd.concat(question_1_data, axis=0, ignore_index=True)


def to_question_2(path) -> pd.DataFrame:
    pass


def run(question: str, force: str):
    method_dict = {
        'q1': to_question_1,
        'q2': to_question_2
    }
    if question in method_dict.keys():
        data_dict = {}
        original_dir = config.INPUT_PATH + '/original'
        for file_name in os.listdir(original_dir):
            if file_name.endswith('csv'):
                file_path = os.path.join(original_dir, file_name)
                data_dict[os.path.splitext(file_name)[0]] = pd.read_csv(file_path)

        print(f'当前执行的是: {question} 方法')
        df = method_dict[question](data_dict)
        path = config.INPUT_PATH + f'/{question}.csv'
        # todo force 强制删除旧的文件用新的替换
        df.to_csv(path)
        print(f'重构数据完成，数据存放在{path}')


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    # model参数
    parser.add_argument('--question', type=str)
    parser.add_argument('--force', type=str)
    args = parser.parse_args()
    run(args.question, args.force)
