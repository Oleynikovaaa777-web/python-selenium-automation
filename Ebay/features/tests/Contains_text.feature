
Feature: Ebay_covid_feature


  Scenario: Check if title contains text eBay
     Given Open Ebay page
     When Click on about COVID-19
     When Check if COVID-19 contains in title
     When Go back
     When Check current page is Ebay page
     Then Check if title contains text eBay


