# Created by alinaoleynikova at 11/18/20
Feature: Count how many results on result page

  Scenario: Count fantasy books
   Given Open Amazon page
    When Input fantasy book into search field
    When Click on search icon
    Then On result page should be 22 results