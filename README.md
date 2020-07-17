# hqcore-python

Python wrapper over the HQ Core REST API. Useful for testing.

```python
    from hqcore import HQCore
    
    hq = HQCore(host="127.0.0.1",port=8080)

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
    
```
