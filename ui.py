import gradio as gr


class UI:
    def __init__(self, brochure_generator):
        self.brochure_generator = brochure_generator
        self.interface = self._create_interface()

    def _create_interface(self):
        return gr.Interface(
            fn=self.brochure_generator.stream_brochure,
            inputs=[
                gr.Textbox(label="Company name:"),
                gr.Textbox(label="Landing page URL including http:// or https://"),
                gr.Dropdown(["GPT", "Claude"], label="Select model"),
            ],
            outputs=[gr.Markdown(label="Brochure:")],
            flagging_mode="never",
        )

    def launch(self, **kwargs):
        self.interface.launch(**kwargs)
