# https://jsonplaceholder.typicode.com/users'''
import requests

res = requests.get('https://jsonplaceholder.typicode.com/users')
users = res.json()

file = open('./stg/users.json', 'w')
file.write(str(users))
file.close()