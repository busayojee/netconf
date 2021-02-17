from acitoolkit.acitoolkit import *

url = 'https://sandboxapicdc.cisco.com'
user = 'admin'
pw = 'ciscopsdt'

session = Session(url,user,pw)
session.login()

# tenants = Tenant.get(session)
# for tenant in tenants:
#     print(tenant.name)
#     print(tenant.descr)
#     print('*'*30)
#     print(' ')

new_tenant = Tenant('Busayo')

anp = AppProfile('Busayo_app',new_tenant)
epg = EPG('Busayo_Epg', anp)

context = Context('I_created_this',new_tenant)
bridge_domain = BridgeDomain('switches',new_tenant)

bridge_domain.add_context(context)
epg.add_bd(bridge_domain)

# print(new_tenant.get_url())
# print(new_tenant.get_json())
#response = session.push_to_apic(new_tenant.get_url(), data = new_tenant.get_json())
#print(response)
tenants = Tenant.get(session)
for tenant in tenants:
    if tenant.name == 'Busayo':
        print(tenant.name)
    else:
        print(tenant.name)
        print(tenant.descr)
        print('*'*30)
        print(' ')
new_tenant.mark_as_deleted()
response = session.push_to_apic(new_tenant.get_url(), data = new_tenant.get_json())
