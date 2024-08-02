from docutils import nodes
from docutils.statemachine import StringList
from sphinx.util.docutils import SphinxDirective
from sphinx.util import nested_parse_with_titles
from importlib import import_module
import re
import numpy as np


class AutoComponentDirective(SphinxDirective):
    has_content = True
    optional_arguments = 1
    option_spec = {}

    def run(self):
        content = "".join(self.content).strip()
        mod_ = import_module(".".join(content.split(".")[:-1]))
        cls_ = getattr(mod_, content.split(".")[-1])

        document = []

        # parse class docstring
        sig = ".. class:: {}\n".format(content)
        sect = nodes.section()
        sl = StringList(
            sig.split("\n") + ("\n    " + cls_.__doc__).split("\n"), self.content.parent
        )
        sect.document = self.state.document
        nested_parse_with_titles(self.state, sl, sect)
        document.extend(sect.children)

        # parse class attributes
        for definition in [
            "_inputs",
            "inwards",
            "_outputs",
            "outwards",
            "_parameters",
            "_constants",
            "_states",
        ]:
            if getattr(cls_, "{}_info".format(definition)):
                attribute = getattr(cls_, "{}_info".format(definition))
                para = nodes.paragraph()
                if definition[0] == "_":
                    definition = definition[1:]
                rubric = nodes.rubric(
                    nodes.Text(definition.capitalize()),
                    nodes.Text(definition.capitalize()),
                )
                para += rubric

                for name, info in attribute.items():
                    field_list = nodes.field_list()
                    # add the name of the attribute
                    field = nodes.field()
                    field += nodes.field_name(text="name")
                    field_body = nodes.field_body()
                    field_body += nodes.paragraph(text=name)
                    field += field_body
                    field_list += field
                    # add the properties of the attribute
                    for key, value in info.items():
                        field = nodes.field()
                        field += nodes.field_name(text=key)
                        field_body = nodes.field_body()
                        if key == "units" and value != "1":
                            sl = StringList(
                                [re.sub("(-?[0-9]+)", "\\ :sup:`\\1`\\ ", value)], field
                            )
                            self.state.nested_parse(sl, 0, field_body)
                        elif key == "default_value":
                            field_body += nodes.paragraph(
                                text=np.format_float_scientific(value, trim="0")
                            )
                        elif key == "to":
                            field_body += nodes.paragraph(text=", ".join(value))
                        else:
                            field_body += nodes.paragraph(text=value)
                        field += field_body
                        field_list += field

                    para += field_list

                document.append(para)

            # spacedomain special properties
            para = nodes.paragraph()
            rubric = nodes.rubric(
                nodes.Text("SpaceDomain Properties"),
                nodes.Text("SpaceDomain Properties"),
            )
            para += rubric

        for name in ["land_sea_mask", "flow_direction", "cell_area"]:
            field_list = nodes.field_list()
            attribute = getattr(cls_, "_requires_{}".format(name))
            # name
            field = nodes.field()
            field += nodes.field_name(text="name")
            field_body = nodes.field_body()
            field_body += nodes.paragraph(text=name)
            field += field_body
            field_list += field
            # required
            field = nodes.field()
            field += nodes.field_name(text="required")
            field_body = nodes.field_body()
            field_body += nodes.paragraph(text=attribute)
            field += field_body
            field_list += field

            para += field_list

        document.append(para)

        return document


def setup(app):
    app.add_directive("autocomponent", AutoComponentDirective)
    return {"parallel_read_safe": True, "parallel_write_safe": True}
