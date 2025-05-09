# Narya Language Overview

!!! note ""
    Narya is designed for clarity and consistency, making programming more enjoyable while maintaining power and flexibility. Like the Elven ring it's named for, it preserves what's good while inspiring creativity.

## Core Language Features

### Clear, Consistent Syntax

Everything in Narya follows consistent patterns - if you know how one feature works, you'll understand similar features:

```narya
// Simple variable declarations
text name = "Frodo"
num age = 50

// Intuitive string interpolation
print 'Hello .name! You are .age years old.'

// Clear object definitions
public obj Hobbit
    text Name
    num Age
    
    public Hobbit(text name, num age)
        Name = name
        Age = age

    public text Greeting
        return 'I am .Name, a hobbit of .Age years.'
```

### Type System

=== "Basic Types"
    ```narya
    // Numbers
    num x = 42       // Smart numeric type that auto-converts
    int y = 42       // 32-bit integer
    big int z = 42   // 64-bit integer, int64 is also valid :)
    float pi = 3.14  // Floating point
    uint i = 4000000000 // unsigned 32-bit integer
    //Can you guess how you call an unsigned 64-bit integer?
    
    // Text
    text msg = "Hi"  // Smart text type, switches between character and string automatically.
    char c = 'a'     // Single character
    string s = "Hi"  // String of characters
    
    // Other
    bool isReady = true
    byte data = 255
    ```

=== "Collections"
    ```narya
    // Initialize collections with or without parentheses
    List(text) fellowship = "Frodo", "Sam", "Merry", "Pippin"
    Dictionary(text = num) ages = ("Aragorn" = 87, "Legolas" = 2931)
    Set(text) realms = "Gondor", "Rohan", "Lothlorien"
    Array(int) numbers = new(5)  // Fixed-size array
    ```

### Objects and Code Organization

Narya uses objects for instantiable types and groups for code organization:

```narya
group Characters  // Organizational container
    obj Being     // Base type for all named characters
        text Name
        num Age
        
        public Being(text name, num age) //longform approach for granularity
            Name = name
            Age = age
        
        public text Greeting
            return 'Greetings! I am .Name.'

    obj NamelessThing(num Age, test Description) //Easily declare with shorthand.

    Being Wizard  // Inherits from Being
        text Color
        
        public Wizard(text name, num age, text color)
            Being(name, age) //Calls the function from its inherited type.
            Color = color
        
        public text Greeting  // Override base greeting
            return 'I am .Name the .Color!'

// Using our types
gandalf = new Wizard("Gandalf", 3000, "Grey")
print gandalf.Greeting  // "I am Gandalf the Grey!"
```

### String Interpolation and Text Handling

String interpolation is built into the language using single quotes:

```narya
text name = "Bilbo"
num age = 111
text home = "Bag End"

// Simple variable interpolation
print 'Welcome to .home!'

// Multiple interpolations
print '.name is .age years old.'

// Expressions in parentheses
print 'In 10 years you will be .(age + 10)'

// Concatenate instead, if you prefer!
print "Sometimes it is " + adjective + " cleaner to use " + noun + " instead!"
```

### Control Flow

Clear, consistent control structures that work how you'd expect:

```narya
// Pattern matching
match creature
    Wizard(name, color)
        print '.name the .color'
    Elf(name)
        print 'The elf .name'
    else
        print "Unknown creature"

// Multiple loop styles
for *int i = 0, i < 10, i++
    print i

for text item in collection
    print item

while hasMoreItems
    ProcessItem
    if isDone
        exit    // break
    if needSkip
        skip    // continue

//Use the repeat keyword to recreate a do-while loop!

do
    AnalyzeData(myQueue.Dequeue)
    myQueue.Count > 0 ? repeat

```

### Immutability by Default

Everything is immutable unless marked with `*`:

```narya
// Immutable by default
text realm = "Rivendell"
realm = "Lothlorien"  // Error: can't modify immutable value

// Mark as mutable with *
*text location = "The Shire"
location = "Bree"     // OK: location is mutable

// Same for collections
List(text) fellowship = "Frodo", "Sam"  // Immutable list
fellowship.Add("Merry")  // Error: can't modify

*List(text) party = "Thorin", "Balin"   // Mutable list
party.Add("Dwalin")     // OK: list is mutable
```

