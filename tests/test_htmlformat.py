import textwrap

import pytest

from htmlhelpers import htmlformat as hf

def test_format_phrase():
    phrase = "<ul><li>cat</li><ul><li>smelly cat</li><li>Happy cat!</li></ul><li>dog</li></ul>"
    output = hf.format_phrase(phrase)
    target = textwrap.dedent("""\
        <ul>
          <li>cat</li>
          <ul>
            <li>smelly cat</li>
            <li>Happy cat!</li>
          </ul>
          <li>dog</li>
        </ul>""")
    
    assert output == target