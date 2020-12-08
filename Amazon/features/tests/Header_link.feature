# Created by alinaoleynikova at 12/4/20
Feature: # Enter feature name here
  # Enter feature description here


  Scenario: Find all header links
    Given Open Amazon page
    When Find all header links
    Then Click elements in loop
    Then Click first link
    Then Click second link