  Feature: Test Scenarios for Cart functionality

  Scenario: User can add to Cart
    Given Open Amazon page
    When Click on search button
    Then Verify that Cart is empty
    Then Input lego into search field
    Then Click on search icon
    And Choose a first item in result list
    And Add it to cart
    Then Verify that result contains 1