Unit-test Plan
==============

Entity resolution:
------------------

    1. An entity can be resolved by its label, interface, or factory name
        a. Resolve by label
        a. Resolve by instance
        a. Resolve by factory
    1. No label needs to be specified if the interface is
    1. No interface needs to be specified
    1. No label or interface needed if factory is specified
    1. Two entities cannot be mapped to the same label
    1. Two entities can share the same interface or factory if they have unique labels

    1. Error cases

        a. Referenced factory top-level module doesn't exist
        a. Referenced factory final model doesn't exist
        a. Referenced factory class doesn't exist
        a. Error instantiating factory
        a. Error building factory
        a. Error instantiating action
        a. Error running action
        a. Singleton entities are not instantiated again, even though they failed
        a. Dynamically referenced entity property doesn't exist
        a. Dynamically referenced dependency doesn't exist

Singleton handling:
-------------------

    1. Only one instance of of an entity is created when marked singleton
    1. A new instance is created each time for resolve() if not marked singleton
    1. A dependency or reference that is itself singleton is only created once,
        even if the client is not singleton
    1. A dependency or reference won't be created twice, if the client is a singleton.
    1. Non-singleton dependencies always created
    1. Singleton dependencies not created twice
    1. Non-singleton parameter references always created
    1. Singleton parameter references not created twice

Entity binding:
---------------

    1. Only one instance of the entity is created for the client, even though entity
        is not a singleton
    1. Binding object is placed outside of a class object

Configuration:
--------------

    1. Load binding configuration from file
    1. Allow relative loading of additional files
    1. Filepath does not exist
    1. File is not YAML
    1. File is corrupted YAML
