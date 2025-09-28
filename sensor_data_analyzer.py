# -*- coding: utf-8 -*-
"""sensor-data-analyzer

このスクリプトは、センサーデータを記録したテキストファイルを読み込み、
指定された閾値を超える異常値を検出して、詳細なレポートを生成します
"""

from datetime import datetime

def get_configuration():
  """
プログラムの全体的な設定値を返す。

    Returns:
        tuple: 以下の3つの設定値を含むタプル。
            - input_filename (str): 読み込むデータファイル名。
            - report_filename (str): 出力するレポートファイル名。
            - threshold (float): 異常を検知する閾値。
  """
  input_filename = 'sensor_data.txt'
  report_filename = 'report.txt'
  threshold = 50.0
  return input_filename , report_filename , threshold

def read_data(filename):
  """
指定されたファイルからセンサーデータを読み込み、数値のリストとして返す。
ファイルが見つからない場合や、数値に変換できない行があった場合は、
エラー/警告メッセージを表示し、処理を続行する。
  """
  datalist = []
  try:
    with open(filename,'r') as f:
      for line in f:
        cleaned_text = line.strip()
        try:
          value = float(cleaned_text)
          datalist.append(value)
        except ValueError:
          print('数値に変換できない文字列が含まれています')
  except FileNotFoundError:
    print(f'ファイル"{filename}"が見つかりません')
    return []
  return datalist

def analyze_data(datalist, threshold):
  """
    数値データのリストを分析し、閾値を超える異常値を検出する。

    Args:
        datalist (list): 解析対象となる数値(float)のリスト。
        threshold (float): 異常と判断するための閾値。

    Returns:
        tuple: 以下の2つの値を含むタプル。
            - anomaly_count (int): 検出された異常の合計数。
            - detected_anomalies (list): 検出された異常値のリスト。
  """
  anomaly_count = 0
  detected_anomalies = []
  for value in datalist:
    if value > threshold:
      anomaly_count += 1
      detected_anomalies.append(value)
  return anomaly_count , detected_anomalies

def write_report(anomaly_count , detected_anomalies, input_filename, report_filename, threshold):
  """
分析結果を整形し、指定されたファイルにレポートとして書き出す。

    Args:
        report_filename (str): 出力するレポートファイル名。
        input_filename (str): 解析に使われた元のデータファイル名。
        threshold (float): 解析に使われた閾値。
        anomaly_count (int): 検出された異常の合計数。
        detected_anomalies (list): 検出された異常値のリスト。
  """
  with open(report_filename,'w') as f:
    f.write('#異常検知レポート\n\n')
    current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    f.write(f'-解析日時:{current_time}\n')
    f.write(f'-解析対象:{input_filename}\n')
    f.write(f'-異常検知の閾値:{threshold}\n\n')
    f.write(f'-------\n異常の合計回数:{anomaly_count}回\n\n')
    f.write(f'検出された異常値：\n')
    for anomaly in detected_anomalies:
      f.write(f'{anomaly}\n')

if __name__ == "__main__":
  input_filename, report_filename, threshold = get_configuration()
  sensor_value = read_data(input_filename)
  anomaly_count , detected_anomalies = analyze_data(sensor_value, threshold)
  write_report(anomaly_count,detected_anomalies,input_filename,report_filename,threshold)
  print(f"レポート'{report_filename}'の作成が完了しました")
