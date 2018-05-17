import pytest
from sc.configmanager import Config
from click.testing import CliRunner
import sys
from os.path import dirname as d
from os.path import abspath, join

root_dir = d(d(d(abspath(__file__))))

@pytest.fixture
def runner():
    return CliRunner()

# Discussion on testing code with an input call.
# https://stackoverflow.com/questions/35851323/pytest-how-to-test-a-function-with-input-call
@pytest.mark.skip(reason="Comment out skip and run pytest -s to test")
def test_genconfig(monkeypatch):
    # monkeypatch the "input" function, so that it returns "Mark".
    # This simulates the user entering "Mark" in the terminal:
    monkeypatch.setitem('builtins.input', lambda x: "Mark")

    # go about using input() like you normally would:
    i = input("What is your name?")
    assert i == "Mark"

def test_read_config():
    configpath = root_dir + '/examples/'
    config = Config()
    data = config.read_config(filepath=configpath)
    assert data['Agent']['givenName'] == 'Charles'
    assert data['Agent']['familyName'] == 'Vardeman'

