import pandas as pd
import re
import numpy as np


def extract_currency_value(x):
    price = float(re.findall('(\\d+[\\.\\d]*)', x)[0])
    if 'бум' in x and 'сая' not in x:
        return price * 1e3
    else:
        return price 
def extract_numeric_area_values(x):
    x = float(re.findall('(\\d+[\\.\\d]*)', x)[0])
    return x

def get_district(x):
    try:
        x = re.findall('(Баянгол|Баянзүрх|Сүхбаатар|Сонгинохайрхан|Хан-Уул|Чингэлтэй|Налайх)', x)[0]
    except:
        pass
    return x

def get_location(x):
    try:
        x = re.findall(r"(?:Баянгол|Баянзүрх|Сүхбаатар|Сонгинохайрхан|Хан-Уул|Чингэлтэй|Налайх)[\s,]+(.*)", x, re.IGNORECASE)
        if len(x) == 0: # this because no sublocation after district
            x = ""
        else:
            x = x[0]        
    except:
        pass


    # because district name is also in the location, twice
    words_to_remove = ["Баянгол, ","Баянзүрх, ","Сүхбаатар, ","Сонгинохайрхан, ","Хан-Уул, ","Чингэлтэй, ","Налайх, "]
    pattern = r"\b(?:{})\b".format("|".join(map(re.escape, words_to_remove)))
    try:
        x = re.sub(pattern, "", x)
    except:
        pass
    return x

        # re.findall('(?<=Баянгол|Баянзүрх|Сүхбаатар|Сонгинохайрхан|Хан-Уул|Чингэлтэй|Налайх)[\s,]+([\w\s,]+)', x)[0] [\w\s,-]+

def get_khoroo(x):
    try:
        x = re.findall(r"(?<=Хороо)\s+(\d*)", x)
        if len(x) == 0: # this because no sublocation after district
            x = ""
        else:
            x = x[0]        
    except:
        pass
    return x

def filter_dataframe_by_column_range(df, column, min_value, max_value):
    df = df[(df[column] >= min_value) & (df[column] <= max_value)]
    return df

df = pd.read_csv("result/df_zarnaoron-.csv")
df = df.iloc[:,1:]

data_list = []
for index, row in df.iterrows():
    print(row)
    for col, value in row.items():
        try:
            value = eval(value)
        except:
            break
        data_list.append(value)
    
df = pd.DataFrame(data_list)
# new_df.to_csv('tmp.csv',encoding="utf-8-sig")


name_cols = {"Title": "Зарын гарчиг",
             "Талбай:": "М2 0",
             "Барилгын давхар:":"Барилгын давхар",
             "Хэдэн давхарт:":"Байрны давхар",
             "room":"Өрөө",
             "Цонхны тоо:":"Цонхны тоо",
             "loc": "Дүүрэгт байршил",
             "Ашиглалтанд орсон он:":"Ашиглалтад орсон огноо",
             "Price": "Нийт үнэ 0",
             "Лизингээр авах боломж:":"Лизингээр авах боломж",
             'Байршил:': 'Байршил 2',
             'Date': "Огноо",
             'Time': "Цаг",
             'id': "Зарын дугаар",
             'phone': "Утасны дугаар",
             "message":"Тайлбар"}

df = df.rename(columns=name_cols)

df[["Хотхоны ID","Хотхоны нэр","Дэд байршил","Lat","Long"]] = None


## TODO
# merge separate data
# remove NA
# year, month, day columns + joint column of all
# Group by size
# Price matrix with district and size group


## LOCATION
df["Дүүрэг"] = df["Дүүрэгт байршил"].apply(get_district)
df["Байршил"] = df["Дүүрэгт байршил"].apply(get_location)
df["Хороо"] = df["Дүүрэгт байршил"].apply(get_khoroo)


## NUMERICAL VALUES
df["Нийт үнэ"] = df["Нийт үнэ 0"].apply(extract_currency_value)
df["М2"] = df["М2 0"].apply(extract_numeric_area_values)
# df["Өрөө"] = df["Өрөө"].apply(extract_numeric_area_values)
# df = filter_dataframe_by_column_range(df, "М2", 10, 1000)

## PRICE
# price_m2
df['М2 үнэ']   = df['Нийт үнэ'].astype(float)
mask = df['Нийт үнэ'].astype(float) >= 5 & ~df['М2'].astype(float).isnull() # no price_m2 higher than or equal to 12 mio at the momemt  
df.loc[mask, 'М2 үнэ'] = df.loc[mask, 'Нийт үнэ'].astype(float) / df.loc[mask, 'М2'].astype(float)

# total price
mask = df['Нийт үнэ'] == df['М2 үнэ']
df.loc[mask, 'Нийт үнэ'] = df.loc[mask, 'М2 үнэ'] * df.loc[mask, 'М2']


df.to_csv("house.csv",encoding="utf-8-sig")


df['Дд'] = [i+1 for i in range(len(df))]

# save prod columns
df_all = df[["Дд","Зарын дугаар","Огноо","Цаг","Зарын гарчиг","Хотхоны ID","Хотхоны нэр","М2","М2 0","Барилгын давхар","Байрны давхар","Өрөө","Цонхны тоо","Дүүрэгт байршил","Дүүрэг","Байршил","Байршил 2","Дэд байршил","Хороо","Lat","Long","Ашиглалтад орсон огноо","М2 үнэ","Нийт үнэ","Нийт үнэ 0","Лизингээр авах боломж","Утасны дугаар","Тайлбар"]]						
df_final = df[["Дд","Зарын дугаар","Огноо","Цаг","Зарын гарчиг","Хотхоны ID","Хотхоны нэр","М2","Барилгын давхар","Байрны давхар","Өрөө","Цонхны тоо","Дүүрэг","Байршил","Дэд байршил","Хороо","Lat","Long","Ашиглалтад орсон огноо","М2 үнэ","Нийт үнэ","Лизингээр авах боломж","Утасны дугаар","Тайлбар"]]						
df_all.to_csv("tmp_pro_all.csv",encoding="utf-8-sig",index=False)
df_final.to_csv("tmp_final.csv",encoding="utf-8-sig",index=False)



# duplication handling
# do not delete, but count how many

df = pd.read_csv("tmp_final_hand.csv")

df_check = df[["М2", "Өрөө","Байрны давхар","Цонхны тоо","Дүүрэг"]]
df_check["М2"] = df_check["М2"].apply(np.round)
# df_check["М2 үнэ"] = df_check["М2 үнэ"].apply(round_to_nearest_half)
df_check['check_col'] = df_check["М2"].astype(str) + df_check["Өрөө"].astype(str) + \
                        df_check["Дүүрэг"].astype(str) + \
                        df_check["Байрны давхар"].astype(str) + df_check["Цонхны тоо"].astype(str) 

mask0 = df_check["check_col"].duplicated(keep=False)
maskhigh = df_check["check_col"].duplicated()
df['check_col'] = df_check['check_col']
df['duplicate_danger'] = mask0
df['duplicate_nonfirst'] = maskhigh

df.to_csv("tmp_final_dupl.csv",encoding="utf-8-sig")   

# 7215621,7226897
