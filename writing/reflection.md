# Object Processing

TODO: Make sure that you delete all of the TODO markers in this file and either
rewrite all of the prompts so that they integrate into the report or delete the
prompts altogether. Ultimately, this document should contain professional
writing suitable for posting on your web site.

## Gregory M. Kapfhammer

## Program Output

### Use two fenced code blocks to provide output from two different runs of `objectprocessor` with two different inputs

TODO: Provide the complete command-line for your use of the `objectprocessor` program

#### Provide the command the output for the first run of the `objectprocessor`

TODO: Provide your own example of a command and the output that it produces
TODO: Make sure that you use proper Markdown syntax to provide the command and its output

#### Provide the command the output for the second run of the `objectprocessor`

TODO: Provide your own example of a command and the output that it produces
TODO: Make sure that you use proper Markdown syntax to provide the command and its output

## Source Code

### Describe in detail how the provided source code works

TODO: Provide a description of each line in the following source code

```python
person_index = create_constants(
    "person", Name=0, Country=1, Phone_Number=2, Job=3, Email=4
)
```

### Describe in detail how the provided source code works

TODO: Provide a description of each line in the following source code

```python
person_attribute = create_constants(
    "person",
    Name="name",
    Country="country",
    Phone_Number="phone_number",
    Job="job",
    Email="email",
)
```

### Describe in detail how the provided source code works

TODO: Provide a description of each line in the following source code

```python
def __init__(
    self, name: str, country: str, phone_number: str, job: str, email: str
) -> None:
    """Define the constructor for a person."""
    self.name = name
    self.country = country
    self.phone_number = phone_number
    self.job = job
    self.email = email
```

### Describe in detail how the provided source code works

TODO: Provide a description of each line in the following source code

```python
def __repr__(self) -> str:
    """Return a textual representation of the person."""
      return f"{self.name} is a {self.job} who lives in {self.country}. You can call this person at {self.phone_number} and email them {self.email}."
```

## Professional Development

### What are the benefits and drawbacks of object-oriented programming in Python?

TODO: Provide a one-paragraph response that answers this question in your own words.

### What was the greatest challenge that you faced when completing this assignment?

TODO: Provide a one-paragraph response that answers this question in your own words.
TODO: Provide a response to this question that is different from any previous answers.

### Leveraging your response to the previous question, how did you overcome the challenge?

TODO: Provide a one-paragraph response that answers this question in your own words.
TODO: Provide a response to this question that is different from any previous answers.
