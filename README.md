# センサーデータ解析＆可視化ツール (Sensor Data Analysis & Visualization Tool)
# 概要 (Overview)
このプロジェクトは、テキストファイル形式のセンサーデータを解析し、異常値を検出して、結果をテキストレポートとグラフで自動的に出力するPythonスクリプトです。

# 主な機能 (Key Features)
高速なデータ処理: pandasを利用して、大規模なデータファイルでも効率的に読み込み、処理します。

異常検知: 設定された閾値（Threshold）を超えるデータを自動で検出します。

レポート自動生成: 解析日時、使用ファイル、検出された異常の総数と値をまとめたテキストレポート (anomaly_report.txt) を生成します。

グラフによる可視化: 全データと検出された異常値をプロットしたグラフ (anomaly_graph.png) を自動で保存し、結果を直感的に理解できます。

堅牢なエラー処理: 解析対象のファイルが存在しない場合や、ファイルが空の場合でもプログラムが停止しないように、エラー処理を実装しています。

# 動作環境 (Requirements)
Python 3.7+

pandas

matplotlib

# 使い方 (Usage)
データファイルの準備:
sensor_data.txt という名前で、1行に1つの数値データが記録されたテキストファイルを用意し、sensor_analyzer.py と同じディレクトリに配置します。

スクリプトの実行:
ターミナルで以下のコマンドを実行します。

python sensor_analyzer.py

結果の確認:
実行が完了すると、同じディレクトリに以下の2つのファイルが自動で生成されます。

anomaly_report.txt：解析結果がまとめられたテキストレポート。

anomaly_graph.png：データと異常値が示されたグラフ画像。

設定の変更 (Configuration)
入力ファイル名、出力ファイル名、異常検知の閾値は、sensor_analyzer.py スクリプト冒頭の以下の定数を変更することで、簡単にカスタマイズできます。

# --- Configuration Constants ---
INPUT_FILENAME = 'sensor_data.txt'
REPORT_FILENAME = 'anomaly_report.txt'
OUTPUT_IMAGE_FILENAME = 'anomaly_graph.png'
THRESHOLD = 100.0
