# Generated from /Users/lorenzobacchiani/Desktop/abs_deployer/bind_preference_grammar/BindPreferenceGrammar.g4 by ANTLR 4.13.1
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,39,149,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,1,0,1,0,1,0,1,1,1,1,3,1,
        42,8,1,1,2,1,2,1,2,1,2,5,2,48,8,2,10,2,12,2,51,9,2,1,3,3,3,54,8,
        3,1,3,1,3,1,4,1,4,3,4,60,8,4,1,5,1,5,1,5,1,5,3,5,66,8,5,1,6,1,6,
        1,6,1,6,5,6,72,8,6,10,6,12,6,75,9,6,1,7,1,7,1,7,1,7,1,7,3,7,82,8,
        7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,
        7,3,7,100,8,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,3,
        7,114,8,7,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,3,8,127,8,
        8,1,9,1,9,3,9,131,8,9,1,10,1,10,1,11,1,11,1,12,1,12,1,13,1,13,1,
        14,1,14,1,15,1,15,1,16,1,16,1,17,1,17,1,17,0,0,18,0,2,4,6,8,10,12,
        14,16,18,20,22,24,26,28,30,32,34,0,5,1,0,20,21,2,0,13,14,18,19,1,
        0,30,32,1,0,24,29,1,0,16,17,147,0,36,1,0,0,0,2,41,1,0,0,0,4,43,1,
        0,0,0,6,53,1,0,0,0,8,59,1,0,0,0,10,61,1,0,0,0,12,67,1,0,0,0,14,113,
        1,0,0,0,16,126,1,0,0,0,18,130,1,0,0,0,20,132,1,0,0,0,22,134,1,0,
        0,0,24,136,1,0,0,0,26,138,1,0,0,0,28,140,1,0,0,0,30,142,1,0,0,0,
        32,144,1,0,0,0,34,146,1,0,0,0,36,37,3,2,1,0,37,38,5,0,0,1,38,1,1,
        0,0,0,39,42,5,1,0,0,40,42,3,12,6,0,41,39,1,0,0,0,41,40,1,0,0,0,42,
        3,1,0,0,0,43,49,3,6,3,0,44,45,3,20,10,0,45,46,3,6,3,0,46,48,1,0,
        0,0,47,44,1,0,0,0,48,51,1,0,0,0,49,47,1,0,0,0,49,50,1,0,0,0,50,5,
        1,0,0,0,51,49,1,0,0,0,52,54,3,28,14,0,53,52,1,0,0,0,53,54,1,0,0,
        0,54,55,1,0,0,0,55,56,3,8,4,0,56,7,1,0,0,0,57,60,3,30,15,0,58,60,
        3,10,5,0,59,57,1,0,0,0,59,58,1,0,0,0,60,9,1,0,0,0,61,65,3,12,6,0,
        62,63,3,26,13,0,63,64,3,12,6,0,64,66,1,0,0,0,65,62,1,0,0,0,65,66,
        1,0,0,0,66,11,1,0,0,0,67,73,3,14,7,0,68,69,3,22,11,0,69,70,3,14,
        7,0,70,72,1,0,0,0,71,68,1,0,0,0,72,75,1,0,0,0,73,71,1,0,0,0,73,74,
        1,0,0,0,74,13,1,0,0,0,75,73,1,0,0,0,76,77,7,0,0,0,77,81,3,32,16,
        0,78,79,5,2,0,0,79,80,5,3,0,0,80,82,3,16,8,0,81,78,1,0,0,0,81,82,
        1,0,0,0,82,83,1,0,0,0,83,84,5,4,0,0,84,85,3,18,9,0,85,86,5,5,0,0,
        86,87,3,4,2,0,87,114,1,0,0,0,88,114,5,38,0,0,89,90,3,32,16,0,90,
        91,5,6,0,0,91,92,5,7,0,0,92,93,3,32,16,0,93,114,1,0,0,0,94,95,5,
        22,0,0,95,99,3,32,16,0,96,97,5,2,0,0,97,98,5,3,0,0,98,100,3,16,8,
        0,99,96,1,0,0,0,99,100,1,0,0,0,100,101,1,0,0,0,101,102,5,4,0,0,102,
        103,3,18,9,0,103,104,5,5,0,0,104,105,3,12,6,0,105,114,1,0,0,0,106,
        107,3,24,12,0,107,108,3,12,6,0,108,114,1,0,0,0,109,110,5,8,0,0,110,
        111,3,4,2,0,111,112,5,9,0,0,112,114,1,0,0,0,113,76,1,0,0,0,113,88,
        1,0,0,0,113,89,1,0,0,0,113,94,1,0,0,0,113,106,1,0,0,0,113,109,1,
        0,0,0,114,15,1,0,0,0,115,127,5,37,0,0,116,127,3,32,16,0,117,118,
        5,37,0,0,118,119,5,10,0,0,119,120,5,37,0,0,120,127,5,11,0,0,121,
        122,5,37,0,0,122,123,5,10,0,0,123,124,3,34,17,0,124,125,5,11,0,0,
        125,127,1,0,0,0,126,115,1,0,0,0,126,116,1,0,0,0,126,117,1,0,0,0,
        126,121,1,0,0,0,127,17,1,0,0,0,128,131,5,35,0,0,129,131,3,34,17,
        0,130,128,1,0,0,0,130,129,1,0,0,0,131,19,1,0,0,0,132,133,7,1,0,0,
        133,21,1,0,0,0,134,135,7,2,0,0,135,23,1,0,0,0,136,137,5,33,0,0,137,
        25,1,0,0,0,138,139,7,3,0,0,139,27,1,0,0,0,140,141,5,15,0,0,141,29,
        1,0,0,0,142,143,7,4,0,0,143,31,1,0,0,0,144,145,5,36,0,0,145,33,1,
        0,0,0,146,147,5,12,0,0,147,35,1,0,0,0,11,41,49,53,59,65,73,81,99,
        113,126,130
    ]

