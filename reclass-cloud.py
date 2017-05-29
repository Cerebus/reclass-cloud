#!/usr/bin/env python

import sys, ruamel.yaml

class Inventory:
# Inventory runs will have a nodes key.  applications and classes keys are inventory metadata
# but are not present in node data.
    def __init__(self, data): 
        # Valid reclass run will have __reclass__ key.
        if "__reclass__" not in data:
            raise KeyError("Input not a valid reclass structure")
        # Load reclass data.  Node output has no nodes key.
        if "nodes" in data:
            self.metadata = {key:data[key] for key in ('applications', 'classes') if key in data}
            # Inventory output can have more than one node
            self.nodes = {key:data['nodes'][key] for key in data['nodes']}
        else:
            # Node output has no inventory metadata and only ever has one node.
            self.metadata = None
            self.nodes = {data['__reclass__']['name']:data}    
    def cloud_config(self):
        def convert(data):
            # Get cloud-config key
            # Dump to string
            # Add #cloud-config header
            return "#cloud-config\n" + ruamel.yaml.safe_dump(data['parameters']['cloud-config'], indent=4, block_seq_indent=2, default_flow_style=False)
        # Munge node data into cloud-config format
        return {key:convert(self.nodes[key]) for key in self.nodes}


if __name__ == "__main__":
    # Ingest yaml from stdin
    inventory = Inventory(ruamel.yaml.safe_load(sys.stdin))
    # Loop over cloud-config data and print files
    configs = inventory.cloud_config()
    for k, v in configs.items():
        print(k)
        print(v)
        