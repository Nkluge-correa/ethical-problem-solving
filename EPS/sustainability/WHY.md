# What is Sustainability?🔎

_6-minute read._

Sustainability for AI systems refers to the design of algorithms that minimize their environmental impact throughout their life cycle. This principle is also related to broader notions of sustainability and how to design and use AI systems to positively impact the well-being of individuals, communities, and the planet.

According to [Worldwide AI Ethics](https://en.airespucrs.org/worldwide-ai-ethics), sustainability is defined as:

> "_...a form of "intergenerational justice," where the well-being of future generations must also be counted during AI development. In AI ethics, sustainability refers to the idea that the development of AI technologies should be carried out with an awareness of their long-term implications, such as environmental costs and non-human life preservation/well-being._"

The literature ([source](https://link.springer.com/article/10.1007/s43681-021-00043-6)) differentiates two main approaches towards sustainability in the field of AI research:

- **AI for sustainability** refers to applying artificial intelligence technologies to address sustainability challenges and promote sustainable development. It involves leveraging AI techniques and tools to tackle environmental, social, and economic issues.

- **Sustainability of AI** refers to developing and deploying artificial intelligence in an environmentally responsible, socially beneficial, and economically viable manner over the long term.

In the EPS, we will focus on the **sustainability of AI**, while the **AI for sustainability** part falls out of our scope. Developing sustainable AI involves leveraging various techniques and tools to minimize environmental impact. Here are some essential techniques commonly used in sustainable AI development:

- **Carbon Tracking:** Carbon tracking allows organizations to quantify their environmental impact for accountability and monitoring.

- **Use of open-source initiatives:** Participating in collaborative and open-source initiatives helps the community minimize the amount of resources required to create and re-create the same types of technologies.

- **Energy-efficient models and hardware:** Designing AI models that prioritize energy efficiency while selecting energy-efficient hardware components for training and inference can reduce AI systems' energy consumption and resource requirements.

- **Lifecycle assessment:** Applying lifecycle assessment (**LCA**) methods can help you evaluate and quantify the ecological impact involved in developing an ML model.

- **Carbon Offset:** Offsetting carbon footprints allows organizations to take responsibility for their greenhouse gas emissions by investing in projects that reduce or capture equivalent emissions.

## Why Should You Care? 🤔

AI systems, especially those involving deep neural network training, often require significant computational power and energy consumption. Training and running AI models can consume large amounts of electricity, leading to increased demand for energy generation, which may contribute to greenhouse gas emissions. Powering and cooling data centers, servers, and high-performance computing infrastructures, which are the bedrest of such models, can also lead to substantial carbon footprints.

At the same time, the rapid advancement of AI technology often leads to frequent upgrades and replacements of hardware components, such as processors and graphics cards, to meet computational demands. Improper disposal or recycling of electronic waste (e-waste) from obsolete AI hardware also results in severe environmental impacts.

Finally, the production and manufacturing of AI hardware components require the extraction and processing of raw materials, which can have adverse environmental consequences, even though mining activities for minerals, such as rare earth elements used in electronics, can lead to habitat destruction, soil degradation, water pollution, biodiversity loss, and workers rights violations.

Managing these issues are all challenges we must face when developing ML systems with **sustainability of AI** in mind.

### A lifetime of emissions

As big data, machine learning, and artificial intelligence grow in popularity in information technology, scientists are becoming increasingly concerned about the carbon footprint and greenhouse gas emissions related to our technological progress.

To confirm this claim, researchers at the University of Massachusetts measured the energy consumption and carbon emissions related to the training of large neural networks for NLP applications ([source](https://arxiv.org/abs/1906.02243)). Their finding revealed that some training runs can produce more than 283 tons of CO2 equivalent, nearly five times the lifetime emissions of the average American car (including car manufacturing).

As model size increases and training runs become longer, the computational and environmental costs of training large neural networks are bound also to increase.

### E-waste in Ghana

According to a [United Nations report issued in 2019](https://www3.weforum.org/docs/WEF_A_New_Circular_Vision_for_Electronics.pdf), around 50 million tons of e-waste are discarded yearly. This figure is expected to more than double by 2050. At the same time, it is estimated that only 20% of e-waste is recycled correctly.

Part of this waste is usually disposed of in countries from the global south (i.e., former colonies). For example, in the case of Ghana, this type of waste arrives via the Port of Tema, 20 miles east of the [Agbogbloshie dump](https://en.wikipedia.org/wiki/Agbogbloshie), one of the biggest centers of environmental dumping in the world. In it, huge containers transport hundreds of thousands of discarded electronics, mainly from Western Europe and the United States. They are usually branded as used consumer goods (a.k.a. they are not categorized as e-waste). Nonetheless, their impact in Ghana is severely toxic to their environment.

It is estimated that up to 10,000 workers sift through tons of discarded goods as part of a vast, informal recycling operation. Hence, if we do not consider the entire life cycle of a piece of technology, we might indirectly contribute to the worsening of conditions in places like Agbogbloshie.

## Final Remarks

Committing to sustainability in AI development is a strategic choice to enhance stakeholder trust and attract socially conscious consumers. However, sustainable AI could become, in the coming years, the key to a balanced and harmonious relationship between humans and the environment, which can result in a healthier and more resilient planet for current and future generations.

## Extra Reading

- [A New Circular Vision for Electronics: Time for a Global Reboot](https://www3.weforum.org/docs/WEF_A_New_Circular_Vision_for_Electronics.pdf). _World Economic Forum_, 2019.
- [What is the environmental footprint of artificial intelligence?](https://www.oecd-events.org/cop27/session/f174ec37-5145-ed11-819a-00224880a4d8) Online, 2022.
- Strubell, E., Ganesh, A. and McCallum, A. [Energy and Policy Considerations for Deep Learning in NLP](https://arxiv.org/abs/1906.02243).  _ArXiv_, 2019.
- Lottick, K., Susai, S., Friedler, S. A., & Wilson, J. P. [Energy Usage Reports: Environmental awareness as part of algorithmic accountability](https://arxiv.org/abs/1911.08354).  _ArXiv_. 2019.
- Cook, G. and Jardim, E. [Clicking Clean Virginia: Greenpeace Reports](https://www.ourenergypolicy.org/wp-content/uploads/2019/03/Greenpeace-Click-Clean-Virginia-2019.pdf). Online, 2019.
- van Wynsberghe, A. [Sustainable AI: AI _for_ sustainability and the sustainability _of_ AI](https://link.springer.com/article/10.1007/s43681-021-00043-6). _AI and Ethics_, 2021.
