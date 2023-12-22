# Generated from /Users/lorenzobacchiani/Desktop/abs_deployer/decl_spec_lang/DeclSpecLanguage.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .DeclSpecLanguageParser import DeclSpecLanguageParser
else:
    from DeclSpecLanguageParser import DeclSpecLanguageParser

# This class defines a complete generic visitor for a parse tree produced by DeclSpecLanguageParser.

class DeclSpecLanguageVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by DeclSpecLanguageParser#statement.
    def visitStatement(self, ctx:DeclSpecLanguageParser.StatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DeclSpecLanguageParser#b_expr.
    def visitB_expr(self, ctx:DeclSpecLanguageParser.B_exprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DeclSpecLanguageParser#b_term.
    def visitB_term(self, ctx:DeclSpecLanguageParser.B_termContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DeclSpecLanguageParser#b_factor.
    def visitB_factor(self, ctx:DeclSpecLanguageParser.B_factorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DeclSpecLanguageParser#relation.
    def visitRelation(self, ctx:DeclSpecLanguageParser.RelationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DeclSpecLanguageParser#expr.
    def visitExpr(self, ctx:DeclSpecLanguageParser.ExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DeclSpecLanguageParser#AtermQuantifier.
    def visitAtermQuantifier(self, ctx:DeclSpecLanguageParser.AtermQuantifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DeclSpecLanguageParser#AtermInt.
    def visitAtermInt(self, ctx:DeclSpecLanguageParser.AtermIntContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DeclSpecLanguageParser#AtermId.
    def visitAtermId(self, ctx:DeclSpecLanguageParser.AtermIdContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DeclSpecLanguageParser#AtermDCObj.
    def visitAtermDCObj(self, ctx:DeclSpecLanguageParser.AtermDCObjContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DeclSpecLanguageParser#AtermSum.
    def visitAtermSum(self, ctx:DeclSpecLanguageParser.AtermSumContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DeclSpecLanguageParser#AexprUnaryArithmetic.
    def visitAexprUnaryArithmetic(self, ctx:DeclSpecLanguageParser.AexprUnaryArithmeticContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DeclSpecLanguageParser#AtermBrackets.
    def visitAtermBrackets(self, ctx:DeclSpecLanguageParser.AtermBracketsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DeclSpecLanguageParser#typeV.
    def visitTypeV(self, ctx:DeclSpecLanguageParser.TypeVContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DeclSpecLanguageParser#AdcIDID.
    def visitAdcIDID(self, ctx:DeclSpecLanguageParser.AdcIDIDContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DeclSpecLanguageParser#AdcIDVar.
    def visitAdcIDVar(self, ctx:DeclSpecLanguageParser.AdcIDVarContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DeclSpecLanguageParser#AdcIDNum.
    def visitAdcIDNum(self, ctx:DeclSpecLanguageParser.AdcIDNumContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DeclSpecLanguageParser#AobjIDID.
    def visitAobjIDID(self, ctx:DeclSpecLanguageParser.AobjIDIDContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DeclSpecLanguageParser#AobjIDVar.
    def visitAobjIDVar(self, ctx:DeclSpecLanguageParser.AobjIDVarContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DeclSpecLanguageParser#AobjIDScenario.
    def visitAobjIDScenario(self, ctx:DeclSpecLanguageParser.AobjIDScenarioContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DeclSpecLanguageParser#AobjIDRE.
    def visitAobjIDRE(self, ctx:DeclSpecLanguageParser.AobjIDREContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DeclSpecLanguageParser#Avariable.
    def visitAvariable(self, ctx:DeclSpecLanguageParser.AvariableContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DeclSpecLanguageParser#bool_binary_op.
    def visitBool_binary_op(self, ctx:DeclSpecLanguageParser.Bool_binary_opContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DeclSpecLanguageParser#arith_binary_op.
    def visitArith_binary_op(self, ctx:DeclSpecLanguageParser.Arith_binary_opContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DeclSpecLanguageParser#arith_unary_op.
    def visitArith_unary_op(self, ctx:DeclSpecLanguageParser.Arith_unary_opContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DeclSpecLanguageParser#comparison_op.
    def visitComparison_op(self, ctx:DeclSpecLanguageParser.Comparison_opContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DeclSpecLanguageParser#unaryOp.
    def visitUnaryOp(self, ctx:DeclSpecLanguageParser.UnaryOpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DeclSpecLanguageParser#boolFact.
    def visitBoolFact(self, ctx:DeclSpecLanguageParser.BoolFactContext):
        return self.visitChildren(ctx)



del DeclSpecLanguageParser