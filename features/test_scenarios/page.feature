Feature: Check search functionality on openweathermap.org home page

  Scenario Outline: User navigates to home page, clicks on search button and is redirected to searching page
    Given I am redirected to home page
    When I type <search_text> on search_box on home page and search
    Then On search result page I want to see search result of <search_text> is <search_result>
    
    Examples:
    |search_text |search_result |
    |ha noi      |True          |
    |Hanoi       |True          |
  
