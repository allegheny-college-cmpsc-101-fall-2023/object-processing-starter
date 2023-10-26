"""Represent a person using an object-oriented approach."""

import collections
import itertools

from typing import List

# TODO: implement all of the required source code for the Person class
# TODO: refer to the course slides on the course web site for more details!


def create_constants(name, *args, **kwargs):
    """Create a namedtuple of constants."""
    # the constants are created such that:
    # the name is the name of the namedtuple
    # for *args with "Constant_Name" or **kwargs with Constant_Name = "AnyConstantName"
    # note that this creates a constant that will
    # throw an AttributeError when attempting to redefine
    new_constants = collections.namedtuple(name, itertools.chain(args, kwargs.keys()))
    return new_constants(*itertools.chain(args, kwargs.values()))


# define the index locations for the person
person_index = create_constants(
    "person", Name=0, Country=1, Phone_Number=2, Job=3, Email=4
)

# define the names of the attributes for the person
person_attribute = create_constants(
    "person",
    Name="name",
    Country="country",
    Phone_Number="phone_number",
    Job="job",
    Email="email",
)


class Person:
    """Define a Person class."""

    def __init__(
        self, name: str, country: str, phone_number: str, job: str, email: str
    ) -> None:
        """Define the constructor for a person."""
        # TODO: implement all of the assignment statemnets for the constructor

    def __repr__(self) -> str:
        """Return a textual representation of the person."""
        # TODO: create a textual representation for a person object

    def create_list(self) -> List[str]:
        """Create a list of strings representing the person."""
        # TODO: implement a function that will create a list from the attributes of a person
        return []
