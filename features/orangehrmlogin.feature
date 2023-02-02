Feature: OrangeHRM Login
    Scenario: login to OrangeHRM with valid parameters
        Given I launch chrome browser
        When I open orange HRM homepage
        And enter username "admin" and password "admin123"
        And click on login button
        Then user must successfully login to the dashboard

    Scenario Outline: login to OrangeHRM with valid parameters
        Given I launch chrome browser
        When I open orange HRM homepage
        And enter username "<username>" and password "<password>"
        And click on login button
        Then user must successfully login to the dashboard

        Examples: 
            | username | password |
            | admin    | admin123 |
            | admin123 | admin    |
            | adminxyz | admin123 |
            | admin    | adminxyz |