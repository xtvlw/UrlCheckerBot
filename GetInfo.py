import requests
import socket

page, html = '', ''


class InternetProtocolInformation:
    def __init__(self, internet_protocol):
        global page, html
        url = f'https://iplogger.org/url-checker/?d={internet_protocol}'
        url = requests.get(url)
        page = url.text
        for i in page:
            html += i

    @staticmethod
    def get_data(source):
        global html
        find = f"alt='{source}'>"
        start = html.find(find)
        find2 = "</div>"
        end = html[start:]
        result = end[end.find('>') + 2:end.find(find2)]
        result = result.replace('\r\n\t\t\t', '')
        return result

    @staticmethod
    def get_port(source):
        global html
        find = f">{source}</div>"
        start = html.find(find)
        find2 = "</div>"
        end = html[start + len(find):]
        result = end[end.find('&nbsp;') + 6:end.find(find2)]
        result = result.replace('</a>\n\t\t\t', '')
        result = result.replace('\r\n\t\t\t', '')
        return result

    @staticmethod
    def get_ip(url):
        url = url.replace('//', '')
        url = url[url.find(':') + 1:url.find('/')]
        try:
            return socket.gethostbyname(url)
        except:
            return 'Invalid'


def main_function(internet_protocol):
    global html
    ip = str(internet_protocol)

    get_info = InternetProtocolInformation(ip)

    data = {
        "ip": get_info.get_ip(ip),
        "region": get_info.get_data('Region'),
        "country": get_info.get_data('Country'),
        "city": get_info.get_data('City'),
        "provider": get_info.get_data('Provider'),
        "port": get_info.get_port('Port')
    }
    html = ''
    return data
