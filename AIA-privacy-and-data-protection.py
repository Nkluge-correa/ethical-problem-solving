import glob
import yaml
import random
import pandas as pd
import abstra.forms as af
import plotly.graph_objects as go
from plotly.subplots import make_subplots

# Get a list of all the file paths that ends with .yaml from in specified directory
# These are the questions that will be used in the survey
fileList = glob.glob('./AIA/privacy-and-data-protection/**.yaml')

# Sort the list of filepaths by number
fileList.sort(key=lambda x: int(x.split('question')[-1].split('.')[0]))

# Initialize a pandas.DataFrame
df = pd.DataFrame(
  columns=['question', 'multiple', 'options', 'scores', 'privacy', 'transparency', 'accountability', 'information']
  )

# Iterate over the list of filepaths
for filePath in fileList:

    with open(filePath) as file:
        # Read the current yaml file
        documents = yaml.full_load(file)
        
        # Concatenate the current yaml file to the DataFrame
        df = pd.concat([df, pd.DataFrame.from_dict(documents, orient='index').T], ignore_index=True)

# Create a new column with the maximum impact increase and decrease
# These values represent the maximum impact that the application can have on society,
# together with the maximal decrease in impact that the application can receive
df["max_impact_increase"] = df.scores.apply(lambda x: sum(num for num in x if num > 0))
df["max_impact_decrease"] = df.scores.apply(lambda x: sum(num for num in x if num < 0))

# We filter the `max_impact_increase` and `max_impact_decrease` to get only the 
# correct scores, in relation to the `multiple` column
mask = df['multiple'] == False
df.loc[mask, 'max_impact_increase'] = df[mask]['scores'].apply(max)
df.loc[mask, 'max_impact_decrease'] = df[mask]['scores'].apply(min)

# We initialize the scores for each principle as an empty list
score_privacy = 0
score_transparency = 0
score_accountability = 0

# We initialize the maximum scores for each principle
max_privacy = df[df['privacy'] == True].max_impact_increase.sum()
max_transparency = df[df['transparency'] == True].max_impact_increase.sum()
max_accountability = df[df['accountability'] == True].max_impact_increase.sum()

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
<h1>Algorithmic Impact Assessment</h1>

<h2><em>Privacy & Data Protection</em></h2>

<p>This <strong>Algorithmic Impact Assessment (AIA)</strong> is a tool that seeks to assess the impact \
  that the application could have on society concerning Privacy and the protection of personal data, \
    using the ethical principles of <em>Privacy</em>, <em>Transparency</em>, and <em>Accountability</em> \
      as points of reference.</p>

<ul>
  <li><strong>Privacy:</strong> "<em>Privacy can be defined as the individual's right to expose oneself \
    voluntarily, and to the extent desired, to the world. This principle also relates to data-protection \
      concepts such as data minimization, anonymity, informed consent, etc</em>."</li><br>

  <li><strong>Transparency:</strong> "<em>This principle supports the idea that the use and development of \
    AI technologies should be transparent for all interested stakeholders. Transparency can be related to \
      'the transparency of an organization' or 'the transparency of an algorithm.' Transparency is also \
        related to the idea that such information should be understandable to nonexperts and, when necessary, \
          subject to auditing</em>."</li><br>

  <li><strong>Accountability:</strong> "<em>Accountability refers to the idea that AI technology developers and \
    deployers should comply with regulatory bodies. These actors should also be accountable for their actions and \
      the impacts caused by their technologies</em>."</li><br>
</ul>

