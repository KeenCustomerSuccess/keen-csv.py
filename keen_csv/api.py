from keen.api import KeenApi
from keen_csv.response import KeenCSVResponse
# from functools import wraps

class KeenCSVApi(KeenApi):
    def query(self, *args, **kwargs):
        response = KeenCSVResponse(KeenApi.query(self, *args, **kwargs))
        return response.generate_csv(self)
