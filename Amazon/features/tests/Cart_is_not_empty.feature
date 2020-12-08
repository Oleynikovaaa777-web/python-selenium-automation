# Created by alinaoleynikova at 11/24/20
Feature: # Enter feature name here
  # Enter feature description here
  Scenario:
    Given Open amazon page
    When  Input lego into search field
    And Click on search button
    And Choose a first item in result list
    And Add it to cart
    And Click on cart icon
    And If cart is not empty - delete item and check cart is empty
    Then Verify that Cart is empty
