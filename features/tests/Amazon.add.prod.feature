# Created by alinaoleynikova at 11/6/20

    Feature: Test Scenarios for Cart functionality

  Scenario: User can add to cart a product
    Given Open Amazon page
    When Input lego into search field
    And Click on search icon
    And Choose a first item in result list
    Then Add it to cart