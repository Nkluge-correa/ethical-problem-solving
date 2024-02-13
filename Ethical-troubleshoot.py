import abstra.forms as af
import pandas as pd

intro = (
    af.Page()
    .display_html("""
<style>
  h1 {
    text-align: center;
    }
  p {
    text-align: justify;
    }
</style>

<h1>Ethical Troubleshoot</h1>

<p>The Ethical Troubleshoot aims to evaluate the ethical impact of AI applications further, especially \
  regarding points that fall outside the scope of our Algorithmic Impact Assessment surveys. \
    From the results of the combined surveys (Algorithmic Impact Assessments + Ethical Troubleshoot), \
      evaluators can use our impact matrix, differentiated into three levels (<b>Low</b>, <b>Intermediate</b>, \
        and <b>High</b>), to frame an AI application.</p>

<p>The EPS survey uses an evaluation matrix to assess impacts associated with an AI application, \
  considering six core ethical principles: <b>Transparency</b>, <b>Fairness</b>, <b>Privacy</b>, <b>Sustainability</b>, \
    <b>Reliability</b>, and <b>Truthfulness</b>. Each one of these principles has a different set of \
      recommendations and How-to instructions.</p>
""")
.run("Start the survey")
)

answers = []

q1 = [
    af.Page()
    .display_html(
    """
    <style>
      h2 {text-align: center;}
    </style>
    <h2>What is the current state of your application?</h2>""")
    .read_cards(
    label=f"",
    options=[{"description": "Development"} , {"description": "Testing/Beta"}, {"description": "Production"}],
    multiple=False,
    required=True,
    initial_value=None,
    hint="The development phase is when the application is being built. The testing/beta phase is when the \
      application is being tested by a small group of users. The production phase is when the application \
        is available to the general public."
)
.display_progress(1, 25, text=F"24 questions remaining ...")
.run("Next")
]

answers.append(("What is the current state of your application?", q1[0]['']['description']))

q2 = [
    af.Page()
    .display_html(
    """
    <style>
      h2 {text-align: center;}
    </style>
    <h2>Was this application created to generate revenue?</h2>""")
    .read_cards(
    label=f"",
    options=[{"description": "For-profit"} , {"description": "Non-profift"}],
    multiple=False,
    required=True,
    initial_value=None,
    hint=None,
)
.display_progress(2, 25, text=F"23 questions remaining ...")
.run("Next")
]

answers.append(("Was this application created to generate revenue?", q2[0]['']['description']))

q3 = [
    af.Page()
    .display_html(
    """
    <style>
      h2 {text-align: center;}
    </style>
    <h2>What is the target audience for this application?</h2>""")
    .read_checklist(
    label=f"",
    options=[
      {"label": "Internal (aimed at the organization's internal public)",
      "value": "Internal (aimed at the organization's internal public)"},
      {"label": "External (intended for the general public)",
      "value": "External (intended for the general public)"}],
    required=True,
    min=1,
    hint=None
)
.display_progress(3, 25, text=F"22 questions remaining ...")
.run("Next")
]

answers.append(("What is the target audience for this application?", q3[0]['']))

q4 = [
    af.Page()
    .display_html(
    """
    <style>
      h2 {text-align: center;}
    </style>
    <h2>What is the estimated age range for the target audience?</h2>""")
    .read_checklist(
    label=f"",
    options=[
      {"label": "Children under 12 years old", "value": "Children under 12 years old"},
      {"label": "Adolescents between 12 and 18 years old", "value": "Adolescents between 12 and 18 years old"},
      {"label": "Adults over 18 and under 59 years old", "value": "Adults over 18 and under 59 years old"},
      {"label": "Elderly over 60 years old", "value": "Elderly over 60 years old"},
      {"label": "Not specified", "value": "Not specified"}],
    required=True,
    min=1,
    hint="According to the Brazilian Child and Adolescent Statute (ECA), a child is an individual under \
      the age of 12 and an adolescent is an individual between the ages of 12 and 18."
)
.display_progress(4, 25, text=F"21 questions remaining ...")
.run("Next")
]

answers.append(("What is the estimated age range for the target audience?", q4[0]['']))

