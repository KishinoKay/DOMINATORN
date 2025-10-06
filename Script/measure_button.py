import flet as ft
import numpy as np

#データ入力

dimension_radio = ft.RadioGroup(content=ft.Row(
    controls=[
        ft.Radio(value=1,label="1"),
        ft.Radio(value=2,label="2"),
        ft.Radio(value=3,label="3"),
        ft.Radio(value=4,label="4"),
        ft.Radio(value=5,label="5")
    ],
    alignment=ft.MainAxisAlignment.CENTER
))
gender_radio = ft.RadioGroup(content=ft.Row(
    controls=[
        ft.Radio(value=1,label="1"),
        ft.Radio(value=2,label="2"),
        ft.Radio(value=3,label="3"),
        ft.Radio(value=4,label="4"),
        ft.Radio(value=5,label="5")
    ],
    alignment=ft.MainAxisAlignment.CENTER
))
reality_radio = ft.RadioGroup(content=ft.Row(
    controls=[
        ft.Radio(value=1,label="1"),
        ft.Radio(value=2,label="2"),
        ft.Radio(value=3,label="3"),
        ft.Radio(value=4,label="4"),
        ft.Radio(value=5,label="5")
    ],
    alignment=ft.MainAxisAlignment.CENTER
))
meta_radio = ft.RadioGroup(content=ft.Row(
    controls=[
        ft.Radio(value=1,label="1"),
        ft.Radio(value=2,label="2"),
        ft.Radio(value=3,label="3"),
        ft.Radio(value=4,label="4"),
        ft.Radio(value=5,label="5")
    ],
    alignment=ft.MainAxisAlignment.CENTER
))
color_radio = ft.RadioGroup(content=ft.Row(
    controls=[
        ft.Radio(value=0,label="赤"),
        ft.Radio(value=30,label="オレンジ"),
        ft.Radio(value=60,label="黄色"),
        ft.Radio(value=120,label="緑"),
        ft.Radio(value=180,label="水色"),
        ft.Radio(value=240,label="青"),
        ft.Radio(value=270,label="紫"),
        ft.Radio(value=300,label="マゼンタ"),
    ],
    alignment=ft.MainAxisAlignment.CENTER
))
age_radio = ft.RadioGroup(content=ft.Row(
    controls=[
        ft.Radio(value=1,label="10歳"),
        ft.Radio(value=2,label="20歳"),
        ft.Radio(value=3,label="40歳"),
        ft.Radio(value=4,label="60歳"),
        ft.Radio(value=5,label="80歳")
    ],
    alignment=ft.MainAxisAlignment.CENTER
))
cute_radio = ft.RadioGroup(content=ft.Row(
    controls=[
        ft.Radio(value=1,label="1"),
        ft.Radio(value=2,label="2"),
        ft.Radio(value=3,label="3"),
        ft.Radio(value=4,label="4"),
        ft.Radio(value=5,label="5")
    ],
    alignment=ft.MainAxisAlignment.CENTER
))
coll_radio = ft.RadioGroup(content=ft.Row(
    controls=[
        ft.Radio(value=1,label="1"),
        ft.Radio(value=2,label="2"),
        ft.Radio(value=3,label="3"),
        ft.Radio(value=4,label="4"),
        ft.Radio(value=5,label="5")
    ],
    alignment=ft.MainAxisAlignment.CENTER
))
hair_radio = ft.RadioGroup(content=ft.Row(
    controls=[
        ft.Radio(value=1,label="1"),
        ft.Radio(value=2,label="2"),
        ft.Radio(value=3,label="3"),
        ft.Radio(value=4,label="4"),
        ft.Radio(value=5,label="5")
    ],
    alignment=ft.MainAxisAlignment.CENTER
))
gentleness_radio = ft.RadioGroup(content=ft.Row(
    controls=[
        ft.Radio(value=1,label="1"),
        ft.Radio(value=2,label="2"),
        ft.Radio(value=3,label="3"),
        ft.Radio(value=4,label="4"),
        ft.Radio(value=5,label="5")
    ],
    alignment=ft.MainAxisAlignment.CENTER
))
mysterious_radio = ft.RadioGroup(content=ft.Row(
    controls=[
        ft.Radio(value=1,label="1"),
        ft.Radio(value=2,label="2"),
        ft.Radio(value=3,label="3"),
        ft.Radio(value=4,label="4"),
        ft.Radio(value=5,label="5")
    ],
    alignment=ft.MainAxisAlignment.CENTER
))
spacey_radio = ft.RadioGroup(content=ft.Row(
    controls=[
        ft.Radio(value=1,label="1"),
        ft.Radio(value=2,label="2"),
        ft.Radio(value=3,label="3"),
        ft.Radio(value=4,label="4"),
        ft.Radio(value=5,label="5")
    ],
    alignment=ft.MainAxisAlignment.CENTER
))
leadership_radio = ft.RadioGroup(content=ft.Row(
    controls=[
        ft.Radio(value=1,label="1"),
        ft.Radio(value=2,label="2"),
        ft.Radio(value=3,label="3"),
        ft.Radio(value=4,label="4"),
        ft.Radio(value=5,label="5")
    ],
    alignment=ft.MainAxisAlignment.CENTER
))
charisma_radio = ft.RadioGroup(content=ft.Row(
    controls=[
        ft.Radio(value=1,label="1"),
        ft.Radio(value=2,label="2"),
        ft.Radio(value=3,label="3"),
        ft.Radio(value=4,label="4"),
        ft.Radio(value=5,label="5")
    ],
    alignment=ft.MainAxisAlignment.CENTER
))

