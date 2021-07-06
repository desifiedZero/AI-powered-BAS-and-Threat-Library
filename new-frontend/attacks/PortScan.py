# -*- coding: utf-8 -*-
"""
Created on Wed May  5 17:23:21 2021

@author: Nasr Sami Khan
"""

import socket
from concurrent import futures

def check_port(targetIp, portNumber, timeout):
    TCPsock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    TCPsock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    TCPsock.settimeout(timeout)
    try:
        TCPsock.connect((targetIp, portNumber))
        return (portNumber)
    except:
        return

def port_scanner(targetIp, timeout):
    threadPoolSize = 500
    ports = [21, 22, 80, 110, 995, 443, 143, 993, 25, 26, 587, 3306, 2082, 2083, 2086, 2087, 2095, 2096, 2077, 2078, 999]

    executor = futures.ThreadPoolExecutor(max_workers=threadPoolSize)
    checks = [
        executor.submit(check_port, targetIp, port, timeout)
        for port in ports
    ]

    for response in futures.as_completed(checks):
        if (response.result()):
            print('[OPEN]{}'.format(response.result()))

    print('[FINISHED]')

def portscan(url):
    targetIp = socket.gethostbyname(url)
    timeout = 300
    port_scanner(targetIp, timeout)