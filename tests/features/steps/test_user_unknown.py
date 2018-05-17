import pytest
from pytest_bdd import given, scenario, then, when

from click.testing import CliRunner
from sc import cli

# @pytest.mark.skip(reason="Currently not implemented")
@scenario('../user.feature', 'An unknown user starts Smart Containers')
def test_an_unknown_user_starts_smart_containers():
    """An unknown user starts Smart Containers."""
    pass

@given('an unknown user')
def an_unknown_user():
    """an unknown user."""
    pass

@when('it is given to smart containers on start')
def it_is_given_to_smart_containers_on_start():
    """it is given to smart containers on start."""
    pass

@then('it should help the user create a configuration')
def it_should_help_the_user_create_a_configuration():
    """it should help the user create a configuration"""
    pass

@then('it should contain a blank node for the unknown user')
def it_should_contain_a_blank_node_for_the_unknown_user():
    """it should contain a blank node for the unknown user."""
    pass

@then('it should contain a has account node containing the username and hostname')
def it_should_contain_a_has_account_node_containing_the_username_and_hostname():
    """it should contain a has account node containing the username and hostname."""
    pass
