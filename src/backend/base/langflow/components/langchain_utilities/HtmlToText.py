from langchain_community.document_transformers import Html2TextTransformer

from langflow.base.document_transformers.model import LCDocumentTransformerComponent
from langflow.inputs import DataInput


class HtmlToTextComponent(LCDocumentTransformerComponent):

    display_name = "HTML to Text"
    description = "Convert HTML content to plain text in markdown format."
    name = "HtmlToText"

    inputs = [
        DataInput(
            name="data_input",
            display_name="Input",
            info="The HTML document to convert to text",
            input_types=["Document", "Data"],
        ),
    ]

    def get_data_input(self):
        return self.data_input

    def build_document_transformer(self):
        return Html2TextTransformer()