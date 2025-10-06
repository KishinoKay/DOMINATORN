import flet as ft
from Script.operation_db import input_db, output_db, delete_db, output_topID

#データ入力
name = ft.TextField(label="推しの名前", hint_text="推しの名前を記入してください")

value_slider = ft.Slider(value=0, min=-5, max=5, divisions=10, label="{value}")
dimension_slider = ft.Slider(min=0, max=5, divisions=5, label="{value}")
gender_slider = ft.Slider(min=0, max=5, divisions=5, label="{value}")
reality_slider = ft.Slider(min=0, max=5, divisions=5, label="{value}")
meta_slider = ft.Slider(min=0, max=5, divisions=5, label="{value}")
color_slider = ft.Slider(min=0, max=7, divisions=7, label="{value}")
age_slider = ft.Slider(min=0, max=5, divisions=5, label="{value}")
cute_slider = ft.Slider(min=0, max=5, divisions=5, label="{value}")
coll_slider = ft.Slider(min=0, max=5, divisions=5, label="{value}")
hair_slider = ft.Slider(min=0, max=5, divisions=5, label="{value}")
gentleness_slider = ft.Slider(min=0, max=5, divisions=5, label="{value}")
mysterious_slider = ft.Slider(min=0, max=5, divisions=5, label="{value}")
spacey_slider = ft.Slider(min=0, max=5, divisions=5, label="{value}")
leadership_slider = ft.Slider(min=0, max=5, divisions=5, label="{value}")
charisma_slider = ft.Slider(min=0, max=5, divisions=5, label="{value}")


value_text = ft.Text("評価値 嫌い＜－－＞好き")
dimension_text = ft.Text("二次元＜－－＞三次元")
gender_text = ft.Text("男＜－－＞女")
reality_text = ft.Text("世界観 リアル＜－－＞ファンタジー")
meta_text = ft.Text("メタ的かどうか")
color_text = ft.Text("イメージカラー\n1:赤 2:オレンジ 3:黄色 4:緑\n5:みずいろ 6:青色 7:紫 8:マゼンタ")
age_text = ft.Text("見た目の年齢 幼い＜－－＞大人")
cute_text = ft.Text("可愛い")
coll_text = ft.Text("カッコいい")
hair_text = ft.Text("髪型 ショート＜－－＞ロング")
gentleness_text = ft.Text("やさしさ")
mysterious_text = ft.Text("ミステリアス")
spacey_text = ft.Text("天然")
leadership_text = ft.Text("リーダーシップ")
charisma_text = ft.Text("カリスマ性")

def date_in(page):
    name_ = name.value
    value_ = int(value_slider.value)
    dimension = int(dimension_slider.value)
    gender = int(gender_slider.value)
    reality = int(reality_slider.value)
    meta = int(meta_slider.value)
    if int(color_slider.value) == 0:
        color = 0
    elif int(color_slider.value) == 1:
        color = 30
    elif int(color_slider.value) == 2:
        color = 60
    elif int(color_slider.value) == 3:
        color = 120
    elif int(color_slider.value) == 4:
        color = 180
    elif int(color_slider.value) == 5:
        color = 240
    elif int(color_slider.value) == 6:
        color = 270
    elif int(color_slider.value) == 7:
        color = 300
    age = int(age_slider.value)
    cute = int(cute_slider.value)
    coll = int(coll_slider.value)
    hair = int(hair_slider.value)
    gentleness = int(gentleness_slider.value)
    mysterious = int(mysterious_slider.value)
    spacey = int(spacey_slider.value)
    leadership = int(leadership_slider.value)
    charisma = int(charisma_slider.value)
    input_db(name_, value_, dimension, gender, reality, meta, color, age, cute, coll, hair, gentleness, mysterious, spacey, leadership, charisma)
    id = int(output_topID())

    #リストのデータをページに追加表示
    date_list.controls.append(
        ft.Card(ft.Container(ft.Column([
            ft.ListTile(
                leading=ft.Icon(ft.icons.INFO, size=48),
                title=ft.Text(name.value),
                subtitle=ft.Text(f"性別:{gender_slider.value}"),
                trailing=ft.Text(f"評価値:{value_slider.value}"),
            ),
            ft.Row([
                ft.VerticalDivider(width=10),
                ft.Column([
                    ft.Text(f"二次元or三次元:{dimension_slider.value}"),
                    ft.Text(f"世界観:{reality_slider.value}"),
                    ft.Text(f"イメージカラー{color_slider.value}"),
                ])
            ]),
            ft.Row([
                ft.TextButton("削除", on_click=lambda e, val=id: remove_item(e, page, val))
            ], alignment=ft.MainAxisAlignment.END),
        ]),
            padding=10,
            width=300,
        ),
            margin=10,
            elevation=5,
        )
    )

    name.value = ""
    value_slider.value = 0
    dimension_slider.value = 0
    gender_slider.value = 0
    reality_slider.value = 0
    meta_slider.value = 0
    color_slider.value = 0
    age_slider.value = 0
    cute_slider.value = 0
    coll_slider.value = 0
    hair_slider.value = 0
    gentleness_slider.value = 0
    mysterious_slider.value = 0
    spacey_slider.value = 0
    leadership_slider.value = 0
    charisma_slider.value = 0
    page.update()

selections = [
    name,
    value_text,
    value_slider,
    dimension_text,
    dimension_slider,
    gender_text,
    gender_slider,
    reality_text,
    reality_slider,
    meta_text,
    meta_slider,
    color_text,
    color_slider,
    age_text,
    age_slider,
    cute_text,
    cute_slider,
    coll_text,
    coll_slider,
    hair_text,
    hair_slider,
    gentleness_text,
    gentleness_slider,
    mysterious_text,
    mysterious_slider,
    spacey_text,
    spacey_slider,
    leadership_text,
    leadership_slider,
    charisma_text,
    charisma_slider
]

#データのリスト
date_list = ft.Row(
        controls=[],
        wrap=True,
        scroll=ft.ScrollMode.ALWAYS,
        expand=True
    )

#データリストを書き換え
def list_append(page):
    _list = output_db()
    for i in _list:
        date_list.controls.append(
            ft.Card(ft.Container(ft.Column([
                ft.ListTile(
                    leading=ft.Icon(ft.icons.INFO, size=48),
                    title=ft.Text(i[1]),
                    subtitle=ft.Text(f"性別:{i[4]}"),
                    trailing=ft.Text(f"評価値:{i[2]}"),
                ),
                ft.Row([
                    ft.VerticalDivider(width=10),
                    ft.Column([
                        ft.Text(f"二次元or三次元:{i[3]}"),
                        ft.Text(f"世界観:{i[5]}"),
                        ft.Text(f"イメージカラー{i[7]}"),
                    ])
                ]),
                ft.Row([
                    ft.TextButton("削除", on_click=lambda e, val=i[0]: remove_item(e, page, val))
                ], alignment=ft.MainAxisAlignment.END),
            ]),
                padding=10,
                width=300,
            ),
                margin=10,
                elevation=5,
            )
        )
    page.update()

def remove_item(e, page, value):
    e.control.disabled = True
    if(value != None):
        delete_db(value)
        date_list.controls.clear()
        list_append(page)