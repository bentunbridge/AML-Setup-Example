from aml_setup.create_envs.create_env import get_hash

def test_get_hash():
    hash = get_hash()
    assert type(hash) == str
