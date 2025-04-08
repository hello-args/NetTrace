from ip_lookup_service import IPLookupService
from file_handler import read_ip_list, write_results_to_excel
from logger import setup_logger
import logging

logger = logging.getLogger(__name__)

def main():
    setup_logger()

    try:
        file_path = input("Enter the full path to the spreadsheet: ").strip()
        ip_list, df = read_ip_list(file_path)

        service = IPLookupService()
        results = [service.lookup(ip) for ip in ip_list]

        save_path = input("Enter the full path to save the updated spreadsheet: ").strip()
        write_results_to_excel(df, results, save_path)
        print(f"Spreadsheet saved successfully at {save_path}")

    except Exception as e:
        logger.exception("An error occurred during processing")
        print("An error occurred. Check error.log for details.")

if __name__ == "__main__":
    main()
