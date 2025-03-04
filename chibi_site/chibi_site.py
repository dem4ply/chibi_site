# -*- coding: utf-8 -*-
from chibi_requests import Chibi_url
from chibi_requests.response import Response as Response_base


class Response( Response_base ):
    is_raise_when_no_ok = True


class Chibi_site( Chibi_url ):
    def __new__( cls, *args, **kw ):
        kw.setdefault( 'response_class', Response )
        obj = super().__new__( cls, *args, **kw )

        return obj

    @property
    def response( self ):
        try:
            return self._response
        except AttributeError:
            self._response = self.get()
            return self._response

    @property
    def soup( self ):
        return self.response.native

    @property
    def images( self ):
        return self.soup.find_all( 'img' )

    @property
    def sections( self ):
        return self.soup.find_all( 'section' )

    @property
    def links( self ):
        return self.soup.find_all( 'a' )

    @property
    def links_as_string( self ):
        return list( a.attrs[ 'href' ] for a in self.links )
