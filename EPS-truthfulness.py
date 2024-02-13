import abstra.forms as af

# Open the glossary file. It contains the definitions of the terms used in the survey
with open("./EPS/truthfulness/WHY.html", "r") as file:
    html_content = file.read()

# Render WHY page
why_page = (
  af.Page()
    .display_html(
        f"""
<style>
h1, h2 {"{text-align: center;}"}
p {"{text-align: justify;}"}
</style>
{html_content}"""
)
.display_html(
"""
<style>
h2 {"{text-align: center;}"}
</style>
<h2>Select the desired impact level for the application being assessed.</h2>
""")
.read_cards(
    label=f"",
    options=[{"title": "LOW", "image": "./img/low.png", 
    "description": "Low Impact: the application does not require great levels of algorithmic truthfulness."}, 
             {"title": "INTERMEDIATE", "image": "./img/medium.png", 
             "description": "Intermediate Impact: the application requires some level of algorithmic truthfulness."}, 
             {"title": "HIGH", "image": "./img/high.png", 
             "description": "High Impact: the application requires a high level of algorithmic truthfulness."}],
    multiple=False,
    required=True,
)
.run("Lern how to deal with algorithmic truthfulness")
)

# Open the source for the SHOULD-HOW page
with open(f"""./EPS/truthfulness/SHOULD-HOW-{why_page['']['title']}.html""", "r") as file:
    html_content = file.read()

# Render SHOULD-HOW page
should_how_page = (
  af.Page()
    .display_html(
        f"""
<style>
h1, h2, {"{text-align: center;}"}
p {"{text-align: justify;}"}
</style>
{html_content}"""
)
.run("Finish")
)
