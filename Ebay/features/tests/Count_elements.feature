# Created by alinaoleynikova at 12/2/20
Feature: # Enter feature name here
  # Enter feature description here

  Scenario: # Enter scenario name here
    # Enter steps here
    Given Open Ebay page
    When Input playstation 5 into search field
    And Click on search icon
    And Count items with label Fast/n free
    And Open first item result
    And Add item to cart
    And If have popup close it
    Then Check 1 item in cart