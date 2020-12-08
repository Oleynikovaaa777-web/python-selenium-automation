# Created by alinaoleynikova at 12/7/20
Feature: # Enter feature name here
  # Enter feature description here

  Scenario: Windows manipulations
    Given Open Ebay page
    When Go to cart
    And Check cart is empty
    And Open another window
    And Switch to new window
    And Open Ebay page
    And Input {search_word} into search field
    And Add to cart
    And Close pop window
    And Close 1 window
    And Switch to window 1
    And Refresh window and check now cart includes iPhone
