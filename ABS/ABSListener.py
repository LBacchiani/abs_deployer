# Generated from /Users/lorenzobacchiani/Desktop/abs_deployer/ABS/ABS.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .ABSParser import ABSParser
else:
    from ABSParser import ABSParser

# This class defines a complete listener for a parse tree produced by ABSParser.
class ABSListener(ParseTreeListener):

    # Enter a parse tree produced by ABSParser#qualified_type_identifier.
    def enterQualified_type_identifier(self, ctx:ABSParser.Qualified_type_identifierContext):
        pass

    # Exit a parse tree produced by ABSParser#qualified_type_identifier.
    def exitQualified_type_identifier(self, ctx:ABSParser.Qualified_type_identifierContext):
        pass


    # Enter a parse tree produced by ABSParser#qualified_identifier.
    def enterQualified_identifier(self, ctx:ABSParser.Qualified_identifierContext):
        pass

    # Exit a parse tree produced by ABSParser#qualified_identifier.
    def exitQualified_identifier(self, ctx:ABSParser.Qualified_identifierContext):
        pass


    # Enter a parse tree produced by ABSParser#any_identifier.
    def enterAny_identifier(self, ctx:ABSParser.Any_identifierContext):
        pass

    # Exit a parse tree produced by ABSParser#any_identifier.
    def exitAny_identifier(self, ctx:ABSParser.Any_identifierContext):
        pass


    # Enter a parse tree produced by ABSParser#type_use.
    def enterType_use(self, ctx:ABSParser.Type_useContext):
        pass

    # Exit a parse tree produced by ABSParser#type_use.
    def exitType_use(self, ctx:ABSParser.Type_useContext):
        pass


    # Enter a parse tree produced by ABSParser#type_exp.
    def enterType_exp(self, ctx:ABSParser.Type_expContext):
        pass

    # Exit a parse tree produced by ABSParser#type_exp.
    def exitType_exp(self, ctx:ABSParser.Type_expContext):
        pass


    # Enter a parse tree produced by ABSParser#paramlist.
    def enterParamlist(self, ctx:ABSParser.ParamlistContext):
        pass

    # Exit a parse tree produced by ABSParser#paramlist.
    def exitParamlist(self, ctx:ABSParser.ParamlistContext):
        pass


    # Enter a parse tree produced by ABSParser#param_decl.
    def enterParam_decl(self, ctx:ABSParser.Param_declContext):
        pass

    # Exit a parse tree produced by ABSParser#param_decl.
    def exitParam_decl(self, ctx:ABSParser.Param_declContext):
        pass


    # Enter a parse tree produced by ABSParser#interface_name.
    def enterInterface_name(self, ctx:ABSParser.Interface_nameContext):
        pass

    # Exit a parse tree produced by ABSParser#interface_name.
    def exitInterface_name(self, ctx:ABSParser.Interface_nameContext):
        pass


    # Enter a parse tree produced by ABSParser#delta_id.
    def enterDelta_id(self, ctx:ABSParser.Delta_idContext):
        pass

    # Exit a parse tree produced by ABSParser#delta_id.
    def exitDelta_id(self, ctx:ABSParser.Delta_idContext):
        pass


    # Enter a parse tree produced by ABSParser#EffExp.
    def enterEffExp(self, ctx:ABSParser.EffExpContext):
        pass

    # Exit a parse tree produced by ABSParser#EffExp.
    def exitEffExp(self, ctx:ABSParser.EffExpContext):
        pass


    # Enter a parse tree produced by ABSParser#PureExp.
    def enterPureExp(self, ctx:ABSParser.PureExpContext):
        pass

    # Exit a parse tree produced by ABSParser#PureExp.
    def exitPureExp(self, ctx:ABSParser.PureExpContext):
        pass


    # Enter a parse tree produced by ABSParser#GetExp.
    def enterGetExp(self, ctx:ABSParser.GetExpContext):
        pass

    # Exit a parse tree produced by ABSParser#GetExp.
    def exitGetExp(self, ctx:ABSParser.GetExpContext):
        pass


    # Enter a parse tree produced by ABSParser#NewExp.
    def enterNewExp(self, ctx:ABSParser.NewExpContext):
        pass

    # Exit a parse tree produced by ABSParser#NewExp.
    def exitNewExp(self, ctx:ABSParser.NewExpContext):
        pass


    # Enter a parse tree produced by ABSParser#AsyncCallExp.
    def enterAsyncCallExp(self, ctx:ABSParser.AsyncCallExpContext):
        pass

    # Exit a parse tree produced by ABSParser#AsyncCallExp.
    def exitAsyncCallExp(self, ctx:ABSParser.AsyncCallExpContext):
        pass


    # Enter a parse tree produced by ABSParser#SyncCallExp.
    def enterSyncCallExp(self, ctx:ABSParser.SyncCallExpContext):
        pass

    # Exit a parse tree produced by ABSParser#SyncCallExp.
    def exitSyncCallExp(self, ctx:ABSParser.SyncCallExpContext):
        pass


    # Enter a parse tree produced by ABSParser#OriginalCallExp.
    def enterOriginalCallExp(self, ctx:ABSParser.OriginalCallExpContext):
        pass

    # Exit a parse tree produced by ABSParser#OriginalCallExp.
    def exitOriginalCallExp(self, ctx:ABSParser.OriginalCallExpContext):
        pass


    # Enter a parse tree produced by ABSParser#ConstructorExp.
    def enterConstructorExp(self, ctx:ABSParser.ConstructorExpContext):
        pass

    # Exit a parse tree produced by ABSParser#ConstructorExp.
    def exitConstructorExp(self, ctx:ABSParser.ConstructorExpContext):
        pass


    # Enter a parse tree produced by ABSParser#FunctionExp.
    def enterFunctionExp(self, ctx:ABSParser.FunctionExpContext):
        pass

    # Exit a parse tree produced by ABSParser#FunctionExp.
    def exitFunctionExp(self, ctx:ABSParser.FunctionExpContext):
        pass


    # Enter a parse tree produced by ABSParser#AndExp.
    def enterAndExp(self, ctx:ABSParser.AndExpContext):
        pass

    # Exit a parse tree produced by ABSParser#AndExp.
    def exitAndExp(self, ctx:ABSParser.AndExpContext):
        pass


    # Enter a parse tree produced by ABSParser#GreaterExp.
    def enterGreaterExp(self, ctx:ABSParser.GreaterExpContext):
        pass

    # Exit a parse tree produced by ABSParser#GreaterExp.
    def exitGreaterExp(self, ctx:ABSParser.GreaterExpContext):
        pass


    # Enter a parse tree produced by ABSParser#MultExp.
    def enterMultExp(self, ctx:ABSParser.MultExpContext):
        pass

    # Exit a parse tree produced by ABSParser#MultExp.
    def exitMultExp(self, ctx:ABSParser.MultExpContext):
        pass


    # Enter a parse tree produced by ABSParser#VarOrFieldExp.
    def enterVarOrFieldExp(self, ctx:ABSParser.VarOrFieldExpContext):
        pass

    # Exit a parse tree produced by ABSParser#VarOrFieldExp.
    def exitVarOrFieldExp(self, ctx:ABSParser.VarOrFieldExpContext):
        pass


    # Enter a parse tree produced by ABSParser#StringExp.
    def enterStringExp(self, ctx:ABSParser.StringExpContext):
        pass

    # Exit a parse tree produced by ABSParser#StringExp.
    def exitStringExp(self, ctx:ABSParser.StringExpContext):
        pass


    # Enter a parse tree produced by ABSParser#CaseExp.
    def enterCaseExp(self, ctx:ABSParser.CaseExpContext):
        pass

    # Exit a parse tree produced by ABSParser#CaseExp.
    def exitCaseExp(self, ctx:ABSParser.CaseExpContext):
        pass


    # Enter a parse tree produced by ABSParser#AddExp.
    def enterAddExp(self, ctx:ABSParser.AddExpContext):
        pass

    # Exit a parse tree produced by ABSParser#AddExp.
    def exitAddExp(self, ctx:ABSParser.AddExpContext):
        pass


    # Enter a parse tree produced by ABSParser#NullExp.
    def enterNullExp(self, ctx:ABSParser.NullExpContext):
        pass

    # Exit a parse tree produced by ABSParser#NullExp.
    def exitNullExp(self, ctx:ABSParser.NullExpContext):
        pass


    # Enter a parse tree produced by ABSParser#EqualExp.
    def enterEqualExp(self, ctx:ABSParser.EqualExpContext):
        pass

    # Exit a parse tree produced by ABSParser#EqualExp.
    def exitEqualExp(self, ctx:ABSParser.EqualExpContext):
        pass


    # Enter a parse tree produced by ABSParser#VariadicFunctionExp.
    def enterVariadicFunctionExp(self, ctx:ABSParser.VariadicFunctionExpContext):
        pass

    # Exit a parse tree produced by ABSParser#VariadicFunctionExp.
    def exitVariadicFunctionExp(self, ctx:ABSParser.VariadicFunctionExpContext):
        pass


    # Enter a parse tree produced by ABSParser#IfExp.
    def enterIfExp(self, ctx:ABSParser.IfExpContext):
        pass

    # Exit a parse tree produced by ABSParser#IfExp.
    def exitIfExp(self, ctx:ABSParser.IfExpContext):
        pass


    # Enter a parse tree produced by ABSParser#OrExp.
    def enterOrExp(self, ctx:ABSParser.OrExpContext):
        pass

    # Exit a parse tree produced by ABSParser#OrExp.
    def exitOrExp(self, ctx:ABSParser.OrExpContext):
        pass


    # Enter a parse tree produced by ABSParser#ParenExp.
    def enterParenExp(self, ctx:ABSParser.ParenExpContext):
        pass

    # Exit a parse tree produced by ABSParser#ParenExp.
    def exitParenExp(self, ctx:ABSParser.ParenExpContext):
        pass


    # Enter a parse tree produced by ABSParser#LetExp.
    def enterLetExp(self, ctx:ABSParser.LetExpContext):
        pass

    # Exit a parse tree produced by ABSParser#LetExp.
    def exitLetExp(self, ctx:ABSParser.LetExpContext):
        pass


    # Enter a parse tree produced by ABSParser#UnaryExp.
    def enterUnaryExp(self, ctx:ABSParser.UnaryExpContext):
        pass

    # Exit a parse tree produced by ABSParser#UnaryExp.
    def exitUnaryExp(self, ctx:ABSParser.UnaryExpContext):
        pass


    # Enter a parse tree produced by ABSParser#IntExp.
    def enterIntExp(self, ctx:ABSParser.IntExpContext):
        pass

    # Exit a parse tree produced by ABSParser#IntExp.
    def exitIntExp(self, ctx:ABSParser.IntExpContext):
        pass


    # Enter a parse tree produced by ABSParser#ThisExp.
    def enterThisExp(self, ctx:ABSParser.ThisExpContext):
        pass

    # Exit a parse tree produced by ABSParser#ThisExp.
    def exitThisExp(self, ctx:ABSParser.ThisExpContext):
        pass


    # Enter a parse tree produced by ABSParser#casebranch.
    def enterCasebranch(self, ctx:ABSParser.CasebranchContext):
        pass

    # Exit a parse tree produced by ABSParser#casebranch.
    def exitCasebranch(self, ctx:ABSParser.CasebranchContext):
        pass


    # Enter a parse tree produced by ABSParser#UnderscorePattern.
    def enterUnderscorePattern(self, ctx:ABSParser.UnderscorePatternContext):
        pass

    # Exit a parse tree produced by ABSParser#UnderscorePattern.
    def exitUnderscorePattern(self, ctx:ABSParser.UnderscorePatternContext):
        pass


    # Enter a parse tree produced by ABSParser#IntPattern.
    def enterIntPattern(self, ctx:ABSParser.IntPatternContext):
        pass

    # Exit a parse tree produced by ABSParser#IntPattern.
    def exitIntPattern(self, ctx:ABSParser.IntPatternContext):
        pass


    # Enter a parse tree produced by ABSParser#StringPattern.
    def enterStringPattern(self, ctx:ABSParser.StringPatternContext):
        pass

    # Exit a parse tree produced by ABSParser#StringPattern.
    def exitStringPattern(self, ctx:ABSParser.StringPatternContext):
        pass


    # Enter a parse tree produced by ABSParser#VarPattern.
    def enterVarPattern(self, ctx:ABSParser.VarPatternContext):
        pass

    # Exit a parse tree produced by ABSParser#VarPattern.
    def exitVarPattern(self, ctx:ABSParser.VarPatternContext):
        pass


    # Enter a parse tree produced by ABSParser#ConstructorPattern.
    def enterConstructorPattern(self, ctx:ABSParser.ConstructorPatternContext):
        pass

    # Exit a parse tree produced by ABSParser#ConstructorPattern.
    def exitConstructorPattern(self, ctx:ABSParser.ConstructorPatternContext):
        pass


    # Enter a parse tree produced by ABSParser#var_or_field_ref.
    def enterVar_or_field_ref(self, ctx:ABSParser.Var_or_field_refContext):
        pass

    # Exit a parse tree produced by ABSParser#var_or_field_ref.
    def exitVar_or_field_ref(self, ctx:ABSParser.Var_or_field_refContext):
        pass


    # Enter a parse tree produced by ABSParser#pure_exp_list.
    def enterPure_exp_list(self, ctx:ABSParser.Pure_exp_listContext):
        pass

    # Exit a parse tree produced by ABSParser#pure_exp_list.
    def exitPure_exp_list(self, ctx:ABSParser.Pure_exp_listContext):
        pass


    # Enter a parse tree produced by ABSParser#list_literal.
    def enterList_literal(self, ctx:ABSParser.List_literalContext):
        pass

    # Exit a parse tree produced by ABSParser#list_literal.
    def exitList_literal(self, ctx:ABSParser.List_literalContext):
        pass


    # Enter a parse tree produced by ABSParser#annotation.
    def enterAnnotation(self, ctx:ABSParser.AnnotationContext):
        pass

    # Exit a parse tree produced by ABSParser#annotation.
    def exitAnnotation(self, ctx:ABSParser.AnnotationContext):
        pass


    # Enter a parse tree produced by ABSParser#VardeclStmt.
    def enterVardeclStmt(self, ctx:ABSParser.VardeclStmtContext):
        pass

    # Exit a parse tree produced by ABSParser#VardeclStmt.
    def exitVardeclStmt(self, ctx:ABSParser.VardeclStmtContext):
        pass


    # Enter a parse tree produced by ABSParser#AssignStmt.
    def enterAssignStmt(self, ctx:ABSParser.AssignStmtContext):
        pass

    # Exit a parse tree produced by ABSParser#AssignStmt.
    def exitAssignStmt(self, ctx:ABSParser.AssignStmtContext):
        pass


    # Enter a parse tree produced by ABSParser#SkipStmt.
    def enterSkipStmt(self, ctx:ABSParser.SkipStmtContext):
        pass

    # Exit a parse tree produced by ABSParser#SkipStmt.
    def exitSkipStmt(self, ctx:ABSParser.SkipStmtContext):
        pass


    # Enter a parse tree produced by ABSParser#ReturnStmt.
    def enterReturnStmt(self, ctx:ABSParser.ReturnStmtContext):
        pass

    # Exit a parse tree produced by ABSParser#ReturnStmt.
    def exitReturnStmt(self, ctx:ABSParser.ReturnStmtContext):
        pass


    # Enter a parse tree produced by ABSParser#AssertStmt.
    def enterAssertStmt(self, ctx:ABSParser.AssertStmtContext):
        pass

    # Exit a parse tree produced by ABSParser#AssertStmt.
    def exitAssertStmt(self, ctx:ABSParser.AssertStmtContext):
        pass


    # Enter a parse tree produced by ABSParser#BlockStmt.
    def enterBlockStmt(self, ctx:ABSParser.BlockStmtContext):
        pass

    # Exit a parse tree produced by ABSParser#BlockStmt.
    def exitBlockStmt(self, ctx:ABSParser.BlockStmtContext):
        pass


    # Enter a parse tree produced by ABSParser#IfStmt.
    def enterIfStmt(self, ctx:ABSParser.IfStmtContext):
        pass

    # Exit a parse tree produced by ABSParser#IfStmt.
    def exitIfStmt(self, ctx:ABSParser.IfStmtContext):
        pass


    # Enter a parse tree produced by ABSParser#WhileStmt.
    def enterWhileStmt(self, ctx:ABSParser.WhileStmtContext):
        pass

    # Exit a parse tree produced by ABSParser#WhileStmt.
    def exitWhileStmt(self, ctx:ABSParser.WhileStmtContext):
        pass


    # Enter a parse tree produced by ABSParser#TryCatchFinallyStmt.
    def enterTryCatchFinallyStmt(self, ctx:ABSParser.TryCatchFinallyStmtContext):
        pass

    # Exit a parse tree produced by ABSParser#TryCatchFinallyStmt.
    def exitTryCatchFinallyStmt(self, ctx:ABSParser.TryCatchFinallyStmtContext):
        pass


    # Enter a parse tree produced by ABSParser#AwaitStmt.
    def enterAwaitStmt(self, ctx:ABSParser.AwaitStmtContext):
        pass

    # Exit a parse tree produced by ABSParser#AwaitStmt.
    def exitAwaitStmt(self, ctx:ABSParser.AwaitStmtContext):
        pass


    # Enter a parse tree produced by ABSParser#SuspendStmt.
    def enterSuspendStmt(self, ctx:ABSParser.SuspendStmtContext):
        pass

    # Exit a parse tree produced by ABSParser#SuspendStmt.
    def exitSuspendStmt(self, ctx:ABSParser.SuspendStmtContext):
        pass


    # Enter a parse tree produced by ABSParser#DurationStmt.
    def enterDurationStmt(self, ctx:ABSParser.DurationStmtContext):
        pass

    # Exit a parse tree produced by ABSParser#DurationStmt.
    def exitDurationStmt(self, ctx:ABSParser.DurationStmtContext):
        pass


    # Enter a parse tree produced by ABSParser#ThrowStmt.
    def enterThrowStmt(self, ctx:ABSParser.ThrowStmtContext):
        pass

    # Exit a parse tree produced by ABSParser#ThrowStmt.
    def exitThrowStmt(self, ctx:ABSParser.ThrowStmtContext):
        pass


    # Enter a parse tree produced by ABSParser#DieStmt.
    def enterDieStmt(self, ctx:ABSParser.DieStmtContext):
        pass

    # Exit a parse tree produced by ABSParser#DieStmt.
    def exitDieStmt(self, ctx:ABSParser.DieStmtContext):
        pass


    # Enter a parse tree produced by ABSParser#MoveCogToStmt.
    def enterMoveCogToStmt(self, ctx:ABSParser.MoveCogToStmtContext):
        pass

    # Exit a parse tree produced by ABSParser#MoveCogToStmt.
    def exitMoveCogToStmt(self, ctx:ABSParser.MoveCogToStmtContext):
        pass


    # Enter a parse tree produced by ABSParser#ExpStmt.
    def enterExpStmt(self, ctx:ABSParser.ExpStmtContext):
        pass

    # Exit a parse tree produced by ABSParser#ExpStmt.
    def exitExpStmt(self, ctx:ABSParser.ExpStmtContext):
        pass


    # Enter a parse tree produced by ABSParser#CaseStmt.
    def enterCaseStmt(self, ctx:ABSParser.CaseStmtContext):
        pass

    # Exit a parse tree produced by ABSParser#CaseStmt.
    def exitCaseStmt(self, ctx:ABSParser.CaseStmtContext):
        pass


    # Enter a parse tree produced by ABSParser#ExpGuard.
    def enterExpGuard(self, ctx:ABSParser.ExpGuardContext):
        pass

    # Exit a parse tree produced by ABSParser#ExpGuard.
    def exitExpGuard(self, ctx:ABSParser.ExpGuardContext):
        pass


    # Enter a parse tree produced by ABSParser#AndGuard.
    def enterAndGuard(self, ctx:ABSParser.AndGuardContext):
        pass

    # Exit a parse tree produced by ABSParser#AndGuard.
    def exitAndGuard(self, ctx:ABSParser.AndGuardContext):
        pass


    # Enter a parse tree produced by ABSParser#ClaimGuard.
    def enterClaimGuard(self, ctx:ABSParser.ClaimGuardContext):
        pass

    # Exit a parse tree produced by ABSParser#ClaimGuard.
    def exitClaimGuard(self, ctx:ABSParser.ClaimGuardContext):
        pass


    # Enter a parse tree produced by ABSParser#DurationGuard.
    def enterDurationGuard(self, ctx:ABSParser.DurationGuardContext):
        pass

    # Exit a parse tree produced by ABSParser#DurationGuard.
    def exitDurationGuard(self, ctx:ABSParser.DurationGuardContext):
        pass


    # Enter a parse tree produced by ABSParser#casestmtbranch.
    def enterCasestmtbranch(self, ctx:ABSParser.CasestmtbranchContext):
        pass

    # Exit a parse tree produced by ABSParser#casestmtbranch.
    def exitCasestmtbranch(self, ctx:ABSParser.CasestmtbranchContext):
        pass


    # Enter a parse tree produced by ABSParser#datatype_decl.
    def enterDatatype_decl(self, ctx:ABSParser.Datatype_declContext):
        pass

    # Exit a parse tree produced by ABSParser#datatype_decl.
    def exitDatatype_decl(self, ctx:ABSParser.Datatype_declContext):
        pass


    # Enter a parse tree produced by ABSParser#data_constructor.
    def enterData_constructor(self, ctx:ABSParser.Data_constructorContext):
        pass

    # Exit a parse tree produced by ABSParser#data_constructor.
    def exitData_constructor(self, ctx:ABSParser.Data_constructorContext):
        pass


    # Enter a parse tree produced by ABSParser#data_constructor_arg.
    def enterData_constructor_arg(self, ctx:ABSParser.Data_constructor_argContext):
        pass

    # Exit a parse tree produced by ABSParser#data_constructor_arg.
    def exitData_constructor_arg(self, ctx:ABSParser.Data_constructor_argContext):
        pass


    # Enter a parse tree produced by ABSParser#typesyn_decl.
    def enterTypesyn_decl(self, ctx:ABSParser.Typesyn_declContext):
        pass

    # Exit a parse tree produced by ABSParser#typesyn_decl.
    def exitTypesyn_decl(self, ctx:ABSParser.Typesyn_declContext):
        pass


    # Enter a parse tree produced by ABSParser#exception_decl.
    def enterException_decl(self, ctx:ABSParser.Exception_declContext):
        pass

    # Exit a parse tree produced by ABSParser#exception_decl.
    def exitException_decl(self, ctx:ABSParser.Exception_declContext):
        pass


    # Enter a parse tree produced by ABSParser#function_decl.
    def enterFunction_decl(self, ctx:ABSParser.Function_declContext):
        pass

    # Exit a parse tree produced by ABSParser#function_decl.
    def exitFunction_decl(self, ctx:ABSParser.Function_declContext):
        pass


    # Enter a parse tree produced by ABSParser#interface_decl.
    def enterInterface_decl(self, ctx:ABSParser.Interface_declContext):
        pass

    # Exit a parse tree produced by ABSParser#interface_decl.
    def exitInterface_decl(self, ctx:ABSParser.Interface_declContext):
        pass


    # Enter a parse tree produced by ABSParser#methodsig.
    def enterMethodsig(self, ctx:ABSParser.MethodsigContext):
        pass

    # Exit a parse tree produced by ABSParser#methodsig.
    def exitMethodsig(self, ctx:ABSParser.MethodsigContext):
        pass


    # Enter a parse tree produced by ABSParser#class_decl.
    def enterClass_decl(self, ctx:ABSParser.Class_declContext):
        pass

    # Exit a parse tree produced by ABSParser#class_decl.
    def exitClass_decl(self, ctx:ABSParser.Class_declContext):
        pass


    # Enter a parse tree produced by ABSParser#field_decl.
    def enterField_decl(self, ctx:ABSParser.Field_declContext):
        pass

    # Exit a parse tree produced by ABSParser#field_decl.
    def exitField_decl(self, ctx:ABSParser.Field_declContext):
        pass


    # Enter a parse tree produced by ABSParser#method.
    def enterMethod(self, ctx:ABSParser.MethodContext):
        pass

    # Exit a parse tree produced by ABSParser#method.
    def exitMethod(self, ctx:ABSParser.MethodContext):
        pass


    # Enter a parse tree produced by ABSParser#module_decl.
    def enterModule_decl(self, ctx:ABSParser.Module_declContext):
        pass

    # Exit a parse tree produced by ABSParser#module_decl.
    def exitModule_decl(self, ctx:ABSParser.Module_declContext):
        pass


    # Enter a parse tree produced by ABSParser#module_export.
    def enterModule_export(self, ctx:ABSParser.Module_exportContext):
        pass

    # Exit a parse tree produced by ABSParser#module_export.
    def exitModule_export(self, ctx:ABSParser.Module_exportContext):
        pass


    # Enter a parse tree produced by ABSParser#module_import.
    def enterModule_import(self, ctx:ABSParser.Module_importContext):
        pass

    # Exit a parse tree produced by ABSParser#module_import.
    def exitModule_import(self, ctx:ABSParser.Module_importContext):
        pass


    # Enter a parse tree produced by ABSParser#decl.
    def enterDecl(self, ctx:ABSParser.DeclContext):
        pass

    # Exit a parse tree produced by ABSParser#decl.
    def exitDecl(self, ctx:ABSParser.DeclContext):
        pass


    # Enter a parse tree produced by ABSParser#delta_decl.
    def enterDelta_decl(self, ctx:ABSParser.Delta_declContext):
        pass

    # Exit a parse tree produced by ABSParser#delta_decl.
    def exitDelta_decl(self, ctx:ABSParser.Delta_declContext):
        pass


    # Enter a parse tree produced by ABSParser#DeltaFieldParam.
    def enterDeltaFieldParam(self, ctx:ABSParser.DeltaFieldParamContext):
        pass

    # Exit a parse tree produced by ABSParser#DeltaFieldParam.
    def exitDeltaFieldParam(self, ctx:ABSParser.DeltaFieldParamContext):
        pass


    # Enter a parse tree produced by ABSParser#DeltaClassParam.
    def enterDeltaClassParam(self, ctx:ABSParser.DeltaClassParamContext):
        pass

    # Exit a parse tree produced by ABSParser#DeltaClassParam.
    def exitDeltaClassParam(self, ctx:ABSParser.DeltaClassParamContext):
        pass


    # Enter a parse tree produced by ABSParser#DeltaHasFieldCondition.
    def enterDeltaHasFieldCondition(self, ctx:ABSParser.DeltaHasFieldConditionContext):
        pass

    # Exit a parse tree produced by ABSParser#DeltaHasFieldCondition.
    def exitDeltaHasFieldCondition(self, ctx:ABSParser.DeltaHasFieldConditionContext):
        pass


    # Enter a parse tree produced by ABSParser#DeltaHasMethodCondition.
    def enterDeltaHasMethodCondition(self, ctx:ABSParser.DeltaHasMethodConditionContext):
        pass

    # Exit a parse tree produced by ABSParser#DeltaHasMethodCondition.
    def exitDeltaHasMethodCondition(self, ctx:ABSParser.DeltaHasMethodConditionContext):
        pass


    # Enter a parse tree produced by ABSParser#DeltaHasInterfaceCondition.
    def enterDeltaHasInterfaceCondition(self, ctx:ABSParser.DeltaHasInterfaceConditionContext):
        pass

    # Exit a parse tree produced by ABSParser#DeltaHasInterfaceCondition.
    def exitDeltaHasInterfaceCondition(self, ctx:ABSParser.DeltaHasInterfaceConditionContext):
        pass


    # Enter a parse tree produced by ABSParser#delta_access.
    def enterDelta_access(self, ctx:ABSParser.Delta_accessContext):
        pass

    # Exit a parse tree produced by ABSParser#delta_access.
    def exitDelta_access(self, ctx:ABSParser.Delta_accessContext):
        pass


    # Enter a parse tree produced by ABSParser#module_modifier.
    def enterModule_modifier(self, ctx:ABSParser.Module_modifierContext):
        pass

    # Exit a parse tree produced by ABSParser#module_modifier.
    def exitModule_modifier(self, ctx:ABSParser.Module_modifierContext):
        pass


    # Enter a parse tree produced by ABSParser#DeltaAddFunctionModifier.
    def enterDeltaAddFunctionModifier(self, ctx:ABSParser.DeltaAddFunctionModifierContext):
        pass

    # Exit a parse tree produced by ABSParser#DeltaAddFunctionModifier.
    def exitDeltaAddFunctionModifier(self, ctx:ABSParser.DeltaAddFunctionModifierContext):
        pass


    # Enter a parse tree produced by ABSParser#DeltaAddDataTypeModifier.
    def enterDeltaAddDataTypeModifier(self, ctx:ABSParser.DeltaAddDataTypeModifierContext):
        pass

    # Exit a parse tree produced by ABSParser#DeltaAddDataTypeModifier.
    def exitDeltaAddDataTypeModifier(self, ctx:ABSParser.DeltaAddDataTypeModifierContext):
        pass


    # Enter a parse tree produced by ABSParser#DeltaAddTypeSynModifier.
    def enterDeltaAddTypeSynModifier(self, ctx:ABSParser.DeltaAddTypeSynModifierContext):
        pass

    # Exit a parse tree produced by ABSParser#DeltaAddTypeSynModifier.
    def exitDeltaAddTypeSynModifier(self, ctx:ABSParser.DeltaAddTypeSynModifierContext):
        pass


    # Enter a parse tree produced by ABSParser#DeltaModifyTypeSynModifier.
    def enterDeltaModifyTypeSynModifier(self, ctx:ABSParser.DeltaModifyTypeSynModifierContext):
        pass

    # Exit a parse tree produced by ABSParser#DeltaModifyTypeSynModifier.
    def exitDeltaModifyTypeSynModifier(self, ctx:ABSParser.DeltaModifyTypeSynModifierContext):
        pass


    # Enter a parse tree produced by ABSParser#DeltaModifyDataTypeModifier.
    def enterDeltaModifyDataTypeModifier(self, ctx:ABSParser.DeltaModifyDataTypeModifierContext):
        pass

    # Exit a parse tree produced by ABSParser#DeltaModifyDataTypeModifier.
    def exitDeltaModifyDataTypeModifier(self, ctx:ABSParser.DeltaModifyDataTypeModifierContext):
        pass


    # Enter a parse tree produced by ABSParser#DeltaAddClassModifier.
    def enterDeltaAddClassModifier(self, ctx:ABSParser.DeltaAddClassModifierContext):
        pass

    # Exit a parse tree produced by ABSParser#DeltaAddClassModifier.
    def exitDeltaAddClassModifier(self, ctx:ABSParser.DeltaAddClassModifierContext):
        pass


    # Enter a parse tree produced by ABSParser#DeltaRemoveClassModifier.
    def enterDeltaRemoveClassModifier(self, ctx:ABSParser.DeltaRemoveClassModifierContext):
        pass

    # Exit a parse tree produced by ABSParser#DeltaRemoveClassModifier.
    def exitDeltaRemoveClassModifier(self, ctx:ABSParser.DeltaRemoveClassModifierContext):
        pass


    # Enter a parse tree produced by ABSParser#DeltaModifyClassModifier.
    def enterDeltaModifyClassModifier(self, ctx:ABSParser.DeltaModifyClassModifierContext):
        pass

    # Exit a parse tree produced by ABSParser#DeltaModifyClassModifier.
    def exitDeltaModifyClassModifier(self, ctx:ABSParser.DeltaModifyClassModifierContext):
        pass


    # Enter a parse tree produced by ABSParser#DeltaAddInterfaceModifier.
    def enterDeltaAddInterfaceModifier(self, ctx:ABSParser.DeltaAddInterfaceModifierContext):
        pass

    # Exit a parse tree produced by ABSParser#DeltaAddInterfaceModifier.
    def exitDeltaAddInterfaceModifier(self, ctx:ABSParser.DeltaAddInterfaceModifierContext):
        pass


    # Enter a parse tree produced by ABSParser#DeltaRemoveInterfaceModifier.
    def enterDeltaRemoveInterfaceModifier(self, ctx:ABSParser.DeltaRemoveInterfaceModifierContext):
        pass

    # Exit a parse tree produced by ABSParser#DeltaRemoveInterfaceModifier.
    def exitDeltaRemoveInterfaceModifier(self, ctx:ABSParser.DeltaRemoveInterfaceModifierContext):
        pass


    # Enter a parse tree produced by ABSParser#DeltaModifyInterfaceModifier.
    def enterDeltaModifyInterfaceModifier(self, ctx:ABSParser.DeltaModifyInterfaceModifierContext):
        pass

    # Exit a parse tree produced by ABSParser#DeltaModifyInterfaceModifier.
    def exitDeltaModifyInterfaceModifier(self, ctx:ABSParser.DeltaModifyInterfaceModifierContext):
        pass


    # Enter a parse tree produced by ABSParser#DeltaAddFieldFragment.
    def enterDeltaAddFieldFragment(self, ctx:ABSParser.DeltaAddFieldFragmentContext):
        pass

    # Exit a parse tree produced by ABSParser#DeltaAddFieldFragment.
    def exitDeltaAddFieldFragment(self, ctx:ABSParser.DeltaAddFieldFragmentContext):
        pass


    # Enter a parse tree produced by ABSParser#DeltaRemoveFieldFragment.
    def enterDeltaRemoveFieldFragment(self, ctx:ABSParser.DeltaRemoveFieldFragmentContext):
        pass

    # Exit a parse tree produced by ABSParser#DeltaRemoveFieldFragment.
    def exitDeltaRemoveFieldFragment(self, ctx:ABSParser.DeltaRemoveFieldFragmentContext):
        pass


    # Enter a parse tree produced by ABSParser#DeltaAddMethodFragment.
    def enterDeltaAddMethodFragment(self, ctx:ABSParser.DeltaAddMethodFragmentContext):
        pass

    # Exit a parse tree produced by ABSParser#DeltaAddMethodFragment.
    def exitDeltaAddMethodFragment(self, ctx:ABSParser.DeltaAddMethodFragmentContext):
        pass


    # Enter a parse tree produced by ABSParser#DeltaModifyMethodFragment.
    def enterDeltaModifyMethodFragment(self, ctx:ABSParser.DeltaModifyMethodFragmentContext):
        pass

    # Exit a parse tree produced by ABSParser#DeltaModifyMethodFragment.
    def exitDeltaModifyMethodFragment(self, ctx:ABSParser.DeltaModifyMethodFragmentContext):
        pass


    # Enter a parse tree produced by ABSParser#DeltaRemoveMethodFragment.
    def enterDeltaRemoveMethodFragment(self, ctx:ABSParser.DeltaRemoveMethodFragmentContext):
        pass

    # Exit a parse tree produced by ABSParser#DeltaRemoveMethodFragment.
    def exitDeltaRemoveMethodFragment(self, ctx:ABSParser.DeltaRemoveMethodFragmentContext):
        pass


    # Enter a parse tree produced by ABSParser#DeltaAddMethodsigFragment.
    def enterDeltaAddMethodsigFragment(self, ctx:ABSParser.DeltaAddMethodsigFragmentContext):
        pass

    # Exit a parse tree produced by ABSParser#DeltaAddMethodsigFragment.
    def exitDeltaAddMethodsigFragment(self, ctx:ABSParser.DeltaAddMethodsigFragmentContext):
        pass


    # Enter a parse tree produced by ABSParser#DeltaRemoveMethodsigFragment.
    def enterDeltaRemoveMethodsigFragment(self, ctx:ABSParser.DeltaRemoveMethodsigFragmentContext):
        pass

    # Exit a parse tree produced by ABSParser#DeltaRemoveMethodsigFragment.
    def exitDeltaRemoveMethodsigFragment(self, ctx:ABSParser.DeltaRemoveMethodsigFragmentContext):
        pass


    # Enter a parse tree produced by ABSParser#DeltaAddModuleImportFragment.
    def enterDeltaAddModuleImportFragment(self, ctx:ABSParser.DeltaAddModuleImportFragmentContext):
        pass

    # Exit a parse tree produced by ABSParser#DeltaAddModuleImportFragment.
    def exitDeltaAddModuleImportFragment(self, ctx:ABSParser.DeltaAddModuleImportFragmentContext):
        pass


    # Enter a parse tree produced by ABSParser#DeltaAddModuleExportFragment.
    def enterDeltaAddModuleExportFragment(self, ctx:ABSParser.DeltaAddModuleExportFragmentContext):
        pass

    # Exit a parse tree produced by ABSParser#DeltaAddModuleExportFragment.
    def exitDeltaAddModuleExportFragment(self, ctx:ABSParser.DeltaAddModuleExportFragmentContext):
        pass


    # Enter a parse tree produced by ABSParser#UpdateDecl.
    def enterUpdateDecl(self, ctx:ABSParser.UpdateDeclContext):
        pass

    # Exit a parse tree produced by ABSParser#UpdateDecl.
    def exitUpdateDecl(self, ctx:ABSParser.UpdateDeclContext):
        pass


    # Enter a parse tree produced by ABSParser#ObjectUpdateDecl.
    def enterObjectUpdateDecl(self, ctx:ABSParser.ObjectUpdateDeclContext):
        pass

    # Exit a parse tree produced by ABSParser#ObjectUpdateDecl.
    def exitObjectUpdateDecl(self, ctx:ABSParser.ObjectUpdateDeclContext):
        pass


    # Enter a parse tree produced by ABSParser#ObjectUpdateAssignStmt.
    def enterObjectUpdateAssignStmt(self, ctx:ABSParser.ObjectUpdateAssignStmtContext):
        pass

    # Exit a parse tree produced by ABSParser#ObjectUpdateAssignStmt.
    def exitObjectUpdateAssignStmt(self, ctx:ABSParser.ObjectUpdateAssignStmtContext):
        pass


    # Enter a parse tree produced by ABSParser#UpdatePreambleDecl.
    def enterUpdatePreambleDecl(self, ctx:ABSParser.UpdatePreambleDeclContext):
        pass

    # Exit a parse tree produced by ABSParser#UpdatePreambleDecl.
    def exitUpdatePreambleDecl(self, ctx:ABSParser.UpdatePreambleDeclContext):
        pass


    # Enter a parse tree produced by ABSParser#productline_decl.
    def enterProductline_decl(self, ctx:ABSParser.Productline_declContext):
        pass

    # Exit a parse tree produced by ABSParser#productline_decl.
    def exitProductline_decl(self, ctx:ABSParser.Productline_declContext):
        pass


    # Enter a parse tree produced by ABSParser#feature.
    def enterFeature(self, ctx:ABSParser.FeatureContext):
        pass

    # Exit a parse tree produced by ABSParser#feature.
    def exitFeature(self, ctx:ABSParser.FeatureContext):
        pass


    # Enter a parse tree produced by ABSParser#delta_clause.
    def enterDelta_clause(self, ctx:ABSParser.Delta_clauseContext):
        pass

    # Exit a parse tree produced by ABSParser#delta_clause.
    def exitDelta_clause(self, ctx:ABSParser.Delta_clauseContext):
        pass


    # Enter a parse tree produced by ABSParser#deltaspec.
    def enterDeltaspec(self, ctx:ABSParser.DeltaspecContext):
        pass

    # Exit a parse tree produced by ABSParser#deltaspec.
    def exitDeltaspec(self, ctx:ABSParser.DeltaspecContext):
        pass


    # Enter a parse tree produced by ABSParser#FIDAIDDeltaspecParam.
    def enterFIDAIDDeltaspecParam(self, ctx:ABSParser.FIDAIDDeltaspecParamContext):
        pass

    # Exit a parse tree produced by ABSParser#FIDAIDDeltaspecParam.
    def exitFIDAIDDeltaspecParam(self, ctx:ABSParser.FIDAIDDeltaspecParamContext):
        pass


    # Enter a parse tree produced by ABSParser#IntDeltaspecParam.
    def enterIntDeltaspecParam(self, ctx:ABSParser.IntDeltaspecParamContext):
        pass

    # Exit a parse tree produced by ABSParser#IntDeltaspecParam.
    def exitIntDeltaspecParam(self, ctx:ABSParser.IntDeltaspecParamContext):
        pass


    # Enter a parse tree produced by ABSParser#BoolOrIDDeltaspecParam.
    def enterBoolOrIDDeltaspecParam(self, ctx:ABSParser.BoolOrIDDeltaspecParamContext):
        pass

    # Exit a parse tree produced by ABSParser#BoolOrIDDeltaspecParam.
    def exitBoolOrIDDeltaspecParam(self, ctx:ABSParser.BoolOrIDDeltaspecParamContext):
        pass


    # Enter a parse tree produced by ABSParser#after_condition.
    def enterAfter_condition(self, ctx:ABSParser.After_conditionContext):
        pass

    # Exit a parse tree produced by ABSParser#after_condition.
    def exitAfter_condition(self, ctx:ABSParser.After_conditionContext):
        pass


    # Enter a parse tree produced by ABSParser#from_condition.
    def enterFrom_condition(self, ctx:ABSParser.From_conditionContext):
        pass

    # Exit a parse tree produced by ABSParser#from_condition.
    def exitFrom_condition(self, ctx:ABSParser.From_conditionContext):
        pass


    # Enter a parse tree produced by ABSParser#when_condition.
    def enterWhen_condition(self, ctx:ABSParser.When_conditionContext):
        pass

    # Exit a parse tree produced by ABSParser#when_condition.
    def exitWhen_condition(self, ctx:ABSParser.When_conditionContext):
        pass


    # Enter a parse tree produced by ABSParser#FeatureApplicationCondition.
    def enterFeatureApplicationCondition(self, ctx:ABSParser.FeatureApplicationConditionContext):
        pass

    # Exit a parse tree produced by ABSParser#FeatureApplicationCondition.
    def exitFeatureApplicationCondition(self, ctx:ABSParser.FeatureApplicationConditionContext):
        pass


    # Enter a parse tree produced by ABSParser#AndApplicationCondition.
    def enterAndApplicationCondition(self, ctx:ABSParser.AndApplicationConditionContext):
        pass

    # Exit a parse tree produced by ABSParser#AndApplicationCondition.
    def exitAndApplicationCondition(self, ctx:ABSParser.AndApplicationConditionContext):
        pass


    # Enter a parse tree produced by ABSParser#ParenApplicationCondition.
    def enterParenApplicationCondition(self, ctx:ABSParser.ParenApplicationConditionContext):
        pass

    # Exit a parse tree produced by ABSParser#ParenApplicationCondition.
    def exitParenApplicationCondition(self, ctx:ABSParser.ParenApplicationConditionContext):
        pass


    # Enter a parse tree produced by ABSParser#NotApplicationCondition.
    def enterNotApplicationCondition(self, ctx:ABSParser.NotApplicationConditionContext):
        pass

    # Exit a parse tree produced by ABSParser#NotApplicationCondition.
    def exitNotApplicationCondition(self, ctx:ABSParser.NotApplicationConditionContext):
        pass


    # Enter a parse tree produced by ABSParser#OrApplicationCondition.
    def enterOrApplicationCondition(self, ctx:ABSParser.OrApplicationConditionContext):
        pass

    # Exit a parse tree produced by ABSParser#OrApplicationCondition.
    def exitOrApplicationCondition(self, ctx:ABSParser.OrApplicationConditionContext):
        pass


    # Enter a parse tree produced by ABSParser#attr_assignment.
    def enterAttr_assignment(self, ctx:ABSParser.Attr_assignmentContext):
        pass

    # Exit a parse tree produced by ABSParser#attr_assignment.
    def exitAttr_assignment(self, ctx:ABSParser.Attr_assignmentContext):
        pass


    # Enter a parse tree produced by ABSParser#product_decl.
    def enterProduct_decl(self, ctx:ABSParser.Product_declContext):
        pass

    # Exit a parse tree produced by ABSParser#product_decl.
    def exitProduct_decl(self, ctx:ABSParser.Product_declContext):
        pass


    # Enter a parse tree produced by ABSParser#product_reconfiguration.
    def enterProduct_reconfiguration(self, ctx:ABSParser.Product_reconfigurationContext):
        pass

    # Exit a parse tree produced by ABSParser#product_reconfiguration.
    def exitProduct_reconfiguration(self, ctx:ABSParser.Product_reconfigurationContext):
        pass


    # Enter a parse tree produced by ABSParser#fextension.
    def enterFextension(self, ctx:ABSParser.FextensionContext):
        pass

    # Exit a parse tree produced by ABSParser#fextension.
    def exitFextension(self, ctx:ABSParser.FextensionContext):
        pass


    # Enter a parse tree produced by ABSParser#feature_decl.
    def enterFeature_decl(self, ctx:ABSParser.Feature_declContext):
        pass

    # Exit a parse tree produced by ABSParser#feature_decl.
    def exitFeature_decl(self, ctx:ABSParser.Feature_declContext):
        pass


    # Enter a parse tree produced by ABSParser#feature_decl_group.
    def enterFeature_decl_group(self, ctx:ABSParser.Feature_decl_groupContext):
        pass

    # Exit a parse tree produced by ABSParser#feature_decl_group.
    def exitFeature_decl_group(self, ctx:ABSParser.Feature_decl_groupContext):
        pass


    # Enter a parse tree produced by ABSParser#fnode.
    def enterFnode(self, ctx:ABSParser.FnodeContext):
        pass

    # Exit a parse tree produced by ABSParser#fnode.
    def exitFnode(self, ctx:ABSParser.FnodeContext):
        pass


    # Enter a parse tree produced by ABSParser#feature_decl_attribute.
    def enterFeature_decl_attribute(self, ctx:ABSParser.Feature_decl_attributeContext):
        pass

    # Exit a parse tree produced by ABSParser#feature_decl_attribute.
    def exitFeature_decl_attribute(self, ctx:ABSParser.Feature_decl_attributeContext):
        pass


    # Enter a parse tree produced by ABSParser#FeatureDeclConstraintIfIn.
    def enterFeatureDeclConstraintIfIn(self, ctx:ABSParser.FeatureDeclConstraintIfInContext):
        pass

    # Exit a parse tree produced by ABSParser#FeatureDeclConstraintIfIn.
    def exitFeatureDeclConstraintIfIn(self, ctx:ABSParser.FeatureDeclConstraintIfInContext):
        pass


    # Enter a parse tree produced by ABSParser#FeatureDeclConstraintIfOut.
    def enterFeatureDeclConstraintIfOut(self, ctx:ABSParser.FeatureDeclConstraintIfOutContext):
        pass

    # Exit a parse tree produced by ABSParser#FeatureDeclConstraintIfOut.
    def exitFeatureDeclConstraintIfOut(self, ctx:ABSParser.FeatureDeclConstraintIfOutContext):
        pass


    # Enter a parse tree produced by ABSParser#FeatureDeclConstraintExclude.
    def enterFeatureDeclConstraintExclude(self, ctx:ABSParser.FeatureDeclConstraintExcludeContext):
        pass

    # Exit a parse tree produced by ABSParser#FeatureDeclConstraintExclude.
    def exitFeatureDeclConstraintExclude(self, ctx:ABSParser.FeatureDeclConstraintExcludeContext):
        pass


    # Enter a parse tree produced by ABSParser#FeatureDeclConstraintRequire.
    def enterFeatureDeclConstraintRequire(self, ctx:ABSParser.FeatureDeclConstraintRequireContext):
        pass

    # Exit a parse tree produced by ABSParser#FeatureDeclConstraintRequire.
    def exitFeatureDeclConstraintRequire(self, ctx:ABSParser.FeatureDeclConstraintRequireContext):
        pass


    # Enter a parse tree produced by ABSParser#mexp.
    def enterMexp(self, ctx:ABSParser.MexpContext):
        pass

    # Exit a parse tree produced by ABSParser#mexp.
    def exitMexp(self, ctx:ABSParser.MexpContext):
        pass


    # Enter a parse tree produced by ABSParser#boundary_int.
    def enterBoundary_int(self, ctx:ABSParser.Boundary_intContext):
        pass

    # Exit a parse tree produced by ABSParser#boundary_int.
    def exitBoundary_int(self, ctx:ABSParser.Boundary_intContext):
        pass


    # Enter a parse tree produced by ABSParser#boundary_val.
    def enterBoundary_val(self, ctx:ABSParser.Boundary_valContext):
        pass

    # Exit a parse tree produced by ABSParser#boundary_val.
    def exitBoundary_val(self, ctx:ABSParser.Boundary_valContext):
        pass


    # Enter a parse tree produced by ABSParser#main_block.
    def enterMain_block(self, ctx:ABSParser.Main_blockContext):
        pass

    # Exit a parse tree produced by ABSParser#main_block.
    def exitMain_block(self, ctx:ABSParser.Main_blockContext):
        pass


    # Enter a parse tree produced by ABSParser#compilation_unit.
    def enterCompilation_unit(self, ctx:ABSParser.Compilation_unitContext):
        pass

    # Exit a parse tree produced by ABSParser#compilation_unit.
    def exitCompilation_unit(self, ctx:ABSParser.Compilation_unitContext):
        pass


    # Enter a parse tree produced by ABSParser#goal.
    def enterGoal(self, ctx:ABSParser.GoalContext):
        pass

    # Exit a parse tree produced by ABSParser#goal.
    def exitGoal(self, ctx:ABSParser.GoalContext):
        pass



del ABSParser