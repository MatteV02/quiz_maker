# HTMLOutputGenerator

## methods

- `write`
  - **input**:
    - list of `Question` objects to add to the HTML page
    - output file
  - **output**: writes on the specified file the expected HTML page
  - **errors**:
        - *type error exception*: if either the first or the second argument are not of the required type
        - *OS error exception*: if output file path is invalid
        - *IO error*: if file cannot be read
