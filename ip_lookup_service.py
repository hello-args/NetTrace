import time
import requests
import logging
from config import API_BASE_URL, FIELDS, RETRY_COUNT, REQUEST_TIMEOUT, RETRY_DELAY

logger = logging.getLogger(__name__)

class IPLookupService:
    def __init__(self, retry_count=RETRY_COUNT):
        self.retry_count = retry_count

    def lookup(self, ip_address):
        for attempt in range(self.retry_count):
            try:
                url = f"{API_BASE_URL}{ip_address}?fields={FIELDS}"
                response = requests.get(url, timeout=REQUEST_TIMEOUT)
                response.raise_for_status()
                data = response.json()

                if data["status"] == "fail":
                    logger.warning(f"Failed lookup ({attempt+1}/{self.retry_count}) for {ip_address}: {data.get('message', 'Unknown error')}")
                    if attempt < self.retry_count - 1:
                        time.sleep(RETRY_DELAY)
                        continue
                    return self._error_result()

                return {
                    "ASN": data.get("as", "N/A"),
                    "ASN Name": data.get("isp", "N/A"),
                    "Country": data.get("country", "N/A"),
                    "State": data.get("regionName", "N/A"),
                }

            except requests.RequestException as e:
                logger.error(f"Request error ({attempt+1}/{self.retry_count}) for {ip_address}: {e}")
            except Exception as e:
                logger.error(f"Unexpected error ({attempt+1}/{self.retry_count}) for {ip_address}: {e}")

            if attempt < self.retry_count - 1:
                time.sleep(RETRY_DELAY)

        return self._error_result()

    def _error_result(self):
        return {"ASN": "Error", "ASN Name": "Error", "Country": "Error", "State": "Error"}
