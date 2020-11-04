# Created by alinaoleynikova at 11/2/20

  Feature: Test Scenarios for Search functionality

  Scenario: User can search for a product
    Given Open Ebay page
    When Input iPhone into search field
    And Click on search icon
    Then Product results for iPhone are shown
    And First result contains iPhone