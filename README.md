---
description: Reads functional content from OpenStreetMap .xml files.
---

# OSMReader

Description can be found on GitBook: [https://app.gitbook.com/@daanieo-vanbeek/s/osm-reader/](https://app.gitbook.com/@daanieo-vanbeek/s/osm-reader/)



## How OpenStreetMap files are structured 

First of all, XML-files. These are structured by means of elements, named using tags, and their attributes. Elements are structured hierarcichally: so any element can, but does not do so per se, contain a sub-element. The tags \(i.e. names\) of any element is not XML, but application-specific. Hence, it depends on the application's API how to read this data. 

OSM uses elements of three types \(code blocks containing examples\): 

**Nodes** are exactly what their names imply; little dots on the map, defined by an id number a longitude/latitude. We need these because they contain the geographical information we're interested in. The node-element does not contain any information on what type of node it is \(ranging from part of a house to a bus stop\).  

```text
 <node id="860988477" visible="true" version="3" changeset="11237420" timestamp="2012-04-09T12:06:43Z" user="Mueko Team" uid="358330" lat="52.1969140" lon="4.9000872"/>
```

**Ways** are a set of nodes forming some kind of physical structure. Don't be misled by the element's tag; ways are not roads per se. The example below for example describes the geographical location of a house. The sub-elements by the name of "nd" contain the Attribute\(s\) "ref", which corresponds to the id-Attribute of the node in the example above. By means of the confusingly named sub-element "tag" additional information on some relevant structure can be added. Here, we know that the house has been built in 1965. 

```text
<way id="283942693" visible="true" version="1" changeset="22520862" timestamp="2014-05-24T10:03:14Z" user="Zugführer_BAG" uid="2078622">
  <nd ref="2877473768"/>
  <nd ref="2877473789"/>
  <nd ref="2877473701"/>
  <nd ref="2877473278"/>
  <nd ref="2877473768"/>
  <tag k="building" v="house"/>
  <tag k="ref:bag" v="736100000013884"/>
  <tag k="source" v="BAG"/>
  <tag k="source:date" v="2014-05-24"/>
  <tag k="start_date" v="1965"/>
 </way>
```

**Relations** are a way to give more information about a set of Ways; for example street names. In an OSM-file, we distinguish between a road that lead from one node to the other and the realistic naming of a street. One street can intersect multiple other streets, and still keep the same name. Such logic we can see being described below. Multiple Ways form one single cano route

```text
<relation id="9238920" visible="true" version="2" changeset="81592554" timestamp="2020-02-28T13:29:44Z" user="padvinder" uid="978786">
  <member type="way" ref="611310958" role=""/>
  <member type="way" ref="195557033" role=""/>
  <member type="way" ref="89503826" role=""/>
  <member type="way" ref="664919015" role=""/>
  <member type="way" ref="664919013" role=""/>
  <member type="way" ref="611310961" role=""/>
  <member type="way" ref="611310959" role=""/>
  <member type="way" ref="664919017" role=""/>
  <member type="way" ref="777016712" role=""/>
  <member type="way" ref="777016711" role=""/>
  <member type="way" ref="664919033" role=""/>
  <member type="way" ref="664919018" role=""/>
  <member type="way" ref="664919026" role=""/>
  <member type="way" ref="664919023" role=""/>
  <tag k="colour" v="red"/>
  <tag k="name" v="Kanoroute Gagel"/>
  <tag k="network" v="lpn"/>
  <tag k="osmc:symbol" v="blue:blue_frame:Gag:blue"/>
  <tag k="route" v="canoe"/>
  <tag k="symbol" v="blue text on white hexagonal sign"/>
  <tag k="type" v="route"/>
 </relation>
```

