from ncclient import manager
from router_info import router

#Using the config.xml
config_template = open("/Users/mac/Documents/Devnet/netconf/config.xml").read()

#Formatting the template to change the configuration of the device 
netconf_config = config_template.format(
    interface_name = "GigabitEthernet2", interface_desc = "Network Interface"
)

with manager.connect(host = router["host"], port = router["port"], username = router["username"], password = router["password"], hostkey_verify = False) as m:

    #Using the editconfig to edit the device configuration
    device_reply = m.edit_config(netconf_config,target = "running") 
    print(device_reply) 