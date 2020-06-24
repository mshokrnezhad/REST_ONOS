from classes.controller import controller

ONOS = controller("ONOS", "172.17.0.5", "8181", "/onos/v1", "onos", "rocks")

#ONOS.get_all_apps()
#ONOS.get_activated_apps()
#ONOS.get_app_info_by_id(84)
#ONOS.get_app_info_by_name("org.onosproject.openflow")
#ONOS.activate_app_by_name("org.onosproject.fwd")
#ONOS.deactivate_app_by_name("org.onosproject.fwd")
#ONOS.activate_app_by_id(262)
#ONOS.deactivate_app_by_id(262)
#ONOS.get_all_devices()
#ONOS.get_all_hosts()
#ONOS.get_all_links()