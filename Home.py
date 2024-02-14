import abstra.forms as af

homepage = (
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

<h1>Ethical Problem Solving 🤔</h1>
<p>Ethical Problem Solving (EPS) is a framework to promote the development of safe and ethical artificial \
  intelligence. EPS is divided into an evaluation stage (performed via <strong>Algorithmic Impact Assessment\
    </strong> tools) and a recommendation stage (the <strong>WHY-SHOULD-HOW</strong> method). Both these stages\
       represent distinct steps in a human-centered <em>EaaS</em> (<strong>Ethics as a Service</strong>) \
        framework developed by <em>Nicholas Kluge Corrêa</em>, <em>James William Santos</em>, <em>Camila Galvão\
          </em>, <em>Marcelo Pasetti</em>, <em>Dieine Schiavon</em>, <em>Faizah Naqvi</em>, <em>Robayet Hossain\
            </em>, and <em>Nythamar de Oliveira</em>.</p>
<p>This repository contains a simple demo of our framework, \
    <strong>and it should not be considered a working EaaS platform. The full implementation of our \
      method as an EaaS is currently under development.</strong></p>
<p>Read more about our framework in our <a href="https://github.com/Nkluge-correa/ethical-problem-solving" target="_blank">paper</a></p> \
<p>The source code for this demo is available on <a href="https://github.com/Nkluge-correa/ethical-problem-solving" \
  target="_blank">GitHub</a>.</p>
""")
.display_image(
    "img/eps-method-scheme.png",
    subtitle="A diagram illustrating the transition from AI to Beneficial AI, facilitated by Algorithmic \
      Impact Assessment and Guidance. The process is depicted as moving from abstract principles to \
        practical implementation.",
)
.display_html("""
<style>
  p {
    text-align: justify;
    }
</style>

<p>The following steps can summarize the flow of the EPS methodology:</p>
<h2>Pre-AIA</h2>
<p>The flow of the ethical problem-solving framework begins with a pre-algorithmic impact assessment (Pre-AIA).\
   The pre-assessment gauges preemptively the realm of impact of a particular system, leading to the actual \
    tools of impact assessment. This preliminary assessment informs the user what algorithmic impact assessment \
      surveys (AIAs) are required to fulfill the evaluation stage. For example, the user must perform the privacy \
        and data protection AIA if the intended application utilizes personally identifiable information.</p>
""")
.display_image(
    "img/eps-pre-aia.png",
    subtitle="A flowchart explaining an ethical and human-centered evaluation process. The process involves a \
      preliminary assessment, various types of AIAs, and an ethical troubleshooting survey, leading to a \
        human-centered evaluation.",
)
.display_html("""
<style>
  p {
    text-align: justify;
    }
</style>

<p>After this brief assessment, the user is directed to the next stage.</p>
<h2>Evaluation Stage</h2>
<p>Our evaluation stage consists of questionnaires with pre-defined questions and answers that can be \
  single-choice or multiple-choice. Our current implementation of these AIAs covers the following themes: \
    <strong>data protection and privacy</strong>, <strong>protection of children and adolescents</strong>, \
      <strong>antidiscrimination</strong>, and <strong>consumer rights</strong>. These AIAs use legally \
        binding standards to deduce the implications of AI systems through an objective lens.</p>
""")
.display_image(
    "img/eps-evaluation-stage.png",
    subtitle="An Algorithmic Impact Assessment with two questions, their answers, and corresponding pie charts. \
      The questions are about the usage of sensitive data and the external audits of the application. The \
        responses and pie charts indicate the levels of privacy and transparency. The legend explains the \
          meaning of the colors.",
)
.display_html("""
<style>
  p {
    text-align: justify;
    }
</style>

<p>The questions of our AIAs identify the system's compliance with at least three ethical principles identified \
  by one of our previous studies (<a href="https://nkluge-correa.github.io/worldwide_AI-ethics/" \
    target="_blank">WAIE</a>). Hence, each AIA generates impact scores relative to these assessed principles.\
      </p>
""")
.display_image(
    "img/eps-aia-question.png",
    subtitle="A survey question of the privacy and data protection AIA about personal data collection, with\
       two answer options and scores and three criteria for privacy, transparency, and accountability.",
)
.display_html("""
<style>
  p {
    text-align: justify;
    }
</style>
<p>Ultimately, these assessments generate a standardized impact level on each ethical principle evaluated by \
  each AIA. i.e., we divide the attained score by the maximum attainable score for each principle. At the same \
    time, the overall cumulative impact of all assessed principles represents the general impact of a system \
      against a specific AIA.</p>
<p>Our AIAs provide an impact score that cannot address all of the ubiquities attached to the ethical issues \
  that AI systems present. Hence, in our current implementation of the EPS framework, we developed a more \
    qualitative survey to accompany the evaluation stage, entitled Ethical Troubleshoot, aimed at going beyond \
      an objective evaluation. In short, this troubleshooting query allows the respondent to divulge how a \
        given AI system or application has been developed in a human-centric way. It utilizes a combination of \
          multiple-choice, single-choice, and open-ended questions to gauge the system's scope, its intended \
            and unintended uses, and its target audience.</p>
<h2>Ethical Framing</h2>
<p>After the evaluation stage, the EPS framework requires that human evaluators classify the system under \
  consideration in an impact matrix. The matrix is constituted by three levels of recommendation tailored to \
    each impact level - <strong>high</strong>, <strong>intermediate</strong>, and <strong>low</strong> - and \
      six different ethical principles gathered from the <a href="https://nkluge-correa.github.io/worldwide_AI-ethics/" \
        target="_blank">WAIE</a> review, i.e., fairness, privacy, transparency, reliability, truthfulness, and \
          sustainability.</p>
""")
.display_image(
    "img/eps-ethical-framing.png",
    subtitle="A graphical representation of an Algorithmic Impact Assessment and Ethical Framing in AI, \
      focusing on human-centered design. The image consists of two main sections with pie charts and a \
        grid layout, indicating levels of privacy, consumer rights, antidiscrimination, transparency, and \
          fairness. A grey silhouette icon represents a human-centered approach. The legend explains the \
            meaning of the colors.",
)
.display_html("""
<style>
  p {
    text-align: justify;
    }
</style>

<p>Hence, each principle has three distinct possible recommendations tailored to specific impact levels, \
  e.g., Sustainability-low, Sustainability-intermediate, and Sustainability-high.</p>
""")
.display_image(
    "img/eps-ethical-framing-2.png",
    subtitle="An infographic illustrating the criteria for Human-Centered Evaluation, with icons and text \
      representing Fairness, Privacy, Reliability, Transparency, Truthfulness, and Sustainability. Each \
        criterion is rated on a scale from low to high. The legend explains the meaning of the colors.",
)
.display_html("""
<style>
  p {
    text-align: justify;
    }
</style>

<h2>Recommendation stage (WHY-SHOULD-HOW)</h2>
<p>The WHY-SHOULD-HOW methodology is the format in which the evaluation outcome is presented.</p>
<p>The WHY step is structured to demonstrate the relevancy of each principle, providing the conceptualization \
  and highlighting paradigmatic cases of deficit implementation in a structure that answers the questions \
    "<em>What is said principle?</em>" and "<em>Why should you care about it?</em>". The SHOULD and HOW \
      are attached to streamline the normative guidance and the practical tools to address it.</p>
<p>The SHOULD provides the metric utilized to gauge the level of recommendation regarding the corresponding \
  principle, the level of recommendations indicated for the specific case, and the set of recommendations in a \
    summarized form. Finally, the HOW component offers the practical tools and strategies required to \
      implement the recommendations made in the SHOULD stage.</p>
""")
.display_image(
    "img/eps-why-should-how.png",
    subtitle="A diagram illustrating the relationship between AI and privacy, with a focus on transparency and \
      fairness levels. The image shows a progression from low to high levels of transparency, privacy, and \
        fairness, leading to AI's role in privacy. Questions about the importance of privacy and methods to \
          protect it are highlighted.",
)
.display_html("""
<style>
  p {
    text-align: justify;
    }
</style>

<h2>Tools</h2>
<p>The HOW step of the WHY-SHOULD-HOW methodology pragmatizes the normative recommendations of our method. \
  Hence, throughout the HOW stage, in every principle evaluated, the developer is presented with ready-to-use \
    tools paired with demonstrations in the form of an <a href="https://github.com/Nkluge-correa/teeny-tiny_castle" \
      target="_blank">open repository of tutorials</a>. The repository has many examples of tools and techniques \
        developed to deal with the potential issues of an AI application (e.g., algorithmic discrimination, model \
          opacity, brittleness, etc.), all being worked through with some of the most common contemporary AI \
            applications (e.g., computer vision, natural language processing, forecasting, etc.)</p>
""")
.display_image(
    "img/eps-tools.png",
    subtitle="A graphical representation of metrics related to sustainability, fairness, and transparency in \
      machine learning or similar technological contexts. The image consists of three sections, each labeled \
        with a different attribute: SUSTAINABILITY, FAIRNESS, and TRANSPARENCY. Each section has an associated \
          icon and is connected to a specific tool or metric. The color scheme varies for each section: blue \
            for SUSTAINABILITY, purple for FAIRNESS, and yellow for TRANSPARENCY.",
)
.display_html("""
<style>
  p {
    text-align: justify;
    }
</style>

<p>By following the EPS framework, evaluators and developers working together can identify ethical concerns and take \
  proactive steps to address them. This ultimately leads to tightening the principle-practice gap, i.e., <em>from AI to \
    beneficial AI</em>.</p>
<h2>Disclaimer</h2>
<ol>
<li>
<p>The tools and assessments in this demo are intended to be an academic display of our research.</p>
</li>
<li>
<p>The results obtained by our tools are not legal/technical advice. We suggest consulting a specialist in all cases.</p>
</li>
<li>
<p>Completing the tools indicates guidelines for mitigating algorithmic impacts and suggests measures to \
  solve ethical problems. However, no warranties, express or implied, are made regarding the future performance\
     of the application or the organization.</p>
</li>
<li>
<p>It is up to the stakeholders who have used the tools and assessments to seek to prevent, mitigate, and resolve\
   the possible impacts identified.</p>
</li>
<li>
<p>The author's disclaimer responsibility and the results presented do not serve as a certificate or \
  attestation for ethical practices.</p>
</li>
<li>
<p>The Algorithmic Impact Assessments (AIAs) are based on some legislative texts (Consumer Defense Code, \
  Criminal Code, Statute of the Child and Adolescent, General Data Protection Law). However, they do not \
    lend themselves to exhausting their content for legal compliance.</p>
</li>
<li>
<p>The information, opinions, estimates, and guidelines contained in the platform refer to the present \
  date and may need to be updated due to the passage of time or possible changes.</p>
</li>
</ol>
<hr/>
<p>This methodology is part of the RAIES initiative, a project supported by FAPERGS - \
  (<a href="https://fapergs.rs.gov.br/inicial" target="_blank">Fundação de Amparo à \
    Pesquisa do Estado do Rio Grande do Sul</a>), Brazil.</p>
<p>Ethical Problem Solving © 2024 by Nicholas Kluge Corrêa, James William Santos, Camila Galvão, Marcelo Pasetti, \
  Dieine Schiavon, Faizah Naqvi, Robayet Hossain, and Nythamar de Oliveira is licensed under \
    <a href="https://creativecommons.org/licenses/by-sa/4.0/" target="_blank">CC BY-SA 4.0</a>.</p>
""")
.run("")
)

