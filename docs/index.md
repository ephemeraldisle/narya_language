# Basic Syntax

## Comments

Narya supports both single-line and multi-line comments:

```narya
Main
    Person(text Name, num Age)

    do
        *List(Person) people = Person("Aragorn", 87), Person("Galadriel", 8372), Person("Mithrandir", 58000)


// This is a single-line comment

/*
This is a
multi-line comment
*/
```


# Narya Programming Language

Here's a simple example of Narya code:

```narya
group Main
    obj Person
        public *num Age
        private text Name
        
        public Person(num age, text name)
            Age = age
            Name = name
        
        public act Greeting
            print 'Hi, my name is .Name and I am .Age years old!'

    do
        Person alice = Person(25, "Alice")
        alice.Age = 55
        
        *List(Person) people = alice, Person(22, "Bob"), Person(37, "Greg")
        *List(Person) oldPeople

        for int i = people.Count - 1, i >= 0, i--
            if people[i].Age >= 30
               oldPeople.Add(people[i])
               people.RemoveAt(i)

        for person in oldPeople
            person.Greeting
```

