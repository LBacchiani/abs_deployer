# Generated from /Users/lorenzobacchiani/Desktop/abs_deployer/ABS/ABS.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .ABSParser import ABSParser
else:
    from ABSParser import ABSParser

# This class defines a complete generic visitor for a parse tree produced by ABSParser.

class ABSVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by ABSParser#qualified_type_identifier.
    def visitQualified_type_identifier(self, ctx:ABSParser.Qualified_type_identifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ABSParser#qualified_identifier.
    def visitQualified_identifier(self, ctx:ABSParser.Qualified_identifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ABSParser#any_identifier.
    def visitAny_identifier(self, ctx:ABSParser.Any_identifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ABSParser#type_use.
    def visitType_use(self, ctx:ABSParser.Type_useContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ABSParser#type_exp.
    def visitType_exp(self, ctx:ABSParser.Type_expContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ABSParser#paramlist.
    def visitParamlist(self, ctx:ABSParser.ParamlistContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ABSParser#param_decl.
    def visitParam_decl(self, ctx:ABSParser.Param_declContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ABSParser#interface_name.
    def visitInterface_name(self, ctx:ABSParser.Interface_nameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ABSParser#delta_id.
    def visitDelta_id(self, ctx:ABSParser.Delta_idContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ABSParser#EffExp.
    def visitEffExp(self, ctx:ABSParser.EffExpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ABSParser#PureExp.
    def visitPureExp(self, ctx:ABSParser.PureExpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ABSParser#GetExp.
    def visitGetExp(self, ctx:ABSParser.GetExpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ABSParser#NewExp.
    def visitNewExp(self, ctx:ABSParser.NewExpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ABSParser#AsyncCallExp.
    def visitAsyncCallExp(self, ctx:ABSParser.AsyncCallExpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ABSParser#SyncCallExp.
    def visitSyncCallExp(self, ctx:ABSParser.SyncCallExpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ABSParser#OriginalCallExp.
    def visitOriginalCallExp(self, ctx:ABSParser.OriginalCallExpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ABSParser#ConstructorExp.
    def visitConstructorExp(self, ctx:ABSParser.ConstructorExpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ABSParser#FunctionExp.
    def visitFunctionExp(self, ctx:ABSParser.FunctionExpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ABSParser#AndExp.
    def visitAndExp(self, ctx:ABSParser.AndExpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ABSParser#GreaterExp.
    def visitGreaterExp(self, ctx:ABSParser.GreaterExpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ABSParser#MultExp.
    def visitMultExp(self, ctx:ABSParser.MultExpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ABSParser#VarOrFieldExp.
    def visitVarOrFieldExp(self, ctx:ABSParser.VarOrFieldExpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ABSParser#StringExp.
    def visitStringExp(self, ctx:ABSParser.StringExpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ABSParser#CaseExp.
    def visitCaseExp(self, ctx:ABSParser.CaseExpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ABSParser#AddExp.
    def visitAddExp(self, ctx:ABSParser.AddExpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ABSParser#NullExp.
    def visitNullExp(self, ctx:ABSParser.NullExpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ABSParser#EqualExp.
    def visitEqualExp(self, ctx:ABSParser.EqualExpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ABSParser#VariadicFunctionExp.
    def visitVariadicFunctionExp(self, ctx:ABSParser.VariadicFunctionExpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ABSParser#IfExp.
    def visitIfExp(self, ctx:ABSParser.IfExpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ABSParser#OrExp.
    def visitOrExp(self, ctx:ABSParser.OrExpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ABSParser#ParenExp.
    def visitParenExp(self, ctx:ABSParser.ParenExpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ABSParser#LetExp.
    def visitLetExp(self, ctx:ABSParser.LetExpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ABSParser#UnaryExp.
    def visitUnaryExp(self, ctx:ABSParser.UnaryExpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ABSParser#IntExp.
    def visitIntExp(self, ctx:ABSParser.IntExpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ABSParser#ThisExp.
    def visitThisExp(self, ctx:ABSParser.ThisExpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ABSParser#casebranch.
    def visitCasebranch(self, ctx:ABSParser.CasebranchContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ABSParser#UnderscorePattern.
    def visitUnderscorePattern(self, ctx:ABSParser.UnderscorePatternContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ABSParser#IntPattern.
    def visitIntPattern(self, ctx:ABSParser.IntPatternContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ABSParser#StringPattern.
    def visitStringPattern(self, ctx:ABSParser.StringPatternContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ABSParser#VarPattern.
    def visitVarPattern(self, ctx:ABSParser.VarPatternContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ABSParser#ConstructorPattern.
    def visitConstructorPattern(self, ctx:ABSParser.ConstructorPatternContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ABSParser#var_or_field_ref.
    def visitVar_or_field_ref(self, ctx:ABSParser.Var_or_field_refContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ABSParser#pure_exp_list.
    def visitPure_exp_list(self, ctx:ABSParser.Pure_exp_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ABSParser#list_literal.
    def visitList_literal(self, ctx:ABSParser.List_literalContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ABSParser#annotation.
    def visitAnnotation(self, ctx:ABSParser.AnnotationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ABSParser#VardeclStmt.
    def visitVardeclStmt(self, ctx:ABSParser.VardeclStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ABSParser#AssignStmt.
    def visitAssignStmt(self, ctx:ABSParser.AssignStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ABSParser#SkipStmt.
    def visitSkipStmt(self, ctx:ABSParser.SkipStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ABSParser#ReturnStmt.
    def visitReturnStmt(self, ctx:ABSParser.ReturnStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ABSParser#AssertStmt.
    def visitAssertStmt(self, ctx:ABSParser.AssertStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ABSParser#BlockStmt.
    def visitBlockStmt(self, ctx:ABSParser.BlockStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ABSParser#IfStmt.
    def visitIfStmt(self, ctx:ABSParser.IfStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ABSParser#WhileStmt.
    def visitWhileStmt(self, ctx:ABSParser.WhileStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ABSParser#TryCatchFinallyStmt.
    def visitTryCatchFinallyStmt(self, ctx:ABSParser.TryCatchFinallyStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ABSParser#AwaitStmt.
    def visitAwaitStmt(self, ctx:ABSParser.AwaitStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ABSParser#SuspendStmt.
    def visitSuspendStmt(self, ctx:ABSParser.SuspendStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ABSParser#DurationStmt.
    def visitDurationStmt(self, ctx:ABSParser.DurationStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ABSParser#ThrowStmt.
    def visitThrowStmt(self, ctx:ABSParser.ThrowStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ABSParser#DieStmt.
    def visitDieStmt(self, ctx:ABSParser.DieStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ABSParser#MoveCogToStmt.
    def visitMoveCogToStmt(self, ctx:ABSParser.MoveCogToStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ABSParser#ExpStmt.
    def visitExpStmt(self, ctx:ABSParser.ExpStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ABSParser#CaseStmt.
    def visitCaseStmt(self, ctx:ABSParser.CaseStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ABSParser#ExpGuard.
    def visitExpGuard(self, ctx:ABSParser.ExpGuardContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ABSParser#AndGuard.
    def visitAndGuard(self, ctx:ABSParser.AndGuardContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ABSParser#ClaimGuard.
    def visitClaimGuard(self, ctx:ABSParser.ClaimGuardContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ABSParser#DurationGuard.
    def visitDurationGuard(self, ctx:ABSParser.DurationGuardContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ABSParser#casestmtbranch.
    def visitCasestmtbranch(self, ctx:ABSParser.CasestmtbranchContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ABSParser#datatype_decl.
    def visitDatatype_decl(self, ctx:ABSParser.Datatype_declContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ABSParser#data_constructor.
    def visitData_constructor(self, ctx:ABSParser.Data_constructorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ABSParser#data_constructor_arg.
    def visitData_constructor_arg(self, ctx:ABSParser.Data_constructor_argContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ABSParser#typesyn_decl.
    def visitTypesyn_decl(self, ctx:ABSParser.Typesyn_declContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ABSParser#exception_decl.
    def visitException_decl(self, ctx:ABSParser.Exception_declContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ABSParser#function_decl.
    def visitFunction_decl(self, ctx:ABSParser.Function_declContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ABSParser#interface_decl.
    def visitInterface_decl(self, ctx:ABSParser.Interface_declContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ABSParser#methodsig.
    def visitMethodsig(self, ctx:ABSParser.MethodsigContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ABSParser#class_decl.
    def visitClass_decl(self, ctx:ABSParser.Class_declContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ABSParser#field_decl.
    def visitField_decl(self, ctx:ABSParser.Field_declContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ABSParser#method.
    def visitMethod(self, ctx:ABSParser.MethodContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ABSParser#module_decl.
    def visitModule_decl(self, ctx:ABSParser.Module_declContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ABSParser#module_export.
    def visitModule_export(self, ctx:ABSParser.Module_exportContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ABSParser#module_import.
    def visitModule_import(self, ctx:ABSParser.Module_importContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ABSParser#decl.
    def visitDecl(self, ctx:ABSParser.DeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ABSParser#delta_decl.
    def visitDelta_decl(self, ctx:ABSParser.Delta_declContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ABSParser#DeltaFieldParam.
    def visitDeltaFieldParam(self, ctx:ABSParser.DeltaFieldParamContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ABSParser#DeltaClassParam.
    def visitDeltaClassParam(self, ctx:ABSParser.DeltaClassParamContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ABSParser#DeltaHasFieldCondition.
    def visitDeltaHasFieldCondition(self, ctx:ABSParser.DeltaHasFieldConditionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ABSParser#DeltaHasMethodCondition.
    def visitDeltaHasMethodCondition(self, ctx:ABSParser.DeltaHasMethodConditionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ABSParser#DeltaHasInterfaceCondition.
    def visitDeltaHasInterfaceCondition(self, ctx:ABSParser.DeltaHasInterfaceConditionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ABSParser#delta_access.
    def visitDelta_access(self, ctx:ABSParser.Delta_accessContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ABSParser#module_modifier.
    def visitModule_modifier(self, ctx:ABSParser.Module_modifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ABSParser#DeltaAddFunctionModifier.
    def visitDeltaAddFunctionModifier(self, ctx:ABSParser.DeltaAddFunctionModifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ABSParser#DeltaAddDataTypeModifier.
    def visitDeltaAddDataTypeModifier(self, ctx:ABSParser.DeltaAddDataTypeModifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ABSParser#DeltaAddTypeSynModifier.
    def visitDeltaAddTypeSynModifier(self, ctx:ABSParser.DeltaAddTypeSynModifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ABSParser#DeltaModifyTypeSynModifier.
    def visitDeltaModifyTypeSynModifier(self, ctx:ABSParser.DeltaModifyTypeSynModifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ABSParser#DeltaModifyDataTypeModifier.
    def visitDeltaModifyDataTypeModifier(self, ctx:ABSParser.DeltaModifyDataTypeModifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ABSParser#DeltaAddClassModifier.
    def visitDeltaAddClassModifier(self, ctx:ABSParser.DeltaAddClassModifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ABSParser#DeltaRemoveClassModifier.
    def visitDeltaRemoveClassModifier(self, ctx:ABSParser.DeltaRemoveClassModifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ABSParser#DeltaModifyClassModifier.
    def visitDeltaModifyClassModifier(self, ctx:ABSParser.DeltaModifyClassModifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ABSParser#DeltaAddInterfaceModifier.
    def visitDeltaAddInterfaceModifier(self, ctx:ABSParser.DeltaAddInterfaceModifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ABSParser#DeltaRemoveInterfaceModifier.
    def visitDeltaRemoveInterfaceModifier(self, ctx:ABSParser.DeltaRemoveInterfaceModifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ABSParser#DeltaModifyInterfaceModifier.
    def visitDeltaModifyInterfaceModifier(self, ctx:ABSParser.DeltaModifyInterfaceModifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ABSParser#DeltaAddFieldFragment.
    def visitDeltaAddFieldFragment(self, ctx:ABSParser.DeltaAddFieldFragmentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ABSParser#DeltaRemoveFieldFragment.
    def visitDeltaRemoveFieldFragment(self, ctx:ABSParser.DeltaRemoveFieldFragmentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ABSParser#DeltaAddMethodFragment.
    def visitDeltaAddMethodFragment(self, ctx:ABSParser.DeltaAddMethodFragmentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ABSParser#DeltaModifyMethodFragment.
    def visitDeltaModifyMethodFragment(self, ctx:ABSParser.DeltaModifyMethodFragmentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ABSParser#DeltaRemoveMethodFragment.
    def visitDeltaRemoveMethodFragment(self, ctx:ABSParser.DeltaRemoveMethodFragmentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ABSParser#DeltaAddMethodsigFragment.
    def visitDeltaAddMethodsigFragment(self, ctx:ABSParser.DeltaAddMethodsigFragmentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ABSParser#DeltaRemoveMethodsigFragment.
    def visitDeltaRemoveMethodsigFragment(self, ctx:ABSParser.DeltaRemoveMethodsigFragmentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ABSParser#DeltaAddModuleImportFragment.
    def visitDeltaAddModuleImportFragment(self, ctx:ABSParser.DeltaAddModuleImportFragmentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ABSParser#DeltaAddModuleExportFragment.
    def visitDeltaAddModuleExportFragment(self, ctx:ABSParser.DeltaAddModuleExportFragmentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ABSParser#UpdateDecl.
    def visitUpdateDecl(self, ctx:ABSParser.UpdateDeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ABSParser#ObjectUpdateDecl.
    def visitObjectUpdateDecl(self, ctx:ABSParser.ObjectUpdateDeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ABSParser#ObjectUpdateAssignStmt.
    def visitObjectUpdateAssignStmt(self, ctx:ABSParser.ObjectUpdateAssignStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ABSParser#UpdatePreambleDecl.
    def visitUpdatePreambleDecl(self, ctx:ABSParser.UpdatePreambleDeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ABSParser#productline_decl.
    def visitProductline_decl(self, ctx:ABSParser.Productline_declContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ABSParser#feature.
    def visitFeature(self, ctx:ABSParser.FeatureContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ABSParser#delta_clause.
    def visitDelta_clause(self, ctx:ABSParser.Delta_clauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ABSParser#deltaspec.
    def visitDeltaspec(self, ctx:ABSParser.DeltaspecContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ABSParser#FIDAIDDeltaspecParam.
    def visitFIDAIDDeltaspecParam(self, ctx:ABSParser.FIDAIDDeltaspecParamContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ABSParser#IntDeltaspecParam.
    def visitIntDeltaspecParam(self, ctx:ABSParser.IntDeltaspecParamContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ABSParser#BoolOrIDDeltaspecParam.
    def visitBoolOrIDDeltaspecParam(self, ctx:ABSParser.BoolOrIDDeltaspecParamContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ABSParser#after_condition.
    def visitAfter_condition(self, ctx:ABSParser.After_conditionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ABSParser#from_condition.
    def visitFrom_condition(self, ctx:ABSParser.From_conditionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ABSParser#when_condition.
    def visitWhen_condition(self, ctx:ABSParser.When_conditionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ABSParser#FeatureApplicationCondition.
    def visitFeatureApplicationCondition(self, ctx:ABSParser.FeatureApplicationConditionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ABSParser#AndApplicationCondition.
    def visitAndApplicationCondition(self, ctx:ABSParser.AndApplicationConditionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ABSParser#ParenApplicationCondition.
    def visitParenApplicationCondition(self, ctx:ABSParser.ParenApplicationConditionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ABSParser#NotApplicationCondition.
    def visitNotApplicationCondition(self, ctx:ABSParser.NotApplicationConditionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ABSParser#OrApplicationCondition.
    def visitOrApplicationCondition(self, ctx:ABSParser.OrApplicationConditionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ABSParser#attr_assignment.
    def visitAttr_assignment(self, ctx:ABSParser.Attr_assignmentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ABSParser#product_decl.
    def visitProduct_decl(self, ctx:ABSParser.Product_declContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ABSParser#product_reconfiguration.
    def visitProduct_reconfiguration(self, ctx:ABSParser.Product_reconfigurationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ABSParser#fextension.
    def visitFextension(self, ctx:ABSParser.FextensionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ABSParser#feature_decl.
    def visitFeature_decl(self, ctx:ABSParser.Feature_declContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ABSParser#feature_decl_group.
    def visitFeature_decl_group(self, ctx:ABSParser.Feature_decl_groupContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ABSParser#fnode.
    def visitFnode(self, ctx:ABSParser.FnodeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ABSParser#feature_decl_attribute.
    def visitFeature_decl_attribute(self, ctx:ABSParser.Feature_decl_attributeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ABSParser#FeatureDeclConstraintIfIn.
    def visitFeatureDeclConstraintIfIn(self, ctx:ABSParser.FeatureDeclConstraintIfInContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ABSParser#FeatureDeclConstraintIfOut.
    def visitFeatureDeclConstraintIfOut(self, ctx:ABSParser.FeatureDeclConstraintIfOutContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ABSParser#FeatureDeclConstraintExclude.
    def visitFeatureDeclConstraintExclude(self, ctx:ABSParser.FeatureDeclConstraintExcludeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ABSParser#FeatureDeclConstraintRequire.
    def visitFeatureDeclConstraintRequire(self, ctx:ABSParser.FeatureDeclConstraintRequireContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ABSParser#mexp.
    def visitMexp(self, ctx:ABSParser.MexpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ABSParser#boundary_int.
    def visitBoundary_int(self, ctx:ABSParser.Boundary_intContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ABSParser#boundary_val.
    def visitBoundary_val(self, ctx:ABSParser.Boundary_valContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ABSParser#main_block.
    def visitMain_block(self, ctx:ABSParser.Main_blockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ABSParser#compilation_unit.
    def visitCompilation_unit(self, ctx:ABSParser.Compilation_unitContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ABSParser#goal.
    def visitGoal(self, ctx:ABSParser.GoalContext):
        return self.visitChildren(ctx)



del ABSParser