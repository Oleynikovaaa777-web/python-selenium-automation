Feature: Selenium windows manipulations

  Scenario: Sample
    Given Open Amazon page
    When Save current window
    When Open new window
    When Switch to new window
    When Make some manipulations
    Then Switch to origin window