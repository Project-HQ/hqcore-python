import argparse
import json
import requests
from pprint import pprint

class HQCore():
    HQCORE_URL = "http://127.0.0.1:8080"
    
    headers = {
     'Content-Type': 'application/json'
    }

    def add_log(self,device_id, int_data=None, str_data=None, float_data=None,json_data=None, is_file=None):
        log= {}
        log["device_id"]=device_id
        if int_data:
            log["int_data"] = int_data
        if str_data:
            log["str_data"] = str_data
        if float_data:
            log["float_data"] = float_data
        if json_data:
            log["json_data"] = json_data
        if is_file is not None:
            log["is_file"] = is_file

        response= requests.request("POST",self.HQCORE_URL+"/logs", headers=self.headers, json=log)
        return response.json()
         
    def add_device(self, name, owner, description=""):
        device = {
            "name": name,
            "description": description,
            "owner": owner
        }
        response= requests.request("POST",f"{self.HQCORE_URL}/devices", headers=self.headers, json=device)
        return response.json()

    def update_device(self,device, device_id=None):
        if(device_id is None):
            device_id= device["id"]

        response= requests.request("PATCH",f"{self.HQCORE_URL}/device/{device_id}", headers=self.headers, json=device)
        return response.json()

    def update_log(self, log, log_id=None):
        if(log_id is None):
            log_id= device["id"]

        response= requests.request("PATCH",f"{self.HQCORE_URL}/log/{log_id}", headers=self.headers, json=log)
        return response.json()

    def update_cluster(self, cluster, cluster_id=None):
        if(cluster_id is None):
            cluster_id= cluster["id"]

        response= requests.request("PATCH",f"{self.HQCORE_URL}/cluster/{cluster_id}", headers=self.headers, json=cluster)
        return response.json()

    def add_cluster(self, name, description=""):
        device = {
            "name": name,
            "description": description
        }
        response= requests.request("POST",self.HQCORE_URL+"/clusters", headers=self.headers, json=device)
        return response.json()

    def get_clusters(self):
        response= requests.request("GET",self.HQCORE_URL+"/clusters", headers=self.headers)
        return response.json()

    def get_devices(self):
        response= requests.request("GET",self.HQCORE_URL+"/devices", headers=self.headers)
        return response.json()
        
    def get_cluster_by_id(self,cluster_id):
        response= requests.request("GET",self.HQCORE_URL+"/cluster/"+cluster_id, headers=self.headers)
        return response.json()

    def get_device_by_id(self,device_id):
        response= requests.request("GET",self.HQCORE_URL+"/device/"+device_id, headers=self.headers)
        return response.json()

    def get_log_by_id(self,log_id):
        response= requests.request("GET",self.HQCORE_URL+"/log/"+log_id, headers=self.headers)
        return response.json()

    def assign_device_to_cluster(self,device_id, cluster_id):
        response= requests.request("GET",f"{self.HQCORE_URL}/cluster/{cluster_id}/assign/{device_id}", headers=self.headers)
        return response.json()

    def remove_device_from_cluster(self,device_id, cluster_id):
        response= requests.request("GET",f"{self.HQCORE_URL}/cluster/{cluster_id}/remove/{device_id}", headers=self.headers)
        return response.json()

    def delete_device_by_id(self,device_id):
        response= requests.request("DELETE", self.HQCORE_URL+"/device/"+device_id, headers=self.headers)
        return response.json()

    def delete_cluster_by_id(self,cluster_id):
        response= requests.request("DELETE", self.HQCORE_URL+"/cluster/"+cluster_id, headers=self.headers)
        return response.json()
    
    def delete_log_by_id(log_id):
        response= requests.request("DELETE", self.HQCORE_URL+"/log/"+log_id, headers=self.headers)
        return response.json()


def _parse_args(parser):
    """Define cli arguments for hqcore wrapper
    """
    parser.add_argument('-v',"--verbose", help="increase verbosity", action="store_true")
    parser.add_argument('-d',"--device", help="flush scheduled tasks", action="store_true")


def main():
    art="""          HQ Core API CLI Tool
    """
    print(art)
    parser = argparse.ArgumentParser()
    _parse_args(parser)
    args= parser.parse_args()

    hq = HQCore()

    print("List Devices...")
    res = hq.get_devices()
    pprint(res)
   
    print("Adding device...")
    res= hq.add_device("Twitter Scraper", "Adam Musciano","description is here")
    device_id= res["id"]
    pprint(res)
    
    print("Adding cluster...")
    res= hq.add_cluster("Tweets Analysis","description is here")
    cluster_id= res["id"]
    pprint(res)
    
    print("Adding log...")
    res= hq.add_log(device_id,str_data="testing")
    pprint(res)
    

if __name__ == "__main__":
    main()