# Core Types

Add content for core-types.md here.



```narya
/*Output:

. , ( ) =     primary structural elements
" ' ! ?   modifiers
+ - / % * ^   maths
& | < <= == != >= > comparators
[ ] : collection access and expression declaration 
----------
&& ^^ || << >> ~ { } _   extremely rare
@ # $ ` ; \    ugh hideous gross keep them away

*/
```


BIT

```narya
type Bit(bit Value)
    [Alias: bit]
    Value = 0 | 1

    [Callable]
        bit And(bit other) => Value == 1 & bit.Value == 1 ? 1 | 0  
        bit Or(bit other) => Value == 1 | bit.Value == 1 ? 1 | 0    
        bit Not => Value == 1 ? 0 | 1    
        bit Xor(bit other) => Value != bit.Value ? 1 | 0
        
        bool Equals(bit other) => Value == other.Value
        text ToString => Value.ToString
        bit Copy => new Bit(Value)
        
        bit ShiftLeft(int positions) => positions > 0 ? 0 | Value
        bit ShiftRight(int positions) => positions > 0 ? 0 | Value

        Operator(&&).Overload(bit other) => And(other)
        Operator(||).Overload(bit other) => Or(other)
        Operator(!!).Overload => Not
        Operator(^^).Overload(bit other) => Xor(other)
        Operator(==).Overload(bit other) => Equals(other)
        Operator(!=).Overload(bit other) => !Equals(other)
        Operator(<<).Overload(int positions) => ShiftLeft(positions)
        Operator(>>).Overload(int positions) => ShiftRight(positions)

type bits8(Array(bit, 8) Value)
    [Callable]
        bit? Get(uint8 index) => 
            index >= 8 ?
                Warning.OutOfBounds |
                Value[index]

        bool? Set(uint8 index, bit value)
            if index >= 8
                return Warning.OutOfBounds 
            Value[index] = value
            return true
                    
        bits8 And(bits8 other)
            bits8 result
            for i = 0..7
                result.Value[i] = Value[i].And(other.Value[i])
            return result

        bits8 Or(bits8 other)
            bits8 result
            for i = 0..7
                result.Value[i] = Value[i].Or(other.Value[i])
            return result

        bits8 Not
            bits8 result
            for i = 0..7
                result.Value[i] = Value[i].Not
            return result

        bits8 Xor(bits8 other)
            bits8 result
            for i = 0..7
                result.Value[i] = Value[i].Xor(other.Value[i])
            return result

        bits8? ShiftLeft(uint8 positions)
            if positions >= 8: return Warning.OutOfBounds
            bits8 result
            for i = positions..7
                result.Value[i] = Value[i - positions]
            for i = 0..positions
                result.Value[i] = 0
            return result

        bits8? ShiftRight(uint8 positions)
            if positions >= 8: return Warning.OutOfBounds
            bits8 result
            uint8 limit = 7 - positions
            for i = 0..limit
                result.Value[i] = Value[i - positions]
            for i = limit..0
                result.Value[i] = 0
            return result

        bits8 RotateLeft(uint8 positions)
            if positions >= 8: return Warning.OutOfBounds
            bits8 result
            for i = 0..7
                uint8 newPos = (i + positions) % 8
                result.Value[newPos] = Value[i]
            return result

        bits8 RotateRight(uint8 positions)
            if positions >= 8: return Warning.OutOfBounds
            bits8 result
            for i = 0..7
                uint8 newPos = (i + (8 - positions)) % 8
                result.Value[newPos] = Value[i]
            return result

        uint8 PopCount
            uint8 count = 0
            for i = 0..7
                if Value[i] == 1: count += 1
            return count

        uint8? LeadingZeros
            for i = 7..0
                if Value[i] == 1: return 7 - i
            return 8

        uint8? TrailingZeros
            for i = 0..7
                if Value[i] == 1: return i
            return 8

        uint8? MostSignificantBit
            for i = 7..0
                if Value[i] == 1: return i
            return Warning.NotFound

        uint8? LeastSignificantBit
            for i = 0..7
                if Value[i] == 1: return i
            return Warning.NotFound

        string ToString
            string result = ""
            for i = 7..0
                result += Value[i].ToString
            return result

        Operator(&&).Overload(bits8 other) => And(other)
        Operator(||).Overload(bits8 other) => Or(other)
        Operator(!!).Overload => Not
        Operator(^^).Overload(bits8 other) => Xor(other)
        Operator(<<).Overload(uint8 positions) => ShiftLeft(positions)
        Operator(>>).Overload(uint8 positions) => ShiftRight(positions)
        Operator(<<<).Overload(uint8 positions) => RotateLeft(positions)
        Operator(>>>).Overload(uint8 positions) => RotateRight(positions)







