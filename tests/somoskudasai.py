#!/usr/bin/env python
# -*- coding: utf-8 -*-
import unittest
from chibi_site import Chibi_site
from vcr_unittest import VCRTestCase
from bs4 import BeautifulSoup


class Test_somoskudasai( VCRTestCase ):
    def _get_vcr_kwargs( self, **kw ):
        kw[ 'ignore_hosts' ] = [ 'localhost' ]
        return kw

    def setUp( self ):
        super().setUp()
        self.site = Chibi_site( 'https://somoskudasai.com/' )


class Test_articles( Test_somoskudasai ):
    def test_articles_should_return_a_list( self ):
        self.assertIsInstance( self.site.articles, list )

    def test_articles_can_be_send_to_html( self ):
        html_file = self.site.articles.to_html( to_temp=True )
        self.assertTrue( html_file )
        self.assertTrue( html_file.exists )

    @unittest.skip( "to slow" )
    def test_html_can_be_open_with_firefox( self ):
        html_file = self.site.articles.to_html( to_temp=True )
        html_file.open_on_browser()


class Test_sections( Test_somoskudasai ):
    def test_section_should_return_a_list( self ):
        self.assertIsInstance( self.site.sections, list )

    def test_section_can_be_send_to_html( self ):
        html_file = self.site.sections.to_html( to_temp=True )
        self.assertTrue( html_file )
        self.assertTrue( html_file.exists )

    @unittest.skip( "to slow" )
    def test_html_can_be_open_with_firefox( self ):
        html_file = self.site.sections.to_html( to_temp=True )
        html_file.open_on_browser()