<p>To access more definitions, visit <a href="https://nkluge-correa.github.io/worldwide_AI-ethics/" \
  target="_blank">Worldwide AI Ethics</a>.</p>"""
).run("Next")
)

# Loop through the questions and render the pages
pages = [
    af.Page()
    .display_html(
    f"""
    <style>
      h2 {"{text-align: center;}"}
    </style>
    <h2>{df.question[i]}</h2>""")
    .read_cards(
    label=f"",
    options=[{"description": x} for x in df.options[i]],
    multiple=True if df.multiple[i] else False,
    required=True,
    initial_value=random.choice([{"description": x} for x in df.options[i]]),
    hint=df.information[i] if df.information[i] else None,
)
.display_progress(i+1, len(df), text=F"")
.run("Next")
for i in range(len(df))
]

# Loop through the pages and calculate the scores
for i, page in enumerate(pages):

      # Get the row from the DataFrame that matches the question
      temp_df = df[df['question'] == df.question[i]]

      # Create a hash map from the options and scores
      hash_map = dict(zip(temp_df.options.iloc[0], temp_df.scores.iloc[0]))

      try:
        # For questions that are not multiple choice, we don't need to iterate
        # over the list, since it only contains one dictionary
        
        if temp_df.privacy.iloc[0]:
            score_privacy += hash_map[page['']['description']]
        
        if temp_df.transparency.iloc[0]:
            score_transparency += hash_map[page['']['description']]
        
        if temp_df.accountability.iloc[0]:
            score_accountability += hash_map[page['']['description']]
      
      except:
        # For a list, we iterate ovver every dictionary in the list and
        # associate the score to the description, adding it to the total score

        for d in page['']:
            
            if temp_df.privacy.iloc[0]:
                score_privacy += hash_map[d['description']]
            
            if temp_df.transparency.iloc[0]:
                score_transparency += hash_map[d['description']]
            
            if temp_df.accountability.iloc[0]:
                score_accountability += hash_map[d['description']]   

# We make sure that the scores are not negative
score_privacy = score_privacy if score_privacy > 0 else 0
score_transparency = score_transparency if score_transparency > 0 else 0
score_accountability = score_accountability if score_accountability > 0 else 0

# We create the indicator plots for each principle

fig = make_subplots(
    rows=1, cols=3,
    specs=[[{"type": "indicator"}, {"type": "indicator"},  {"type": "indicator"}]],
    subplot_titles=("<b>Impact on Privacy</b>","<b>Impact on Transparency</b>", "<b>Impact on Accountability</b>"),
    horizontal_spacing = 0.10,
)

fig.add_trace(go.Indicator(
    mode = "gauge+number",
    value = (score_privacy/max_privacy) * 100,
    domain = {'x': [0, 1], 'y': [0, 1]},
    gauge = {
        'axis': {'range': [None, 100], 'tickwidth': 1, 'tickcolor': "black"},
        'bar': {'color': "slategray"},
        'bgcolor': "white",
        'borderwidth': 2,
        'bordercolor': "gray",
        'steps': [
            {'range': [0, 30], 'color': 'yellowgreen'},
            {'range': [30, 70], 'color': 'yellow'},
            {'range': [70, 100], 'color': 'tomato'}],
        'threshold': {
            'line': {'color': "black", 'width': 4},
            'thickness': 0.75,
            'value': (score_privacy/max_privacy) * 100}}),
              row=1, col=1)

fig.add_trace(go.Indicator(
    mode = "gauge+number",
    value = (score_transparency/max_transparency) * 100,
    domain = {'x': [0, 1], 'y': [0, 1]},
    gauge = {
        'axis': {'range': [None, 100], 'tickwidth': 1, 'tickcolor': "black"},
        'bar': {'color': "slategray"},
        'bgcolor': "white",
        'borderwidth': 2,
        'bordercolor': "gray",
        'steps': [
            {'range': [0, 30], 'color': 'yellowgreen'},
            {'range': [30, 70], 'color': 'yellow'},
            {'range': [70, 100], 'color': 'tomato'}],
        'threshold': {
            'line': {'color': "black", 'width': 4},
            'thickness': 0.75,
            'value': (score_transparency/max_transparency) * 100}}),
              row=1, col=2)

fig.add_trace(go.Indicator(
    mode = "gauge+number",
    value = (score_accountability/max_accountability) * 100,
    domain = {'x': [0, 1], 'y': [0, 1]},
    gauge = {
        'axis': {'range': [None, 100], 'tickwidth': 1, 'tickcolor': "black"},
        'bar': {'color': "slategray"},
        'bgcolor': "white",
        'borderwidth': 2,
        'bordercolor': "gray",
        'steps': [
            {'range': [0, 30], 'color': 'yellowgreen'},
            {'range': [30, 70], 'color': 'yellow'},
            {'range': [70, 100], 'color': 'tomato'}],
        'threshold': {
            'line': {'color': "black", 'width': 4},
            'thickness': 0.75,
            'value': (score_accountability/max_accountability) * 100}}),
              row=1, col=3)

fig.update_layout(
  paper_bgcolor='rgba(0,0,0,0)',
  plot_bgcolor='rgba(0,0,0,0)',
  template='plotly_white', 
  font = {'color': "black", 'family': "Arial"})

fig_total = go.Figure(go.Indicator(
    mode = "gauge+number",
    value = (((score_privacy/max_privacy) + 
    (score_transparency/max_transparency) + 
    (score_accountability/max_accountability))/ 3) * 100,
    domain = {'x': [0, 1], 'y': [0, 1]},
    gauge = {
        'axis': {'range': [None, 100], 'tickwidth': 1, 'tickcolor': "black"},
        'bar': {'color': "slategray"},
        'bgcolor': "white",
        'borderwidth': 2,
        'bordercolor': "gray",
        'steps': [
            {'range': [0, 30], 'color': 'yellowgreen'},
            {'range': [30, 70], 'color': 'yellow'},
            {'range': [70, 100], 'color': 'tomato'}],
        'threshold': {
            'line': {'color': "black", 'width': 4},
            'thickness': 0.75,
            'value': (((score_privacy/max_privacy) + 
            (score_transparency/max_transparency) + 
            (score_accountability/max_accountability))/ 3) * 100}}))

fig_total.update_layout(
  paper_bgcolor='rgba(0,0,0,0)',
  plot_bgcolor='rgba(0,0,0,0)',
  template='plotly_white',
  title=dict(text='<b>Total Impact Score (Privacy & Data Protection)</b>', x=0.5, y=0.9, font={'size': 24}), 
  font = {'color': "black", 'family': "Arial"})

# Render the results page ...
result = (
  af.Page()
    .display_html(
        f"""
<style>
  h1, h2, p {"{text-align: center;}"}
</style>

<h1>Algorithmic Impact Assessment</h1>

<h2><em>Results</em></h2>

<hr>

<p>This report contains the risk assessment carried out by our tool. Our assessment consists of a set of risk indicators \
  relating to the three principles assessed in the survey: <strong>Privacy</strong>, <strong>Transparency</strong>, \
    and <strong>Accountability</strong>.</p>

<p>The result below is an estimate of the relative risk of your application (Scores range from 0 to 100).</p>"""
)
.display_plotly(fig, full_width=True)
.display_plotly(fig_total, full_width=False)
.run("Finish")
)