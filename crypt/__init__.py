# standard libs
import datetime
import hashlib
import os
import sys

def expect_hexstr():
    """
        Small function to wrap type checking for string
    """
    if type(hexstr) is not str:
        sys.exit('Method expects hexadecimal string as input')

def sha256(ingest):
    """
        Wrapper for sha256 hashlib function with included UTF-8 formatting and
        output in Hexadecimal (Base16).
    """
    return hashlib.sha256(ingest.encode('utf-8')).hexdigest()

def get_nonce_hash():
    """
        Simple utility function to generate a hashed_nonce from the environment
        variable NONCE.
    """
    try:
        return sha256(os.environ['NONCE'])
    except KeyError:
        sys.exit('Must set environment variable \'NONCE\'')

def bitflip(hexstr):
    # check that hexstr is string
    expect_hexstr()

def encode_dtime(hexstr):
    # check that hexstr is string
    expect_hexstr()

def scramble_hash(hexstr):
    # check that hexstr is string
    expect_hexstr()
