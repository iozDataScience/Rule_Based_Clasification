import numpy as np
import pandas as pd

df = pd.read_csv("dersler/hafta_2/persona.csv")

bins_ = [0, 18, 24, 35, 50, 70]
labels_ = ["0_18", "19_24", "25_35", "36_50", "51_70"]

df["AGE_CAT"] = pd.cut(df["AGE"], bins=bins_, labels=labels_)
cols = [col for col in df.columns if col not in ["AGE", "PRICE"]]
df["customers_level_based"] = ["_".join(row).upper() for row in df[cols].values]
df = df.groupby("customers_level_based").mean("PRICE").astype(int).reset_index()
df["SEGMENT"] = pd.cut(df["PRICE"], 4, labels=["D", "C", "B", "A"])
df.drop("AGE", axis=1, inplace=True)

def predict_price(dataframe, col, new_age, new_source , new_country , new_sex ):
    if    0 <= int(new_age) <= 18:
        new_age = "0_18"
    elif 19 <= int(new_age) <= 24:
        new_age = "19_24"
    elif 25 <= int(new_age) <= 35:
        new_age = "25_35"
    elif 36 <= int(new_age) <= 50:
        new_age = "36_50"
    else:
        new_age = "51_70"
    a = new_source.upper() + "_" + new_sex.upper() + "_" + new_country.upper() + "_" + new_age
    b = dataframe[dataframe[col] == a]["PRICE"].iloc[0]
    c = dataframe[dataframe[col] == a]["SEGMENT"].iloc[0]

    print("Girilen Değerlere Göre Tahmini Gelir: " + f"{b}" + " ve Segment: " + f"{c}")

new_age = input("Bir yaş değeri giriniz: ")
new_source = input("Bir Kaynak Seçiniz -> ANDROID/IOS: ").upper()
new_country = input("Bir Ülke Seçiniz -> USA/BRA/DEU/TUR/FRA/CAN: ").upper()
new_sex = input("Cinsiyet Seçiniz -> Male/Female: ").upper()
predict_price(df, "customers_level_based", new_age, new_source, new_country, new_sex)

