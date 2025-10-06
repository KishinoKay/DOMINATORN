# ドミネー担（DOMINATORN）

## 概要

「ドミネー担」は、アニメ『PSYCHO-PASS』のドミネーターをモチーフにした、キャラクター評価・心理診断アプリです。Flet（Python GUIフレームワーク）を用いて開発されており、ユーザーがキャラクターの属性や好みを入力し、独自のアルゴリズムで「同担係数」を算出します。音声・画像演出やデータベース機能も搭載しています。

## 主な機能

- キャラクター属性・好みの入力（複数パラメータ）
- 入力値に基づく「同担係数」の自動計算（k近傍法＋正規化）
- 計測・診断結果に応じた音声・画像演出
- キャラクターデータのデータベース管理・閲覧
- ダークテーマ・カスタムカラースキーム対応

## 画面構成

- **メイン画面**：タイトル・開始ボタン・DBアクセスボタン
- **計測画面**：キャラクター属性入力・計測確定/中断
- **執行画面**：同担係数の表示・執行モード演出
- **データベース画面**：キャラクターデータの追加・一覧表示

## ディレクトリ構成

- `main.py` : アプリのエントリーポイント
- `View/` : 各画面のUIロジック
	- `main_page.py` : メイン画面
	- `measure_page.py` : 計測画面
	- `Execution_page.py` : 執行画面
	- `access_SibylSystem.py` : データベース画面
- `Script/` : ロジック・補助スクリプト
	- `system_script.py` : 同担係数計算アルゴリズム
	- `measure_button.py` など
- `Database/` : データベース関連
	- `FaveList.db` : SQLite DB
	- `create_db.py` : DB作成スクリプト
	- `DatabaseDefinition.txt` : DB設計書
- `assets/` : 画像素材
- `Audio/` : 効果音・音声ファイル

## 必要環境

- Python 3.8以降
- Flet 0.22.*
- pygame
- numpy

## インストール

1. 必要なパッケージをインストール
   ```sh
   pip install -r requirements.txt
   pip install pygame numpy
   ```
2. アプリを起動
   ```sh
   flet run main.py
   ```

## データベース仕様

`Database/DatabaseDefinition.txt` を参照してください。

## ライセンス

本プロジェクトは個人開発・学習目的です。