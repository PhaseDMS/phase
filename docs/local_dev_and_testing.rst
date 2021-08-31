Development and test
####################

Installation
------------

Check the `deployment` doc to see how to properly install Phase on a local
machine.

Note: the `deployment` directory holds a `local_vm_creation.sh` script that
can be used to create an empty LXC virtual machine, ready to be provisioned
by the ansible playbook.

Configuration
-------------
You might need to override some local or test settings. You can create either a `local_private.py` or `test_private.py`
and add you own settings.  These files will be gitignored.
