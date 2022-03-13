import requests
import ipaddress


def get_ip():
    ip = input('Enter your IP Address: ')
    validate_ip_address(ip)

def validate_ip_address(ip):
    try:
        ip = ipaddress.ip_address(ip)
        main(ip)
    except ValueError:
        print('[!] IP is not valid')
        return None

def main(ip):
    response = requests.get(f'http://ip-api.com/json/{ip}').json()
    
    if response['status'] == 'fail':
        print('[!] Failed to find info')
        return None
    
    info = {
            'Status': response['status'],
            'IP': response['query'],
            'Country': response['country'],
            'Region Name': response['regionName'],
            'City': response['city'],
            'Organization': response['org'],
            'Latitude': response['lat'],
            'Longitude': response['lon']
        }

    for key, value in info.items():
        print(f'{key}: {value}')

if __name__=='__main__':
    get_ip()
    