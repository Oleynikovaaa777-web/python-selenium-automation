# Created by alinaoleynikova at 11/10/20

  Feature: Verify that lego contains in title

  Scenario: find lego text
    Given Open amazon page
    When Input lego into search field
    When Click on search button
    Then Choose a first item in result list
    Then Check in title o first item will be lego text