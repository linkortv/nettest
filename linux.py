import os
from dotenv import dotenv_values, load_dotenv
config = dotenv_values(".env")

ping_office = f"ping -c 10 {config['office']}" # ping to office vist
ping_yandex = "ping -c 10 ya.ru" # ping to yandex
ping_google = "ping -c 10 google.com" # ping to google
ping_dns1 = f"ping -c 10 {config['DNS1']}"
ping_dns2 = f"ping -c 10 {config['DNS2']}"

valorant_ip = '162.249.72.1' #valorant ip

#кластеры серверов wargaming
wot_cluster = [ 'login.p1.worldoftanks.net',
                'login.p2.worldoftanks.net',
                'login.p4.worldoftanks.net',
                'login.p5.worldoftanks.net',
                'login.p6.worldoftanks.net',
                'login.p7.worldoftanks.net',
                'login.p8.worldoftanks.net',
                'login.p9.worldoftanks.net' ]
world_of_warships_cluster = [ 'login1.worldofwarships.ru' ]
world_of_warplanes_cluster = [ 'login-ru.worldofwarplanes.com' ]
wot_ips = []

for domen in wot_cluster:
    command = "dig +short {domen}".format(domen = domen)
    ips = list(filter(None, os.popen(command).read().split("\n")))
    wot_ips.append(ips)
# print(wot_ips)
traceroute = "traceroute {ip}".format(ip = valorant_ip)

def test():
    # os.system(ping_office)
    os.system(ping_yandex)
    # os.system(ping_google)
    # os.system(ping_dns1)
    os.system(ping_dns2)
    m = os.popen(traceroute).read()
    return m