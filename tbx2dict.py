# tbx2dict.py - Read TermBase eXchange files as Python multiligual dict

# Written in 2018 by Long-Huei Chen <longhuei@g.ecc.u-tokyo.ac.jp>

# To the extent possible under law, the author(s) have dedicated all copyright
# and related and neighboring rights to this software to the public domain
# worldwide. This software is distributed without any warranty.

# You should have received a copy of the CC0 Public Domain Dedication along
# with this software. If not, see <http://creativecommons.org/publicdomain/zero/1.0/>.

import xml.etree.ElementTree as ET
from collections import defaultdict
from pathlib import Path

# List of all languages in the term base
full_lang = [
    'bg', 'cs', 'da', 'de', 'el', 'en', 'es', 'et', 'fi', 'fr', 'ga', 'hr',
    'hu', 'it', 'la', 'lt', 'lv', 'mt', 'mul', 'nl', 'pl', 'pt', 'ro', 'sk',
    'sl', 'sv'
]


def tbx2dict(src_file, lang_list=full_lang, lang_src='en'):
    """ Read TermBase eXchange files as Python multiligual dict

    Arguments:
        lang_src: (str) source language of the dict. If the term entry does not
            exist in the source language, the entry is not included
        lang_list: (str) list of target language to be included
        src_file: (str) path to the TermBase eXchange data file

    Output:
        entry: (list) of term entries in the source language
        ent_dict: (dict) of multilingual dictionary pointing source language
            terms to another language. ent_dict[lang] is a dictionary of a
            particular language.
    """
    print('Reading TBX file...')
    tree = ET.parse(src_file)

    root = tree.getroot()
    entry = []
    ent_dict = defaultdict(dict)

    print('Processing entries...')
    for term in root[1][0].iter('termEntry'):
        for term_lang in term.iter('langSet'):
            lang = term_lang.get('{http://www.w3.org/XML/1998/namespace}lang')
            if lang == lang_src:
                entry.append(term_lang[0][0].text)

        if entry:
            for term_lang in term.iter('langSet'):
                lang = term_lang.get(
                    '{http://www.w3.org/XML/1998/namespace}lang')
                if lang in lang_list and lang != lang_src:
                    ent_dict[lang][entry] = term_lang[0][0].text

    return entry, ent_dict
