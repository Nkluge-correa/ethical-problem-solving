# What is Reliability? 🔎

_6-minute read._

**Reliability** refers to the propensity of a system or process to produce reliable results. In the context of AI systems, **reliability** determines the trustworthiness and effectiveness of the system. Autonomous systems are increasingly used in critical applications, such as autonomous vehicles, medical diagnosis, or financial trading. Any failure or error in the system can have serious consequences.

According to [Worldwide AI Ethics](https://en.airespucrs.org/worldwide-ai-ethics), reliability is:

> "_...the idea that AI technologies should be reliable, in the sense that their use can be verifiably attested as safe and robust, promoting user trust and better acceptance of AI technologies_."

**Reliability** and **Robustness** are two crucial concepts in AI development, and they are closely related but not interchangeable. **Robustness** has become a relevant concept in the AI field because of the growing complexity and diversity of applications and their interactions with real-world environments. There are different ways to approach the concept of robustness in AI applications, but one possible way to categorize it is by considering three levels of robustness:

- **Algorithmic Robustness:** Refers to the AI system maintaining its performance in the face of variations or perturbations in the data it is processing. In other words, an algorithmically robust AI system should be able to handle noisy, incomplete, or ambiguous data and still produce reliable and accurate results.

- **Operational Robustness:** Refers to the AI system performing consistently and reliably under different operating conditions or scenarios (**OOD** - [out-of-distribution robustness](https://arxiv.org/abs/2110.07007)). An operationally robust AI system should be able to handle large volumes of data, operate in different environments, recover from failures, prevent malicious attacks, and protect sensitive information.

- **Ethical Robustness:** Refers to the ability of an AI system to align its decisions and actions with ethical and social norms, values, and expectations. An ethically robust AI system should be transparent, accountable, and fair in its processes, avoid bias and discrimination, and respect human rights and dignity.

**Reliability** rests on the field of **Operational Robustness**, in the sense that it refers particularly to the ability of an AI system to perform consistently and reliably under different operating conditions or scenarios. For the EPS, we shall focus on **Reliability** since the other conceptualizations of **Robustness** are contemplated in different principles (e.g., **Ethical Robustness** is usually treated in [**Alignment**](https://arxiv.org/abs/2001.09768)).

Here are some key steps that can help you achieve **reliability:**

- **Robust training:** Systems should be trained on a sufficiently large and diverse dataset, and the process should be carefully monitored to avoid overfitting or underfitting. Minimal performance levels should be required depending on the level of impact associated with the application.

- **Rigorous testing:** AI systems should be tested thoroughly under various conditions to produce reliable results consistently. Testing should include automated testing and human review to identify potential sources of issues.

- **Continuous monitoring:** Once the AI system is deployed, it should be continuously monitored to ensure that it produces reliable results over time. It may involve regularly tuning the system on new data or retraining the model from scratch.

- **Adversarial machine learning:** AI applications should be able to defend against adversarial attacks. The techniques used during the development of applications to prepare against such attacks may include adversarial training or tuning, robust optimization, defensive distillation, red teaming, and others.

## Why Should You Care? 🤔

One of the most significant risks of avoiding **reliability** in AI development is that the system may produce erroneous results or make incorrect decisions, leading to undesirable outcomes. A lack of **reliability** in AI systems can also lead to security risks. If the system is not designed to be reliable, it may be vulnerable to adversarial attacks, resulting in data breaches and other security threats. Additionally, unreliable AI systems may be utilized for malicious purposes outside their original scope.

### Tesla Autopilot crashes

Tesla's Autopilot system is a well-known example of an AI-based application that relies on operational robustness to ensure safety and **reliability**. However, the US National Highway Traffic Safety Administration (NHTSA) has launched an investigation into Tesla vehicles using its Autopilot driver assistance system (Full Self-Driving) mode.

According to NHTSA data, vehicles utilizing Autopilot features were involved in 273 known crashes from July 2021 to June 2022. Teslas accounted for almost 70 percent of 329 crashes in which advanced driver assistance systems were involved, as well as a majority of fatalities and serious injuries.

There are still [no US federal restrictions](https://www.nytimes.com/2021/12/23/business/tesla-self-driving-regulations.html) on testing autonomous vehicles on public roads, though states have imposed limits in certain cases.

More on the subject of the Tesla Autopilot [here](https://www.washingtonpost.com/technology/2022/06/15/tesla-autopilot-crashes/).

### Microsoft Tay chatbot

Microsoft's Tay chatbot was designed to learn from human interactions and mimic human behavior. Engineers at Microsoft trained Tay's algorithm on a dataset of anonymized public data along with some pre-written material provided to give it a basic grasp of the language. The plan was to release Tay online to discover language patterns through its interactions, which it would emulate in subsequent conversations. Eventually, her programmers hoped, Tay would sound just like the Internet.

On March 23, 2016, Microsoft released Tay to the public on Twitter. At first, Tay engaged harmlessly with her growing number of followers with banter and lame jokes. However, within hours of its launch, the chatbot became the target of malicious users who taught it to spew racist and offensive comments. This incident highlights the importance of safeguards against malicious attacks, monitoring, and moderation tools.

More on the subject of Tay [here](https://demtech.oii.ox.ac.uk/research/posts/ijoc-talking-to-bots-symbiotic-agency-and-the-case-of-tay/).

### Boeing 737 MAX crashes

The crashes of two Boeing 737 MAX planes in Indonesia and Ethiopia, which killed a total of 346 people, were precipitated by a software glitch in the plane's Maneuvering Characteristics Augmentation System (MCAS). The MCAS system was implemented in the Boeing 737 Max to improve its stability and control during flight. However, in 2018 and 2019, two deadly crashes occurred involving the 737 Max, leading to a worldwide grounding of the aircraft. The cause of these crashes was related to the MCAS system.

During the flight, the MCAS system automatically adjusted the angle of the plane's nose to prevent the aircraft from stalling. However, in the case of the two crashes, the MCAS system received faulty data from a sensor, which caused it to activate repeatedly and push the nose of the plane downward. The pilots were unable to regain control, leading to both crashes.

The investigation into the crashes revealed several flaws in the design and implementation of the MCAS system, as well as shortcomings in the training and communication with the pilots.

Boeing settled to pay over $2.5 billion after being charged with fraud over the company's hiding information from safety regulators: a criminal monetary penalty of $243.6 million, $1.77 billion of damages to airline customers, and a $500 million crash-victim beneficiaries fund.

## Final Remarks

Avoiding **reliability** in the development of AI systems can have serious consequences for the system itself and the people who interact with it. As AI systems increasingly decide people's lives, reliable outputs are the ultimate goal. If an AI system is unreliable, it can lead to harmful outcomes for individuals, legal challenges, fines, or even lawsuits. Ensuring **reliability** in your AI system is critical for ethical, legal, business, and technical reasons.

## Extra reading

- Papernot, N. [A Marauder's Map of Security and Privacy in Machine Learning](https://arxiv.org/abs/1811.01134). _ArXiv_, 2018.
- Kurakin, A., Goodfellow, I. and Bengio, S. [Adversarial Machine Learning at Scale](https://arxiv.org/abs/1611.01236). _ArXiv_, 2017
- Goodfellow, I.J., Shlens, J. and Szegedy, C. [Explaining and Harnessing Adversarial Examples](https://arxiv.org/abs/1412.6572) _ArXiv_, 2015.
- Hendrycks, D., Carlini, N., Schulman, J. and Steinhardt, J. [Unsolved Problems in ML Safety](https://arxiv.org/abs/2109.13916). _ArXiv_, 2022.
- Ziegles, D.M., Seraphina, N., Chan, L., Bauman, T., Schmidt-Nielsen, P., Lin, T., Scherlis, A., Nabeshima, N., Weinstein-Raun, B., Haas, D., Shlegeris, B. and Thomas N. [Adversarial Training for High-Stakes Reliability](https://arxiv.org/abs/2205.01663). _ArXiv_, 2022.
- Perez, E., Huang, S., Song, F., Cai, T., Ring, R., Aslanides, J., Glaese, A., McAleese, N. and Irving, G. [Red Teaming Language Models with Language Models](https://arxiv.org/abs/2202.03286). _ArXiv_, 2022.
- Jayaswal, V. [Performance Metrics: Confusion matrix, Precision, Recall, and F1 Score](https://towardsdatascience.com/performance-metrics-confusion-matrix-precision-recall-and-f1-score-a8fe076a2262). Online. 2020.
- Necula, G. [Proof-carrying Code](https://www.cs.jhu.edu/~fabian/courses/CS600.624/proof-carrying-code.pdf). School of Computer Science Carnegie Mellon University. 1997.
- Pandey, V., Kadekodi, P., Bhatarkar, G., and Manohar, R. [A Proposed Systematic Software Robustness Verification Framework (SRVF) for Enhancing Critical Software Module Robustness](https://www.sae.org/publications/technical-papers/content/2021-26-0481/). _Symposium on International Automotive Technology_. 2021.
