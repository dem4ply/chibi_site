#!/usr/bin/env python
# -*- coding: utf-8 -*-
import unittest
from chibi_site import Chibi_site
from vcr_unittest import VCRTestCase
from bs4 import BeautifulSoup
from chibi_site.chibi_file import Chibi_file_html
from chibi.file.temp import Chibi_temp_path


class Test_danbooru( VCRTestCase ):
    def setUp( self ):
        super().setUp()
        self.site = Chibi_site( 'https://danbooru.donmai.us/' )
        response = self.site.get()
        self.tmp = Chibi_temp_path()
        self.html_file = self.tmp + 'site.html'
        self.html_file.open().write( response.content )
        self.assertTrue( self.html_file.open().read() )


class Test_chibi_file_html( Test_danbooru ):
    def test_file_should_be_chibi_file_html( self ):
        file = self.html_file.open( chibi_file_class=Chibi_file_html )
        self.assertIsInstance( file, Chibi_file_html )

    def test_read_should_return_a_intance_of_bs( self ):
        file = self.html_file.open( chibi_file_class=Chibi_file_html )
        result = file.read()
        self.assertIsInstance( result, BeautifulSoup )
