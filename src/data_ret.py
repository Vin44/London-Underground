import pandas as pd

def get_cleaned_data(filename):
    station_pairs = []
    un_impeded_time = []
    AM_peak = []
    inter_peak = []
    
    df = pd.read_excel(filename, header = 1)
    df.head()

    avg_7_8 = df.iloc[:, 6:7].mean(axis=1).round(2)
    df.iloc[:, 5] = df.iloc[:, 5].fillna(avg_7_8).round(2)

    station_pairs = list(zip(df.iloc[:, 2], df.iloc[:, 3]))
    # print(station_pairs)

    un_impeded_time = df.iloc[:, 5].round(2).tolist()
    # print(un_impeded_time)

    AM_peak = df.iloc[:, 6].round(2).tolist()
    # print(AM_peak)

    inter_peak = df.iloc[:, 7].round(2).tolist()
    # print(inter_peak)

    un_impeded_time_cleaned = []
    for time in un_impeded_time:
        secs = round(time*60)
        un_impeded_time_cleaned.append(secs)
    # print(un_impeded_time_cleaned)

    AM_peak_cleaned = []
    for time in AM_peak:
        secs = round(time*60)
        AM_peak_cleaned.append(secs)
    # print(AM_peak_cleaned)

    inter_peak_cleaned = []
    for time in inter_peak:
        secs = round(time*60)
        inter_peak_cleaned.append(secs)
    # print(inter_peak_cleaned)

    return station_pairs, un_impeded_time_cleaned, AM_peak_cleaned, inter_peak_cleaned