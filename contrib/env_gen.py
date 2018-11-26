#!/usr/bin/env python

CONFIG_STRING = """
BLING_API_KEY=Y0uR_Bling_API_Key
"""

# Writing our configuration file to '.env'
with open('.env', 'w') as configfile:
    configfile.write(CONFIG_STRING)