q5 = [
    af.Page()
    .display_html(
    """
    <style>
      h2 {text-align: center;}
    </style>
    <h2>What is the geographical scope of the target audience?</h2>""")
    .read_checklist(
    label=f"",
    options=[
      {"label": "Local", "value": "Local"}, 
      {"label": "Regional", "value": "Regional"}, 
      {"label": "National", "value": "National"}, 
      {"label": "International", "value": "International"},
      {"label": "Not specified", "value": "Not specified"}],
    required=True,
    min=1,
    hint=None
)
.display_progress(5, 25, text=F"20 questions remaining ...")
.run("Next")
]

answers.append(("What is the geographical scope of the target audience?", q5[0]['']))

q6 = [
    af.Page()
    .display_html(
    """
    <style>
      h2 {text-align: center;}
    </style>
    <h2>What is the estimated audience size?</h2>""")
    .read_cards(
    label=f"",
    options=[{"description": "Up to 2,500 direct and indirect users"} , 
    {"description": "From 2,501 to 8,000 direct and indirect users"}, 
    {"description": "From 8,001 to 20,000 direct and indirect users"}, 
    {"description": "From 20,001 to 500,000 direct and indirect users"}, 
    {"description": "More than 500 thousand direct and indirect users"}],
    multiple=False,
    required=True,
    initial_value=None,
    hint=None
)
.display_progress(6, 25, text=F"19 questions remaining ...")
.run("Next")
]

answers.append(("What is the estimated audience size?", q6[0]['']['description']))

q7 = [
    af.Page()
    .display_html(
    """
    <style>
      h2 {text-align: center;}
    </style>
    <h2>What is the purpose of this application?</h2>""")
    .read_textarea(
      label=f"",
      required=True,
      placeholder="My application's purpose is to ...",
      initial_value="",
    )
.display_progress(7, 25, text=F"18 questions remaining ...")
.run("Next")
]

answers.append(("What is the purpose of this application?", q7[0]['']))

q8 = [
    af.Page()
    .display_html(
    """
    <style>
      h2 {text-align: center;}
    </style>
    <h2>Check any intended primary uses of the application:</h2>""")
    .read_checklist(
    label="",
    options=[
    {"label": "Automation of Industrial Process", "value": "Automation of Industrial Process"},
    {"label": "Chatbot", "value": "Chatbot"},
    {"label": "Communication", "value": "Communication"},
    {"label": "Court lawsuits", "value": "Court lawsuits"},
    {"label": "Cultural Development", "value": "Cultural Development"},
    {"label": "Customer Service", "value": "Customer Service"},
    {"label": "Cybersecurity", "value": "Cybersecurity"},
    {"label": "Data protection", "value": "Data protection"},
    {"label": "Ecological Development", "value": "Ecological Development"},
    {"label": "Face Recognition", "value": "Face Recognition"},
    {"label": "Financial Investing", "value": "Financial Investing"},
    {"label": "Financial or Tax Operations", "value": "Financial or Tax Operations"},
    {"label": "Forecasting", "value": "Forecasting"},
    {"label": "General Automation", "value": "General Automation"},
    {"label": "Granting of Financial Benefits", "value": "Granting of Financial Benefits"},
    {"label": "Granting of Social Benefits", "value": "Granting of Social Benefits"},
    {"label": "Health Insurance", "value": "Health Insurance"},
    {"label": "Health/Medical Applications", "value": "Health/Medical Applications"},
    {"label": "Health system", "value": "Health system"},
    {"label": "Hiring/Human Relations", "value": "Hiring/Human Relations"},
    {"label": "Image/Video Generation or Enhancement", "value": "Image/Video Generation or Enhancement"},
    {"label": "Information/Journalism", "value": "Information/Journalism"},
    {"label": "Insurance", "value": "Insurance"},
    {"label": "Learning/Teaching", "value": "Learning/Teaching"},
    {"label": "Legislative processes", "value": "Legislative processes"},
    {"label": "Marketing", "value": "Marketing"},
    {"label": "Medical Diagnoses", "value": "Medical Diagnoses"},
    {"label": "Navigation/Location", "value": "Navigation/Location"},
    {"label": "Nuclear Energy", "value": "Nuclear Energy"},
    {"label": "Others", "value": "Others"},
    {"label": "Policing", "value": "Policing"},
    {"label": "Public Contracts", "value": "Public Contracts"},
    {"label": "Recommendation System", "value": "Recommendation System"},
    {"label": "Renewable Energy", "value": "Renewable Energy"},
    {"label": "Retirement and Pensions", "value": "Retirement and Pensions"},
    {"label": "Robotics", "value": "Robotics"},
    {"label": "Scientific/Academic Improvement", "value": "Scientific/Academic Improvement"},
    {"label": "Security (external)", "value": "Security (external)"},
    {"label": "Security (internal)", "value": "Security (internal)"},
    {"label": "Social Media", "value": "Social Media"},
    {"label": "Sports Analytics", "value": "Sports Analytics"},
    {"label": "State Defense", "value": "State Defense"},
    {"label": "Surveillance", "value": "Surveillance"},
    {"label": "Telemedicine", "value": "Telemedicine"},
    {"label": "Text Classification", "value": "Text Classification"},
    {"label": "Text Generation or Enhancement", "value": "Text Generation or Enhancement"},
    {"label": "Text-to-voice Applications", "value": "Text-to-voice Applications"},
    {"label": "Translations", "value": "Translations"},
    {"label": "Voice-to-text Applications", "value": "Voice-to-text Applications"},
    {"label": "Weather forecast", "value": "Weather forecast"},],
    required=True,
    min=1,
    hint="Primary uses are the main purposes of the application. Check all that apply."
    )
.display_progress(8, 25, text=F"17 questions remaining ...")
.run("Next")
]

