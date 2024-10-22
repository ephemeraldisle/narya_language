from pygments.lexers import get_all_lexers
from pygments.formatters import HtmlFormatter
from pygments import highlight
from pygments.util import ClassNotFound

# Print all available lexers
print("Available lexers:")
for lexer in get_all_lexers():
    print(f"- {lexer[0]} ({lexer[1]})")

# Try to use our Narya lexer
try:
    from pygments.lexers import get_lexer_by_name
    narya_lexer = get_lexer_by_name("narya")
    print("\nNarya lexer found!")
    
    # Test the lexer
    code = '''ring Main
    group Person
        num Age
        text Name'''
    
    print("\nTest highlighting:")
    print(highlight(code, narya_lexer, HtmlFormatter()))
except ClassNotFound:
    print("\nNarya lexer not found!")