type uint8(bits8 Value)
    [Alias: byte]
    [Constructors]
        uint8?(int value)
            if value < 0 || value > 255
                return Warning.OutOfRange
            Value = bits8
            for i = 0..7
                Value.Set(i, (value & (1 << i)) != 0 ? 1 | 0)

    [Callable]
        uint8? Add(uint8 other)
            uint8 result = 0
            bit carry = 0
            for i = 0..7
                bit a = Value.Get(i)
                bit b = other.Value.Get(i)
                
                bit sum = a.Xor(b).Xor(carry)
                carry = (a.And(b)).Or(b.And(carry)).Or(carry.And(a))
                
                result.Value.Set(i, sum)
            
            return carry == 1 ? Warning.Overflow | result

        uint8? Subtract(uint8 other)
            uint8 result = 0
            bit borrow = 0
            for i = 0..7
                bit a = Value.Get(i)
                bit b = other.Value.Get(i)
                
                bit diff = a.Xor(b).Xor(borrow)
                borrow = (!a.And(b)).Or(b.And(borrow)).Or(borrow.And(!a))
                
                result.Value.Set(i, diff)
            
            return borrow == 1 ? Warning.Underflow | result

        uint8? Multiply(uint8 other)
            uint8 result = 0
            uint8 temp = Value
            
            for i = 0..7
                if other.Value.Get(i) == 1
                    result? = result.Add(temp)
                    if result is Warning: return Warning.Overflow
                temp? = temp.ShiftLeft(1)
                if temp is Warning: return Warning.Overflow
            
            return result

        uint8? Divide(uint8 other)
            if other == 0: return Warning.DivideByZero
            
            uint8 quotient = 0
            uint8 remainder = Value
            
            for i = 7..0
                remainder? = remainder.ShiftLeft(1)
                if remainder is Warning: return Warning.DivideByZero
                
                quotient? = quotient.ShiftLeft(1)
                if quotient is Warning: return Warning.DivideByZero
                
                if remainder >= other
                    remainder? = remainder.Subtract(other)
                    if remainder is Warning: return Warning.DivideByZero
                    quotient.Value.Set(0, 1)
            
            return quotient

        // Comparison operations
        bool GreaterThan(uint8 other)
            for i = 7..0
                bit a = Value.Get(i)
                bit b = other.Value.Get(i)
                if a != b: return a > b
            return false

        bool LessThan(uint8 other)
            for i = 7..0
                bit a = Value.Get(i)
                bit b = other.Value.Get(i)
                if a != b: return a < b
            return false

        // Conversion operations
        string ToString
            uint result = 0
            uint power = 1
            for i = 0..7
                if Value.Get(i) == 1
                    result += power
                power *= 2
            return result.ToString

        // Operator overloads
        Operator(+).Overload(uint8 other) => Add(other)
        Operator(-).Overload(uint8 other) => Subtract(other)
        Operator(*).Overload(uint8 other) => Multiply(other)
        Operator(/).Overload(uint8 other) => Divide(other)
        Operator(>).Overload(uint8 other) => GreaterThan(other)
        Operator(<).Overload(uint8 other) => LessThan(other)
        Operator(>=).Overload(uint8 other) => GreaterThan(other) || Equals(other)
        Operator(<=).Overload(uint8 other) => LessThan(other) || Equals(other)


```