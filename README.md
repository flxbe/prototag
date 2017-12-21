# Prototag

My preferred way of memorizing ideas I have is by just creating a short `.md` file.
I then use the naming convetion `JJJJ-MM-DD_name_with_underscores_for_spaces.md`.
I tried several other tools to organize my ideas, but this just works best for me.

However, as the amount of files increase, it gets difficult to easily scan for protocolls
that belong to a certain topic. Prototag solves this issue by extracting tags from a
header in my `.md` files. The files can be filtered using the `prototag` CLI.

## Example

```md
<!--
authors: 
  - flxbe
tags: 
  - idea
  - python
  - the-next-google
-->

# Heading

This will be the next big thing.
```

One can then filter any folder for files by tag.

```bash
ptototag -t "idea, python" -t "the-next-google"
```
