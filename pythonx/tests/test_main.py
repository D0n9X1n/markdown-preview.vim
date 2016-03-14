#!/usr/bin/env python
# encoding: utf-8

import mistune
import unittest


class mytest(unittest.TestCase):

    def testRender(self):
        self.assertEqual(False, False, 'Unit Test Start')

    def test_escape(self):
        ret = mistune.markdown('<div>**foo**</div>', escape=True)
        self.assertIn('&gt;', ret, 'success')

        ret = mistune.markdown('this **foo** is <b>bold</b>', escape=True)
        self.assertIn('&gt;', ret, 'success')

    def test_linebreak(self):
        ret = mistune.markdown('this **foo** \nis me')
        self.assertIsNot('<br>', ret, 'success')

        ret = mistune.markdown('this **foo** \nis me', hard_wrap=True)
        self.assertIn('<br>', ret, 'success')

    def test_skip_style(self):
        ret = mistune.markdown(
            'foo\n<style>body{color:red}</style>', skip_style=True
        )
        self.assertEqual(ret, '<p>foo</p>\n', 'success')

    def test_use_xhtml(self):
        ret = mistune.markdown('foo\n\n----\n\nbar')
        self.assertIn('<hr>', ret, 'success')
        ret = mistune.markdown('foo\n\n----\n\nbar', use_xhtml=True)
        self.assertIn('<hr />', ret, 'success')

        ret = mistune.markdown('foo  \nbar', use_xhtml=True)
        self.assertIn('<br />', ret, 'success')

        ret = mistune.markdown('![foo](bar "title")', use_xhtml=True)
        self.assertIn('<img src="bar" alt="foo" title="title" />', ret, 'success')

    def test_parse_inline_html(self):
        ret = mistune.markdown(
            '<div>**foo**</div>', parse_inline_html=True, escape=False
        )
        self.assertIsNot('<strong>', ret, 'success')
        ret = mistune.markdown(
            '<span>**foo**</span>', parse_inline_html=True, escape=False
        )
        self.assertIn('<span><strong>', ret, 'success')

        ret = mistune.markdown(
            '<a>http://lepture.com</a>', parse_inline_html=True, escape=False
        )
        self.assertIsNot('href', ret, 'sucess')

    def test_parse_block_html(self):
        ret = mistune.markdown(
            '<div>**foo**</div>', parse_block_html=True, escape=False
        )
        self.assertIn('<div><strong>', ret, 'success')
        ret = mistune.markdown(
            '<span>**foo**</span>', parse_block_html=True, escape=False
        )
        self.assertIsNot('<strong>', ret, 'success')

    def test_trigger_more_cases(self):
        markdown = mistune.Markdown(
            inline=mistune.InlineLexer,
            block=mistune.BlockLexer,
            skip_html=True
        )
        ret = markdown.render('foo[^foo]\n\n[^foo]: foo\n\n[^foo]: bar\n')
        self.assertEqual(ret.find('bar'), -1, 'success')

    def test_not_escape_block_tags(self):
        text = '<h1>heading</h1> text'
        self.assertIn(text, mistune.markdown(text, escape=False), 'success')

    def test_not_escape_inline_tags(self):
        text = '<a name="top"></a>'
        self.assertIn(text, mistune.markdown(text, escape=False), 'success')

    def test_hard_wrap_renderer(self):
        text = 'foo\nnewline'
        renderer = mistune.Renderer(hard_wrap=True)
        func = mistune.Markdown(renderer=renderer)
        self.assertIsNot('<br>', func(text), 'success')


if __name__ == '__main__':
    unittest.main()
