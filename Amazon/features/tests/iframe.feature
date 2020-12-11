# Created by alinaoleynikova at 12/11/20
Feature: # Enter feature name here
  # Enter feature description here

  Scenario: # Enter scenario name here
    Given Open home depot page
    When Go to cart
    And Check cart is empty
    And Open new window
    And Switch to new window
    And Open home depot page
    And Search for Saw
    And Choose first item
    And Add to cart
    And Close popup window
#    And Close new window and switch no previous one
#    And Refresh page
#    Then Check cart now is not empty