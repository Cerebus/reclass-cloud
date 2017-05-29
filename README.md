# reclass-cloud
Script to generate cloud-config user data from a reclass model.  

[Immutable infrastructure](https://blog.codeship.com/immutable-deployments/) is an important 
advance in managing IT infrastructure, but it's incompatible with traditional configuration management 
tools because they allow deployed systems to be modified in place.  However, without a CM
platform how do you automate the deployment of systems and applications?  Containers are an answer, 
but not every organization or application is ready to containerize.

[cloud-init](https://cloud-init.io) is a relatively broadly supported tool for instantiating systems
in public and private cloud providers, and can even be used for servers on metal with the right 
provisioning environment.  cloud-init modules can manage most aspects of system and application
deployment, and has predictable and repeatable results.  cloud-init user-data is written in YAML.

Managing lots of YAML files for systems in various versions would be ugly, though.

Enter [reclass](https://github.com/madduck/reclass).  reclass is a tool for defining system configuration data in a structured external repository that can be leveraged by a configuration maangement toolchain.  reclass models are written in YAML, and the reclass engine handles finding, merging, and resolving variable references between them.

Together, reclass and cloud-init can solve this problem.  reclass files can be written to merge and
generate cloud-config data, which can then be fed into system instantiation as normal.  Instances can be composed in test with access keys, and then recomposed in deployment without--making the instance fully immutable.

This script depends on specific conventions in your model.  