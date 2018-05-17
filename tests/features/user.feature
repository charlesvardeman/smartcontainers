Feature: User Information Generation

    Scenario: A known user with a configuration file runs Smart Containers
        Given a valid yaml configuration file
        When it is given to smart containers on start
        Then it should parse user identity information
        And it should contain the user's information for prov

    Scenario: An unknown user starts Smart Containers
        Given an unknown user
        When it is given to smart containers on start
        Then it should help the user create a configuration
        And it should contain a blank node for the unknown user
        And it should contain a has account node containing the username and hostname
