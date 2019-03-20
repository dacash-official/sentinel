import pytest
import sys
import os
import re
os.environ['SENTINEL_ENV'] = 'test'
os.environ['SENTINEL_CONFIG'] = os.path.normpath(os.path.join(os.path.dirname(__file__), '../test_sentinel.conf'))
sys.path.append(os.path.join(os.path.dirname(__file__), '..', '..', 'lib'))
sys.path.append(os.path.join(os.path.dirname(__file__), '..', '..'))
import config

from dacashd import DACashDaemon
from dacash_config import DACashConfig


def test_dacashd():
    config_text = DACashConfig.slurp_config_file(config.dacash_conf)
    network = 'mainnet'
    is_testnet = False
    genesis_hash = u'00000b8ab13e8a9fa1108a80c066b95e48209616cf142b5f87527516a564a9c2'
    for line in config_text.split("\n"):
        if line.startswith('testnet=1'):
            network = 'testnet'
            is_testnet = True
            genesis_hash = u'0000074f17a346a7a4df7c7f4e5c48b18d6f9d3313a7b20fc8090b490d2c80ef'

    creds = DACashConfig.get_rpc_creds(config_text, network)
    dacashd = DACashDaemon(**creds)
    assert dacashd.rpc_command is not None

    assert hasattr(dacashd, 'rpc_connection')

    # DACash testnet block 0 hash == 00000bafbc94add76cb75e2ec92894837288a481e5c005f6563d91623bf8bc2c
    # test commands without arguments
    info = dacashd.rpc_command('getinfo')
    info_keys = [
        'blocks',
        'connections',
        'difficulty',
        'errors',
        'protocolversion',
        'proxy',
        'testnet',
        'timeoffset',
        'version',
    ]
    for key in info_keys:
        assert key in info
    assert info['testnet'] is is_testnet

    # test commands with args
    assert dacashd.rpc_command('getblockhash', 0) == genesis_hash
