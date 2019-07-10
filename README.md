# icedbroccoli.5th.ch

My very own first sparql endpoint. It is contains the dataset broccoli with its subgraphs.

![depiction of my sparql endpoint](/sparql_endpoint.jpg?raw=true)
![the dataset broccoli -> icedbroccoli.5th.ch/broccoli](/broccoli_dataset.jpg?raw=true)

The dataset */broccoli* contains all sorts of data about me. Here some sample queries:
 - [list of doap:Projects with description][1]
 - [list of subgraphs and triple count][2]

This repository contains the scripts and Dockerfiles to build it and to sponge all the data from all around into the named subgraphs.


[1]:http://icedbroccoli.5th.ch/dataset.html?tab=query&ds=/broccoli&query=prefix%20doap%3A%20%3Chttp%3A%2F%2Fusefulinc.com%2Fns%2Fdoap%23%3E%0A%0ASELECT%20%3Fproject%20%3Fdescription%0AWHERE%20%7B%0A%20%20%3Fproject%20a%20doap%3AProject%20.%20%0A%20%20%3Fproject%20doap%3Adescription%20%3Fdescription%20.%20%0A%7D

[2]:http://icedbroccoli.5th.ch/dataset.html?tab=query&ds=/broccoli&query=prefix%20doap%3A%20%3Chttp%3A%2F%2Fusefulinc.com%2Fns%2Fdoap%23%3E%0A%0ASELECT%20%3Fgraph%20%28count%28%3Fs%29%20as%20%3Fcount%29%0AWHERE%20%7B%20GRAPH%20%3Fgraph%20%7B%20%3Fs%20%3Fp%20%3Fo%20%7D%7D%0AGROUP%20BY%20%3Fgraph


