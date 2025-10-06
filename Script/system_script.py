import flet as ft
import numpy as np
from Script.measure_button import target_date
from Script.operation_db import output_db

#データの成形(評価値以外)
def transform_data(data):
    # 必要な列の順番を定義（ID, name, value を削除）
    new_order = [3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]

    # データ変換（指定された順番で並び替え）
    new_data = [[row[i] for i in new_order] for row in data]

    return new_data

#データの成形(評価値)
def vote_data(data):
    # 必要な列の順番を定義（ID, name, value を削除）
    new_order = [2]

    # データ変換（指定された順番で並び替え）
    new_data = [row[i] for row in data for i in new_order]  # 二次元を一次元に

    return new_data


#正規化
def normalize(data):

    # 最大値（color のみ 360、他は 5 と仮定）
    max_values = np.array([5, 5, 5, 5, 360, 5, 5, 5, 5, 5, 5, 5, 5, 5])
    min_values = np.zeros_like(max_values)  # 全ての最小値は 0

    # Min-Max 正規化 (各列ごとに適用)
    normalized_data = (data - min_values) / (max_values - min_values)

    return normalized_data

#円環距離
def circular_distance(a, b):
    # 角度の場合、絶対差を取る（円環上の距離）
    diff = abs(a - b)
    return min(diff, 2 * np.pi - diff)

#距離計算
def euclidean_distances(target, data, circular_index=4):
    target = np.array(target)
    data = np.array(data)
    
    # 通常のユークリッド距離計算
    euclidean_dist = np.linalg.norm(data[:, :circular_index] - target[:circular_index], axis=1)
    
    # 要素番号4の位置が円環状の値の場合、円環的距離を計算
    circular_dist = np.array([circular_distance(data[i, circular_index], target[circular_index]) for i in range(data.shape[0])])
    
    # ユークリッド距離と円環的距離を合わせて新しい距離を計算
    total_distances = np.sqrt(euclidean_dist**2 + circular_dist**2)
    
    return total_distances

#k近傍法
def neighborhood(distance, values):

    # 最小距離のインデックスを取得 (k個)
    k = 11
    sorted_indices = np.argsort(distance)[:k]

    values = np.array(values)  # valuesをNumPy配列に変換
    # 最小距離のインデックスを使って評価値を取り出す
    distance_values = values[sorted_indices]

    return distance_values

#予測評価値を計算
def average(result):
    # 配列の合計を計算
    total = sum(result)

    # 配列の要素数を取得
    count = len(result)

    # 平均値を計算
    average = total / count

    return f"{average:.2f}"

coefficient = ft.Text(value="",
        size=42,  # 文字サイズを明示的に指定
        weight=ft.FontWeight.BOLD
        )

def main_script():
    #ターゲットのデータ
    target = target_date()
    #データベースのデータ
    output_list = output_db()
    # データの成形(評価値以外)
    new_list = transform_data(output_list)
    # データの成形(評価値)
    values = vote_data(output_list)
    #正規化
    normalized_data = normalize(new_list)
    #距離計算
    distance = euclidean_distances(target, normalized_data)
    #k近傍法
    result_list = neighborhood(distance, values)
    #予測評価値
    result = average(result_list)

    coefficient.value = round(float(result)*100)

