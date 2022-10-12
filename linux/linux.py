import os

valorant_cluster = ['162.249.72.1'] #valorant ip

DNS1 = "213.234.0.2"
DNS2 = "213.234.2.6"

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

warface_cluster = ['s1.warface.ru', 'krasnodar.ping.warface.ru', 'novosibirsk.ping.warface.ru', 'khabarovsk.ping.warface.ru']

def getAddress(service):
    switcher={
                'valorant': valorant_cluster[0],
                "world of tanks": wot_cluster[0],
                "world of warships": world_of_warships_cluster[0],
                "world of warplanes": world_of_warplanes_cluster[0],
                "warface": warface_cluster[0]
             }
    return switcher.get(service,"Invalid service")

def fping_service(service, count = 1):
    result = os.popen(f"ping -c {count} {service}").read()
    return result

def fping_dns1(count = 1):
    result = os.popen(f"ping -c {count} {DNS1}").read()
    return result

def fping_dns2(count = 1):
    result = os.popen(f"ping -c {count} {DNS2}").read()
    return result

def trace_service(ip):
    result = os.popen(f"traceroute {ip}").read()
    return result

def dir_open(directory):
    os.system(f"xdg-open {directory}")


