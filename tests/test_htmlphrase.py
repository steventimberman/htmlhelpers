import textwrap

import pytest

from htmlhelpers.htmlstring import li, html, ul
from htmlhelpers.htmlphrase import tag_series, tag_phrase

def test_tag_series():
	tag_fn = li
	text_list = ["cat", "dog", "rabbit"]
	tag_series_output = tag_series(tag_fn, text_list)
	tag_series_target = "<li>cat</li><li>dog</li><li>rabbit</li>"

	assert tag_series_output == tag_series_target

def test_tag_phrase():
	tag_fn_list = [html, ul]
	inner_tags = "<li>cat</li><li>dog</li><li>rabbit</li>"
	tag_phrase_output = tag_phrase(tag_fn_list, inner_tags)
	tag_phrase_target = "<html><ul><li>cat</li><li>dog</li><li>rabbit</li></ul></html>"
	assert tag_phrase_output == tag_phrase_target

def test_tag_phrase_using_tag_series():
	tag_fn_list = [html, ul]

	tag_fn = li
	text_list = ["cat", "dog", "rabbit"]
	tag_series_output = tag_series(tag_fn, text_list)

	inner_tags = tag_series_output
	tag_phrase_output = tag_phrase(tag_fn_list, inner_tags)
	tag_phrase_target = "<html><ul><li>cat</li><li>dog</li><li>rabbit</li></ul></html>"
	assert tag_phrase_output == tag_phrase_target

def test_tag_phrase_with_formatting():
	tag_fn_list = [html, ul]
	inner_tags = "<li>cat</li><li>dog</li><li>rabbit</li>"
	
	tag_phrase_output = tag_phrase(tag_fn_list, inner_tags, True)
	tag_phrase_false_target = "<html><ul><li>cat</li><li>dog</li><li>rabbit</li></ul></html>"
	assert tag_phrase_output != tag_phrase_false_target

	tag_phrase_target = textwrap.dedent("""\
        <html>
          <ul>
            <li>cat</li>
            <li>dog</li>
            <li>rabbit</li>
          </ul>
        </html>""")

	assert tag_phrase_output == tag_phrase_target

