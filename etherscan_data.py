# -*- coding: utf-8 -*-
"""
Created on Sun Mar 25 22:17:26 2018
Functions for calling the Etherscan API in python

@author: ariahklages-mundt
"""

import pandas as pd

def eth_url(module, action, address):
    if module not in ['account']:
        raise Exception('{} not valid module'.format(module))
    if action not in ['txlist','balance']:
        raise Exception('{} not valid action'.format(action))
    return 'http://api.etherscan.io/api?module={}&action={}&address={}'.format(module, action, address)

def from_etherscan(url, api_key, typ='df'):
    url += '&apikey={}'.format(api_key['key'])
    if typ == 'df':
        df = pd.read_json(url)
    elif typ == 'series':
        df = pd.read_json(url,typ='series')
    return df

def get_txlist(address, startblock=0, endblock=99999999):
    url = eth_url('account','txlist',address)
    url += '&startblock={}&endblock={}&sort=asc'.format(startblock,endblock)
    df = from_etherscan(url, api_key)
    return df

def get_curr_bal(address):
    url = eth_url('account','balance',address)
    url += '&tag=latest'
    df = from_etherscan(url, api_key, typ='series')
    return wei2ether(df['result'])

def wei2ether(amount):
    return float(amount)/10**18

address = '0x2fa0ac498d01632f959d3c18e38f4390b005e200' #example wallet address
api_key = {'key': my_api_key}

