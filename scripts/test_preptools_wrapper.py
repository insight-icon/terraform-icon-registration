import preptools_wrapper as pc
import os
import pytest


def test_working():
    """Test working."""


    network_name = "testnet"
    keystore_path = os.path.abspath(os.path.join("..", "test", "fixtures", "keystore", "testnet"))
    op_keystore_path = keystore_path + '-operator'
    if os.path.exists(op_keystore_path):
        os.remove(op_keystore_path)

    register_json = os.path.abspath(os.path.join("..", "test", "fixtures", "registerPRep-valid.json"))
    keystore_password = "testing1."
    p = pc.PRepChecker(network_name, keystore_path, register_json, keystore_password, "https://zicon.net.solidwallet.io", 80)
    p.prep_reg()
    print(p.operator_keystore_password)
    print(p.output)
    print(p.err)
    print(p.command)
    assert p.err == b''
    os.remove(op_keystore_path)


def test_input_op_wallet():
    """Test working."""

    network_name = "testnet"
    keystore_path = os.path.abspath(os.path.join("..", "test", "fixtures", "keystore", "testnet"))
    register_json = os.path.abspath(os.path.join("..", "test", "fixtures", "registerPRep-valid.json"))
    keystore_password = "testing1."

    op_ks = '-'.join([keystore_path, 'operator1'])
    p = pc.PRepChecker(network_name,
                       keystore_path,
                       register_json,
                       keystore_password,
                       "https://zicon.net.solidwallet.io",
                       80,
                       operator_keystore_path=op_ks,
                       operator_keystore_password="blahblah")
    p.prep_reg()
    print(p.operator_keystore_password)
    print(p.output)
    print(p.err)
    print(p.command)
    assert p.operator_keystore_password == "blahblah"
    assert p.operator_wallet_address == 'hx14e660bf54221f4747a6b8e31b298b8a97fc6ebe'



def test_empty():
    """Test working."""

    network_name = "zicon"
    keystore_path = os.path.abspath(os.path.join("..", "test", "fixtures", "keystore", "empty"))
    register_json = os.path.abspath(os.path.join("..", "registerPRep-valid.json"))
    keystore_password = "testing1."
    p = pc.PRepChecker(network_name, keystore_path, register_json, keystore_password, "https://zicon.net.solidwallet.io", 80)
    with pytest.raises(ValueError) as e:
        p.prep_reg()

    assert e

def test_invalid_uri():
    """Test not working."""
    network_name = "zicon"
    keystore_path = os.path.abspath(os.path.join("..", "test", "fixtures", "keystore", "testnet"))
    register_json = os.path.abspath(os.path.join("..", "test", "fixtures", "registerPRep-invalid.json"))
    keystore_password = "testing1."
    p = pc.PRepChecker(network_name, keystore_path, register_json, keystore_password, "https://zicon.net.solidwallet.io", 80)
    with pytest.raises(ValueError) as e:
        p.prep_reg()

    assert e


def test_no_gen_when_has_operator_keystore():
    """Test working."""

    network_name = "zicon"
    keystore_path = os.path.abspath(os.path.join("..", "test", "fixtures", "keystore", "testnet"))
    operator_keystore_path = os.path.abspath(os.path.join("..", "test", "fixtures", "keystore", "testnet-operator-save"))
    operator_keystore_password = "Ud(eE)WEo,20"
    register_json = os.path.abspath(os.path.join("..", "registerPRep.json"))
    keystore_password = "testing1."

    p = pc.PRepChecker(network_name,
                       keystore_path,
                       register_json,
                       keystore_password,
                       "https://zicon.net.solidwallet.io",
                       80,
                       operator_keystore_password=operator_keystore_password,
                       operator_keystore_path=operator_keystore_path)

    p.prep_reg()
    assert p.operator_keystore_password == operator_keystore_password
