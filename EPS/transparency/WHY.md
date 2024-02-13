# What is Transparency? 🔎

_5-minute read_

Artificial Intelligence (AI) is being increasingly used to automate decisions in everyday life, which can have both negative and positive effects. Understanding how AI makes its decisions and the effects an AI has is _Transparency_.

According to [Worldwide AI Ethics](https://nkluge-correa.github.io/worldwide_AI-ethics/), transparency is defined as:

> "_The idea that the use and development of AI technologies should be transparent for all interested stakeholders. Transparency can be related to "the transparency of an organization" or "the transparency of an algorithm." This set of principles is also related to the idea that such information should be understandable to nonexperts and, when necessary, subject to auditing._"

Transparency also involves how the public understands the basic premise of AI and how they assess their relationship to a service, product, or company ([source](https://www.sciencedirect.com/science/article/abs/pii/S0004370218305988?via%3Dihub)). This principle is crucial to AI application development since it helps ensure the system is accountable, fair, and trustworthy. When the inner workings of an AI system are transparent, it is easier to understand how the system arrived at a particular decision or recommendation. It can help to build confidence in the system and encourage people to use it. Transparent applications include the disclosure of the AI system that powers the application. In the case of a specific output, mechanistic interpretability techniques should be used to explain singular outputs (e.g., in a contested classification) when requested.

There are several approaches to promoting transparency in AI application development:

- **Explainable AI (XAI):** This refers to developing AI systems whose decision-making processes are understandable to humans. XAI is considered an attempt to implement the social [right to explanation](https://en.wikipedia.org/wiki/Right_to_explanation), a relevant aspect of AI Ethics, even though (_sometimes_) [there is no legal right or regulatory requirement](https://www.gov.br/acessoainformacao/pt-br/perguntas-frequentes/aspectos-gerais) for such.

- **Open source code:** Making the source code for an AI system available to the public can help to increase transparency by allowing others to review and understand how the system works.

- **Testing and evaluation:** Thoroughly testing and evaluating an AI system ensures its proper function. The conduction of audits, bias assessments, and other evaluation forms can help ensure that a system is currently working as expected.

- **Data provenance:** Ensuring that the data used to train an AI system is transparent and traceable allows insight into how a system was developed and what information grounds its decisions.

- **Human oversight:** Incorporating human oversight into an AI system's decision-making process promotes transparency by inserting an understandable element (a.k.a. a human) into the decision loop. It involves having human reviewers check the decisions made by the AI system or providing a way for users to appeal its decisions.

## Why Should You Care? 🤔

One of the biggest challenges is not building the right model but getting the stakeholders to believe that the model makes a _better_ decision than a human. A better decision should not only be framed as higher accuracy scores during a test evaluation. "_Better_" decisions can also be framed as "_explainable_" because users often would like to understand the reasons behind a given outcome. In the end, informed users are better than non-informed ones.

Artificial intelligence, particularly _deep neural networks_, is already pervasive in several applications, including biometrics, healthcare, and vehicles. Soon, these systems might come to mediate the way we communicate with our entire digital world. However,  AI creates new qualitative and quantitative risks and vulnerabilities despite its evident advantages. With its rising adoption comes the need for audit procedures that provide assurances of trustworthiness and enable the operationalization of impending AI standards and AI regulatory efforts.

Some instances of technology developed in a **transparent and audited manner** are provided below (**even in high-risk scenarios**).

### Electronic Ballot Boxes for E-voting

Transparent algorithmic designs for high-stakes applications include electronic ballot boxes. The Brazilian Supreme Electoral Court (TSE) funds and maintains electronic voting system research and development in Brazil. The code for these computers has not been made public (_they still are black boxes_). Still, it is available to specific stakeholders such as the Armed Forces, Political Parties, and the OAB (Order of Attorneys of Brazil).

However, _if we don't understand how the software works, how can we audit it_? Numerous auditing procedures are utilized in Brazil for this type of system.

In Brazil, for example, auditing agencies conduct a mock election before the actual elections and double-check the results to ensure that all e-voting devices operate as they should ([source](https://en.airespucrs.org/post/auditability-in-black-box-scenarios-brazil-and-electronic-voting)).

### AI-assisted Art generation

Until recently, cutting-edge image production was only feasible via APIs owned by giant corporations. However, with the creation of _Stable Diffusion_, all of this has changed.

[Stable Diffusion](https://huggingface.co/stabilityai/stable-diffusion-xl-base-1.0) is a latent diffusion model for image generation from a text developed by [Stability AI](https://stability.ai/) and [LAION](https://laion.ai/). Unlike models such as [DALL-E 3](https://openai.com/dall-e-3), Stable Diffusion has all of its [source code](https://github.com/CompVis/stable-diffusion) as well as pre-trained weights are available.

Transparent models allow developers to experiment with and improve their processes. The communal aspect of perpetual improvement is impossible when an API restricts developers. At the same time, allowing the open-source community to explore and build upon open-source models usually improves our understanding of their capabilities and limitations in a more transparent way.

Stability AI also provides a model card outlining the potential biases and limitations of Stable Diffusion. Its license (Responsible AI License) allows users to take advantage of the model in a wide range of settings (including free use and redistribution) as long as they respect the specific use case restrictions outlined, which correspond to model applications the licensor deems ill-suited for the model or is likely to cause harm ([libel](https://en.wikipedia.org/wiki/Libel "Libel"), [harassment](https://en.wikipedia.org/wiki/Harassment "Harassment"), [doxxing](https://en.wikipedia.org/wiki/Doxxing "Doxxing"), "exploiting minors", etc.), showing how responsible and open source deployment can be performed at scale.

## Final Remarks

Transparent algorithms and AI systems enable us to explain, inspect, and replicate how they make decisions, generate content, and use data. Transparency also allows us to trace accountability and allocate responsibility, avoiding the requirement of blind faith into something nobody can understand.

In AI-driven contexts, leaders participating in AI governance must understand how and where AI is used. However, this can only be achieved if the information is available in an understandable format. Hence, organizations must disclose accurate, complete, and timely information to stakeholders about their developmental practices to promote transparency in the field.

## Extra reading

- Molnar, C. [Interpretable machine learning](https://christophm.github.io/interpretable-ml-book/). _Lulu. com_, 2020.
- Xu, Feiyu, _et al_. [Explainable AI: A brief survey on history, research areas, approaches, and challenges](https://doi.org/10.1007/978-3-030-32236-6_51). Natural Language Processing and Chinese Computing: 8th CCF International Conference, NLPCC 2019, Dunhuang, China, October 9–14, 2019, Proceedings, Part II 8. _Springer International Publishing_, 2019.
- Prince, S. [Understanding Deep Learning](https://udlbook.github.io/udlbook/). _MIT press_, 2023.
- Nanda, N. [A Comprehensive Mechanistic Interpretability Explainer & Glossary](https://dynalist.io/d/n2ZWtnoYHrU1s4vnFSAQ519J). _Dynalist_, 2024.
