import pickle

from find_hot_tables import find_hot_tables


def read_file_to_df(file_name="log_week_end.csv"):
    import pandas as pd
    df = pd.read_csv(file_name)
    df = df.sort_values(by='rn', ascending=True)
    return df


def save_to_pickle():
    df = read_file_to_df("log_week_end.csv")
    # print(df.columns)
    # print(df)
    with open('df.pickle', 'wb') as handle:
        pickle.dump(df, handle, protocol=pickle.HIGHEST_PROTOCOL)
    data = df.values.tolist()
    with open('data.pickle', 'wb') as handle:
        pickle.dump(data, handle, protocol=pickle.HIGHEST_PROTOCOL)
    hot_tables = find_hot_tables()
    with open('hot_tables.pickle', 'wb') as handle:
        pickle.dump(hot_tables, handle, protocol=pickle.HIGHEST_PROTOCOL)


def read_pickle():
    with open('df.pickle', 'rb') as handle:
        df = pickle.load(handle)
    with open('data.pickle', 'rb') as handle:
        data = pickle.load(handle)
    with open('hot_tables.pickle', 'rb') as handle:
        hot_tables = pickle.load(handle)

    return (df, data, hot_tables)


if __name__ == '__main__':
    # save_to_pickle()
    (df, data, hot_tables) = read_pickle()
    # print(hot_tables)
    import numpy as np
    import matplotlib.pyplot as plt

    x, y = [], []
    for tables in hot_tables[-10:-1]:
        x.append(tables[0])
        y.append(tables[1])
    fig, ax = plt.subplots()
    ax.bar(x, y)
    ax.set_facecolor('seashell')
    fig.set_facecolor('floralwhite')
    fig.set_figwidth(12)  # ширина Figure
    fig.set_figheight(6)  # высота Figure
    plt.show()
