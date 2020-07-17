# hqcore-python

Python wrapper over the HQ Core REST API. Useful for testing.

```python
    from hqcore import HQCore
    
    hq = HQCore(host="127.0.0.1",port=8080)

    print("List Devices...")
    print(hq.get_devices())
   
    print("Adding device...")
    device= hq.add_device("device_name", "owner","description of the device")
    device_id= device["id"]
    
    print("Adding cluster...")
    cluster= hq.add_cluster("cluster_name","Description of the cluster")
    cluster_id= cluster["id"]
    
```
