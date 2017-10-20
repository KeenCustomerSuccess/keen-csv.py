from keen_csv.client import KeenCSVClient
from keen_csv.response import KeenCSVResponse

def to_csv(response):
    keen_csv_client = KeenCSVClient(response)
    return keen_csv_client.generate_csv()
