# -*- coding: utf-8 -*-
"""
This script analyzes sensor data from a text file using pandas and matplotlib.
It detects anomalies, generates a text report, and visualizes the data in a graph.
"""
import sys
from datetime import datetime
from typing import List, Tuple, Optional

import pandas as pd
import matplotlib.pyplot as plt

# --- Configuration Constants ---
INPUT_FILENAME = 'sensor_data.txt'
REPORT_FILENAME = 'anomaly_report.txt'
OUTPUT_IMAGE_FILENAME = 'anomaly_graph.png'
THRESHOLD = 100.0

def load_data_with_pandas(filename: str) -> Optional[pd.DataFrame]:
    """
    Loads data from a CSV/text file into a pandas DataFrame.

    Args:
        filename (str): The path to the input file.

    Returns:
        Optional[pd.DataFrame]: A DataFrame with a 'value' column,
                                or None if the file is not found.
    """
    try:
        df = pd.read_csv(filename, header=None, names=['value'])
        return df
    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.", file=sys.stderr)
        return None
    except pd.errors.EmptyDataError:
        print(f"Warning: The file '{filename}' is empty.", file=sys.stderr)
        return pd.DataFrame(columns=['value'])


def find_anomalies(
    df: pd.DataFrame, threshold: float
) -> Tuple[int, List[float], pd.DataFrame]:
    """
    Finds anomalies in the DataFrame that exceed a given threshold.

    Args:
        df (pd.DataFrame): The input DataFrame with a 'value' column.
        threshold (float): The threshold for detecting anomalies.

    Returns:
        Tuple[int, List[float], pd.DataFrame]:
            A tuple containing:
            - The count of anomalies.
            - A list of anomalous values.
            - A DataFrame containing only the anomalous data.
    """
    anomalies_df = df[df['value'] > threshold]
    anomalies_count = len(anomalies_df)
    detected_anomalies = anomalies_df['value'].tolist()
    return anomalies_count, detected_anomalies, anomalies_df

def generate_text_report(
    report_filename: str,
    input_filename: str,
    threshold: float,
    anomaly_count: int,
    detected_anomalies: List[float]
) -> None:
    """
    Generates a text-based report of the analysis results.

    Args:
        report_filename (str): The name of the output report file.
        input_filename (str): The name of the source data file.
        threshold (float): The threshold used for analysis.
        anomaly_count (int): The total count of detected anomalies.
        detected_anomalies (List[float]): A list of the detected values.
    """
    current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    with open(report_filename, 'w', encoding='utf-8') as f:
        f.write("# Anomaly Detection Report\n\n")
        f.write(f"- Analysis Timestamp: {current_time}\n")
        f.write(f"- Data Source: {input_filename}\n")
        f.write(f"- Anomaly Threshold: {threshold}\n\n")
        f.write("-------\n")
        f.write(f"Total Anomalies Detected: {anomaly_count}\n\n")
        
        if detected_anomalies:
            f.write("Detected Anomalous Values:\n")
            for anomaly in detected_anomalies:
                f.write(f"- {anomaly}\n")
        else:
            f.write("No anomalous values were detected.\n")

def generate_anomaly_graph(
    full_df: pd.DataFrame,
    anomalies_df: pd.DataFrame,
    output_filename: str
) -> None:
    """
    Creates and saves a graph visualizing the sensor data and anomalies.

    Args:
        full_df (pd.DataFrame): The DataFrame containing all data points.
        anomalies_df (pd.DataFrame): The DataFrame containing only anomalies.
        output_filename (str): The filename for the saved graph image.
    """
    plt.style.use('seaborn-v0_8-whitegrid')
    fig, ax = plt.subplots(figsize=(15, 7))
    
    ax.plot(full_df.index, full_df['value'], label='Sensor Value', color='cornflowerblue', linewidth=2)
    ax.scatter(anomalies_df.index, anomalies_df['value'], label='Anomaly Detected', color='red', s=50, zorder=5)
    
    ax.set_xlabel('Data Point Index', fontsize=12)
    ax.set_ylabel('Sensor Value', fontsize=12)
    ax.set_title('Sensor Data Analysis Results', fontsize=16, weight='bold')
    ax.legend()
    ax.grid(True)
    
    plt.tight_layout()
    plt.savefig(output_filename)
    plt.close()
    print(f"Graph saved as '{output_filename}'")


def main() -> None:
    """Main function to orchestrate the data analysis and report generation."""
    print(f"Starting analysis of '{INPUT_FILENAME}'...")
    
    data_df = load_data_with_pandas(INPUT_FILENAME)

    if data_df is None:
        print("Analysis stopped because the data file could not be loaded.")
        return

    anomaly_count, detected_anomalies, anomalies_df = find_anomalies(data_df, THRESHOLD)
    
    generate_text_report(
        REPORT_FILENAME,
        INPUT_FILENAME,
        THRESHOLD,
        anomaly_count,
        detected_anomalies
    )
    print(f"Text report '{REPORT_FILENAME}' has been generated.")

    generate_anomaly_graph(data_df, anomalies_df, OUTPUT_IMAGE_FILENAME)
    
    print("\nAnalysis complete.")


if __name__ == "__main__":
    main()

