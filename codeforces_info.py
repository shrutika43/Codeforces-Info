'''
This script displays information like Codeforces User handle,rating,rank,maxRating,maxRank by fetching the data from Codeforces API
'''
import requests
uname = input('Enter your Codeforces Handle: ')

res = requests.get('http://codeforces.com/api/user.info?handles=' + uname)
data = res.json()

if data['status'] == 'OK':
    print('Handle :', data['result'][0]['handle'])
    print('Current Rating :', data['result'][0]['rating'])
    print('Rank :', data['result'][0]['rank'])
    print('Max Rating :', data['result'][0]['maxRating'])
    print('Max Rank :', data['result'][0]['maxRank'])
elif data['status'] == 'FAILED':
    print("This username does not exist")