### The Three Rings: Memory Management

Memory management in Narya uses a ring-based system that makes it clear how long things live:

=== "Inner Ring (Default)"
    ```narya
    do  // New scope
        text message = "Hello"
        print message
    // message is automatically cleaned up
    ```

=== "Outer Ring"
    ```narya
    outer SharedLog log = new SharedLog
    do
        outer SharedLog view = log  // Share the reference
    // log lives until all references are gone
    ```

=== "Core Ring"
    ```narya
    core RawResource resource = GetResource
    // Must manually manage
    resource.Release
    ```

### Error Handling

Narya handles errors through its type system using `?`:

```narya
Ring? FindRing(text location)
    if location == "Mordor"
        return Error("Too dangerous!")
    if location == "River"
        return Error.Null  // While not always erroneous, Narya treats null as an error.
    return new Ring("Lesser Ring")

match FindRing("Mordor")
    Ring(ring)
        print 'Found .ring.Name'
    null // But you don't have to refer to it as an error if you don't want :)
        print "Ring is lost"
    Error(msg)
        print 'Error: .msg'
```

### Advanced Features

=== "Pointers"
    ```narya
    int value = 42
    Pointer(int) ptr = Pointer.To(value)   // Immutable pointer
    *Pointer(int) mutPtr = Pointer.To(value)    // Mutable pointer
    // Too much to type? Try it this way:
    int^ ptr = value^
    int*^ mutPtr = value^
    ```

=== "Convenient Shorthands"
    ```narya 
    /*There's always a consistent long form way of doing things, 
    but that doesn't mean we expect you to type them out all the time!*/

    List(text) items = "sword", "axe", "bow"
    for item in items //type inference for "for each" loops.
        print item
    
    for i = 0, i < items.Count, i++ //type inference for i in "for" loops
        print item[i]

    for i = 0..60  //type inference and range shorthand
        Shadowfax.SetSpeed(i)
    
    for 0..60       //automatic variable assignment and range shorthand
        Gwaihir.SetSpeed(j)
        Gwaihir.Speed == Shadowfax.Speed ? exit | print "Not yet!" //ternary expressions
    
    if (Gwaihir.Speed == 60 & Shadowfax.Speed == 60) | Ancalagon.Speed == 100  //compare using symbols
        print "It's all ogre"

    ```

=== "Aliases and Multi-variable Assignemnts"
    ```narya
    num value/count/size = 42  // All names are aliases for one single spot in memory.
    text worth, amount, area = "Undecided" 
    //All three are different variables, each taking up a spot in memory, set to "Undecided."
    ```

=== "Flexible Coding Styles"
    ```narya
    //Use { } for anonymous scopes, or to organize your code in a more classical way
    obj Entwife(text Name, *Location = "?"){
        public bool IsNearby(text searchLocation): return searchLocation == Location
    }

    //Like typing lots of extra characters? Go for it!
    object Entwife {
        *string Name = "";
        *string Location = "";

        public Entwife(string _name, string _location){
            Name = _name;
            Location = _location;
        }

        public bool IsNearby(string searchLocation){
            if (searchLocation == Location){
                return true;
            }
            else {
                return false;
            }
        }        
    }
    ```

=== "Operator Overloading"

    ```narya
    hi this code block works but the next one is broken:
    Operator().Overload(string s1, string s2) => '.(s1).(s2)'
    ```

    ```narya
    Operator(+).Overload(string s1, string s2) => '.(s1).(s2)'
    print "Hello " + "there!" 
    //Output: Hello there!

    obj Point(public int X, Y)
        Operator(+).Overload(Point a, Point b)
            return new Point(a.X + b.X, a.Y + b.Y)
        Operator(*).Overload(Point a, Point b)
            return new Point(a.X * b.X, a.Y * b.Y)
        public string ToString
            return '(.X, .Y)'
    
    print Point(2, 3) + Point(4, 5) 
    //(Print implicitly calls .ToString if given an object that has the method)
    //Output: (6, 8)
    ```

=== "Optional Language Features"
    ```narya
    //The using keyword lets you use optional language features
    
    using Narya.AutomaticMemoryManagement //Manages your memory for you, in case you're prone to forgetfulness.

    using Narya.VarType //Enables the use of the "var" type to automatically infer types

    using Narya.TypeInferencing //Automatically infers all types.

    using Narya.ClassicalOperators //Switch & and | back with && and ||. 




    ```

