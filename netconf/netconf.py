from ncclient import manager
import xml.dom.minidom
from pprint import pprint
import xmltodict
from router_info import router
from router2 import router2
#Yang Datamodel for requesting data from the router
netconf_filter =open("/Users/mac/Documents/Devnet/netconf/netconf_filter.xml").read()

#To connect with the router
with manager.connect(host=router["host"],port=router["port"],username=router["username"],password=router["password"],hostkey_verify=False) as m:
    
    
    #To check through all the possible comments 
    
   # for capability in m.server_capabilities:
       # print("*" * 50)
       # print(capability)
   # print("connected")

#used to get the datamodel that was already given to it
    interfaces_netconf = m.get(netconf_filter)
   # print("interfaces_netconf")

   # Used to get the datamodel in a ordered xml format
   # xmlDom = xml.dom.minidom.parseString(str(interfaces_netconf))
   # print (xmlDom.toprettyxml(indent=" "))
   # print("*" * 25 + "break" + "*" * 50)

    print("getting running config")

   #Using xml to dict to convert xml output to a python dictionary
    interface_python = xmltodict.parse(interfaces_netconf.xml)['rpc-reply']['data']
    pprint(interface_python)

    #To get the name of the interface
    name = interface_python['interfaces']['interface']['name']['#text']
    print(name)

    #To get the description/configuration and state of the device 
    config = interface_python['interfaces']['interface']
    op_state = interface_python['interfaces-state']['interface']

    print('start')
    print(f'Description: {config["description"]}')
    print(f'packetsIn: {op_state["statistics"]["in-unicast-pkts"]}')






   