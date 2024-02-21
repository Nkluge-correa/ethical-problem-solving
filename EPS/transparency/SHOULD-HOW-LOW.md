# Low

EPS uses an evaluation matrix to calculate impacts associated with an application. The three categories in this matrix are **Low**, **Intermediate**, and **High**. From low to high, each category has a set of suggestions to guide future implementations.

EPS measures the impact level of an application regarding transparency through a correlation between the algorithmic complexity and how critical the system decision is considering the scope of use.

The following intended uses are representative of the Low-impact level:

- **Industrial automation:** AI systems used to automate industrial processes, like quality control.

- **Spam filters:** Machine learning algorithms used to filter out spam emails from your inbox.

- **Entertainment:** AI-powered systems used for games and other recreational activities.

The following recommendations are for an application evaluated as having a **Low** impact level regarding the principle of **transparency**.

## Recommendations

An application with a **low level of impact** should implement the following measures:

- Details about the model and dataset must be provided in a **model card**. [Model cards](https://arxiv.org/abs/1810.03993) provide an easy way to ensure _transparency_ and _accountability_. In a **Low-impact** application, the following information should be disclosed:

  - General information about the responsible developers (e.g., development team leader).
  - General information about the nature of the model (e.g., what type of model?).
  - A performance report.
  - The origins of the data used, data collection, pre-processing, and possible sources of bias that may influence future statistical models.
  - Adequate operational domain and out-of-scope applications.

Also, white-box models should always be preferred when it comes to transparency. However, Black-box models have more leeway when dealing with low-impact situations due to the inexpressibility of possible errors. As a result, **Low**-impact situations are those in which opaque models are acceptable or even appropriate, depending on the application (e.g., digit recognition).

## How to increase transparency?

### Model Cards for Model Reporting

[**Model cards**](https://arxiv.org/abs/1810.03993) are short documents accompanying machine learning models. Such cards provide details and performance characteristics of a model in question, helping to visualize transparency and accountability behaviors in developing autonomous systems.

Platforms like Hugging Face incentivize the display of model cards and dataset cards for all objects hosted in the Hub. [Here](https://huggingface.co/docs/hub/model-cards) and [here](https://huggingface.co/docs/hub/datasets-cards), you can find examples of how to develop your own model and dataset cards, while [here](https://huggingface.co/spaces/huggingface/Model_Cards_Writing_Tool) you can find and application to help you fill this document. We also provide a tutorial on generating this kind of report [[👉 notebook]((https://github.com/Nkluge-correa/TeenyTinyCastle/blob/master/ML-Accountability/Model-Reporting/model_card_generator.ipynb))].
