import requests
import json
from .color import color
import re
from .device import device
from .host import host
import matplotlib.pyplot as plt
import networkx as nx


class controller:

    def __init__(self, name, ip, port, base, username, password):
        self.name = name
        self.ip = ip
        self.port = port
        self.base = base
        self.username = username
        self.password = password

    def send(self, method, url, query, data, authentication):

        response = requests.request(method=method, url=url, params=query, data=data, auth=authentication)

        return (response.status_code, response.text)

    def is_successful(self, response_code, scenario):

        if scenario == "Get Info":
            if response_code == 200:
                return True
            else:
                return False
        elif scenario == "Activation":
            if response_code == 200:
                return True
            else:
                return False
        elif scenario == "Deactivation":
            if response_code == 204:
                return True
            else:
                return False

        elif scenario == "Intent Creation":
            if response_code == 201:
                return True
            else:
                return False

    def get_all_apps(self):

        path = "/applications"
        url = "http://" + self.ip + ":" + self.port + self.base + path
        query = None
        data = None
        authentication = (self.username, self.password)
        response = self.send("GET", url, query, data, authentication)

        if self.is_successful(response[0], "Get Info") == True:
            print(color.bold + color.ok_green + "Connection Established." + color.end_color)
            print("Following apps are currently " + color.ok_blue + "installed" + color.end_color + " on " +
                  color.underline + self.name + color.end_color)
            output = response[1]
            temp = json.loads(output)
            for app in temp['applications']:
                print("Id: " + str(app['id']) + ", Name: " + app['name'] + ", State: " + app['state'])
        else:
            print(color.fail + "Connection failed." + color.end_color)

    def get_activated_apps(self):

        path = "/applications"
        url = "http://" + self.ip + ":" + self.port + self.base + path
        query = None
        data = None
        authentication = (self.username, self.password)
        response = self.send("GET", url, query, data, authentication)

        if self.is_successful(response[0], "Get Info") == True:
            print(color.bold + color.ok_green + "Connection Established." + color.end_color)
            print("Following apps are currently " + color.ok_blue + "activated" + color.end_color + " on " +
                  color.underline + self.name + color.end_color)
            output = response[1]
            temp = json.loads(output)
            for app in temp['applications']:
                if app['state'] == "ACTIVE":
                    print("Id: " + str(app['id']) + ", Name: " + app['name'])
        else:
            print(color.fail + "Connection failed." + color.end_color)

    def get_app_info_by_id(self, id):

        path = "/applications"
        url = "http://" + self.ip + ":" + self.port + self.base + path
        query = None
        data = None
        authentication = (self.username, self.password)
        response = self.send("GET", url, query, data, authentication)

        if self.is_successful(response[0], "Get Info") == True:
            availability_flag = 0
            print(color.bold + color.ok_green + "Connection established." + color.end_color)
            output = response[1]
            temp = json.loads(output)
            for app in temp['applications']:
                if app['id'] == id:
                    availability_flag = 1
                    print("Id: " + str(app['id']) + ", Name: " + app['name'])
                    print("App description: " + app['readme'])
            if availability_flag == 0:
                print(color.fail + "Requested ID is not available " + " on " +
                      color.underline + self.name + color.end_color)
        else:
            print(color.fail + "Connection failed." + color.end_color)

    def get_app_info_by_name(self, name):

        path = "/applications"
        url = "http://" + self.ip + ":" + self.port + self.base + path
        query = None
        data = None
        authentication = (self.username, self.password)
        response = self.send("GET", url, query, data, authentication)

        if self.is_successful(response[0], "Get Info") == True:
            availability_flag = 0
            print(color.bold + color.ok_green + "Connection established." + color.end_color)
            output = response[1]
            temp = json.loads(output)
            for app in temp['applications']:
                if app['name'] == str(name):
                    availability_flag = 1
                    print("Id: " + str(app['id']) + ", Name: " + app['name'])
                    print("App description: " + app['readme'])
            if availability_flag == 0:
                print(color.fail + "Requested name is not available " + " on " +
                      color.underline + self.name + color.end_color)
        else:
            print(color.fail + "Connection failed." + color.end_color)

    def activate_app_by_name(self, name):

        path = "/applications" + "/" + str(name) + "/active"
        url = "http://" + self.ip + ":" + self.port + self.base + path
        query = None
        data = None
        authentication = (self.username, self.password)
        response = self.send("POST", url, query, data, authentication)

        if self.is_successful(response[0], "Activation") == True:
            print(color.bold + color.ok_green + "Connection established." + color.end_color)
            output = response[1]
            temp = json.loads(output)
            if temp['state'] == "ACTIVE":
                print(color.underline + temp['name'] + color.end_color + " is activated on " +
                      color.underline + self.name + color.end_color)
            else:
                print(color.fail + "Activation failed." + color.end_color)
        else:
            print(color.fail + "Connection failed." + color.end_color)

    def deactivate_app_by_name(self, name):

        path = "/applications" + "/" + name + "/active"
        url = "http://" + self.ip + ":" + self.port + self.base + path
        query = None
        data = None
        authentication = (self.username, self.password)
        response = self.send("DELETE", url, query, data, authentication)

        if self.is_successful(response[0], "Deactivation") == True:
            print(color.bold + color.ok_green + "Connection established." + color.end_color)
            print(color.underline + name + color.end_color + " is deactivated on " +
                  color.underline + self.name + color.end_color)
        else:
            print(color.fail + "Deactivation failed." + color.end_color)
            print(color.fail + "Connection failed." + color.end_color)

    def activate_app_by_id(self, id):

        name = None
        path = "/applications"
        url = "http://" + self.ip + ":" + self.port + self.base + path
        query = None
        data = None
        authentication = (self.username, self.password)
        response = self.send("GET", url, query, data, authentication)

        if self.is_successful(response[0], "Get Info") == True:
            availability_flag = 0
            output = response[1]
            temp = json.loads(output)
            for app in temp['applications']:
                if app['id'] == id:
                    name = app['name']

        path = "/applications" + "/" + str(name) + "/active"
        url = "http://" + self.ip + ":" + self.port + self.base + path
        response = self.send("POST", url, query, data, authentication)

        if self.is_successful(response[0], "Activation") == True:
            print(color.bold + color.ok_green + "Connection established." + color.end_color)
            output = response[1]
            temp = json.loads(output)
            if temp['state'] == "ACTIVE":
                print(color.underline + temp['name'] + " (ID: " + str(id) + ")" + color.end_color +
                      " is activated on " + color.underline + self.name + color.end_color)
            else:
                print(color.fail + "Activation failed." + color.end_color)
        else:
            print(color.fail + "Connection failed." + color.end_color)

    def deactivate_app_by_id(self, id):

        name = None
        path = "/applications"
        url = "http://" + self.ip + ":" + self.port + self.base + path
        query = None
        data = None
        authentication = (self.username, self.password)
        response = self.send("GET", url, query, data, authentication)

        if self.is_successful(response[0], "Get Info") == True:
            availability_flag = 0
            output = response[1]
            temp = json.loads(output)
            for app in temp['applications']:
                if app['id'] == id:
                    name = app['name']

        path = "/applications" + "/" + name + "/active"
        url = "http://" + self.ip + ":" + self.port + self.base + path
        query = None
        data = None
        authentication = (self.username, self.password)
        response = self.send("DELETE", url, query, data, authentication)

        if self.is_successful(response[0], "Deactivation") == True:
            print(color.bold + color.ok_green + "Connection established." + color.end_color)
            print(color.underline + name + " (ID: " + str(id) + ")" + color.end_color + " is deactivated on " +
                  color.underline + self.name + color.end_color)
        else:
            print(color.fail + "Deactivation failed." + color.end_color)
            print(color.fail + "Connection failed." + color.end_color)

    def get_all_devices(self):

        path = "/devices"
        url = "http://" + self.ip + ":" + self.port + self.base + path
        query = None
        data = None
        authentication = (self.username, self.password)
        response = self.send("GET", url, query, data, authentication)

        if self.is_successful(response[0], "Get Info") == True:
            # print(color.bold + color.ok_green + "Connection Established." + color.end_color)
            # print("Following devices are currently connected to " + color.underline + self.name + color.end_color)
            output = response[1]
            temp = json.loads(output)
            device_index = 0
            devices = []
            for d in temp['devices']:
                # print("Id: " + str(d['id']) + ", Name: " + d['annotations']['name'] + ", Hardware Type: " + d['hw'])
                device_obj = device(device_index, re.sub("of:000000000000000", "SW_", d['id']),
                                    d['annotations']['name'], d['hw'], [])
                # device_obj = device(device_index, d['id'], d['annotations']['name'], d['hw'], [])
                devices.append(device_obj)
                device_index += 1
        else:
            print(color.fail + "here Is No Connection to Get the List of Devices." + color.end_color)

        path = "/links"
        url = "http://" + self.ip + ":" + self.port + self.base + path
        query = None
        data = None
        authentication = (self.username, self.password)
        response = self.send("GET", url, query, data, authentication)

        if self.is_successful(response[0], "Get Info") == True:
            # print(color.bold + color.ok_green + "Connection Established." + color.end_color)
            # print("Following links are currently connected in the network.")
            output = response[1]
            temp = json.loads(output)
            for l in temp['links']:
                for device_obj in devices:
                    if re.sub("of:000000000000000", "SW_", device_obj.get_id()) == re.sub("of:000000000000000", "SW_",
                                                                                          str(l['src']['device'])):
                        device_obj.add_connection(re.sub("of:000000000000000", "SW_", str(l['dst']['device'])))
        else:
            print(color.fail + "here Is No Connection to Get the List of Links." + color.end_color)

        return (devices, len(devices))

    def get_all_hosts(self):

        path = "/hosts"
        url = "http://" + self.ip + ":" + self.port + self.base + path
        query = None
        data = None
        authentication = (self.username, self.password)
        response = self.send("GET", url, query, data, authentication)

        if self.is_successful(response[0], "Get Info") == True:
            # print(color.bold + color.ok_green + "Connection Established." + color.end_color)
            # print("Following hosts are currently active in the network.")
            output = response[1]
            temp = json.loads(output)
            host_index = 0
            hosts = []
            for h in temp['hosts']:
                # print("Id: " + re.sub("/None", '', str(h['id'])) + ", IP: " + re.sub("[][']", '', str(h['ipAddresses'])) +
                #      ", Connected to: " + h['locations'][0]['elementId'])
                host_obj = host(host_index, re.sub("00:00:00:00:00:", "H_", re.sub("/None", "", h['id'])),
                                re.sub("[][']", '', str(h['ipAddresses'])), [])
                host_obj.add_connection(re.sub("of:000000000000000", "SW_", str(h['locations'][0]['elementId'])))
                hosts.append(host_obj)
                host_index += 1
        else:
            print(color.fail + "There Is No Connection to Get the List of Hosts." + color.end_color)

        return (hosts, len(hosts))

    def get_all_links(self):

        path = "/links"
        url = "http://" + self.ip + ":" + self.port + self.base + path
        query = None
        data = None
        authentication = (self.username, self.password)
        response = self.send("GET", url, query, data, authentication)

        if self.is_successful(response[0], "Get Info") == True:
            print(color.bold + color.ok_green + "Connection Established." + color.end_color)
            print("Following links are currently connected in the network.")
            output = response[1]
            temp = json.loads(output)
            for link in temp['links']:
                print("Source: " + str(link['src']['device']) + ", Destination: " + str(link['dst']['device']) + ".")
        else:
            print(color.fail + "Connection failed." + color.end_color)

    def show_topology(self):

        (devices, number_of_devices) = self.get_all_devices()
        (hosts, number_of_hosts) = self.get_all_hosts()

        G = nx.Graph()

        for device_obj1 in devices:
            device_obj1_id = device_obj1.get_id()
            for con in device_obj1.get_connections():
                for device_obj2 in devices:
                    device_obj2_id = device_obj2.get_id()
                    if con == device_obj2_id:
                        # G.add_edge(re.sub("of:000000000000000", '', str(device_obj1_id)),
                        re.sub("of:000000000000000", "", str(device_obj2_id))
                        G.add_edge(device_obj1_id, device_obj2_id)

        for host_obj in hosts:
            host_obj_id = host_obj.get_id()
            for con in host_obj.get_connections():
                for device_obj in devices:
                    device_obj_id = device_obj.get_id()
                    if con == device_obj_id:
                        # G.add_edge(re.sub("of:000000000000000", '', str(device_obj1_id)),
                        re.sub("of:000000000000000", '', str(device_obj2_id))
                        G.add_edge(host_obj_id, device_obj_id)

        pos = nx.spring_layout(G)
        nx.draw(G, pos, font_size=10, with_labels=False)
        for p in pos:  # raise text positions
            pos[p][1] += 0.1
        nx.draw_networkx_labels(G, pos)
        plt.show()

    def add_host_to_host_intent(self, host_id_1, host_id_2):

        appId = "org.onosproject.cli"
        intentJson = {"two": str(host_id_2), "selector": {"criteria": []}, "priority": 7, "treatment":
            {"deferred": [], "instructions": []}, "appId": appId, "one": str(host_id_1), "type": "HostToHostIntent",
                      "constraints": [{"type": "LinkTypeConstraint", "types": ["OPTICAL"], "inclusive": 'false'}]}

        path = "/intents"
        url = "http://" + self.ip + ":" + self.port + self.base + path
        query = None
        data = json.dumps(intentJson)
        authentication = (self.username, self.password)
        response = self.send("POST", url, query, data, authentication)
        if self.is_successful(response[0], "Intent Creation") == True:
            print(color.bold + color.ok_green + "Connection Established." + color.end_color)
            print("An intent is successfully created between " + str(host_id_1) + " and " + str(host_id_2) + ".")

    def get_all_intents(self):

        path = "/intents"
        url = "http://" + self.ip + ":" + self.port + self.base + path
        query = None
        data = None
        authentication = (self.username, self.password)
        response = self.send("GET", url, query, data, authentication)

        if self.is_successful(response[0], "Get Info") == True:
            # print(color.bold + color.ok_green + "Connection Established." + color.end_color)
            # print("Following hosts are currently active in the network.")
            output = response[1]
            intent_index = 0
            temp = json.loads(output)
            for i in temp['intents']:
                print("Intent " + str(intent_index+1) + " - Key: " + i['key'] + ", ID: " + i['id'] + ", State: " +
                      i['state'] + ", Type: " + i['type'] + ", Source: " +
                      re.sub("00:00:00:00:00:", "H_", re.sub("/None", "", i['resources'][0])) +
                      ", Destination: " +
                      re.sub("00:00:00:00:00:", "H_",re.sub("/None", "", i['resources'][1])))
                intent_index += 1
        else:
            print(color.fail + "There Is No Connection to Get the List of Hosts." + color.end_color)

    def remove_intent(self, intent_id):

        appId = "org.onosproject.cli"
        path = "/intents" + "/" + str(appId) + "/" + str(int(intent_id, 16))
        url = "http://" + self.ip + ":" + self.port + self.base + path
        query = None
        data = None
        authentication = (self.username, self.password)

        response = self.send("DELETE", url, query, data, authentication)
        if self.is_successful(response[0], "Deactivation") == True:
            print(color.bold + color.ok_green + "Connection Established." + color.end_color)
            print("Intent " + str(intent_id) + " is successfully deleted.")