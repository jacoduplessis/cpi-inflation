# cpi-inflation

## install

```
pip install cpi-inflation
```

## usage

```python
from cpi_inflation import add_inflation_single, add_inflation_multiple
from cpi_inflation.za import CPI_INFLATION
from datetime import datetime, timedelta

today = datetime.now().date()
six_years_ago = today.replace(year=today.year-6)
six_years_ahead = today.replace(year=today.year+6)
amount = 100_000

# the first argument to the function below is and
# ordered dict of the  structure
# {<date_str>: <index_value>}

# if the lookup map does not contain the required values, the initial amount is returned unchanged.

# add inflation to historic value
val = add_inflation_single(CPI_INFLATION, amount, dt=six_years_ago, to=today)

# discount a present value using historic inflation
val = add_inflation_single(CPI_INFLATION, amount, dt=today, to=six_years_ago)

# discount a future value at fixed yearly rate
val = add_inflation_single(CPI_INFLATION, amount, dt=six_years_ahead, to=today, discounting_rate=1.06)

# get future value at fixed yearly rate
val = add_inflation_single(CPI_INFLATION, amount, dt=today, to=six_years_ahead, discounting_rate=1.06)

# calculating multiple values
table = [
    (amount, today),
    (amount, six_years_ago)
]
vals = add_inflation_multiple(CPI_INFLATION, table, to=six_years_ahead, discounting_rate=1.06)


```

## run tests

```
python -m unittest discover tests
```

## inflation data

Historic CPI inflation for South Africa is included under the `za` module.

### internal notes

*index_maps*: maps should be ordered. Either use python3.7 or OrderedDicts.