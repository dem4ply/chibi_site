#!/usr/bin/env python
# -*- coding: utf-8 -*-
import unittest
from chibi_site import Chibi_site
from vcr_unittest import VCRTestCase
from bs4 import BeautifulSoup


class Test_chibi_site( unittest.TestCase ):
    def setUp( self ):
        pass

    def tearDown( self ):
        pass

    def test_should_work( self ):
        Chibi_site( 'https://danbooru.donmai.us/' )


class Test_danbooru( VCRTestCase ):
    def setUp( self ):
        super().setUp()
        self.site = Chibi_site( 'https://danbooru.donmai.us/' )


class Test_soup( Test_danbooru ):
    def test_soup_should_work( self ):
        self.assertTrue( self.site.soup )

    def test_soup_should_be_instance_soup( self ):
        self.assertIsInstance( self.site.soup, BeautifulSoup )


class Test_soup_images( Test_danbooru ):
    def test_soup_should_work( self ):
        self.assertTrue( self.site.images )


class Test_soup_sections( Test_danbooru ):
    def test_soup_should_work( self ):
        self.assertTrue( self.site.sections )


class Test_soup_links( Test_danbooru ):
    def test_soup_should_work( self ):
        self.assertTrue( self.site.links )

    def test_links_should_be_a_list( self ):
        self.assertIsInstance( self.site.links, list )

    def test_links_as_string_should_be_a_list( self ):
        self.assertIsInstance( self.site.links_as_string, list )

    def test_links_as_string_all_items_should_be_strings( self ):
        self.assertTrue( self.site.links_as_string )
        for link in self.site.links_as_string:
            self.assertIsInstance( link, str )

    def test_urls_should_be_urls( self ):
        self.assertTrue( self.site.links_as_string )
        for link in self.site.urls:
            self.assertIsInstance( link, Chibi_site )
