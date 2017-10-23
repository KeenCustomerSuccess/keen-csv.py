# keen-csv.rb

Perform a Keen query, and get the results in a multiline CSV string

### Installation

Install this module via Pip:

```bash
  pip install keen_csv
```

### Usage

This module may be used in a couple of ways:

#### Direct conversion from the standard Keen Python client

Perform a query from the [Keen Python client](https://github.com/keenlabs/KeenClient-Python) like normal, and convert the results via `keen_csv.to_csv`. For configuring the CSV output using this method, include each option as a keyword argument.

```python
  import keen
  from keen_csv import to_csv

  keen.project_id = "xxxx"  # your project ID for collecting cycling data
  keen.read_key = "zzzz"

  keen_response = keen.sum("purchases", target_property="price", group_by="item.id", timeframe="this_14_days") # => [{ "item.id": 123, "result": 240 }, { ... }]

  to_csv(keen_response, ...keyword_options)
  # => item.id,result\n123,240\n...
```
#### Instantiating keen_csv.KeenCSVClient in place of keen.KeenClient
Follow the instructions for instantiating and querying with KeenClient in the [Keen Python client](https://github.com/keenlabs/KeenClient-Python), except using KeenCSVClient. For configuring the CSV output using this method, include an `options` dictionary as the value for the keword argument `csv`

```python
  from keen_csv import KeenCSVClient

  keen_client = KeenCSVClient(
      project_id="xxxx",
      read_key="zzzz",
  )

  # note: the `csv` dictionary here is purely optional
  client.sum("purchases", target_property="price", group_by="item.id", timeframe="this_14_days", csv={...options})
   # => item.id,result\n123,240\n...
```

### Options
*  `delimiter`:        Use this character rather than a comma
*  `delimiterSub`:     If we encounter any `delimiter` characters, we'll substitute them for this
*  `nestedDelimiter`:  The nature of a Keen response sometimes entails nested objects. In these cases we'll flatten the keys using this character/string
*  `filteredColumns`:  An array of column headers to filter out of the final CSV results
