# file_handler.py
import os
import pandas as pd
import logging

logger = logging.getLogger(__name__)

def read_ip_list(file_path):
    if not os.path.exists(file_path):
        logger.error(f"File not found: {file_path}")
        raise FileNotFoundError("File not found.")
    df = pd.read_excel(file_path, header=0, usecols=[0], names=["IP"])
    logger.info(f"Loaded {len(df)} IPs from {file_path}")
    return df["IP"].dropna().tolist(), df

def write_results_to_excel(df, results, save_path):
    if not save_path.lower().endswith(".xlsx"):
        logger.error("Output file must be an .xlsx file")
        raise ValueError("Output file must be an .xlsx file")
    df[["ASN", "ASN Name", "Country", "State"]] = pd.DataFrame(results)
    df.to_excel(save_path, index=False)
    logger.info(f"Results written to {save_path}")
