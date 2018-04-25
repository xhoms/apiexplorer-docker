=====================
API Explorer - Docker
=====================

Dockerized sample application for the Palo Alto Networks Application Framework.

* Free software: ISC license

-----

|travis|

-----

Getting Started
---------------
First, ensure Docker_ is installed and running version 17.09.0 or greater.
If you are using Docker for Mac_ or Windows_, `Docker Compose`__ should already
be installed. If you're on Linux, you may need to install `docker-compose`
using `pip`. Ensure you are running version 1.17.0-rc1 or greater.

* Compose file version: 3.4

Build:

    $ docker-compose build

Run:

    $ docker-compose up

Daemon Mode:

    $ docker-compose up -d

Scale:

    $ docker-compose up -d --scale apiexplorer=4

    or (if already running in daemon mode)

    $ docker-compose scale apiexplorer=4

Features
--------

- Docker composition layered with API Explorer and NGiNX containers.
- Automatic DNS load-balancing when scaling.

CI/CD
-----

- Automatic `build`, `test` and `push` to docker hub.

Status
------

`API Explorer - Docker` is considered **alpha** at this time.

Contributors
------------

- Steven Serrata - `github <https://github.com/sserrata>`__
- Francesco Vigo - `github <https://github.com/fvigo>`__

.. |travis| image:: https://img.shields.io/travis/PaloAltoNetworks/apiexplorer-docker.svg
        :target: https://travis-ci.org/PaloAltoNetworks/apiexplorer-docker


.. _Docker: https://www.docker.com/what-docker
.. _Mac: https://www.docker.com/docker-mac
.. _Windows: https://www.docker.com/docker-windows
.. _Docker_Compose: https://docs.docker.com/compose/
__ Docker_Compose_

