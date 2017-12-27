Prototag
========

.. image:: https://travis-ci.org/flxbe/prototag.svg?branch=master
    :target: https://travis-ci.org/flxbe/prototag

A simple CLI tool to filter and list ``.md`` files based on comment headers.

Motivation
----------

After testing multiple sophisticated tools to document small ideas or meetups,
I found plain ``.md`` files to work best for me. Until a project deserves its
own repository, I just create small protocols in a single, dedicated directory.
I have built this tool to help me search this directory via the terminal.

The cli tool ``ptag`` scans a given directory for ``.md`` files and tries to
extract a block comment at the start. If this comment includes valid ``yaml``,
the file is considered valid. One can specify selectors to filter these
valid files. The list of results is then printed to stdout.

Installation
------------

.. code-block:: bash

    pip install prototag

Synopsis
--------

Usage: ``ptag [options] [<dir>]``

-h, --help              
    Show help.
-v, --version           
    Show version.
-t <selector>, --tag <selector>
    Filter the files by tags by specifying a selector.
-a <selector>, --author <selector>
    Filter the files by their author by specifying a selector.

One can use logical AND and OR conditions to filter the found files with
valid headers. AND terms are combined using ',' and OR terms are
combined using ':'. OR terms are evaluated before AND terms. The OR
conditions are not exclusive.

Select all files, that have both tag1 and tag2.

.. code-block:: bash

    ptag -t tag1,tag2

Select all files, that have at least one of both tags.

.. code-block:: bash

    ptag -t tag1:tag2
    
Select all files, that have either tag1 and tag2 or tag3 or both.

.. code-block:: bash

    ptag -t tag1,tag2:tag3

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
following command would return the filename of the above created file.

.. code-block:: bash

    ptag -t idea,python -a jan ~/protocols

The directory is optional and defaults to the current working directory. This
is therefore equivalent to

.. code-block:: bash

    cd ~/protocols
    ptag -t idea,python -a jan

Roadmap
-------
- Add a ``date`` field.
- Add command to list all tags and authors.
- Add command to create new protocols.
- Add command to list files with invalid headers including debug messages.
