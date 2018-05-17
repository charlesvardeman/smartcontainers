import pytest
from pytest_bdd import given, scenario, then, when

@pytest.mark.skip(reason="Currently not implemented")
@scenario('../user.feature', 'A known user with a configuration file runs Smart Containers')

@given('a valid yaml configuration file')
def a_valid_orcid_id():
    """a valid orcid id."""

@when('it is given to smart containers on start')
def it_is_given_to_smart_containers_on_start():
    """it is given to smart containers on start."""

@then('it should parse user identity information')
def it_should_create_an_rdf_graph():
    """it should create an RDF graph."""

@then('it should contain the user\'s information for prov')
def it_should_contain_the_users_orcid_information():
    """it should contain the user's ORCID information."""
