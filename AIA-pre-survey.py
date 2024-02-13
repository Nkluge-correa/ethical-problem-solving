import abstra.forms as af

# Render Intro page
intro = (
  af.Page()
    .display_html(
        """
<style>
  h1, h2 {
    text-align: center;
  }
  p {
    text-align: justify;
  }
</style>
<h1>Pre-Algorithmic Impact Assessment survey</h1>

<p>This preliminary survey aims to indicate which <strong>Algorithmic Impact Assessments \
  (AIAs)</strong> the user/organization should conduct. The AIAs currently available are:</p>

<ul>
  <li><strong>AIA - Privacy and Data Protection.</strong><br><br>
  <li><strong>AIA - Consumer Rights.</strong><br><br>
  <li><strong>AIA - Protection of Children and Adolescents.</strong><br><br>
  <li><strong>AIA - Antidiscrimination and Truthfulness.</strong><br><br>
</ul>

<p>These AIAs are based on the principles of <em>Privacy</em>, <em>Transparency</em>, \
  <em>Responsibility</em>, <em>Autonomy</em>, <em>Beneficence</em>, <em>Reliability</em>, and \
    <em>Equity</em>, in addition to the legislation in force in Brazil. \
      To learn more about ethical principles, visit \
        <a href="https://www.airespucrs.org/worldwide-ai-ethics" target="_blank">Worldwide AI Ethics</a>.</p>"""
).run("Start Pre-AIA survey")
)

q1 = [
    af.Page()
    .display_html(
    """
    <style>
      h2 {text-align: center;}
    </style>
    <h2>Does the application process personal data or creates a behavioral profile from its users?</h2>""")
    .read_cards(
    label=f"",
    options=[{"description": "Yes"} , {"description": "No"}],
    multiple=False,
    required=True,
    initial_value=None,
    hint="Personal data refers to any information that can be used to identify an individual. \
      A behavioral profile, on the other hand, is a collection of data that describes an individual's \
        actions, preferences, and habits."
)
.display_progress(1, 4, text=F"3 questions remaining ...")
.run("Next")
]

q2 = [
    af.Page()
    .display_html(
    """
    <style>
      h2 {text-align: center;}
    </style>
    <h2>Is the intended use of the application the consumption of products or services?</h2>""")
    .read_cards(
    label=f"",
    options=[{"description": "Yes"} , {"description": "No"}],
    multiple=False,
    required=True,
    initial_value=None,
    hint="Products are tangible, physical items that are manufactured, produced, or assembled and \
      can be bought and sold. Services, in contrast, are intangible offerings that involve performing \
        specific tasks or providing assistance to meet the needs or desires of customers."
)
.display_progress(2, 4, text=F"2 questions remaining ...")
.run("Next")
]

q3 = [
    af.Page()
    .display_html(
    """
    <style>
      h2 {text-align: center;}
    </style>
    <h2>Is your application intended to be used by children or adolescents (i.e., individuals under 18)?</h2>""")
    .read_cards(
    label=f"",
    options=[{"description": "Yes"} , {"description": "No"}],
    multiple=False,
    required=True,
    initial_value=None,
    hint="Any individual under the age of 18 is considered a child or adolescent. The Brazilian Child \
      and Adolescent Statute (ECA) defines a child as an individual under the age of 12 and an adolescent \
        as an individual between the ages of 12 and 18."
)
.display_progress(3, 4, text=F"1 questions remaining ...")
.run("Next")
]

q4 = [
    af.Page()
    .display_html(
    """
    <style>
      h2 {text-align: center;}
    </style>
    <h2>Can your app be used in a way that (1) could produce toxic/discriminatory content, (2) \
      could make decisions that unequally benefit or disadvantage individuals based on sensitive \
        attributes (e.g., race, gender, etc.), or (3) could generate false/untrue content?</h2>""")
    .read_cards(
    label=f"",
    options=[{"description": "Yes"} , {"description": "No"}],
    multiple=False,
    required=True,
    initial_value=None,
    hint="Toxic content refers to content that is harmful, offensive, or abusive. False information \
      refers to inaccurate or deliberately misleading content."
)
.display_progress(4, 4, text=F"Last question!")
.run("Next")
]

result = "<ul>"

if q1[0]['']['description'] == "Yes":
  result += "<li><strong>AIA - Privacy and Data Protection.</strong><br>"

if q2[0]['']['description'] == "Yes":
  result += "<li><strong>AIA - Consumer Rights.</strong><br>"

if q3[0]['']['description'] == "Yes":
  result += "<li><strong>AIA - Protection of Children and Adolescents.</strong><br>"

if q4[0]['']['description'] == "Yes":
  result += "<li><strong>AIA - Antidiscrimination and Truthfulness.</strong><br>"

result += "</ul><br><p><strong>After completing the above mentioned AIAs, please proceed to the Ethical Troubleshoot survey.</strong></p>" if result != "<ul>" else "<p><strong>No AIA required. Please, procced to the Ethical Troubleshoot survey.</strong></p>"

# Render the results page ...
result = (
  af.Page()
    .display_html(
        f"""
<style>
  h1, h2, p {"{text-align: center;}"}
</style>

<h1>Pre-Algorithmic Impact Assessment survey</h1>

<h2><em>Results</em></h2>

<hr>

<p>Based on your answers, the following AIAs are recommended:</p><br>

{result}

"""
)
.run("Finish")
)