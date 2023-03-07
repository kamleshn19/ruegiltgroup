Feature: Test Registration Password Field
  Scenario Outline: Test the chnage in number of characters allowed by password field
    Given I launch chrome browser
    When I open Rue La La or Gilt website "<url>"
    Then I verify the landing page and move to signup
    When I enter email address "<emailId>"
    And I click on Continue
    When I enter password "<password>" for registering new user
    And I click on Start Shopping or Shop Now Button
    Then I Verify that the user is landed to Home Page

    Examples:
      | url | emailId | password |
      | https://www.ruelala.com/boutique/ | test@testemail.com |  |
      | https://www.ruelala.com/boutique/ | test1@testemail.com | 1 |
      | https://www.ruelala.com/boutique/ | test2@testemail.com | 12 |
      | https://www.ruelala.com/boutique/ | test3@testemail.com | 54* |
      | https://www.ruelala.com/boutique/ | test4@testemail.com | 487£ |
      | https://www.ruelala.com/boutique/ | test4@testemail.com | £$457% |
      | https://www.ruelala.com/boutique/ | test6@testemail.com | 123456 |
      | https://www.ruelala.com/boutique/ | test7@testemail.com | 45@@458 |
      | https://www.ruelala.com/boutique/ | test8@testemail.com | Hello123 |
      | https://www.ruelala.com/boutique/ | test9@testemail.com | Test9Pass |
      | https://www.ruelala.com/boutique/ | test10@testemail.com | 123456789@ |
      | https://www.ruelala.com/boutique/ | test11@testemail.com | Welcome145@@ |