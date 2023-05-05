from sslproxies import ProxyManager
from selenium.webdriver.common.proxy import Proxy, ProxyType


def PROXY():
    proxy = ProxyManager().get_new_proxy()
    prox = Proxy()
    prox.proxy_type = ProxyType.MANUAL
    prox.http_proxy = str(proxy.ip)+str(proxy.port)
    #prox.socks_proxy = str(proxy.ip)+str(proxy.port)
    #prox.ssl_proxy = str(proxy.ip)+str(proxy.port)

    return prox


