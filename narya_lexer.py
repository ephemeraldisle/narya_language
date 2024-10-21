from pygments.lexer import RegexLexer, words
from pygments.token import *

class NaryaLexer(RegexLexer):
    name = 'Narya'
    aliases = ['narya']
    filenames = ['*.narya']

    keywords = (
        'if', 'else', 'while', 'for', 'foreach', 'match', 'return', 'skip', 
        'exit', 'repeat', 'using', 'with', 'in', 'group', 'obj', 'object', 
        'enum', 'trait', 'act', 'action', 'do', 'new', 'const', 'core', 
        'inner', 'outer', 'public', 'private', 'viewable'
    )

    types = (
        'num', 'int', 'big int', 'uint', 'big uint', 'float', 'big float', 
        'text', 'char', 'string', 'bool', 'byte', 'List', 'Dictionary', 
        'Array', 'Set'
    )

    tokens = {
        'root': [
            (r'\s+', Text),
            (r'//.*?$', Comment.Single),
            (r'/\*.*?\*/', Comment.Multiline),
            (words(keywords, suffix=r'\b'), Keyword),
            (words(types, suffix=r'\b'), Keyword.Type),
            (r'"([^"\\]|\\.)*"', String),
            (r'\'([^\'\\]|\\.)*\'', String),
            (r'\d+\.\d+', Number.Float),
            (r'\d+', Number.Integer),
            (r'[a-zA-Z_]\w*', Name),
            (r'[.,;(){}[\]=<>+\-*/^%]', Punctuation),
        ]
    }