# Created by alinaoleynikova at 12/7/20
Feature: # Enter feature name here
  # Enter feature description here

  Scenario: Windows manipulations
    Given Open Ebay page
    When Go to cart
    And Check cart is empty
    And Save current window
    And Open another window
    And Switch to new window
    And Open Ebay page
    And Input lamp into search field
    And Click on search icon
    And Choose device
    And Add to cart
    And Close pop window
    And Close window 2 and switch to window 1
    And Refresh window and check now cart includes lamp
    And Check if cart contains lamp