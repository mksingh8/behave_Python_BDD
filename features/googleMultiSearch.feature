Feature: Google Search

  Background: common steps
    Given launch chrome browser
    When open google home page
    Then verify logo present on the page

  Scenario: Single in Google
    Then enter text "red wine" and hit enter
    Then verify the page title has Google Search
    And close browser

  Scenario Outline: Google search for different item
    Then enter text "<searchTxt>" and hit enter
    Then verify the page title has Google Search
    And close browser

    Examples:
      | searchTxt   |
      | black wine  |
      | orange wine |

#    To generate the allure report, use following commands
#  behave -f allure_behave.formatter:AllureFormatter -o reports/ features
#  then run allure serve reports/