## Next Steps

- Dive into the [Basic Syntax](syntax/basic-syntax.md)
- Master the [Ring System](advanced-concepts/memory-management.md)
- Learn about [Collections](syntax/collections.md)
- Understand [Error Handling](syntax/error-handling.md)























# Narya Language Overview

!!! note ""
    Narya is designed around rings of power - each feature serving its purpose while maintaining harmony with the whole. Like the Elven rings themselves, Narya offers preservation, inspiration, and resistance to weariness... of programming.

## Core Language Features

### Memory Management: The Three Rings

Every value in Narya belongs to one of three memory management layers. Think of your program as a series of interlocking rings orbiting an orb, each representing a level of scope. Short-lived variables stay on the inside of each ring, while longer-lived variables that need to be shared stay on their outside. At the center lies the core - shared by every ring but volatile and dangerous to manipulate.

=== "Inner Ring (Default)"
    The most common assignment, providing automatic scope-based memory management.

    ```narya
    text name = "Glorfindel"
    do
        inner text greeting = "Mae govannen"  
        print '.name says .greeting'
        // greeting is cleaned up here
    print greeting // <- Error, would fail - greeting is out of scope
    ```

=== "Outer Ring"
    For objects that need to live beyond their creating scope.

    ```narya
    outer Palantír sharedVision = new Palantír("Minas Tirith")
    do
        outer Palantír anotherView = sharedVision
        // Both references keep the Palantír alive
    // Palantír remains until all references are gone
    ```

=== "Core Ring"
    Manual memory management for maximum control.

    ```narya
    core Silmaril jewel = Fëanor.CreateSilmaril
    // Must be manually managed
    jewel.Release
    ```
### Type System

=== "Basic Types"
    **Primitive Types**

    - Numbers: `int`, `int64`, `uint`, `uint64`, `float`, `double`, `byte`
    - Text: `char`, `string`
    - Logic: `bool`

    **Flexible Types**

    - `num`: Smart numeric type
    - `text`: Smart text type
    
    ```narya
    num age = 87  // Automatically handles numeric conversions
    text name = "Aragorn"  // Handles both single chars and strings
    ```

=== "Collection Types"
    **Built-in Collections**
    ```narya
    List(text) hobbits = ("Frodo", "Sam", "Merry", "Pippin")
    Dictionary(text = num) ages = ("Aragorn" = 87, "Legolas" = 2931) // Use () if it helps clarity
    Set(text) uniqueRealms = "Gondor", "Rohan", "Lothlorien" // Leave () off if you want!
    Array(int) numbers = new(5)  // Fixed-size array
    ```

=== "Structural Types"
    - `group`: Code organization (like namespaces)
    - `obj`/`object`: Instantiable types
    - `trait`: Shareable behavior
    - `act`/`action`: Procedures (functions with no return value)
    - `enum`: Value sets

=== "System Types"
    - `Warning`: Base class for all warnings and errors
    - `Error`: Derived from Warning, for error conditions
    - `Pointer`: For direct memory access


### Variables and Initialization

All variables are immutable by default and must be initialized when declared. Use `*` to mark something as mutable.

```narya
// Immutable by default
text realm = "Rivendell"
*text location = "The Shire"  // Mutable
```

### Warning Handling

Narya uses `?` to indicate possible Warnings (including null) or Errors:

```narya
Ring? FindOneRing(text location)
    if location == "Gollum"
        return null  // Ring is missing
    else if location == "Mordor"
        return Error("Too dangerous!")
    else
        return new Ring("The One Ring")

match FindOneRing("Mordor")
    Ring(ring)
        print "Found .ring.Name"
    null
        print "The ring is lost"
    Error(msg)
        print "Cannot search: .msg"
```

### Code Structure

Groups and objects provide flexible code organization:

```narya
group Beings  // Organizational container
    obj Creature  // Base type
        text Name
        num Age

    Creature Elf  // Inheritance
        num LightLevel
        
    trait Magical  // Shareable behavior
        act CastSpell(text spellName)
        num ManaLevel

    Elf Galadriel  // Implementation
        Traits = Magical
        act CastSpell(text spellName)
            print 'Casting .spellName with Nenya'
```

