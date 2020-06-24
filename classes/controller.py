import requests

import json

from .color import color

import re





class controller:





    def __init__(self, name, ip, port, base, username, password):

        self.name = name

        self.ip = ip

        self.port = port

        self.base = base

        self.username = username

        self.password = password





    def send(self, method, url, query, data, authentication):



        response = requests.request(method = method, url = url, params = query, data = data, auth = authentication)



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

                print(color.fail + "Requested ID is not available "+ " on " +

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

                print(color.fail + "Requested name is not available "+ " on " +

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

                print(color.underline + temp['name'] + " (ID: "+ str(id) + ")" + color.end_color +

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

            print(color.underline + name + " (ID: "+ str(id) + ")" + color.end_color + " is deactivated on " +

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

            print(color.bold + color.ok_green + "Connection Established." + color.end_color)

            print("Following devices are currently connected to " + color.underline + self.name + color.end_color)

            output = response[1]

            temp = json.loads(output)

            for device in temp['devices']:

               print("Id: " + str(device['id']) + ", Name: " + device['annotations']['name'] + ", Hardware Type: " + device['hw'])

        else:

            print(color.fail + "Connection failed." + color.end_color)






    def get_all_hosts(self):

        path = "/hosts"

        url = "http://" + self.ip + ":" + self.port + self.base + path

        query = None

        data = None

        authentication = (self.username, self.password)

        response = self.send("GET", url, query, data, authentication)


        if self.is_successful(response[0], "Get Info") == True:

            print(color.bold + color.ok_green + "Connection Established." + color.end_color)

            print("Following hosts are currently active in the network.")

            output = response[1]

            temp = json.loads(output)

            for host in temp['hosts']:

               print("Id: " + re.sub("/None", '', str(host['id'])) + ", IP: " + re.sub("[][']", '', str(host['ipAddresses'])) + ", Connected to: " +

                     host['locations'][0]['elementId'])

        else:

            print(color.fail + "Connection failed." + color.end_color)





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
#3 more functions are added