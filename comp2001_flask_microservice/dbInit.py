import pyodbc

server = 'dist-6-505.uopnet.plymouth.ac.uk'
database = 'COMP2001_DPhipps'
username = 'DPhipps'
password = 'OomT490+'
driver = '{ODBC Driver 17 for SQL Server}'

conn_str = (
    f'DRIVER={driver};'
    f'SERVER={server};'
    f'DATABASE={database};'
    f'UID={username};'
    f'PWD={password};'
    'Encrypt=Yes;'
    'TrustServerCertificate=Yes;'
    'Connection Timeout=30;'
    'Trusted_Connection=No'
)

conn = pyodbc.connect(conn_str)
cursor = conn.cursor()

people = [
    "'Grace', 'Hopper', '2024-11-19 16:15:10'",
    "'Tim', 'Berners-Lee', '2024-11-19 16:15:13'",
    "'Ada', 'Lovelace', '2024-11-19 16:15:27'",
]

cursor.execute("SELECT * FROM person")

people = cursor.fetchall()
for person in people:
    print(person)

cursor.close()
conn.close()