answers.append(("Check any intended primary uses of the application:", q8[0]['']))

q9 = [
    af.Page()
    .display_html(
    """
    <style>
      h2 {text-align: center;}
    </style>
    <h2>Check any potential out-of-scope uses of the application:</h2>""")
    .read_checklist(
    label="",
    options=[
    {"label": "Automation of Industrial Process", "value": "Automation of Industrial Process"},
    {"label": "Chatbot", "value": "Chatbot"},
    {"label": "Communication", "value": "Communication"},
    {"label": "Court lawsuits", "value": "Court lawsuits"},
    {"label": "Cultural Development", "value": "Cultural Development"},
    {"label": "Customer Service", "value": "Customer Service"},
    {"label": "Cybersecurity", "value": "Cybersecurity"},
    {"label": "Data protection", "value": "Data protection"},
    {"label": "Ecological Development", "value": "Ecological Development"},
    {"label": "Face Recognition", "value": "Face Recognition"},
    {"label": "Financial Investing", "value": "Financial Investing"},
    {"label": "Financial or Tax Operations", "value": "Financial or Tax Operations"},
    {"label": "Forecasting", "value": "Forecasting"},
    {"label": "General Automation", "value": "General Automation"},
    {"label": "Granting of Financial Benefits", "value": "Granting of Financial Benefits"},
    {"label": "Granting of Social Benefits", "value": "Granting of Social Benefits"},
    {"label": "Health Insurance", "value": "Health Insurance"},
    {"label": "Health/Medical Applications", "value": "Health/Medical Applications"},
    {"label": "Health system", "value": "Health system"},
    {"label": "Hiring/Human Relations", "value": "Hiring/Human Relations"},
    {"label": "Image/Video Generation or Enhancement", "value": "Image/Video Generation or Enhancement"},
    {"label": "Information/Journalism", "value": "Information/Journalism"},
    {"label": "Insurance", "value": "Insurance"},
    {"label": "Learning/Teaching", "value": "Learning/Teaching"},
    {"label": "Legislative processes", "value": "Legislative processes"},
    {"label": "Marketing", "value": "Marketing"},
    {"label": "Medical Diagnoses", "value": "Medical Diagnoses"},
    {"label": "Navigation/Location", "value": "Navigation/Location"},
    {"label": "Nuclear Energy", "value": "Nuclear Energy"},
    {"label": "Others", "value": "Others"},
    {"label": "Policing", "value": "Policing"},
    {"label": "Public Contracts", "value": "Public Contracts"},
    {"label": "Recommendation System", "value": "Recommendation System"},
    {"label": "Renewable Energy", "value": "Renewable Energy"},
    {"label": "Retirement and Pensions", "value": "Retirement and Pensions"},
    {"label": "Robotics", "value": "Robotics"},
    {"label": "Scientific/Academic Improvement", "value": "Scientific/Academic Improvement"},
    {"label": "Security (external)", "value": "Security (external)"},
    {"label": "Security (internal)", "value": "Security (internal)"},
    {"label": "Social Media", "value": "Social Media"},
    {"label": "Sports Analytics", "value": "Sports Analytics"},
    {"label": "State Defense", "value": "State Defense"},
    {"label": "Surveillance", "value": "Surveillance"},
    {"label": "Telemedicine", "value": "Telemedicine"},
    {"label": "Text Classification", "value": "Text Classification"},
    {"label": "Text Generation or Enhancement", "value": "Text Generation or Enhancement"},
    {"label": "Text-to-voice Applications", "value": "Text-to-voice Applications"},
    {"label": "Translations", "value": "Translations"},
    {"label": "Voice-to-text Applications", "value": "Voice-to-text Applications"},
    {"label": "Weather forecast", "value": "Weather forecast"},],
    required=True,
    min=1,
    hint="Out-of-scope uses are the potential uses of the application that were not initially planned. \
      Check all that apply."
    )
.display_progress(9, 25, text=F"16 questions remaining ...")
.run("Next")
]

