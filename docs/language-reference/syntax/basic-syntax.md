# Basic Syntax

## Comments

Narya supports both single-line and multi-line comments:

```narya
main
    Person(text Name, num Person)

    do
        *List(Person) people = Person("Aragorn", 87), Person("Galadriel", 8372), Person("Mithrandir", 58000)
// This is a single-line comment

/*
This is a
multi-line comment
*/
```