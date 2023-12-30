Feature: TODO list

  Scenario: Create a TODO card
    Given that i am in todo page
    When create a TODO card
      """
      {
        "name": "sleep",
        "description": "it is good"
      }
      """
    Then this TODO card should be in the stack "TODO"
