from sly import Lexer
from sly import Parser

class CalcLexer(Lexer):
    tokens = {}
    ignore = ' \t'
    ignore_newline = r'\n+'
      
    @_(r'\d+')
    def NUMBER(self, t):
        t.value = int(t.value) 
        return t
    
    @_(r'\n+')
    def ignore_newline(self, t):
        self.lineno += t.value.count('\n')
        
    def error(self, t):
        print('Line %d: Bad character %r' % (self.lineno, t.value[0])) 
        self.index += 1
        
class CalcParser(Parser): 
    def __init__(self):
    tokens = CalcLexer.tokens
    debugfile = 'parser.log' 
    
    @_('BEGIN INST END')
    def S(self,p):
        self.lista = []
        return p.INST

   
    @_('')
    def empty(self, p):
        pass

    @_('empty')
    def INST(self,p):
        pass

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