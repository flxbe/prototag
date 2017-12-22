Prototag
========

A simple CLI tool to filter and list ``.md`` files based on comment headers.

Motivation
----------

After testing multiple sophisticated tools to document small ideas or meetups,
I found plain ``.md`` files and a flat directory structure to work best
for me. I have built this tool to help me search these protocols in the
terminal.

The cli tool ``ptag`` scans a given directory for ``.md`` files and tries to
extract a block comment at the start. If this comment includes valid ``yaml``,
the file is considered valid. One can specify selectors to further filter all
valid files. The list of results is then printed to stdout.

Example
-------

Consider the file ``~/protocols/example.md``:

.. code-block:: md

    <!--
    author: 
      - jan
      - olli
    tag: 
      - idea
      - python
    -->

    # Heading

    Some text.

One can filter the ``~/protocols`` directory using the cli tool ``ptag``. The
following command would return the above created filename.

.. code-block:: bash

    ptag -t idea,python -a jan ~/protocols

This is equivalent to

.. code-block:: bash

    cd ~/protocols
    ptag -t idea,python -a jan
