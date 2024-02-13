# What is Fairness? 🔎

_5-minute read._

AI Fairness refers to the various attempts at correcting algorithmic bias in automated decision processes based on machine learning models. It aims to ensure that AI systems do not produce biased outcomes against particular individuals or groups based on race, gender, socioeconomic status, or other sensitive attributes. At the same time, AI fairness is also about creating proactive measures to prevent the production of AI-generated inadvertently harmful or malicious content.

According to [Worldwide AI Ethics](https://en.airespucrs.org/worldwide-ai-ethics), fairness is:

> "_the idea of non-discrimination and bias mitigation (discriminatory algorithmic biases AI systems can be subject to). It defends the idea that, regardless of the different sensitive attributes that may characterize an individual, all should be treated fairly_."

Achieving fairness in AI development requires a multi-faceted approach considering various aspects of the AI system's design, development, and deployment. Here are a few measures that organizations and developers can take to ensure fairness in AI applications:

- **Data Representation:** Fairness in AI entails ensuring that the training data used to develop the AI system is representative of the population it will serve. This process demands that the data be diverse and inclusive.

- **Algorithm Design:** Algorithms can perpetuate and amplify existing biases in the data if they are not designed "_fairly_." Developers can use fairness constraints and bias correction algorithms to ensure that the AI system is unbiased by design.

- **Monitoring and Evaluation:** Regular monitoring and evaluation of AI systems are essential to ensure they remain fair and unbiased over time. It involves tracking key metrics, such as false positive and false negative rates, and making adjustments to ensure a system remains fair while they are active.

- **Stakeholder Engagement:** Engaging with key stakeholders, such as communities likely to be affected by the AI system, can help ensure equitable development. It includes incorporating stakeholder feedback and concerns into the development and deployment of the AI system.

In our methodology, the fairness of an AI system is measured by its use of sensitive attributes, proxies, and intended use:

- **Sensitive attributes:** They are features of an individual closely tied to their membership in a protected group, such as race, gender, religion, or sexual orientation. These attributes are considered sensitive because they are often the basis for discrimination.

- **Proxies:** They are other attributes highly correlated with sensitive attributes and can be a substitute for them. For example, zip code or educational attainment may be utilized as a proxy for race in determinate contexts.

- **Intended Use:** This is the purpose for which the system is designed.

**Note:** Fundamentally, achieving fairness is a sociotechnical challenge. The task of developers is to evaluate their situation and employ the most appropriate mitigation measures possible.

It is crucial to underline that ignoring sensitive attributes to achieve equitable outcomes (i.e., [the original position](https://plato.stanford.edu/entries/original-position/) most commonly known as the veil of ignorance approach) has limitations, and in specific domains (generative AI) is almost impossible. Realizing AI fairness requires a deep understanding of social and cultural factors that may impact different groups, which is not always straightforward or dismissible.

## Why Should You Care? 🤔

As the use of AI spreads to critical areas such as criminal justice, healthcare, and finance, the importance of ensuring AI systems are fair and unbiased increases. Hence, the haphazard use of AI in critical areas of life can result in unfair treatment against particular groups of people. The following cases underline the problems associated with AI fairness regarding the general public.

### Correctional Offender Management Profiling for Alternative Sanctions (**COMPAS**)

Northpointe's tool, called COMPAS, is a case management and decision support tool used by US courts to assess the likelihood of a defendant becoming a recidivist. When defendants are arrested, they answer a COMPAS questionnaire. Their responses are processed into the COMPAS software, which generates scores such as risk of recidivism and violent recidivism.

ProPublica analyzed more than 10,000 criminal defendants in Broward County, Florida, and compared the recidivism risk categories predicted by the COMPAS tool to the actual recidivism rates of defendants two years after they scored.

ProPublica found that black individuals are almost twice as likely as whites to be labeled a higher risk but not re-offend. In contrast, white individuals are much more likely than blacks to be labeled as lower risk but go on to commit other crimes.

You can find more information on the COMPAS case [here](https://www.propublica.org/article/how-we-analyzed-the-compas-recidivism-algorithm) and [here](https://www.propublica.org/article/machine-bias-risk-assessments-in-criminal-sentencing).

### Discrimination in the use of FRTs

Facial recognition techniques are a form of biometric technology that involves identifying and verifying an individual's identity by analyzing facial features. Facial recognition is commonly used in security systems, such as surveillance cameras and border control checkpoints, to verify individuals' identities. The accuracy of facial recognition techniques depends on various factors, including the quality of the images captured, the complexity of the algorithms used, and the size and diversity of the database used to train the model.

While some facial recognition systems have remarkable classification accuracy, these results are not universal. A growing corpus of studies reveals disparities in error rates across demographic categories, with female, black, and 18- to 30-year-olds consistently showing the lowest accuracy.

Three gender classification algorithms, including those produced by IBM and Microsoft, were evaluated in the seminal research "Gender Shades." Darker-skinned women, darker-skinned men, lighter-skinned women, and lighter-skinned men were divided into four groups. All three algorithms performed the worst in the subgroup composed of darker-skinned women, with error rates up to 34% higher than in lighter-skinned men.

The US National Institute of Standards and Technology (NIST) independently corroborated these findings, indicating that facial recognition systems in 189 algorithms are the least reliable for black women.

You can find more information on the subject of FRTs [here](https://nvlpubs.nist.gov/nistpubs/ir/2019/NIST.IR.8280.pdf) and [here](http://proceedings.mlr.press/v81/buolamwini18a/buolamwini18a.pdf). You could also read the [AIRES-RAIES Technical Report](https://www.airespucrs.org/nota-tecnica-frt) on the risks associated with FRTs.

### Discrimination in HR practices

Due to its efficiency, the use of ML models has become increasingly popular in human resources (HR) as an approach to streamline the hiring process. However, there are concerns about the fairness and accuracy of such systems.

Algorithms can perpetuate biases that already exist in the hiring process. For example, if the model is trained on a biased dataset, it may generate biased outputs. It can lead to discrimination against certain groups of people, such as women or non-white people, who may be overlooked by the algorithm even if they are qualified for the job, helping to propagate historical trends of discrimination embedded in their training data.

Targeted ads for jobs are also a field where automated decision-making plays a significant part. According to recent studies ([source](https://pubsonline.informs.org/doi/10.1287/mnsc.2018.3093)), online job adverts in the scientific, technology, engineering, and math sectors were more likely to be shown to males than females in an empirical-quantitative field test among 191 nations.

You can find more information on the problems related to automated decision-making in HR [here](https://link.springer.com/article/10.1007/s40685-020-00134-w) and [here](https://pubsonline.informs.org/doi/10.1287/mnsc.2018.3093).

## Final Remarks

Ensuring fairness in development is essential for building public trust and acceptance of AI systems. The benefits of AI should be widely distributed and not concentrated on particular groups. At the same time, the content generated by such systems should represent our multifaceted society fairly and not help perpetuate the biases we constantly try to overcome.

## Extra Reading

- Molnar, C. [On the (im)possibility of fairness](https://arxiv.org/abs/1609.07236). _ArXiv_, 2016.
- Kateifides, A. _et al_. [Machine Bias - ProPublica Case Study](https://www.dataguidance.com/sites/default/files/gdpr_v_lgpd_revised_edition.pdf), 2018.
- Rubin, J. and Verma, S. [Fairness Definitions Explained](https://fairware.cs.umass.edu/papers/Verma.pdf). _IEEE_, 2018.
- The White House [Blueprint for AI Bill of Rights](https://www.whitehouse.gov/ostp/ai-bill-of-rights/#discrimination). _Online_, 2022.
- O'Neil, C. [Weapons of Math Destruction](https://drive.google.com/uc?export=download&id=12vYWr1vy14C4xJ3U54Lj7EItiwVVjrTn). _Crown Publishers_, 2016.
