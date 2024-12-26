import secrets
import struct
import argparse
import random
import pefile
import os
import lznt1
import time

def exception( func ):
    def capture( *args, **kwargs ):
        try:
            return func( *args, **kwargs )
        except Exception as e:
            print( f'[-] error: { e }' )
            exit( 1 )

    return capture

class Pack( object ):
    def __init__( self ):
        self.__data   = bytes()
        self.__endian = "<"

    def long( self, value ):
        self.__data += struct.pack( f"{self.__endian}I", value )

    def bool( self, value ):
        if value:
            self.long( 1 )
        else:
            self.long( 0 )

    def byts( self, value ):
        self.long( len( value ) )
        self.__data += value

    def strs( self, value ):
        self.long( len( value ) )
        self.__data += value.encode( 'utf-8' )

    def join( self, value ):
        if isinstance( value, str ):
            self.__data += value.encode( 'utf-8' )
        elif isinstance( value, bytes ):
            self.__data += value
        elif isinstance( value, bytearray ):
            self.__data += bytes( value )
        else:
            raise TypeError( 'value must be str or bytes or bytearray' )
    
    def build( self ) -> bytes:
        return self.__data

def enable( value ) -> bool:
    return value.lower() == 'true'

def arch( args ) -> str:
    with pefile.PE( args.file ) as pe:
        arch = pe.FILE_HEADER.Machine == 0x8664 and 'x64' or 'x86'
    return arch

def boot( args ) -> bytes:
    with open( f'bin/peload.{ arch( args ) }.bin', 'rb' ) as f:
        return f.read()

def file( args ) -> bytes:
    with open( args.file, 'rb' ) as f:
        return f.read()
    
def keys( args ) -> bytes:
    if not enable( args.garble ):
        return bytes( 0 )
    
    return secrets.token_bytes( random.randrange( 256, 2048 ) )

def argv( args ) -> str:
    return f'{ os.path.basename( args.file ) } { " ".join( args.parameter ) }' + '\x00'

def compre( args, data : bytes ) -> bytes:
    if not enable( args.compress ):
        return data

    return lznt1.compress( data )

def garble( args, data : bytes, key : bytes ) -> bytes:
    if not enable( args.garble ):
        return data

    data = bytearray( data )
    size = len( key )

    for i in range( len( data ) ):
        data[ i ] ^= key[ i % size ]

    return bytes( data )

@exception
def main():
    parser : argparse.ArgumentParser = argparse.ArgumentParser( description = 'Convert PE file to shellcode' )
    parser.add_argument( '-f', '--file',      required = True,   help = 'PE file to be converted into shellcode' )
    parser.add_argument( '-o', '--output',    required = True,   help = 'Output file name' )
    parser.add_argument( '-g', '--garble',    default  = 'true', help = 'Specify whether to enable obfuscation [ obfuscate PE and parameters ]' )
    parser.add_argument( '-c', '--compress',  default  = 'true', help = 'Specify whether to enable compression, which can significantly reduce the size' )
    parser.add_argument( '-p', '--parameter', default  = '',     help = 'Execution parameters to be passed to the PE file', type = str, nargs = argparse.REMAINDER )

    # parse arguments
    stat = time.time()
    args = parser.parse_args()
    key  = keys( args )
    para = Pack()
    data = Pack()
    comp = Pack()

    # output prompt message
    print( f'[+] file:      { args.file    }' )
    print( f'[+] parameter: { argv( args ) }' )
    print( f'[+] output:    { args.output  }' )
    print( f'[+] arch:      { arch( args ) }' )

    # build payload arguments
    para.strs( argv( args ) )
    para.byts( file( args ) )

    # process payload
    buff = compre( args, para.build() )
    buff = garble( args, buff, key )

    # build compressed payload
    comp.bool( enable( args.compress ) )
    comp.long( len( para.build() ) )
    comp.byts( buff )
    comp.byts( key )

    # compress payload
    data.join( boot( args ) )
    data.byts( comp.build() )

    # write shellcode
    with open( args.output, 'wb' ) as f:
        f.write( data.build() )

    print( f'[+] compress: { enable( args.compress ) }' )
    print( f'[+] garble:   { enable( args.garble ) }' )
    print( f'[+] save:     { args.output } | size: { len( data.build() ) }' )
    print( f'[+] time:     { int( time.time() ) - int( stat ) }s' )

if __name__ == "__main__":
    main()
