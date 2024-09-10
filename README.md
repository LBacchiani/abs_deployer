# TIMED SMART DEPLOYER
Timed Smart Deployer is a tool to automatically generate the ABS timed deployment code based on a declarative
specification.

A description of the old version of the functionalities of the tool is available at
[here](http://heim.ifi.uio.no/~jacopom/publication/dblpconf__esocc__gouwmnz16/).

## Prerequsites

Timed Smart Delployer requires a zephyrus2 running container. To install it please run the
following commands.

```
sudo docker pull lorenzobacchiani/my_zephyrus2
sudo docker run -d -p <PORT>:9001 lorenzobacchiani/my_zephyrus2
```

## Running Timed Smart Deployer

To interact with Smart Deployer,pplease run the
following command, passing as parameter <PORT> (the PORT exposed by the zephyrus2 container) and the ABS file containing 
the declarative specifications.

`python abs_deployer.py`

## Limitations

The input file needs to be a abs program that can be parsed, following the ABS grammar.

SmartDeployCost classes (i.e., the classes that are referred using a SmartDeployCost annotation)
and all their interfaces (including the extended ones) need to be defined in the file.
These classes and interfaces need to have a simple name, i.e., the notation module_name.interface_name or 
module_name.class_name is not allowed.

SmartDeployCost classes can not have a add/remove method to add a reference to an object of interface I if they have
parameters requiring an object or a list of objects of interface I.