### Scoping and Line Continuation

Use parentheses to continue lines and braces for explicit scoping:

```narya
// Parentheses for line continuation
List(text) fellowship = (
    "Frodo", "Sam",
    "Gandalf", "Aragorn"
)

// Braces for explicit scoping
{
    num rings = 3
    print 'There were .rings rings'
}

// Traditional style fully supported, if preferred!
group Warrior {
    text Name;
    num Strength;
}
```

### Control Flow

Narya offers clear, consistent control structures:

```narya
// Classic loop with range
for int i = 0..9
    print 'Processing ring .i'

// Foreach loop for collections
List(text) fellowship = "Frodo", "Sam", "Aragorn"
for member in fellowship
    print '.member has joined the quest'

// While loop with skip (continue) and exit (break)
while isSearching
    match SearchForRing()
        Ring
            print "Found the ring!"
            exit
        Warning.NotFound
            print "Keep searching..."
            skip
        Error
            print "Must abandon search"
            exit

// Pattern matching for complex decisions
match creature
    Elf(name, realm)
        print '.name hails from .realm'
    Wizard(name, color)
        print '.name the .color'
    else
        print "Unknown creature"

// Nested control with scoping
for realm in MiddleEarth.Realms
    if realm.HasRing
        for bearer in realm.RingBearers
            if bearer.IsCorrupted
                print 'Found corrupted bearer in .realm.Name'
                exit
```



## Next Steps

- Dive into the [Basic Syntax](syntax/basic-syntax.md)
- Master the [Ring System](advanced-concepts/memory-management.md)
- Learn about [Collections](syntax/collections.md)
- Understand [Error Handling](syntax/error-handling.md)









































































































# Narya Language Overview

## Core Design Philosophy

Narya's architecture is built around the concept of rings - layers of functionality that work together to create a cohesive whole. Just as the Elven rings were crafted with purpose and precision, each feature of Narya serves a specific purpose while maintaining harmony with the others.

## Language Architecture

### The Three Layers of Memory

Every value in Narya belongs to one of three memory management layers. If we imagine a program as a series of interlocking rings orbiting around an orb, each representing a level of scope, short lived variables stay on the inside of each ring, whereas longer lived variables that need to be shared stay on their outside. At the center, the core is shared by every ring, but is volatile and dangerous to mess with - use caution!

=== "Inner Ring (Default)"
    The most common, providing automatic scope-based memory management. When an inner variable leaves scope, it gets cleaned up.

    **Best For:**

    - Local variables
    - Temporary objects
    - Simple use cases with zero overhead

    ```narya
    text name = "Glorfindel"
    do //Sets a new scope.
        text greeting = "Mae govannen"  
        print name + " says " + greeting
        // greeting's memory is reclaimed here
    print greeting //Produces an error
    ```

=== "Outer Ring"
    When something needs to live longer than just one scope, this uses reference counting for predictable cleanup.

    **Best For:**

    - Shared resources
    - Objects with dynamic lifetimes
    - Cross-scope communication

    ```narya
    outer Palantír sharedVision = new Palantír("Minas Tirith")
    // sharedVision is cleaned up when all observers cease watching
    ```

=== "Core Ring"
    The ring of ultimate control, offering manual memory management. Without manual release, core memory will stay assigned forever.

    **Best For:**

    - System-level programming
    - Performance-critical code
    - Direct resource control

    ```narya
    core Silmaril jewel = Fëanor.CreateSilmaril
    // Must be manually protected and released
    jewel.Release
    ```

### Core Language Features

#### Scoping and Line Continuation
Narya offers flexible scoping and line continuation:

```narya
// Use parentheses to keep a throught together, such as for line continuation
List(text) fellowship = (
    "Frodo", "Sam", "Merry", "Pippin",
    "Gandalf", "Aragorn", "Boromir",
    "Legolas", "Gimli"
)

// Use braces to help make scoping explicit, or to declare an anonymous scope
{
    num ringBearers = 3
    print 'There were .ringBearers rings for the Elven-kings'
}

// This enables you to write more traditional looking code if you want!
group Warrior {
    text Name;
    num Strength;
}
```

### Type System

#### Core Types
- **Precise Types**:
    - Numbers: `int`, `big int` / `int64`, `uint`, `big uint` / `uint64`, `float`, `big float` / `double`, `byte`
    - Text: `char`, `string`
    - Logic: `bool`
