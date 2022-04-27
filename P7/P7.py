from sly import Lexer
from sly import Parser
import turtle
class CalcLexer(Lexer):
    # Set of token names. This is always required 
    tokens = { NUMBER, BEGIN, FORWARD, RIGHT, LEFT, BACK, END, REPEAT, LCORCH, RCORCH }
    #literals = {'+', '*', '-'}
    ignore = ' \t;'
    BEGIN = r'BEGIN'
    FORWARD = r'FORWARD'
    RIGHT = r'RIGHT'
    LEFT = r'LEFT'
    BACK = r'BACK'
    END = r'END'
    REPEAT = r'REPEAT'
    LCORCH = r'\['
    RCORCH = r'\]'
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
        self.lista = []
        self.t = turtle.Turtle()
    # Get the token list from the lexer (required)
    tokens = CalcLexer.tokens
    debugfile = 'parser.log' 
    # Grammar rules and actions   
    @_('BEGIN INST END')
    def S(self,p):
        self.lista = []
        return p.INST

    @_('INST REPEAT NUMBER LCORCH INST RCORCH')
    def INST(self,p):
        print("Se repite " + str(p.NUMBER) + " veces: ")
        i = 0
        while i < p.NUMBER-1:
            for j,k in self.lista:
                if j == 1:
                    self.t.forward(k)
                elif j == 2:
                    self.t.back(k)
                elif j == 3:
                    self.t.left(k)
                else:
                    self.t.right(k)
            i = i+1
        return p.INST
       
    @_('INST FORWARD NUMBER')
    def INST(self,p):
        print("Movimiento hacia delante de " + str(p.NUMBER) + " unidades")
        self.t.forward(p.NUMBER)
        self.lista.append([1,p.NUMBER])
        return p.INST

    @_('INST BACK NUMBER')
    def INST(self,p):
        print("Movimiento hacia detras de " + str(p.NUMBER) + " unidades")
        self.t.back(p.NUMBER)
        self.lista.append([2,p.NUMBER])
        return p.INST

    @_('INST LEFT NUMBER')
    def INST(self,p):
        print("Giro a la izquierda de " + str(p.NUMBER) + " grados")
        self.t.left(p.NUMBER)
        self.lista.append([3,p.NUMBER])
        return p.INST

    @_('INST RIGHT NUMBER')
    def INST(self,p):
        print("Giro a la derecha de " + str(p.NUMBER) + " grados")
        self.t.right(p.NUMBER)
        self.lista.append([4,p.NUMBER])
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