from jnpr.junos.factory.factory_loader import FactoryLoader
import yaml

# from existing table/view
from jnpr.junos.op.routes import RouteTable

tbls = RouteTable(path='/var/tmp/get-route-information.xml')
tbls.get()
for item in tbls:
    print 'protocol:', item.protocol
    print 'age:', item.age
    print 'via:', item.via


# From user defined table/view
yaml_data="""
---
RemoteVxlanTable:
  rpc: get-ethernet-switching-vxlan-rvtep-info
  item: vxlan-source-vtep-information/vxlan-remote-vtep-information
  key: remote-vtep-address
  view: RemoteVxlanView

RemoteVxlanView:
  groups:
    vnis: vxlan-dynamic-information
  fields_vnis:
    vni: vxlan-format/vn-id

"""

globals().update(FactoryLoader().load(yaml.load(yaml_data)))
rvxlans = RemoteVxlanTable(path='/var/tmp/show_ethernet-switching_vxlan-tunnel-end-point_remote.xml')
rvxlans.get()
for rvxlan in rvxlans:
    print rvxlan.vni
