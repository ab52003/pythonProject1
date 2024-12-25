import requests
import pandas as pd
import numpy as np

r = requests.get('https://lenta.ru', auth=('user', 'pass'))
print(r.status_code)
print(r.headers['content-type'])

data = pd.read_excel(r'C:\Users\ab520\Documents\GitHub\pythonProject1\Test1.xlsx')
print(data)

print(data.sort_values('Age', ascending=False).head())
print(data[data['Age'] > 25])
print(data['Age'].agg(['mean']))

a = np.array([1,2,3,4,5])
print(a)

print(a.size)
print(a.sum())
print(a.mean())