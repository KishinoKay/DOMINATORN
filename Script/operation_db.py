import sqlite3

#データを出力するための関数
def output_db():
    #pythonでSQLを使用するための文章
    conn = sqlite3.connect("./Database/FaveList.db")
    cur = conn.cursor()

    #すべてのデータを出力するSQL
    SQL_data = f"""
    SELECT ID,name,value,
        dimension,gender,
        reality,meta,color,
        age,cute,coll,hair,
        gentleness,mysterious,
        spacey,leadership,charisma
    FROM FaveList
    ORDER BY ID ASC
    """

    #data変数にSQLで出力したデータを格納
    data = cur.execute(SQL_data)

    #データをリスト化する
    list_ = [list(row) for row in data]

    # データベースの接続を解除
    cur.close()
    conn.close()

    #すべてのデータを格納した配列を返す
    return list_

#最新のidを取得
def output_topID():
    #pythonでSQLを使用するための文章
    conn = sqlite3.connect("./Database/FaveList.db")
    cur = conn.cursor()

    data = cur.execute("SELECT ID FROM FaveList ORDER BY ID DESC LIMIT 1;")
    
    result = cur.fetchone()

    num = result[0]

    # データベースの接続を解除
    cur.close()
    conn.close()

    #すべてのデータを格納した配列を返す
    return num

#引数で与えられたデータをデータベースに格納するための関数
def input_db(name, value, dimension, gender, reality, meta, color, age, cute, coll, hair, gentleness, mysterious, spacey, leadership, charisma):
    #pythonでSQLを使用するための文章
    conn = sqlite3.connect("./Database/FaveList.db")
    cur = conn.cursor()

    # 挿入または更新のSQL
    data = (name, value, dimension, gender, reality, meta, color, age, cute, coll, hair, gentleness, mysterious, spacey, leadership, charisma)
    cur.execute('''
        INSERT INTO FaveList (name, value, dimension, gender, reality, meta, color, age, cute, coll, hair, gentleness, mysterious, spacey, leadership, charisma)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    ''', data)

    conn.commit()
    conn.close()

    #データ削除
def delete_db(record_id):
    #pythonでSQLを使用するための文章
    conn = sqlite3.connect("./Database/FaveList.db")
    cur = conn.cursor()


    
    # 削除のSQL
    cur.execute("DELETE FROM FaveList WHERE ID = ?", (record_id,))

    conn.commit()
    conn.close()