dimension_text = ft.Text("二次元＜－－＞三次元")
gender_text = ft.Text("男＜－－＞女")
reality_text = ft.Text("世界観 リアル＜－－＞ファンタジー")
meta_text = ft.Text("メタ的かどうか")
color_text = ft.Text("好きな色")
age_text = ft.Text("見た目の年齢 幼い＜－－＞大人")
cute_text = ft.Text("可愛い")
coll_text = ft.Text("カッコいい")
hair_text = ft.Text("髪型 ショート＜－－＞ロング")
gentleness_text = ft.Text("やさしさ")
mysterious_text = ft.Text("ミステリアス")
spacey_text = ft.Text("天然")
leadership_text = ft.Text("リーダーシップ")
charisma_text = ft.Text("カリスマ性")

selections = [
    dimension_text,
    dimension_radio,
    gender_text,
    gender_radio,
    reality_text,
    reality_radio,
    meta_text,
    meta_radio,
    color_text,
    color_radio,
    age_text,
    age_radio,
    cute_text,
    cute_radio,
    coll_text,
    coll_radio,
    hair_text,
    hair_radio,
    gentleness_text,
    gentleness_radio,
    mysterious_text,
    mysterious_radio,
    spacey_text,
    spacey_radio,
    leadership_text,
    leadership_radio,
    charisma_text,
    charisma_radio
]

def target_date():
    dimension = int(dimension_radio.value)
    gender = int(gender_radio.value)
    reality = int(reality_radio.value)
    meta = int(meta_radio.value)
    color = int(color_radio.value)
    age = int(age_radio.value)
    cute = int(cute_radio.value)
    coll = int(coll_radio.value)
    hair = int(hair_radio.value)
    gentleness = int(gentleness_radio.value)
    mysterious = int(mysterious_radio.value)
    spacey = int(spacey_radio.value)
    leadership = int(leadership_radio.value)
    charisma = int(charisma_radio.value)
    list_ = [dimension, gender, reality, meta, color, age, cute, coll, hair, gentleness, mysterious, spacey, leadership, charisma]

    # 各特徴の最大値（color だけ 360、それ以外は 5）
    max_values = np.array([5, 5, 5, 5, 360, 5, 5, 5, 5, 5, 5, 5, 5, 5])
    min_values = np.zeros_like(max_values)  # 全ての最小値は 0

    normalized_list = (list_ - min_values) / (max_values - min_values)

    return normalized_list