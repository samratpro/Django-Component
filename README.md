
# Proxy
proxy= requests.get('https://api.ipify.org/?format=json').json()
requests.get(proxies=proxy)
