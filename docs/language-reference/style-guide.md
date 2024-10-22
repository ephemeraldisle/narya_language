# Narya Syntax Highlighting Guide

## Theme Philosophy
The Narya syntax highlighting scheme draws inspiration from the Ring of Fire and the craftsmanship of the Elves. The color palette emphasizes warmth and power while maintaining readability for extended coding sessions.

## Core Colors

### Ring-Inspired Colors
- `--narya-red: #ff2b48` - Bright red representing Narya's power, used for type keywords
- `--firey-orange: #ff3f3f` - Warm orange for control keywords (if, for, while)
- `--bright-gold: #c5a572` - Rich gold for classes and operators, echoing the ring's metalwork
- `--pale-gold: #f3c551` - Softer gold providing contrast where needed

### Elven-Crafted Colors
- `--nenya-blue: #5db6ff` - Clear blue for access modifiers (public, private)
- `--vilya-white: #dcd6c0` - Soft white for base text and variables
- `--mithril-silver: #c1c1cd` - Standard string literals
- `--mithrilium-silver: #c4c4e1` - Interpolated strings, slightly brighter than regular strings
- `--forest-green: #53b953` - Lothlorien green for attributes and functions

### Supporting Colors
- `--shadow-grey: #7b6645` - Recessed color for punctuation
- `#ac5eb6` (purple) - Comments, suggesting ancient wisdom
- `#3b2d28` - Rich brown background evoking aged parchment

## Semantic Color Usage

### Keywords and Structure
- Control flow (if, for, while) → Firey Orange
- Type keywords (num, text) → Narya Red
- Access modifiers (public, private) → Nenya Blue

### Names and Identifiers
- Classes/Types → Bright Gold
- Attributes/Functions → Forest Green
- Variables → Vilya White
- Constants → Narya Red

### Literals
- Regular Strings → Mithril Silver
- Interpolated Strings → Mithrilium Silver (slightly brighter)
- Numbers inherit from base text → Vilya White

### Operators and Punctuation
- Operators → Bright Gold (matching classes for visual weight)
- Punctuation → Shadow Grey (visually recessed)

### Documentation
- Comments → Purple (distinct from code elements)

## Usage Notes
- The warm background color promotes readability during long coding sessions
- Semantic color relationships help reinforce language concepts
- Critical elements (keywords, operators) use warmer colors
- Supporting elements (punctuation, strings) use cooler colors
- Color contrasts are designed to be clear but not harsh