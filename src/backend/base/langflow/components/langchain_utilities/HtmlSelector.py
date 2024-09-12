from bs4 import BeautifulSoup
from langchain_community.document_transformers import Html2TextTransformer

from langflow.base.document_transformers.model import LCDocumentTransformerComponent
from langflow.custom import CustomComponent, Component
from langflow.inputs import DataInput, IntInput, BoolInput, StrInput
from langflow.schema import Data
from langflow.template import Output


class HtmlSelectorComponent(Component):

    display_name = "HTML selector"
    description = "Selects HTML content based on CSS selectors."
    name = "HtmlSelector"

    inputs = [
        StrInput(
            name="selectors",
            display_name="Selectors",
            info="The CSS selectors to use to select the HTML content. The first match will be selected.",
            is_list=True,
        ),

        DataInput(
            name="data_input",
            display_name="Input",
            info="The HTML to convert to text",
            input_types=["Data"],
        ),
    ]

    outputs = [
        Output(display_name="Data", name="data", method="select_data"),
    ]


    def select_data(self) -> list[Data]:
        data_input = self.data_input
        outputs = []

        if not isinstance(data_input, list):
            data_input = [data_input]

        for _input in data_input:
            output = _input.copy()
            soup = BeautifulSoup(_input.get_text(), "html.parser")
            for selector in self.selectors:
                if not selector:
                    continue
                elements = soup.select(selector)
                if elements:
                    output.data[output.text_key] = str(elements[0])
                    outputs.append(output)
                    break

        return outputs