answers.append(("Check any potential out-of-scope uses of the application:", q9[0]['']))

q10 = [
    af.Page()
    .display_html(
    """
    <style>
      h2 {text-align: center;}
    </style>
    <h2>Describe the intended use of your application:</h2>""")
    .read_textarea(
      label=f"",
      required=True,
      placeholder="The intended use of my application is to ...",
      initial_value="",
    )
.display_progress(10, 25, text=F"15 questions remaining ...")
.run("Next")
]

answers.append(("Describe the intended use of your application:", q10[0]['']))

q11 = [
    af.Page()
    .display_html(
    """
    <style>
      h2 {text-align: center;}
    </style>
    <h2>Please describe any potential out-of-scope uses of your application:</h2>""")
    .read_textarea(
      label=f"",
      required=True,
      placeholder="The potential out-of-scope uses of my application are ...",
      initial_value="",
    )
.display_progress(11, 25, text=F"14 questions remaining ...") 
.run("Next")
]

answers.append(("Please describe any potential out-of-scope uses of your application:", q11[0]['']))

q12 = [
    af.Page()
    .display_html(
    """
    <style>
      h2 {text-align: center;}
    </style>
    <h2>If your application uses user-sourced data, please explain how data was handled and whether \
      it was collected consensually.</h2>""")
    .read_textarea(
      label=f"",
      required=True,
      placeholder="My application uses user-sourced data in the following way ...",
      hint=None,
      initial_value="",
    )
.display_progress(12, 25, text=F"13 questions remaining ...") 
.run("Next")
]

answers.append(("If your application uses user-sourced data, please explain how data was handled and whether \
  it was collected consensually.", q12[0]['']))

q13 = [
    af.Page()
    .display_html(
    """
    <style>
      h2 {text-align: center;}
    </style>
    <h2>If your application uses sensitive or personal data, please describe situations that such information could \
      affect the functionality of the application or the measures taken to prevent such happenings.</h2>""")
    .read_textarea(
      label=f"",
      required=True,
      initial_value="",
      placeholder="My application uses sensitive/personal data in the following way ...",
      hint="Sensitive data is any data that can be deemed sensitive, such as health data, financial data, \
        biometric data, etc. Personal data is any data that can be used to identify an individual, \
          such as name, address, phone number, etc.",
    )
.display_progress(13, 25, text=F"12 questions remaining ...") 
.run("Next")
]

answers.append(("If your application uses sensitive/personal data, please describe situations that such data\
   could affect the functionality of the application or the measures taken to prevent such happenings.", q13[0]['']))

q14 = [
    af.Page()
    .display_html(
    """
    <style>
      h2 {text-align: center;}
    </style>
    <h2>Specify whether user needs or feedback were considered during application development.</h2>""")
    .read_textarea(
      label=f"",
      required=True,
      initial_value="",
      placeholder="User needs/feedback were considered during application development ...",
      hint=None
    )
.display_progress(14, 25, text=F"11 questions remaining ...") 
.run("Next")
]

