from classes.controller import controller
from classes.device import device
import matplotlib.pyplot as plt
import networkx as nx
import re

ONOS = controller("ONOS", "172.17.0.5", "8181", "/onos/v1", "onos", "rocks")

#ONOS.get_all_apps()
#ONOS.get_activated_apps()
#ONOS.get_app_info_by_id(84)
#ONOS.get_app_info_by_name("org.onosproject.openflow")
#ONOS.activate_app_by_name("org.onosproject.fwd")
#ONOS.deactivate_app_by_name("org.onosproject.fwd")
#ONOS.activate_app_by_id(262)
#ONOS.deactivate_app_by_id(262)
#(devices,number_of_devices) = ONOS.get_all_devices()
#print("\n\n\n" + str(number_of_devices) + "\n\n\n")
#(hosts,number_of_hosts) = ONOS.get_all_hosts()
#print("\n\n\n" + str(number_of_hosts) + "\n\n\n")
#ONOS.get_all_links()

# G = nx.Graph()
#
# for device_obj1 in devices:
# 	device_obj1_id = device_obj1.get_id()
# 	for con in device_obj1.get_connections():
# 		for device_obj2 in devices:
# 			device_obj2_id = device_obj2.get_id()
# 			if con == device_obj2_id:
# 				#G.add_edge(re.sub("of:000000000000000", '', str(device_obj1_id)),
# 				re.sub("of:000000000000000", '', str(device_obj2_id)))
# 				G.add_edge(device_obj1_id, device_obj2_id)
#
# for host_obj in hosts:
# 	host_obj_id = host_obj.get_id()
# 	for con in host_obj.get_connections():
# 		for device_obj in devices:
# 			device_obj_id = device_obj.get_id()
# 			if con == device_obj_id:
# 				#G.add_edge(re.sub("of:000000000000000", '', str(device_obj1_id)),
# 				re.sub("of:000000000000000", '', str(device_obj2_id)))
# 				G.add_edge(host_obj_id, device_obj_id)
#
# pos = nx.spring_layout(G)
# nx.draw(G, pos, font_size=10, with_labels=False)
# for p in pos:  # raise text positions
#     pos[p][1] += 0.1
# nx.draw_networkx_labels(G, pos)
# plt.show()



