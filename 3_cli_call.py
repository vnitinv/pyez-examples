from jnpr.junos import Device

with Device(host='xxxx', user='demo', password='demo123') as dev:
    print (dev.cli("show version", warning=False))
