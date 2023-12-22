# Generated from /Users/lorenzobacchiani/Desktop/abs_deployer/decl_spec_lang/DeclSpecLanguage.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .DeclSpecLanguageParser import DeclSpecLanguageParser
else:
    from DeclSpecLanguageParser import DeclSpecLanguageParser

# This class defines a complete listener for a parse tree produced by DeclSpecLanguageParser.
class DeclSpecLanguageListener(ParseTreeListener):

    # Enter a parse tree produced by DeclSpecLanguageParser#statement.
    def enterStatement(self, ctx:DeclSpecLanguageParser.StatementContext):
        pass

    # Exit a parse tree produced by DeclSpecLanguageParser#statement.
    def exitStatement(self, ctx:DeclSpecLanguageParser.StatementContext):
        pass


    # Enter a parse tree produced by DeclSpecLanguageParser#b_expr.
    def enterB_expr(self, ctx:DeclSpecLanguageParser.B_exprContext):
        pass

    # Exit a parse tree produced by DeclSpecLanguageParser#b_expr.
    def exitB_expr(self, ctx:DeclSpecLanguageParser.B_exprContext):
        pass


    # Enter a parse tree produced by DeclSpecLanguageParser#b_term.
    def enterB_term(self, ctx:DeclSpecLanguageParser.B_termContext):
        pass

    # Exit a parse tree produced by DeclSpecLanguageParser#b_term.
    def exitB_term(self, ctx:DeclSpecLanguageParser.B_termContext):
        pass


    # Enter a parse tree produced by DeclSpecLanguageParser#b_factor.
    def enterB_factor(self, ctx:DeclSpecLanguageParser.B_factorContext):
        pass

    # Exit a parse tree produced by DeclSpecLanguageParser#b_factor.
    def exitB_factor(self, ctx:DeclSpecLanguageParser.B_factorContext):
        pass


    # Enter a parse tree produced by DeclSpecLanguageParser#relation.
    def enterRelation(self, ctx:DeclSpecLanguageParser.RelationContext):
        pass

    # Exit a parse tree produced by DeclSpecLanguageParser#relation.
    def exitRelation(self, ctx:DeclSpecLanguageParser.RelationContext):
        pass


    # Enter a parse tree produced by DeclSpecLanguageParser#expr.
    def enterExpr(self, ctx:DeclSpecLanguageParser.ExprContext):
        pass

    # Exit a parse tree produced by DeclSpecLanguageParser#expr.
    def exitExpr(self, ctx:DeclSpecLanguageParser.ExprContext):
        pass


    # Enter a parse tree produced by DeclSpecLanguageParser#AtermQuantifier.
    def enterAtermQuantifier(self, ctx:DeclSpecLanguageParser.AtermQuantifierContext):
        pass

    # Exit a parse tree produced by DeclSpecLanguageParser#AtermQuantifier.
    def exitAtermQuantifier(self, ctx:DeclSpecLanguageParser.AtermQuantifierContext):
        pass


    # Enter a parse tree produced by DeclSpecLanguageParser#AtermInt.
    def enterAtermInt(self, ctx:DeclSpecLanguageParser.AtermIntContext):
        pass

    # Exit a parse tree produced by DeclSpecLanguageParser#AtermInt.
    def exitAtermInt(self, ctx:DeclSpecLanguageParser.AtermIntContext):
        pass


    # Enter a parse tree produced by DeclSpecLanguageParser#AtermId.
    def enterAtermId(self, ctx:DeclSpecLanguageParser.AtermIdContext):
        pass

    # Exit a parse tree produced by DeclSpecLanguageParser#AtermId.
    def exitAtermId(self, ctx:DeclSpecLanguageParser.AtermIdContext):
        pass


    # Enter a parse tree produced by DeclSpecLanguageParser#AtermDCObj.
    def enterAtermDCObj(self, ctx:DeclSpecLanguageParser.AtermDCObjContext):
        pass

    # Exit a parse tree produced by DeclSpecLanguageParser#AtermDCObj.
    def exitAtermDCObj(self, ctx:DeclSpecLanguageParser.AtermDCObjContext):
        pass


    # Enter a parse tree produced by DeclSpecLanguageParser#AtermSum.
    def enterAtermSum(self, ctx:DeclSpecLanguageParser.AtermSumContext):
        pass

    # Exit a parse tree produced by DeclSpecLanguageParser#AtermSum.
    def exitAtermSum(self, ctx:DeclSpecLanguageParser.AtermSumContext):
        pass


    # Enter a parse tree produced by DeclSpecLanguageParser#AexprUnaryArithmetic.
    def enterAexprUnaryArithmetic(self, ctx:DeclSpecLanguageParser.AexprUnaryArithmeticContext):
        pass

    # Exit a parse tree produced by DeclSpecLanguageParser#AexprUnaryArithmetic.
    def exitAexprUnaryArithmetic(self, ctx:DeclSpecLanguageParser.AexprUnaryArithmeticContext):
        pass


    # Enter a parse tree produced by DeclSpecLanguageParser#AtermBrackets.
    def enterAtermBrackets(self, ctx:DeclSpecLanguageParser.AtermBracketsContext):
        pass

    # Exit a parse tree produced by DeclSpecLanguageParser#AtermBrackets.
    def exitAtermBrackets(self, ctx:DeclSpecLanguageParser.AtermBracketsContext):
        pass


    # Enter a parse tree produced by DeclSpecLanguageParser#typeV.
    def enterTypeV(self, ctx:DeclSpecLanguageParser.TypeVContext):
        pass

    # Exit a parse tree produced by DeclSpecLanguageParser#typeV.
    def exitTypeV(self, ctx:DeclSpecLanguageParser.TypeVContext):
        pass


    # Enter a parse tree produced by DeclSpecLanguageParser#AdcIDID.
    def enterAdcIDID(self, ctx:DeclSpecLanguageParser.AdcIDIDContext):
        pass

    # Exit a parse tree produced by DeclSpecLanguageParser#AdcIDID.
    def exitAdcIDID(self, ctx:DeclSpecLanguageParser.AdcIDIDContext):
        pass


    # Enter a parse tree produced by DeclSpecLanguageParser#AdcIDVar.
    def enterAdcIDVar(self, ctx:DeclSpecLanguageParser.AdcIDVarContext):
        pass

    # Exit a parse tree produced by DeclSpecLanguageParser#AdcIDVar.
    def exitAdcIDVar(self, ctx:DeclSpecLanguageParser.AdcIDVarContext):
        pass


    # Enter a parse tree produced by DeclSpecLanguageParser#AdcIDNum.
    def enterAdcIDNum(self, ctx:DeclSpecLanguageParser.AdcIDNumContext):
        pass

    # Exit a parse tree produced by DeclSpecLanguageParser#AdcIDNum.
    def exitAdcIDNum(self, ctx:DeclSpecLanguageParser.AdcIDNumContext):
        pass


    # Enter a parse tree produced by DeclSpecLanguageParser#AobjIDID.
    def enterAobjIDID(self, ctx:DeclSpecLanguageParser.AobjIDIDContext):
        pass

    # Exit a parse tree produced by DeclSpecLanguageParser#AobjIDID.
    def exitAobjIDID(self, ctx:DeclSpecLanguageParser.AobjIDIDContext):
        pass


    # Enter a parse tree produced by DeclSpecLanguageParser#AobjIDVar.
    def enterAobjIDVar(self, ctx:DeclSpecLanguageParser.AobjIDVarContext):
        pass

    # Exit a parse tree produced by DeclSpecLanguageParser#AobjIDVar.
    def exitAobjIDVar(self, ctx:DeclSpecLanguageParser.AobjIDVarContext):
        pass


    # Enter a parse tree produced by DeclSpecLanguageParser#AobjIDScenario.
    def enterAobjIDScenario(self, ctx:DeclSpecLanguageParser.AobjIDScenarioContext):
        pass

    # Exit a parse tree produced by DeclSpecLanguageParser#AobjIDScenario.
    def exitAobjIDScenario(self, ctx:DeclSpecLanguageParser.AobjIDScenarioContext):
        pass


    # Enter a parse tree produced by DeclSpecLanguageParser#AobjIDRE.
    def enterAobjIDRE(self, ctx:DeclSpecLanguageParser.AobjIDREContext):
        pass

    # Exit a parse tree produced by DeclSpecLanguageParser#AobjIDRE.
    def exitAobjIDRE(self, ctx:DeclSpecLanguageParser.AobjIDREContext):
        pass


    # Enter a parse tree produced by DeclSpecLanguageParser#Avariable.
    def enterAvariable(self, ctx:DeclSpecLanguageParser.AvariableContext):
        pass

    # Exit a parse tree produced by DeclSpecLanguageParser#Avariable.
    def exitAvariable(self, ctx:DeclSpecLanguageParser.AvariableContext):
        pass


    # Enter a parse tree produced by DeclSpecLanguageParser#bool_binary_op.
    def enterBool_binary_op(self, ctx:DeclSpecLanguageParser.Bool_binary_opContext):
        pass

    # Exit a parse tree produced by DeclSpecLanguageParser#bool_binary_op.
    def exitBool_binary_op(self, ctx:DeclSpecLanguageParser.Bool_binary_opContext):
        pass


    # Enter a parse tree produced by DeclSpecLanguageParser#arith_binary_op.
    def enterArith_binary_op(self, ctx:DeclSpecLanguageParser.Arith_binary_opContext):
        pass

    # Exit a parse tree produced by DeclSpecLanguageParser#arith_binary_op.
    def exitArith_binary_op(self, ctx:DeclSpecLanguageParser.Arith_binary_opContext):
        pass


    # Enter a parse tree produced by DeclSpecLanguageParser#arith_unary_op.
    def enterArith_unary_op(self, ctx:DeclSpecLanguageParser.Arith_unary_opContext):
        pass

    # Exit a parse tree produced by DeclSpecLanguageParser#arith_unary_op.
    def exitArith_unary_op(self, ctx:DeclSpecLanguageParser.Arith_unary_opContext):
        pass


    # Enter a parse tree produced by DeclSpecLanguageParser#comparison_op.
    def enterComparison_op(self, ctx:DeclSpecLanguageParser.Comparison_opContext):
        pass

    # Exit a parse tree produced by DeclSpecLanguageParser#comparison_op.
    def exitComparison_op(self, ctx:DeclSpecLanguageParser.Comparison_opContext):
        pass


    # Enter a parse tree produced by DeclSpecLanguageParser#unaryOp.
    def enterUnaryOp(self, ctx:DeclSpecLanguageParser.UnaryOpContext):
        pass

    # Exit a parse tree produced by DeclSpecLanguageParser#unaryOp.
    def exitUnaryOp(self, ctx:DeclSpecLanguageParser.UnaryOpContext):
        pass


    # Enter a parse tree produced by DeclSpecLanguageParser#boolFact.
    def enterBoolFact(self, ctx:DeclSpecLanguageParser.BoolFactContext):
        pass

    # Exit a parse tree produced by DeclSpecLanguageParser#boolFact.
    def exitBoolFact(self, ctx:DeclSpecLanguageParser.BoolFactContext):
        pass



del DeclSpecLanguageParser