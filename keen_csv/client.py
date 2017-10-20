from keen import KeenClient

from keen_csv.response import KeenCSVResponse

class KeenCSVClient(KeenClient):
    wrapped_methods = [ 'count',
                        'count_unique',
                        'minimum',
                        'maximum',
                        'sum',
                        'average',
                        'median',
                        'percentile',
                        'select_unique',
                        'multi_analysis'
                        'extraction'
                      ]

    def __getattribute__(self, attr):
        attribute = super(KeenCSVClient, self).__getattribute__(attr)
        if attr in KeenClient.__getattribute__(self, 'wrapped_methods'):
            return(self._wrap(attribute))
        else:
            return(attribute)

    def _wrap(self, attribute):
        def _wrapper(*args, **kwargs):
            raw_response = attribute(*args, **kwargs)
            keen_csv_response = KeenCSVResponse(raw_response)
            return keen_csv_response.generate_csv()
        return _wrapper