- **Special Types**:
    - Placeholder, primarily for pointers: `any`
    - Automatically convert between number types: `number` / `num`
    - Automatically convert between text types: `text`
- **Collection Types**: `List`, `Dictionary`, `Array`, `Set`
- **Structural Types**: `group`, `trait`, `enum`, `object` / `obj`, `action` / `act` 
- **System Types**: `Warning`, `Pointer`

#### Initialization and Pointers
All variables are immutable by default, and must be initialized when declared. It's easy to mark any type as mutable if you prefer - just prefix it with an *. Isn't that pretty?

```narya
// Must initialize regular variables
text name = "Tom Bombadil" // This will never change.
*text name = "Gandalf the Grey" // This will change.

// If you want to reserve a spot in memory to set a value for later, initialize a pointer there, with several forms of shorthand.
Pointer(any) wizard = Pointer.At(memoryAddress, sizeToAllocate) //Reserves a section of memory for a pointer to be assigned to at a specific address.
string*^ istari = Pointer.Auto //Automatically reserve a section of memory for a mutable pointer that opoints to an immutable string, and can later be changed to point elsewhere.
*int^ ithryn  // Shorthand declaration, does the same as Pointer.Auto
```

### Error and Warning Handling

Narya uses `?` to indicate possible lack of expected value in the form of a Warning or Error, such as for a null value:

```narya
Ring? FindRing(text location)
    if location == "Anduin"
        return Warning.Null  // Ring is lost
    if location == "Mordor"
        return Error("Too dangerous to search")
    return new Ring("Lesser")

match FindRing("Mordor")
    Ring
        print "Found: .Ring.Name"
    null  //shorthand for Warning.Null
        print "Ring is lost"
    Error
        print "Search failed: .Error.Message"
```

### Code Organization

#### Groups and Traits
Groups are flexible containers used to organize your code. They serve the same purpose as things like namespaces and some forms of classes in other languages. Groups are purely organizational. A special subtype of a Group is an Object, or obj for short. Objects are groups that can be instantiated and destroyed, the most similar thing to a class in other languages. If object oriented code isn't your jam, don't use them! :grin:

Groups support both inheritance and traits, offering flexibility in code organization:

```narya
obj Being
    text Name
    num Age

Being Elf
    num LightLevel
    
trait Magical
    act CastSpell(text spellName)
    num ManaLevel

Elf Galadriel
    Traits = Magical
    act CastSpell(text spellName)
        print 'Casting .spellName with the power of Nenya'
```

### Control Flow

Narya offers clear, consistent control structures for managing program flow:

```narya
// Classic loop with range
for i = 0 -> 9
    print 'Processing ring .i'

// Foreach loop for collections
List(text) fellowship = "Frodo", "Sam", "Aragorn"
foreach member in fellowship
    print '.member has joined the quest'

// While loop with skip (continue) and exit (break)
while isSearching
    match SearchForRing()
        Ring
            print "Found the ring!"
            exit
        Warning.NotFound
            print "Keep searching..."
            skip
        Error
            print "Must abandon search"
            exit

// Pattern matching for complex decisions
match creature
    Elf(name, realm)
        print '.name hails from .realm'
    Wizard(name, color)
        print '.name the .color'
    else
        print "Unknown creature"

// Nested control with scoping
for realm in MiddleEarth.Realms
    if realm.HasRing
        foreach bearer in realm.RingBearers
            if bearer.IsCorrupted
                print "Found corrupted bearer in .realm.Name"
                exit
```

## Next Steps

- Learn the details of [Basic Syntax](syntax/basic-syntax.md)
- Master the [Ring System](advanced-concepts/memory-management.md)
- Explore [Collections](syntax/collections.md)
- Understand [Error Handling](syntax/error-handling.md)


camelCase:

Built-in primitive types (num, text, bool)
Keywords (public, private, do, if, while)
Method parameter names (personAge, personName)
Local variables (alice, people)

PascalCase:

Groups/Objects (Person)
Collections (List, Dictionary)
Public fields (Age, Name)
Methods/Functions (Greet, Length)
Properties (IsValid, Count)

SCREAMING_SNAKE_CASE:

Constants (PI, MAX_VALUE)

