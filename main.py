import pandas as pd

df = pd.read_csv(
    'dirty_crm_clients.csv',
    sep= ';',
    encoding='latin-1',
    dtype={'client_id': str}
)

#adding data inspection
print("Data Shape")
print(df.shape)

print("\nDataset Info")
df.info()

#Data Cleaning and Standarization

df['migration_date_clean'] = pd.to_datetime(df['migration_dates'], errors='coerce')

original_not_null = df['migration_dates'].notna()
failed_rows = df[original_not_null] & df['migration_dates'].isna()

if not failed_rows.empty:
    print(f"⚠️ Alerta de Migración: Se encontraron {len(failed_rows)} registros con formatos inválidos.")
    df_failed_dates = pd.DataFrame(failed_rows)
    df_failed_dates.to_csv('failed_date.csv')
    print("File 'failed_date.csv' successfully generated!")

df['full_name'] = df['full_name'].fillna)("MISSING NAME")

df['full_name'] = df['full_name'].str.strip().str.title()

