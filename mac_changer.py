#!/usr/bin/env python
import optparse
import subprocess
import re


def get_arguments():
    parser = optparse.OptionParser()
    parser.add_option("-i", "--interface", dest="interface", help="Interface to change its MAC address")
    parser.add_option("-m", "--mac", dest="new_mac", help="New MAC address")
    (options,arguments)= parser.parse_args()
    if not options.interface:
        parser.error("[-] please specift an interface for more use take help of --help")
        #code to handle error
    elif not options.new_mac:
        parser.error("[-] please specify an mac address for more use take help of --help")
        #code to handle error
    return options
def change_mac(interface,new_mac):
    print("[+] changing MAC address for " + interface + " to " + new_mac)
    subprocess.call(["ifconfig", interface, "down"])
    subprocess.call(["ifconfig", interface, "down"])
    subprocess.call(["ifconfig", interface, "hw", "ether", new_mac])
    subprocess.call(["ifconfig", interface, "up"])

def get_current_mac(interface):
    ifconfig_result = subprocess.check_output(["ifconfig",interface])
    mac_address_search_result = re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w", ifconfig_result)
    if mac_address_search_result:
        return mac_address_search_result.group(0)
    else:
        print("[-] Could not read MAC address")
def running():
    options=get_arguments()
    current_mac = get_current_mac(options.interface)
    if current_mac is not None:
        print("Current MAC= "+current_mac)
    change_mac(options.interface,options.new_mac)
    changed_mac=get_current_mac(options.interface)
    if changed_mac is not None:
        print("Changed MAC= "+changed_mac)
running()



