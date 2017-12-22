# Prototag

A simple CLI tool to filter and list `.md` files by comment headers.

## Motivation

After testing multiple sophisticated tools to document small ideas or
meetups, I found plain `.md` files and a flat directory structure to work best
for me. I built this tool to filter these protocols in the terminal.

Each `.md` file, that has a valid block comment at the start,
can be interpreted by this tool. By passing suitable selectors, the results
can be filtered.

## Example

`~/protocols/example.md`

```md
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
```

One can then filter any folder for files by tag.

```bash
ptag -t "idea,python" -a "jan" ~/protocols
```

This would create the output

```
example.md
```
