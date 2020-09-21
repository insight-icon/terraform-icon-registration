import preptools_wrapper as pc
import os



def test_looped_nuki():
    """Verify Jinja2 time extension work correctly."""

    network_name = "testnet"
    keystore_path = os.path.abspath(os.path.join("..", "test", "fixtures", "keystore", "testnet"))
    register_json = os.path.abspath(os.path.join("..", "registerPRep.json"))
    keystore_password = "testing1."
    p = pc.PRepChecker(network_name, keystore_path, register_json, keystore_password)
    p.prep_reg()

