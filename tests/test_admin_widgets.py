# coding=utf-8
"""Test cases for Zinnia's admin widgets"""
from django.test import TestCase
from django.utils.encoding import smart_text

from zinnia.admin.widgets import MPTTFilteredSelectMultiple


class MPTTFilteredSelectMultipleTestCase(TestCase):

    def test_render_option(self):
        widget = MPTTFilteredSelectMultiple('test', False)

        option = widget.render_option([], 1, 'Test', (4, 5))

        self.assertEqual(
            option,
            '<option value="1" data-tree-id="4"'
            ' data-left-value="5">Test</option>')

        option = widget.render_option(['0', '1', '2'], 1, 'Test', (4, 5))

        self.assertEqual(
            option,
            '<option value="1" selected="selected" data-tree-id="4"'
            ' data-left-value="5">Test</option>')

    def test_render_option_non_ascii_issue_317(self):
        widget = MPTTFilteredSelectMultiple('test', False)

        option = widget.render_option([], 1, 'тест', (1, 1))

        self.assertEqual(
            option,
            smart_text('<option value="1" data-tree-id="1"'
                       ' data-left-value="1">тест</option>'))

    def test_render_options(self):
        widget = MPTTFilteredSelectMultiple('test', False)
        self.assertEqual(widget.render_options([], []), '')

        options = widget.render_options([
            (1, 'Category 1', (1, 1)),
            (2, '|-- Category 2', (1, 2))], [])

        self.assertEqual(
            options,
            '<option value="1" data-tree-id="1" data-left-value="1">'
            'Category 1</option>\n<option value="2" data-tree-id="1" '
            'data-left-value="2">|-- Category 2</option>')

        options = widget.render_options([
            (1, 'Category 1', (1, 1)),
            (2, '|-- Category 2', (1, 2))], [2])

        self.assertEqual(
            options,
            '<option value="1" data-tree-id="1" data-left-value="1">'
            'Category 1</option>\n<option value="2" selected="selected" '
            'data-tree-id="1" data-left-value="2">|-- Category 2</option>')
