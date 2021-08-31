Phase deployment
################

Phase is designed to be a lightweight alternative to traditional bloated and slow
DMS. Hence a Phase instance can be run on a single virtual machine.


Hosting Phase on a dedicated server
-----------------------------------

The recommanded settings is to install Phase on a dedicated machine (physical or virtual).

Once you have setup a new machine with ssh access (Debian stable is recommended), use
the Ansible playbook to easily deploy Phase.::

    git@github.com:PhaseDMS/phase.git
    cd phase
    ansible-playbook -i /etc/ansible/hosts deployment/site.yml -l client1.stage


Configuring Ansible
-------------------

Here is a working `/etc/ansible/hosts` file defining several environments::

    [local]
    phase.local

    [stage]
    client1.stage

    [prod]
    client1.prod

    [client1:children]
    stage
    prod

    [phase:children]
    client1


Note: `client1.stage` and `client1.prod` are entries in the `.ssh/config` file.


Ansible variables
-----------------

Some variables depends on the environment context, and can be defined in `group_vars` or `host_vars`
subdirectories.

Example in `/etc/ansible/group_vars/client1.yml`::

    document_apps:
      - { repo: "git@github.com:PhaseDMS/client1docs.git", name: "client1docs" }

Example in `/etc/ansible/host_vars/client1.prod.yml`::

    project_domain: phase.client1.com
    settings_file: client1_prod_private.py
