# Narya - Unmatched Simplicity, Unlimited Power

!!! quote ""
    Once thought only to be the stuff of fantasy and legend, **Narya** is your next favorite programming language. Built with developer ergonomics at the forefront, Narya's faster to type, and more powerful and flexible than any other language (probably). A joy to type and to read, Narya is both blazingly fast to develop in and deep enough to rival the performance of C (probably). Read on to learn why you should give Narya a chance today.


## Core Principles

Good code should be easy to write. Every decision that has gone into creating **Narya** has had these core principles in mind:


### 1. Unmatched Simplicity
!!! note "Perfection is achieved, not when there is nothing more to add, but when there is nothing left to take away"
    Programming languages are burdened with the legacy of conventions and punctuation that are intimidating to beginners, and waste thousands of keystrokes a day for the average developer. **Narya** seeks to eliminate as much boilerplate and keystrokes as possible, while leaving only the purest core of what remains. In other words: you can basically write psuedo-code, and it will run.


```narya
group Person(text Name, num Age)
    public text Greeting
        return 'Greetings! I am .Name, .Age years young!'

do
    *List(Person) people = Person("Aragorn", 87), Person("Galadriel", 8372),
                           Person("Olórin", 58000)
    for person in people
        print person.Greeting

/*
Output:
Greetings! I am Aragorn, 87 years young!
Greetings! I am Galadriel, 8372 years young!
Greetings! I am Olórin, 58000 years young!
*/
```

### 2. Aggressive Consistency
!!! tip "We are what we repeatedly do. Excellence, then, is not an act, but a habit."
    In **Narya**, similar concepts always use similar syntax. No special cases, no "well, except for..." moments. Every piece of punctuation has a predictable and consistent use case. 

```narya
// Collections follow one consistent pattern
List(int) numbers = 1, 2, 3
Dictionary(string = float) distanceInFeet = ("ranga" = 3.16667, "lár" = 15833.33)
Set(char) vowels = 'a', 'e', 'i', 'o', 'u'
```

### 3. Built-In Power
!!! success "The power of the sun, in the palm of your hand."
    Common programming tasks shouldn't require external libraries. Narya includes powerful built-in features for:
    
    - 🎯 Memory management at *your* level of comfort
    - 🛡️ Built-in error handling
    - 🔄 Comprehensive string interpolation
    - 🧩 Rich collection types
    - 🔗 Trait-based composition
    - ✨ Metaprogram to your wildest dreams

## Why Narya?

### 🌟 Inspiration
After a night of frustration with inconsistencies in both Python and C#, **Narya** was born with the audacious goal to truly make "one programming language to rule them all." Unfortunately, Ring is already a programming language, and any combination of **Ash Nazg Durbatulûk** ("one ring to rule them all") just doesn't quite roll off the tongue. So instead, sticking with actually named rings of power, we look instead to the Ring of Fire, Narya, which has the best name (sorry Nenya and Vilya, your time will come). Just as it was crafted to inspire others to resist tyranny and despair, **Narya** is designed to resist the tyranny of complexity and the despair of inconsistent design. Naturally, of course, it is and will always be free and open source, forever. *Hopefully I'll never need some help keeping the Tolkien estate off my back.* 😇

### 🙌 Developer Ergonomics
Your hands are important. Why should we continue to sacrifice them in the name of code that's easier for computers to parse like it’s still 1972 or 1987? As someone with a history of various wrist and finger repetitive strain injuries, I view every extra keypress, every extra held modifier, or layer-shifting key as one more tiny dagger into your hands' longevity. Narya aims to be as friendly to type as possible by using a limited set of symbols and reducing unnecessary syntactic noise, making it both more comfortable to write and more aesthetically pleasing.

### 🎯 Design Philosophy
Unlike languages that grow organically over decades, Narya is purposefully crafted with a clear vision. Every feature must pass the "Ring Test":

1. Does it maintain simplicity?
2. Does it follow established patterns?
3. Does it serve a common need?

### 💎 Key Features

=== "Memory Management"
    The innovative Ring system provides three levels of memory management:
    ```narya
    inner int x = 5        // Automatic scope-based (default)
    outer Config configuration = new  // Reference counted
    core Resource resource = new  // Manual management
    ```

=== "String Interpolation"
    Powerful, consistent string formatting:
    ```narya
    text name = "World"
    print 'Hello, .name!'  // Simple variable
    print 'Sum: .(x + y)'  // Expressions
    ```

=== "Error Handling"
    Built-in error handling without exceptions:
    ```narya
    int? result = RiskyOperation
    if result is Error
        // Handle error
    else
        // Use result
    ```

## Get Started

Jump into Narya with our [Getting Started Guide](getting-started.md) or explore the comprehensive [Language Reference](language-reference/overview.md).

---

<div class="grid cards" markdown>

-   :material-clock-fast:{ .lg .middle } __Quick Start in 5 Minutes__

    ---

    Create your first Narya program quickly

    [:octicons-arrow-right-24: Getting started](getting-started.md)

-   :material-book:{ .lg .middle } __Language Reference__

    ---

    Comprehensive language documentation

    [:octicons-arrow-right-24: Documentation](language-reference/overview.md)

-   :material-library:{ .lg .middle } __Standard Library__

    ---

    Explore built-in features

    [:octicons-arrow-right-24: Standard library](standard-library/overview.md)

-   :material-help:{ .lg .middle } __FAQ__

    ---

    Common questions and answers

    [:octicons-arrow-right-24: FAQ](faq.md)

</div>
































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
        
        public action Greeting
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

