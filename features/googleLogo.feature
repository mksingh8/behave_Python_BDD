Feature: Google Logo
  Scenario: Logo presence in Google home page
    Given launch chrome browser
    When open google home page
    Then verify logo present on the page
    And close browser
