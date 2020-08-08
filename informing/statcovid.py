from requests import get
from re import findall

url = 'https://coronavirus-monitor.info'


def get_stats(country, city):
    res = [[], [], []]

    try:
        data = get(url).text
        res = {}
        res['0'] = findall(r'Заражено<br>[\d ]+', data)[0].replace('<br>', ': ').replace('(','').replace(')','').replace(',','')
        res['1'] = findall(r'Вылечено<br>[\d ]+', data)[0].replace('<br>', ': ').replace('(','').replace(')','').replace(',','')
        res['2'] = findall(r'Погибло<br>[\d ]+', data)[0].replace('<br>', ': ').replace('(','').replace(')','').replace(',','')

        data = get(url + '/country/{}'.format(country)).text
        res['3'] = findall(r'Заражено<br>[\d ]+', data)[0].replace('<br>', ': ').replace('(','').replace(')','').replace(',','')
        res['4'] = findall(r'Вылечено<br>[\d ]+',
                           data)[0].replace('<br>', ': ').replace('(','').replace(')','').replace(',','')
        res['5'] = findall(r'Погибло<br>[\d ]+', data)[0].replace('<br>', ': ')

        data = get(url + '/country/{}/{}/'.format(country, city)).text
        res['6'] = findall(r'Заражено<br>[\d ]+', data)[0].replace('<br>', ': ').replace('(','').replace(')','').replace(',','')
        res['7'] = findall(r'Вылечено<br>[\d ]+',
                           data)[0].replace('<br>', ': ').replace('(','').replace(')','').replace(',','')
        res['8'] = findall(r'Погибло<br>[\d ]+', data)[0].replace('<br>', ': ').replace('(','').replace(')','').replace(',','')
    except:
        res = [['Error'] * 3]

    return res
