#!/usr/bin/python

"""
Global Settings...
"""

#
# Plex Media Server
def getPlexGDM():
    return True  # True: use PlexGDM (GoodDayMate) to auto discover PMS

def getIP_PMS():  # default IP, if GDM fails... todo: do we need this fall back?
    return '172.16.1.17'
def getPort_PMS():
    return 32400

#
# DNS/WebServer
def getIP_DNSmaster():  # Router, ISP's DNS, ...
    return '172.16.1.254'  # google public DNS

def getHostToIntercept():
    return 'trailers.apple.com'