class BindPreferenceGrammarParser ( Parser ):

    grammarFileName = "BindPreferenceGrammar.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'local'", "'of'", "'type'", "'in'", "':'", 
                     "'used'", "'by'", "'('", "')'", "'['", "']'", "<INVALID>", 
                     "'and'", "'or'", "'not'", "'true'", "'false'", "'impl'", 
                     "'iff'", "'exists'", "'forall'", "'sum'", "'cost'", 
                     "'<='", "'='", "'>='", "'<'", "'>'", "'!='", "'+'", 
                     "'-'", "'*'", "'abs'", "'obj'", "'DC'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "RE", "AND", "OR", "NOT", "TRUE", "FALSE", "IMPL", 
                      "IFF", "EXISTS", "FORALL", "SUM", "COST", "LEQ", "EQ", 
                      "GEQ", "LT", "GT", "NEQ", "PLUS", "MINUS", "TIMES", 
                      "ABS", "OBJ", "DC", "VARIABLE", "ID", "INT", "WS" ]

    RULE_statement = 0
    RULE_preference = 1
    RULE_b_expr = 2
    RULE_b_term = 3
    RULE_b_factor = 4
    RULE_relation = 5
    RULE_expr = 6
    RULE_term = 7
    RULE_objId = 8
    RULE_typeV = 9
    RULE_bool_binary_op = 10
    RULE_arith_binary_op = 11
    RULE_arith_unary_op = 12
    RULE_comparison_op = 13
    RULE_unaryOp = 14
    RULE_boolFact = 15
    RULE_variable = 16
    RULE_re = 17

    ruleNames =  [ "statement", "preference", "b_expr", "b_term", "b_factor", 
                   "relation", "expr", "term", "objId", "typeV", "bool_binary_op", 
                   "arith_binary_op", "arith_unary_op", "comparison_op", 
                   "unaryOp", "boolFact", "variable", "re" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    T__6=7
    T__7=8
    T__8=9
    T__9=10
    T__10=11
    RE=12
    AND=13
    OR=14
    NOT=15
    TRUE=16
    FALSE=17
    IMPL=18
    IFF=19
    EXISTS=20
    FORALL=21
    SUM=22
    COST=23
    LEQ=24
    EQ=25
    GEQ=26
    LT=27
    GT=28
    NEQ=29
    PLUS=30
    MINUS=31
    TIMES=32
    ABS=33
    OBJ=34
    DC=35
    VARIABLE=36
    ID=37
    INT=38
    WS=39

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class StatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def preference(self):
            return self.getTypedRuleContext(BindPreferenceGrammarParser.PreferenceContext,0)


        def EOF(self):
            return self.getToken(BindPreferenceGrammarParser.EOF, 0)

        def getRuleIndex(self):
            return BindPreferenceGrammarParser.RULE_statement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStatement" ):
                listener.enterStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStatement" ):
                listener.exitStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStatement" ):
                return visitor.visitStatement(self)
            else:
                return visitor.visitChildren(self)




    def statement(self):

        localctx = BindPreferenceGrammarParser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 36
            self.preference()
            self.state = 37
            self.match(BindPreferenceGrammarParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PreferenceContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return BindPreferenceGrammarParser.RULE_preference

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class ApreferenceExprContext(PreferenceContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a BindPreferenceGrammarParser.PreferenceContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self):
            return self.getTypedRuleContext(BindPreferenceGrammarParser.ExprContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterApreferenceExpr" ):
                listener.enterApreferenceExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitApreferenceExpr" ):
                listener.exitApreferenceExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitApreferenceExpr" ):
                return visitor.visitApreferenceExpr(self)
            else:
                return visitor.visitChildren(self)


    class ApreferenceLocalContext(PreferenceContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a BindPreferenceGrammarParser.PreferenceContext
            super().__init__(parser)
            self.copyFrom(ctx)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterApreferenceLocal" ):
                listener.enterApreferenceLocal(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitApreferenceLocal" ):
                listener.exitApreferenceLocal(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitApreferenceLocal" ):
                return visitor.visitApreferenceLocal(self)
            else:
                return visitor.visitChildren(self)



    def preference(self):

        localctx = BindPreferenceGrammarParser.PreferenceContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_preference)
        try:
            self.state = 41
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [1]:
                localctx = BindPreferenceGrammarParser.ApreferenceLocalContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 39
                self.match(BindPreferenceGrammarParser.T__0)
                pass
            elif token in [8, 20, 21, 22, 33, 36, 38]:
                localctx = BindPreferenceGrammarParser.ApreferenceExprContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 40
                self.expr()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class B_exprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def b_term(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BindPreferenceGrammarParser.B_termContext)
            else:
                return self.getTypedRuleContext(BindPreferenceGrammarParser.B_termContext,i)


        def bool_binary_op(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BindPreferenceGrammarParser.Bool_binary_opContext)
            else:
                return self.getTypedRuleContext(BindPreferenceGrammarParser.Bool_binary_opContext,i)


        def getRuleIndex(self):
            return BindPreferenceGrammarParser.RULE_b_expr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterB_expr" ):
                listener.enterB_expr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitB_expr" ):
                listener.exitB_expr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitB_expr" ):
                return visitor.visitB_expr(self)
            else:
                return visitor.visitChildren(self)




    def b_expr(self):

        localctx = BindPreferenceGrammarParser.B_exprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_b_expr)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 43
            self.b_term()
            self.state = 49
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,1,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 44
                    self.bool_binary_op()
                    self.state = 45
                    self.b_term() 
                self.state = 51
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,1,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class B_termContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def b_factor(self):
            return self.getTypedRuleContext(BindPreferenceGrammarParser.B_factorContext,0)


        def unaryOp(self):
            return self.getTypedRuleContext(BindPreferenceGrammarParser.UnaryOpContext,0)


        def getRuleIndex(self):
            return BindPreferenceGrammarParser.RULE_b_term

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterB_term" ):
                listener.enterB_term(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitB_term" ):
                listener.exitB_term(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitB_term" ):
                return visitor.visitB_term(self)
            else:
                return visitor.visitChildren(self)




    def b_term(self):

        localctx = BindPreferenceGrammarParser.B_termContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_b_term)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 53
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==15:
                self.state = 52
                self.unaryOp()


            self.state = 55
            self.b_factor()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class B_factorContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def boolFact(self):
            return self.getTypedRuleContext(BindPreferenceGrammarParser.BoolFactContext,0)


        def relation(self):
            return self.getTypedRuleContext(BindPreferenceGrammarParser.RelationContext,0)


        def getRuleIndex(self):
            return BindPreferenceGrammarParser.RULE_b_factor

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterB_factor" ):
                listener.enterB_factor(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitB_factor" ):
                listener.exitB_factor(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitB_factor" ):
                return visitor.visitB_factor(self)
            else:
                return visitor.visitChildren(self)




    def b_factor(self):

        localctx = BindPreferenceGrammarParser.B_factorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_b_factor)
        try:
            self.state = 59
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [16, 17]:
                self.enterOuterAlt(localctx, 1)
                self.state = 57
                self.boolFact()
                pass
            elif token in [8, 20, 21, 22, 33, 36, 38]:
                self.enterOuterAlt(localctx, 2)
                self.state = 58
                self.relation()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class RelationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BindPreferenceGrammarParser.ExprContext)
            else:
                return self.getTypedRuleContext(BindPreferenceGrammarParser.ExprContext,i)


        def comparison_op(self):
            return self.getTypedRuleContext(BindPreferenceGrammarParser.Comparison_opContext,0)


        def getRuleIndex(self):
            return BindPreferenceGrammarParser.RULE_relation

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRelation" ):
                listener.enterRelation(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRelation" ):
                listener.exitRelation(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRelation" ):
                return visitor.visitRelation(self)
            else:
                return visitor.visitChildren(self)




    def relation(self):

        localctx = BindPreferenceGrammarParser.RelationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_relation)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 61
            self.expr()
            self.state = 65
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
            if la_ == 1:
                self.state = 62
                self.comparison_op()
                self.state = 63
                self.expr()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def term(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BindPreferenceGrammarParser.TermContext)
            else:
                return self.getTypedRuleContext(BindPreferenceGrammarParser.TermContext,i)


        def arith_binary_op(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BindPreferenceGrammarParser.Arith_binary_opContext)
            else:
                return self.getTypedRuleContext(BindPreferenceGrammarParser.Arith_binary_opContext,i)


        def getRuleIndex(self):
            return BindPreferenceGrammarParser.RULE_expr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpr" ):
                listener.enterExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpr" ):
                listener.exitExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr" ):
                return visitor.visitExpr(self)
            else:
                return visitor.visitChildren(self)




    def expr(self):

        localctx = BindPreferenceGrammarParser.ExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_expr)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 67
            self.term()
            self.state = 73
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,5,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 68
                    self.arith_binary_op()
                    self.state = 69
                    self.term() 
                self.state = 75
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,5,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TermContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return BindPreferenceGrammarParser.RULE_term

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class AexprQuantifierContext(TermContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a BindPreferenceGrammarParser.TermContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def variable(self):
            return self.getTypedRuleContext(BindPreferenceGrammarParser.VariableContext,0)

        def typeV(self):
            return self.getTypedRuleContext(BindPreferenceGrammarParser.TypeVContext,0)

        def b_expr(self):
            return self.getTypedRuleContext(BindPreferenceGrammarParser.B_exprContext,0)

        def EXISTS(self):
            return self.getToken(BindPreferenceGrammarParser.EXISTS, 0)
        def FORALL(self):
            return self.getToken(BindPreferenceGrammarParser.FORALL, 0)
        def objId(self):
            return self.getTypedRuleContext(BindPreferenceGrammarParser.ObjIdContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAexprQuantifier" ):
                listener.enterAexprQuantifier(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAexprQuantifier" ):
                listener.exitAexprQuantifier(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAexprQuantifier" ):
                return visitor.visitAexprQuantifier(self)
            else:
                return visitor.visitChildren(self)


    class AexprSumContext(TermContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a BindPreferenceGrammarParser.TermContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def SUM(self):
            return self.getToken(BindPreferenceGrammarParser.SUM, 0)
        def variable(self):
            return self.getTypedRuleContext(BindPreferenceGrammarParser.VariableContext,0)

        def typeV(self):
            return self.getTypedRuleContext(BindPreferenceGrammarParser.TypeVContext,0)

        def expr(self):
            return self.getTypedRuleContext(BindPreferenceGrammarParser.ExprContext,0)

        def objId(self):
            return self.getTypedRuleContext(BindPreferenceGrammarParser.ObjIdContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAexprSum" ):
                listener.enterAexprSum(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAexprSum" ):
                listener.exitAexprSum(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAexprSum" ):
                return visitor.visitAexprSum(self)
            else:
                return visitor.visitChildren(self)


    class AexprBindContext(TermContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a BindPreferenceGrammarParser.TermContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def variable(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BindPreferenceGrammarParser.VariableContext)
            else:
                return self.getTypedRuleContext(BindPreferenceGrammarParser.VariableContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAexprBind" ):
                listener.enterAexprBind(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAexprBind" ):
                listener.exitAexprBind(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAexprBind" ):
                return visitor.visitAexprBind(self)
            else:
                return visitor.visitChildren(self)


    class AexprBracketsContext(TermContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a BindPreferenceGrammarParser.TermContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def b_expr(self):
            return self.getTypedRuleContext(BindPreferenceGrammarParser.B_exprContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAexprBrackets" ):
                listener.enterAexprBrackets(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAexprBrackets" ):
                listener.exitAexprBrackets(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAexprBrackets" ):
                return visitor.visitAexprBrackets(self)
            else:
                return visitor.visitChildren(self)


    class AexprUnaryArithmeticContext(TermContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a BindPreferenceGrammarParser.TermContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def arith_unary_op(self):
            return self.getTypedRuleContext(BindPreferenceGrammarParser.Arith_unary_opContext,0)

        def expr(self):
            return self.getTypedRuleContext(BindPreferenceGrammarParser.ExprContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAexprUnaryArithmetic" ):
                listener.enterAexprUnaryArithmetic(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAexprUnaryArithmetic" ):
                listener.exitAexprUnaryArithmetic(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAexprUnaryArithmetic" ):
                return visitor.visitAexprUnaryArithmetic(self)
            else:
                return visitor.visitChildren(self)


    class AexprIntContext(TermContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a BindPreferenceGrammarParser.TermContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def INT(self):
            return self.getToken(BindPreferenceGrammarParser.INT, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAexprInt" ):
                listener.enterAexprInt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAexprInt" ):
                listener.exitAexprInt(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAexprInt" ):
                return visitor.visitAexprInt(self)
            else:
                return visitor.visitChildren(self)



    def term(self):

        localctx = BindPreferenceGrammarParser.TermContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_term)
        self._la = 0 # Token type
        try:
            self.state = 113
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [20, 21]:
                localctx = BindPreferenceGrammarParser.AexprQuantifierContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 76
                _la = self._input.LA(1)
                if not(_la==20 or _la==21):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 77
                self.variable()
                self.state = 81
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==2:
                    self.state = 78
                    self.match(BindPreferenceGrammarParser.T__1)
                    self.state = 79
                    self.match(BindPreferenceGrammarParser.T__2)
                    self.state = 80
                    self.objId()


                self.state = 83
                self.match(BindPreferenceGrammarParser.T__3)
                self.state = 84
                self.typeV()
                self.state = 85
                self.match(BindPreferenceGrammarParser.T__4)
                self.state = 86
                self.b_expr()
                pass
            elif token in [38]:
                localctx = BindPreferenceGrammarParser.AexprIntContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 88
                self.match(BindPreferenceGrammarParser.INT)
                pass
            elif token in [36]:
                localctx = BindPreferenceGrammarParser.AexprBindContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 89
                self.variable()
                self.state = 90
                self.match(BindPreferenceGrammarParser.T__5)
                self.state = 91
                self.match(BindPreferenceGrammarParser.T__6)
                self.state = 92
                self.variable()
                pass
            elif token in [22]:
                localctx = BindPreferenceGrammarParser.AexprSumContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 94
                self.match(BindPreferenceGrammarParser.SUM)
                self.state = 95
                self.variable()
                self.state = 99
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==2:
                    self.state = 96
                    self.match(BindPreferenceGrammarParser.T__1)
                    self.state = 97
                    self.match(BindPreferenceGrammarParser.T__2)
                    self.state = 98
                    self.objId()


                self.state = 101
                self.match(BindPreferenceGrammarParser.T__3)
                self.state = 102
                self.typeV()
                self.state = 103
                self.match(BindPreferenceGrammarParser.T__4)
                self.state = 104
                self.expr()
                pass
            elif token in [33]:
                localctx = BindPreferenceGrammarParser.AexprUnaryArithmeticContext(self, localctx)
                self.enterOuterAlt(localctx, 5)
                self.state = 106
                self.arith_unary_op()
                self.state = 107
                self.expr()
                pass
            elif token in [8]:
                localctx = BindPreferenceGrammarParser.AexprBracketsContext(self, localctx)
                self.enterOuterAlt(localctx, 6)
                self.state = 109
                self.match(BindPreferenceGrammarParser.T__7)
                self.state = 110
                self.b_expr()
                self.state = 111
                self.match(BindPreferenceGrammarParser.T__8)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ObjIdContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return BindPreferenceGrammarParser.RULE_objId

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class AobjIDScenarioContext(ObjIdContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a BindPreferenceGrammarParser.ObjIdContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(BindPreferenceGrammarParser.ID)
            else:
                return self.getToken(BindPreferenceGrammarParser.ID, i)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAobjIDScenario" ):
                listener.enterAobjIDScenario(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAobjIDScenario" ):
                listener.exitAobjIDScenario(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAobjIDScenario" ):
                return visitor.visitAobjIDScenario(self)
            else:
                return visitor.visitChildren(self)


    class AobjIDREContext(ObjIdContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a BindPreferenceGrammarParser.ObjIdContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def ID(self):
            return self.getToken(BindPreferenceGrammarParser.ID, 0)
        def re(self):
            return self.getTypedRuleContext(BindPreferenceGrammarParser.ReContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAobjIDRE" ):
                listener.enterAobjIDRE(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAobjIDRE" ):
                listener.exitAobjIDRE(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAobjIDRE" ):
                return visitor.visitAobjIDRE(self)
            else:
                return visitor.visitChildren(self)


    class AobjIDVarContext(ObjIdContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a BindPreferenceGrammarParser.ObjIdContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def variable(self):
            return self.getTypedRuleContext(BindPreferenceGrammarParser.VariableContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAobjIDVar" ):
                listener.enterAobjIDVar(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAobjIDVar" ):
                listener.exitAobjIDVar(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAobjIDVar" ):
                return visitor.visitAobjIDVar(self)
            else:
                return visitor.visitChildren(self)


    class AobjIDIDContext(ObjIdContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a BindPreferenceGrammarParser.ObjIdContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def ID(self):
            return self.getToken(BindPreferenceGrammarParser.ID, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAobjIDID" ):
                listener.enterAobjIDID(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAobjIDID" ):
                listener.exitAobjIDID(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAobjIDID" ):
                return visitor.visitAobjIDID(self)
            else:
                return visitor.visitChildren(self)



    def objId(self):

        localctx = BindPreferenceGrammarParser.ObjIdContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_objId)
        try:
            self.state = 126
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,9,self._ctx)
            if la_ == 1:
                localctx = BindPreferenceGrammarParser.AobjIDIDContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 115
                self.match(BindPreferenceGrammarParser.ID)
                pass

            elif la_ == 2:
                localctx = BindPreferenceGrammarParser.AobjIDVarContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 116
                self.variable()
                pass

            elif la_ == 3:
                localctx = BindPreferenceGrammarParser.AobjIDScenarioContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 117
                self.match(BindPreferenceGrammarParser.ID)
                self.state = 118
                self.match(BindPreferenceGrammarParser.T__9)
                self.state = 119
                self.match(BindPreferenceGrammarParser.ID)
                self.state = 120
                self.match(BindPreferenceGrammarParser.T__10)
                pass

            elif la_ == 4:
                localctx = BindPreferenceGrammarParser.AobjIDREContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 121
                self.match(BindPreferenceGrammarParser.ID)
                self.state = 122
                self.match(BindPreferenceGrammarParser.T__9)
                self.state = 123
                self.re()
                self.state = 124
                self.match(BindPreferenceGrammarParser.T__10)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TypeVContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def DC(self):
            return self.getToken(BindPreferenceGrammarParser.DC, 0)

        def re(self):
            return self.getTypedRuleContext(BindPreferenceGrammarParser.ReContext,0)


        def getRuleIndex(self):
            return BindPreferenceGrammarParser.RULE_typeV

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTypeV" ):
                listener.enterTypeV(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTypeV" ):
                listener.exitTypeV(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTypeV" ):
                return visitor.visitTypeV(self)
            else:
                return visitor.visitChildren(self)




    def typeV(self):

        localctx = BindPreferenceGrammarParser.TypeVContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_typeV)
        try:
            self.state = 130
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [35]:
                self.enterOuterAlt(localctx, 1)
                self.state = 128
                self.match(BindPreferenceGrammarParser.DC)
                pass
            elif token in [12]:
                self.enterOuterAlt(localctx, 2)
                self.state = 129
                self.re()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Bool_binary_opContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def AND(self):
            return self.getToken(BindPreferenceGrammarParser.AND, 0)

        def OR(self):
            return self.getToken(BindPreferenceGrammarParser.OR, 0)

        def IMPL(self):
            return self.getToken(BindPreferenceGrammarParser.IMPL, 0)

        def IFF(self):
            return self.getToken(BindPreferenceGrammarParser.IFF, 0)

        def getRuleIndex(self):
            return BindPreferenceGrammarParser.RULE_bool_binary_op

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBool_binary_op" ):
                listener.enterBool_binary_op(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBool_binary_op" ):
                listener.exitBool_binary_op(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBool_binary_op" ):
                return visitor.visitBool_binary_op(self)
            else:
                return visitor.visitChildren(self)




    def bool_binary_op(self):

        localctx = BindPreferenceGrammarParser.Bool_binary_opContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_bool_binary_op)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 132
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 811008) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Arith_binary_opContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def PLUS(self):
            return self.getToken(BindPreferenceGrammarParser.PLUS, 0)

        def MINUS(self):
            return self.getToken(BindPreferenceGrammarParser.MINUS, 0)

        def TIMES(self):
            return self.getToken(BindPreferenceGrammarParser.TIMES, 0)

        def getRuleIndex(self):
            return BindPreferenceGrammarParser.RULE_arith_binary_op

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterArith_binary_op" ):
                listener.enterArith_binary_op(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitArith_binary_op" ):
                listener.exitArith_binary_op(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArith_binary_op" ):
                return visitor.visitArith_binary_op(self)
            else:
                return visitor.visitChildren(self)




    def arith_binary_op(self):

        localctx = BindPreferenceGrammarParser.Arith_binary_opContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_arith_binary_op)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 134
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 7516192768) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Arith_unary_opContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ABS(self):
            return self.getToken(BindPreferenceGrammarParser.ABS, 0)

        def getRuleIndex(self):
            return BindPreferenceGrammarParser.RULE_arith_unary_op

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterArith_unary_op" ):
                listener.enterArith_unary_op(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitArith_unary_op" ):
                listener.exitArith_unary_op(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArith_unary_op" ):
                return visitor.visitArith_unary_op(self)
            else:
                return visitor.visitChildren(self)




    def arith_unary_op(self):

        localctx = BindPreferenceGrammarParser.Arith_unary_opContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_arith_unary_op)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 136
            self.match(BindPreferenceGrammarParser.ABS)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Comparison_opContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LEQ(self):
            return self.getToken(BindPreferenceGrammarParser.LEQ, 0)

        def EQ(self):
            return self.getToken(BindPreferenceGrammarParser.EQ, 0)

        def GEQ(self):
            return self.getToken(BindPreferenceGrammarParser.GEQ, 0)

        def LT(self):
            return self.getToken(BindPreferenceGrammarParser.LT, 0)

        def GT(self):
            return self.getToken(BindPreferenceGrammarParser.GT, 0)

        def NEQ(self):
            return self.getToken(BindPreferenceGrammarParser.NEQ, 0)

        def getRuleIndex(self):
            return BindPreferenceGrammarParser.RULE_comparison_op

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterComparison_op" ):
                listener.enterComparison_op(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitComparison_op" ):
                listener.exitComparison_op(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitComparison_op" ):
                return visitor.visitComparison_op(self)
            else:
                return visitor.visitChildren(self)




    def comparison_op(self):

        localctx = BindPreferenceGrammarParser.Comparison_opContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_comparison_op)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 138
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 1056964608) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class UnaryOpContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NOT(self):
            return self.getToken(BindPreferenceGrammarParser.NOT, 0)

        def getRuleIndex(self):
            return BindPreferenceGrammarParser.RULE_unaryOp

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterUnaryOp" ):
                listener.enterUnaryOp(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitUnaryOp" ):
                listener.exitUnaryOp(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitUnaryOp" ):
                return visitor.visitUnaryOp(self)
            else:
                return visitor.visitChildren(self)




    def unaryOp(self):

        localctx = BindPreferenceGrammarParser.UnaryOpContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_unaryOp)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 140
            self.match(BindPreferenceGrammarParser.NOT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BoolFactContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def TRUE(self):
            return self.getToken(BindPreferenceGrammarParser.TRUE, 0)

        def FALSE(self):
            return self.getToken(BindPreferenceGrammarParser.FALSE, 0)

        def getRuleIndex(self):
            return BindPreferenceGrammarParser.RULE_boolFact

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBoolFact" ):
                listener.enterBoolFact(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBoolFact" ):
                listener.exitBoolFact(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBoolFact" ):
                return visitor.visitBoolFact(self)
            else:
                return visitor.visitChildren(self)




    def boolFact(self):

        localctx = BindPreferenceGrammarParser.BoolFactContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_boolFact)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 142
            _la = self._input.LA(1)
            if not(_la==16 or _la==17):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VariableContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def VARIABLE(self):
            return self.getToken(BindPreferenceGrammarParser.VARIABLE, 0)

        def getRuleIndex(self):
            return BindPreferenceGrammarParser.RULE_variable

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVariable" ):
                listener.enterVariable(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVariable" ):
                listener.exitVariable(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVariable" ):
                return visitor.visitVariable(self)
            else:
                return visitor.visitChildren(self)




    def variable(self):

        localctx = BindPreferenceGrammarParser.VariableContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_variable)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 144
            self.match(BindPreferenceGrammarParser.VARIABLE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ReContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def RE(self):
            return self.getToken(BindPreferenceGrammarParser.RE, 0)

        def getRuleIndex(self):
            return BindPreferenceGrammarParser.RULE_re

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRe" ):
                listener.enterRe(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRe" ):
                listener.exitRe(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRe" ):
                return visitor.visitRe(self)
            else:
                return visitor.visitChildren(self)




    def re(self):

        localctx = BindPreferenceGrammarParser.ReContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_re)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 146
            self.match(BindPreferenceGrammarParser.RE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





