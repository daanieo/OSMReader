# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import xml.dom.minidom as md

import matplotlib.pyplot as plt 

doc = md.parse("/home/daan/Downloads/map(4).osm")

# Respectively filter all Nodes and Ways (OSM vocabulary)
nodes = doc.getElementsByTagName("node")
ways = doc.getElementsByTagName("way")

# Empty dictionary to store the roads 
roads_dict = {}


# Loop through the "ways" to filter those labelled "highway"
for way in ways:
    
    tags = way.getElementsByTagName("tag")
    
    for tag in tags:
        if (tag.getAttribute("k") == "highway" ):
            roads_dict[way.getAttribute("id")] = way
            print("road added")
    
    

# # Print the names of streets in the XML file
# for i in roads_dict:
    
#     for j in roads_dict[i].getElementsByTagName("tag"):
#         if j.getAttribute("k") == "name":
#             print(j.getAttribute("v"))    


# Loop through dictionary & plot every road (NOTE: osm and real naming are asynchronous)
for index in roads_dict: 
    lons = list()
    lats = list()

    road = roads_dict[index]
    
    for nd in road.getElementsByTagName("nd"):
        
        refnr = nd.getAttribute("ref")
        
        for node in nodes:
            if (node.getAttribute("id") == refnr):
                lons.append(float(node.getAttribute("lon")))
                lats.append(float(node.getAttribute("lat")))
                
    plt.plot(lons,lats)
              
        
