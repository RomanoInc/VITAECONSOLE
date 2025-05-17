from textual.screen import Screen
from textual import events
from textual.app import App, ComposeResult
from textual.widgets import RichLog

from rich.syntax import Syntax
from rich.table import Table
from rich.traceback import Traceback



from textual import containers, events, lazy, on
from textual.app import ComposeResult
from textual.binding import Binding
from textual.demo.data import COUNTRIES, DUNE_BIOS, MOVIES, MOVIES_TREE
from textual.demo.page import PageScreen
from textual.reactive import reactive, var
from textual.suggester import SuggestFromList
from textual.theme import BUILTIN_THEMES
from textual.widgets import (
    Input,
    Label,
    Markdown,
    MaskedInput,
    RichLog,

)
WIDGETS_MD = """\
# Informacion hoja de vida
 
"""


INPUT_DATA = []

# class InputApp(App):
#     """App to display key events."""

#     def compose(self) -> ComposeResult:
#         yield RichLog()

#     def on_key(self, event: events.Key) -> None:
#         self.query_one(RichLog).write(event)


class Inputs(containers.VerticalGroup ):
    def __init__(self, title = "", labels = []):
        super().__init__(self, title = "", labels = [])
        # Inicializar los atributos de la clase
        self.title = title
        self.labels = labels

    ALLOW_MAXIMIZE = True
    DEFAULT_CLASSES = "column"
    INPUTS_MD = """\## hola """
    DEFAULT_CSS = """
    Inputs {
        Grid {
            background: $boost;
            padding: 1 2;
            height: auto;
            grid-size: 2;
            grid-gutter: 1;
            grid-columns: auto 1fr;
            border: tall blank;
            &:focus-within {
                border: tall $accent;
            }
            Label {
                width: 100%;
                padding: 1;
                text-align: right;
            }
        }
    }
    """

    def compose(self) -> ComposeResult:
        yield Markdown(self.INPUTS_MD)
        with containers.Grid():
            for i in self.labels:
                lbl = yield Label(f"{i}")
                inp = yield Input()

                INPUT_DATA.append(lbl)


            # yield Label("name")
            # yield Input(placeholder="Type anything here")
            # yield Label("id")
            # yield Input(
            #     type="number", placeholder="Type a number here", valid_empty=True
            # )
            # yield Label("email")
            # r = yield MaskedInput(
            #     "9999-9999-9999-9999;0",
            #     tooltip="Obviously not your real credit card!",
            #     valid_empty=True,
            # )
            # yield Label("Country")
            # yield Input(
            #     suggester=SuggestFromList(COUNTRIES, case_sensitive=False),
            #     placeholder="Country",
            # )

class WidgetsScreen(PageScreen):
    """The Widgets screen"""

    CSS = """
    WidgetsScreen { 
        align-horizontal: center;
        Markdown { background: transparent; }
        & > VerticalScroll {
            scrollbar-gutter: stable;
            & > * {                          
                &:even { background: $boost; }
                padding-bottom: 1;
            }
        }
    }
    """

    BINDINGS = [Binding("escape", "blur", "Unfocus any focused widget", show=False)]
    
    def compose(self) -> ComposeResult:
        with lazy.Reveal(containers.VerticalScroll(can_focus=True)):
            loquesea = ["name","id","email","tel","dir"]
            yield Markdown(WIDGETS_MD, classes="column")
            # yield Buttons()
            # yield Checkboxes()
            # yield Datatables()
            objet = Inputs("hola",loquesea)
            yield objet
            # yield ListViews()
            # yield Logs()
            # yield Markdowns()
            # yield Selects()
            # yield Sparklines()
            # yield Switches()
            # yield TabsDemo()
            # yield TextAreas()
            # yield Trees()
            # yield YourWidgets()
        # yield Footer()


if __name__ == "__main__":
    from textual.app import App

    class cv_inputs(App):
        def get_default_screen(self) -> Screen: # type: ignore
            return WidgetsScreen()
        # def run_input_data():
        #     return INPUT_DATA

    # data = cv_inputs.run_input_data()
    # print(data)
    app = cv_inputs()
    app.run()

