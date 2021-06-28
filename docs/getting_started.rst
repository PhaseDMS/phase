Getting started
###############

Introduction
------------

Phase is a document management system specifically designed for the needs of engineering and construction projects to manage the documentation of oil & gas, water treatment, nuclear, solar and wind facilities.

Phase offers the following characteristics:

* Management of document and data lists containing thousands of items
* Management of multiple metadata related to engineering, review, schedule, etc.
* Spreadsheet like filtering/search capabilities
* Document and data versioning
* Management of relationships between documents and data

Phase is intended to be used on projects where:

* Thousands of documents are generated
* Documents have to be produced, exchanged, reviewed, revised and used all along the project phases by multiple parties (owner/operator, contractors, vendors, partners, authorities, etc.)


Installation
------------

We provide an Ansible recipe that can be used for both production server and
local development machine provisioning.

Check the `deployment` doc to see how to properly use the Ansible script.

We also provide a script helper to create a local development machine using
LXC.

    git clone https://github.com/PhaseDMS/phase.git
    cd phase/deployment
    ./local_vm_creation.sh

Contributing
------------

To make Phase work on a local environment, you must have the following
processes running:

 * Phase (django runserver)
 * Celery (run locally with *DJANGO_SETTINGS_MODULE=core.settings.local celery -A
   core.celery worker -l info*)
 * RabbitMQ
 * Postgres
 * Elasticsearch
 * Memcached


Available fabric commands
-------------------------

A fabric script is available to run custom commands. Check `fabfile.py` to have
an up to date list.
