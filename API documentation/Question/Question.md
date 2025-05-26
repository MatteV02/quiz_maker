# Question

## Attributes

- `question`: string representing the question
- `answers`: list of strings containing the possible answers
- `solution`: reference to correct answers
  - **note**: this reference should always point to an existing answer

## methods

- `Question(question, answers, solutions)`: constructor
- setters and getters
  - **note**: answers and solutions setter should maintain information consistency (answers is prioritized over solutions)
  - **errors**: if question, answers or solution are put to types different from the ones above
