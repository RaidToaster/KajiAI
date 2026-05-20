"""Gradio interface — web UI for claim analysis."""


import gradio as gr
from kaji.flow import KajiFlow


def analyse(claim: str, domain: str) -> str:
    result = KajiFlow().kickoff(inputs={"claim": claim, "domain": domain})
    return result.raw if hasattr(result, "raw") else str(result)


def create_ui() -> gr.Blocks:
    with gr.Blocks(title="KajiSF-DJ") as ui:
        gr.Markdown("# KajiSF-DJ — Claim Analysis Tool")
        claim = gr.Textbox(label="Claim", placeholder="Enter a claim to analyse...")
        domain = gr.Dropdown(
            choices=["general", "scientific", "political", "health_medical"],
            value="general",
            label="Domain",
        )
        output = gr.Markdown()
        btn = gr.Button("Analyse")
        btn.click(fn=analyse, inputs=[claim, domain], outputs=output)
    return ui


def main() -> None:
    create_ui().launch()
