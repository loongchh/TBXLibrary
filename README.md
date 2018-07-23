tbx2dict
--------

This script reads a TermBase eXchange (TBX) to a multi-lingual Python
dictionary. By specifying a XML file in the TBX format, the function obtains:

- **entry**: A list of term entries in the specified source language.

- **ent_dict**: A nested dictionary of term entries in the given list of target
languages. Specifically,

    `ent_dict['language']['source_term']` produces the entry in the particular
language translation given the source term (in the source language).

Notably, the `ent_dict` only includes terms of which there is entry in the
source langauge.

I wrote and published this simple script since I wasn't able to find Python
packages dealing with TBX formats on GitHub.
