import preptools_wrapper as pc
import os
import pytest


def test_working():
    """Test working."""

    network_name = "testnet"
    keystore_path = os.path.abspath(os.path.join("..", "test", "fixtures", "keystore", "testnet"))
    register_json = os.path.abspath(os.path.join("..", "registerPRep.json"))
    keystore_password = "testing1."
    p = pc.PRepChecker(network_name, keystore_path, register_json, keystore_password, "https://zicon.net.solidwallet.io", 80)
    p.prep_reg()
    print(p.operator_wallet_password)
    print(p.output)
    print(p.err)
    print(p.command)


def test_empty():
    """Test working."""

    network_name = "zicon"
    keystore_path = os.path.abspath(os.path.join("..", "test", "fixtures", "keystore", "empty"))
    register_json = os.path.abspath(os.path.join("..", "registerPRep.json"))
    keystore_password = "testing1."
    p = pc.PRepChecker(network_name, keystore_path, register_json, keystore_password, "https://zicon.net.solidwallet.io", 80)
    with pytest.raises(ValueError) as e:
        p.prep_reg()

    assert e

def test_invalid_uri():
    """Test not working."""
    network_name = "zicon"
    keystore_path = os.path.abspath(os.path.join("..", "test", "fixtures", "keystore", "empty"))
    register_json = os.path.abspath(os.path.join("..", "test", "fixtures", "registerPRep-invalid.json"))
    keystore_password = "testing1."
    p = pc.PRepChecker(network_name, keystore_path, register_json, keystore_password, "https://zicon.net.solidwallet.io", 80)
    with pytest.raises(ValueError) as e:
        p.prep_reg()

    assert e