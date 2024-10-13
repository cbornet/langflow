import ast


class RequiredInputsVisitor(ast.NodeVisitor):
    def __init__(self, inputs) -> None:
        self.inputs = inputs
        self.required_inputs = set()

    def visit_Attribute(self, node) -> None:
        if isinstance(node.value, ast.Name) and node.value.id == "self" and node.attr in self.inputs:
            self.required_inputs.add(node.attr)
        self.generic_visit(node)
