Feature: Pointzi Login

  Scenario: Login to Pointzi
    Given Launch Chrome Browser
    When Open Pointzi home Page
    And Enter all details
    Then click Login
    Then Login to Dashboard
