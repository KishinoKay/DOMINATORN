#データベースを作成するためのファイル。一度データベースを作成してしまえばそれ以降実行する必要無し
import sqlite3

conn = sqlite3.connect("./Database/FaveList.db")

# カーソルオブジェクトを作成
cursor = conn.cursor()

# テーブルを作成
cursor.execute('''
    CREATE TABLE IF NOT EXISTS FaveList (
        ID INTEGER PRIMARY KEY,
        name TEXT,
        value INTEGER,
        dimension INTEGER,
        gender INTEGER,
        reality INTEGER,
        meta INTEGER,
        color INTEGER,
        
        age INTEGER,
        cute INTEGER,
        coll INTEGER,
        hair INTEGER,
        
        gentleness INTEGER,
        mysterious INTEGER,
        spacey INTEGER,
        leadership INTEGER,
        charisma INTEGER
    )
''')


# ファイルを読み込み、各行をタプルに変換
data = []
with open('./Database/fave_characters_500.csv', 'r', encoding='utf-8-sig') as f:
    for line in f:
        values = line.strip().split(',')
        if len(values) == 16:  # カラム数が一致することを確認
            name = values[0]
            value = int(values[1])
            dimension = int(values[2])
            gender = int(values[3])
            reality = int(values[4])
            meta = int(values[5])
            color = int(values[6])
            age = int(values[7])
            cute = int(values[8])
            coll = int(values[9])
            hair = int(values[10])
            gentleness = int(values[11])
            mysterious = int(values[12])
            spacey = int(values[13])
            leadership = int(values[14])
            charisma = int(values[15])

            data.append((
                name, value, dimension, gender, reality, meta, color,
                age, cute, coll, hair, gentleness, mysterious, spacey, leadership, charisma
            ))

# データを挿入
cursor.executemany('''
    INSERT INTO FaveList (
        name, value, dimension, gender, reality, meta, color,
        age, cute, coll, hair, gentleness, mysterious, spacey, leadership, charisma
    ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
''', data)


# コミットして変更を保存
conn.commit()

# 接続を閉じる
conn.close()
