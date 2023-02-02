Feature: OrangeHRM Login

    Background: common steps
        Given I launch browser
        When I open Application
        And Enter valid username and password
        And click on login

    Scenario: Login to HRM Application 
        Then user must successfully see the dashboard

    Scenario: Search user
        When Navigate to search page
        Then search page should display

    Scenario: Advanced search user 
        When navigate to advanced search page
        Then advance search page should display
