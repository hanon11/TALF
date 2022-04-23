from sly import Lexer
from sly import Parser
class CalcLexer(Lexer):
    # Set of token names. This is always required 
    tokens = { NUMBER, PLUS, TIMES, MINUS, DIV, ASSIGN, ID, LPAREN,RPAREN }
    #literals = {'+', '*', '-'}
    ignore = ' \t'
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
    
    @_('NUMBER')
    def E(self, p):
        return p.NUMBER
    
    @_('ID')
    def E(self, p):
        return self.vars[p.ID]
    
    @_('E')
    def E1(self,p):
        return p.E

    @_('E DIV E1')
    def E(self, p):
        return p.E / p.E1
    
    @_('E TIMES E1')
    def E(self, p):
        return p.E * p.E1

    @_('E PLUS E1')
    def E(self, p):
        return p.E + p.E1

    @_('E MINUS E1')
    def E(self, p):
        return p.E - p.E1
   
    @_('LPAREN E RPAREN')
    def E(self, p):
        return p.E

    @_('MINUS E')
    def E(self, p):
        return -p.E
    
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