answers.append(("Specify whether user needs/feedback were considered during application development.", q14[0]['']))

q15 = [
    af.Page()
    .display_html(
    """
    <style>
      h2 {text-align: center;}
    </style>
    <h2>If there are any warnings that should be alerted to the user (for example, possible failures in the \
      application's performance), specify how such information will be brought to the user's attention.</h2>""")
    .read_textarea(
      label=f"",
      required=True,
      initial_value="",
      placeholder="The warnings that should be alerted to the user are ...",
      hint="Warnings are any information that the user should be aware of in order to use the application."
    )
.display_progress(15, 25, text=F"10 questions remaining ...") 
.run("Next")
]

answers.append(("If there are any warnings that should be alerted to the user (for example, possible failures \
  in the application's performance), specify how such information will be brought to the user's attention.", q15[0]['']))

q16 = [
    af.Page()
    .display_html(
    """
    <style>
      h2 {text-align: center;}
    </style>
    <h2>Specify the techniques for value-sensitive design (human-centered approach) that were used in \
      developing this application.</h2>""")
    .read_textarea(
      label=f"",
      required=True,
      initial_value="",
      placeholder="We used the following techniques for value-sensitive design ...",
      hint="Value-sensitive design is a human-centered approach to the design of technology. It aims to \
        ensure that the values of the users are taken into account during the design process."
    )
.display_progress(16, 25, text=F"9 questions remaining ...") 
.run("Next")
]

answers.append(("Specify the techniques for value-sensitive design (human-centered approach) that were used \
  in developing this application.", q16[0]['']))

q17 = [
    af.Page()
    .display_html(
    """
    <style>
      h2 {text-align: center;}
    </style>
    <h2>If the application has variable performance tied to sensitive attributes \
      (sex, gender, race, ethnicity, etc.), elaborate on how such variation occurs.</h2>""")
    .read_textarea(
      label=f"",
      required=True,
      initial_value="",
      placeholder="The application has variable performance tied to sensitive attributes in the following way ...",
      hint=None,
    )
.display_progress(17, 25, text=F"8 questions remaining ...") 
.run("Next")
]

answers.append(("If the application has variable performance tied to sensitive attributes \
  (sex, gender, race, ethnicity, etc.), elaborate on how such variation occurs.</h2>""" , q17[0]['']))

q18 = [
    af.Page()
    .display_html(
    """
    <style>
      h2 {text-align: center;}
    </style>
    <h2>Elaborate on the possibilities of misuse of the application.</h2>""")
    .read_textarea(
      label=f"",
      required=True,
      initial_value="",
      placeholder="The possibilities of misuse of the application are ...",
      hint="Misuse is any use of the application that is not intended by the developers."
    )
.display_progress(18, 25, text=F"7 questions remaining ...") 
.run("Next")
]

answers.append(("Elaborate on the possibilities of misuse of the application.", q18[0]['']))

q19 = [
    af.Page()
    .display_html(
    """
    <style>
      h2 {text-align: center;}
    </style>
    <h2>Does your application use other applications (for example, APIs) that were not produced \
      by your organization?</h2>""")
    .read_cards(
    label=f"",
    options=[{"description": "Yes"} , {"description": "No"}],
    multiple=False,
    required=True,
    initial_value=None,
    hint=None
)
.display_progress(19, 25, text=F"6 questions remaining ...") 
.run("Next")
]

answers.append(("Does your application use other applications (for example, APIs) that were not produced \
  by your organization?", q19[0]['']['description']))

if q19[0]['']['description'] == "Yes":

  q20 = [
      af.Page()
      .display_html(
      """
      <style>
        h2 {text-align: center;}
      </style>
      <h2>If yes, please describe the possible problems related to the interaction and \
        compatibility between the systems that form your application.</h2>""")
      .read_textarea(
        label=f"",
        required=True,
        initial_value="",
        placeholder="The possible problems related to the interaction and compatibility between the systems are ...",
        hint=None
      )
  .display_progress(20, 25, text=F"5 questions remaining ...") 
  .run("Next")
  ]

  answers.append(("If yes, please describe the possible problems related to the interaction and \
    compatibility between the systems that form your application.", q20[0]['']))


