from classes.controller import controller

ONOS = controller("ONOS", "172.17.0.7", "8181", "/onos/v1", "onos", "rocks")

# ONOS.get_all_apps()
# ONOS.get_activated_apps()
# ONOS.get_app_info_by_id(84)
# ONOS.get_app_info_by_name("org.onosproject.openflow")
# ONOS.activate_app_by_name("org.onosproject.fwd")
# ONOS.deactivate_app_by_name("org.onosproject.fwd")
# ONOS.activate_app_by_id(262)
# ONOS.deactivate_app_by_id(262)
# ONOS.get_all_links()
# ONOS.show_topology()
# ONOS.add_host_to_host_intent("00:00:00:00:00:02/None", "00:00:00:00:00:14/None")
# ONOS.get_all_intents()
# ONOS.remove_intent("0x6")