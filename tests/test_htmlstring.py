import pytest

from htmlhelpers.htmlstring import html, li, p

def test_li():
	output_str = li("dog!")
	target_str = "<li>dog!</li>"
	assert output_str == target_str

def test_html_p_heirarchy():
	output_str = html(p("dog!"))
	target_str = "<html><p>dog!</p></html>"
	assert output_str == target_str