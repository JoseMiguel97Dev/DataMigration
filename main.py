import pandas as pd

df = pd.read_csv(
    'dirty_crm_clients.csv',
    sep= ';',
    encoding='latin-1',
    dtype={'client_id': str}
)