age_intersection = [
    af.Page()
    .display_html(
    """
    <style>
      h2 {text-align: center;}
    </style>
    <h2>The following questions are only for applications whose user base includes \
      children and adolescents. Does your application have this type of user base?</h2>""")
    .read_cards(
    label=f"",
    options=[{"description": "Yes"} , {"description": "No"}],
    multiple=False,
    required=True,
    initial_value=None,
    hint="The age range for children and adolescents is from 0 to 18 years old."
)
.run("Next")
]

answers.append(("The following questions are only for applications whose user base includes \
  children and adolescents. Does your application have this type of user base?", age_intersection[0]['']['description']))

if age_intersection[0]['']['description'] == "No":
  df = pd.DataFrame(answers, columns=['Question', 'Answer'])
  df.to_csv('answers.csv', index=False)

else:

  q21 = [
    af.Page()
    .display_html(
    """
    <style>
      h2 {text-align: center;}
    </style>
    <h2>Elaborate on the expected effects of the application on young audiences.</h2>""")
    .read_textarea(
      label=f"",
      required=True,
      initial_value="",
      placeholder="The expected effects of the application on young audiences are ...",
      hint=None
    )
  .display_progress(21, 25, text=F"4 questions remaining ...")
  .run("Next")
  ]

  answers.append(("Elaborate on the expected effects of the application on young audiences.", q21[0]['']))

  q22 = [
    af.Page()
    .display_html(
    """
    <style>
      h2 {text-align: center;}
    </style>
    <h2>Elaborate on what has been done to accommodate and mitigate the expected side effects of your application.</h2>""")
    .read_textarea(
      label=f"",
      required=True,
      initial_value="",
      placeholder="We have done the following to accommodate/mitigate any side effects expected of our application ...",
      hint=None
    )
  .display_progress(22, 25, text=F"3 questions remaining ...")
  .run("Next")
  ]

  answers.append(("Elaborate on what has been done to accommodate and mitigate the expected side effects\
     of your application.", q22[0]['']))

  q23 = [
    af.Page()
    .display_html(
    """
    <style>
      h2 {text-align: center;}
    </style>
    <h2>If the application has a specific target audience beyond the age range mentioned, please detail \
      which sub-group best represents your target audience (e.g., teens aged 12-18 years with hearing loss).</h2>""")
    .read_textarea(
      label=f"",
      required=True,
      initial_value="",
      placeholder="Our application's target audience is ...",
      hint=None
    )
  .display_progress(23, 25, text=F"2 questions remaining ...")
  .run("Next")
  ]

  answers.append(("If the application has a specific target audience beyond the age range mentioned, please detail \
    which sub-group best represents your target audience (e.g., teens aged 12-18 years with hearing loss).", q23[0]['']))
  
  q24 = [
    af.Page()
    .display_html(
    """
    <style>
      h2 {text-align: center;}
    </style>
    <h2>What measures have been taken to ensure that the advertisement of the application \
      is clearly and unambiguously exposed.</h2>""")
    .read_textarea(
      label=f"",
      required=True,
      initial_value="",
      placeholder="The measures that have been taken to ensure that the advertisement of the application \
        is clearly and unambiguously exposed are ...",
      hint=None
    )
  .display_progress(24, 25, text=F"1 questions remaining ...")
  .run("Next")
  ]

  answers.append(("What measures have been taken to ensure that the advertisement of the application \
    is clearly and unambiguously exposed.", q24[0]['']))
  
  q25 = [
    af.Page()
    .display_html(
    """
    <style>
      h2 {text-align: center;}
    </style>
    <h2>What measures were taken to ensure that if the application contains third-party \
      advertising, such advertisements are appropriate for the age \
        range of your target audience.</h2>""")
    .read_textarea(
      label=f"",
      required=True,
      initial_value="",
      placeholder="The measures that were taken to ensure that if the application contains third-party \
        advertising, such advertisements are appropriate for the age \
          range of our target audience are ...",
      hint=None
    )
  .display_progress(25, 25, text=F"Last question!")
  .run("Next")
  ]

  answers.append(("What measures were taken to ensure that if the application contains third-party \
      advertising, such advertisements are appropriate for the age \
        range of your target audience", q25[0]['']))
  
  df = pd.DataFrame(answers, columns=['Question', 'Answer'])
  df.to_csv('answers.csv', index=False)