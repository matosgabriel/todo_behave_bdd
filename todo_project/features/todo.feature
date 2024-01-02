Feature: TODO list

  Scenario: Create a TODO card
    Given that i am in "todo" page
    When create a TODO card
      """
      {
        "name": "sleep",
        "description": "it is good"
      }
      """
    Then this TODO card should be in the stack "A fazer"

  @critical
  Scenario: Create many TODO cards
    Given that i am in "todo" page
    When create the following TODO cards
      | name  | description   |
      | sleep | it is good    |
      | eat   | it is awesome |
    Then the following TODO cards should be in the stack "A fazer"
      | name  | description   |
      | sleep | it is good    |
      | eat   | it is awesome |