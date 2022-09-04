from sly import Lexer
from sly import Parser
class CalcLexer(Lexer):
    # Set of token names. This is always required 
    tokens = { NUMBER, PLUS, TIMES, MINUS, DIV, ASSIGN, ID, LPAREN, RPAREN }
    #literals = {'+', '*', '-'}
    ignore = ' \t;'
    PLUS   = r'\+' 
    TIMES  = r'\*'
    MINUS  = r'\-' 
    DIV    = r'\/' 
    ASSIGN = r'\='
    LPAREN = r'\('
    RPAREN = r'\)'
    ignore_newline = r'\n+'
      
    @_(r'\d+')
    def NUMBER(self, t):
        t.value = int(t.value) 
        return t
        # Line number tracking
        
    @_(r'\w+')
    def ID(self, t):
        return t
    
    @_(r'\n+')
    def ignore_newline(self, t):
        self.lineno += t.value.count('\n')
        
    def error(self, t):
        print('Line %d: Bad character %r' % (self.lineno, t.value[0])) 
        self.index += 1
        

class CalcParser(Parser): 
    def __init__(self):
        self.vars = {}
    # Get the token list from the lexer (required)
    tokens = CalcLexer.tokens
    # Grammar rules and actions   
    @_('ID ASSIGN E')
    def assign(self,p):
        self.vars[p.ID] = p.E
        print(self.vars[p.ID])

    @_('E')
    def assign(self,p):
        return p.E

    @_('ID ASSIGN E')
    def E(self,p):
        self.vars[p.ID] = p.E
        return p.E

    @_('E PLUS suma')
    def E(self, p):
        return p.E + p.suma

    @_('E MINUS suma')
    def E(self, p):
        return p.E - p.suma

    @_('suma')
    def E(self, p):
        return p.suma

    @_('suma TIMES fact')
    def suma(self, p):
        return p.suma * p.fact

    @_('suma DIV fact')
    def suma(self, p):
        return p.suma / p.fact

    @_('fact')
    def suma(self, p):
        return p.fact

    @_('MINUS LPAREN E RPAREN')
    def fact(self,p):
        return -p.E

    @_('LPAREN E RPAREN')
    def fact(self, p):
        return p.E

    @_('NUMBER')
    def fact(self, p):
        return p.NUMBER

    @_('MINUS NUMBER')
    def fact(self, p):
        return -p.NUMBER

    @_('ID')
    def fact(self, p):
        return self.vars[p.ID]


    
    
lexer = CalcLexer() 
parser = CalcParser()
while True: 
    try:
        text = input('Introduce operation: ') 
        result = parser.parse(lexer.tokenize(text)) 
        print(result)
        if len(text)==0:
            break 
    except:
        break