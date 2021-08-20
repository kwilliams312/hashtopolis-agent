import requests
import os
import argparse

parser = argparse.ArgumentParser(description="Start a hashtopolis agent.")
parser.add_argument('--url', required=True, help='hashtopolis base url')
parser.add_argument('--apikey', required=True, help='api user token')

args = parser.parse_args()

user_url='%s/api/user.php' % (args.url) 
server_url='%s/api/server.php' % (args.url)
#api_key='yqXpyhnZR8JC7Z7Cuq9GspJCrk3jb4'

def verify_access(api_key):
    '''
    takes user API key as input
    returns BOOL of connection status
    '''
    access_test = {
    "section": "test",
    "request": "access",
    "accessKey": api_key
    }

    r = requests.post(user_url, json=access_test)
    r.json()
    return True

def list_agent_voucher(api_key):
    '''
    takes user API key as input
    return list of current vouchers on hashtopolis server
    '''
    list_vouchers = {
    "section": "agent",
    "request": "listVouchers",
    "accessKey": api_key
    }

    r = requests.post(user_url, json=list_vouchers)
    return r.json()['vouchers']


def create_agent_voucher(api_key):
    '''
    takes user API key as input
    returns a valid hashtopolis voucher string
    '''
    create_voucher = {
    "section": "agent",
    "request": "createVoucher",
    "accessKey": api_key
    }

    r = requests.post(user_url, json=create_voucher)
    return r.json()['voucher']

voucher=create_agent_voucher(args.apikey)
os.system("python3 hashtopolis.zip --url %s --voucher %s" % (server_url, voucher))
