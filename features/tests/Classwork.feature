# Created by alinaoleynikova at 11/10/20

  Feature: Verify that lego contains in title

  Scenario: find lego text
    Given Open amazon page
    When Search for lego
    When Click on search icon
    Then Choose a first item in result list
    Then Check in title that first item will be lego text