# Generated from /Users/lorenzobacchiani/Desktop/abs_deployer/bind_preference_grammar/BindPreferenceGrammar.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .BindPreferenceGrammarParser import BindPreferenceGrammarParser
else:
    from BindPreferenceGrammarParser import BindPreferenceGrammarParser

# This class defines a complete generic visitor for a parse tree produced by BindPreferenceGrammarParser.

class BindPreferenceGrammarVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by BindPreferenceGrammarParser#statement.
    def visitStatement(self, ctx:BindPreferenceGrammarParser.StatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BindPreferenceGrammarParser#ApreferenceLocal.
    def visitApreferenceLocal(self, ctx:BindPreferenceGrammarParser.ApreferenceLocalContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BindPreferenceGrammarParser#ApreferenceExpr.
    def visitApreferenceExpr(self, ctx:BindPreferenceGrammarParser.ApreferenceExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BindPreferenceGrammarParser#b_expr.
    def visitB_expr(self, ctx:BindPreferenceGrammarParser.B_exprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BindPreferenceGrammarParser#b_term.
    def visitB_term(self, ctx:BindPreferenceGrammarParser.B_termContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BindPreferenceGrammarParser#b_factor.
    def visitB_factor(self, ctx:BindPreferenceGrammarParser.B_factorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BindPreferenceGrammarParser#relation.
    def visitRelation(self, ctx:BindPreferenceGrammarParser.RelationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BindPreferenceGrammarParser#expr.
    def visitExpr(self, ctx:BindPreferenceGrammarParser.ExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BindPreferenceGrammarParser#AexprQuantifier.
    def visitAexprQuantifier(self, ctx:BindPreferenceGrammarParser.AexprQuantifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BindPreferenceGrammarParser#AexprInt.
    def visitAexprInt(self, ctx:BindPreferenceGrammarParser.AexprIntContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BindPreferenceGrammarParser#AexprBind.
    def visitAexprBind(self, ctx:BindPreferenceGrammarParser.AexprBindContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BindPreferenceGrammarParser#AexprSum.
    def visitAexprSum(self, ctx:BindPreferenceGrammarParser.AexprSumContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BindPreferenceGrammarParser#AexprUnaryArithmetic.
    def visitAexprUnaryArithmetic(self, ctx:BindPreferenceGrammarParser.AexprUnaryArithmeticContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BindPreferenceGrammarParser#AexprBrackets.
    def visitAexprBrackets(self, ctx:BindPreferenceGrammarParser.AexprBracketsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BindPreferenceGrammarParser#AobjIDID.
    def visitAobjIDID(self, ctx:BindPreferenceGrammarParser.AobjIDIDContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BindPreferenceGrammarParser#AobjIDVar.
    def visitAobjIDVar(self, ctx:BindPreferenceGrammarParser.AobjIDVarContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BindPreferenceGrammarParser#AobjIDScenario.
    def visitAobjIDScenario(self, ctx:BindPreferenceGrammarParser.AobjIDScenarioContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BindPreferenceGrammarParser#AobjIDRE.
    def visitAobjIDRE(self, ctx:BindPreferenceGrammarParser.AobjIDREContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BindPreferenceGrammarParser#typeV.
    def visitTypeV(self, ctx:BindPreferenceGrammarParser.TypeVContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BindPreferenceGrammarParser#bool_binary_op.
    def visitBool_binary_op(self, ctx:BindPreferenceGrammarParser.Bool_binary_opContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BindPreferenceGrammarParser#arith_binary_op.
    def visitArith_binary_op(self, ctx:BindPreferenceGrammarParser.Arith_binary_opContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BindPreferenceGrammarParser#arith_unary_op.
    def visitArith_unary_op(self, ctx:BindPreferenceGrammarParser.Arith_unary_opContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BindPreferenceGrammarParser#comparison_op.
    def visitComparison_op(self, ctx:BindPreferenceGrammarParser.Comparison_opContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BindPreferenceGrammarParser#unaryOp.
    def visitUnaryOp(self, ctx:BindPreferenceGrammarParser.UnaryOpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BindPreferenceGrammarParser#boolFact.
    def visitBoolFact(self, ctx:BindPreferenceGrammarParser.BoolFactContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BindPreferenceGrammarParser#variable.
    def visitVariable(self, ctx:BindPreferenceGrammarParser.VariableContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BindPreferenceGrammarParser#re.
    def visitRe(self, ctx:BindPreferenceGrammarParser.ReContext):
        return self.visitChildren(ctx)



del BindPreferenceGrammarParser