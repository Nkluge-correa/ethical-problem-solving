# Low

EPS uses an evaluation matrix to calculate impacts associated with an application. The three categories in this matrix are **Low**, **Intermediate**, and **High**. From low to high, each category has a set of suggestions.

EPS measures the level of impact of an application regarding fairness through how sensitive attributes or proxies are related to the workings of a given AI system and application.

The following intended uses are representative of the **Low** level of impact:

- **Spam filters:** Machine learning algorithms used to filter out spam emails from your inbox.

- **Recommendation engines:** AI-powered recommendation engines suggest products or services based on a user's past behavior and preferences.

- **Weather Forecast:** AI-powered models used to predict the weather.

- **Navigation:** AI systems used for navigation and orientation.

- **Entertainment:** AI-powered systems used for games and other recreational activities.

The following recommendations are for an application evaluated as having a **Low** impact level regarding the principle of **fairness**.

## Recommendations

An application with a **low level of impact** should implement the following measures:

- **Model card:** Details about the model and dataset must be provided in a [model card](https://arxiv.org/abs/1810.03993). It is an easy way to disclose possible or potential biases.

- **Fairness Statement:** This assertion outlines the organization's approach to the issue of fairness in the performance of the system/application.

- **Disparate Impact Score:** It is a metric used to measure the degree to which an outcome may disparate impact different groups. A **DIS** aims to help identify and quantify potential sources of bias and facilitate the development of strategies to mitigate those biases.

## How to increase fairness?

### Model Cards for Model Reporting

[**Model cards**](https://arxiv.org/abs/1810.03993) are short documents accompanying machine learning models. Such cards provide details and performance characteristics of a model in question and can help publicize potential biases of a dataset or model.

Platforms like Hugging Face incentivize the display of model cards and dataset cards for all objects hosted in the Hub. [Here](https://huggingface.co/docs/hub/model-cards) and [here](https://huggingface.co/docs/hub/datasets-cards), you can find examples of how to develop your own model and dataset cards. We also provide a tutorial on generating this kind of report [[👉 notebook]((https://github.com/Nkluge-correa/TeenyTinyCastle/blob/master/ML-Accountability/Model-Reporting/model_card_generator.ipynb))].

### Fairness Statement (**fairness metrics**, **bias mitigation techniques**)

A **fairness statement** typically includes information about the data used to train the model, the **fairness metrics** used to evaluate the model's performance, the **bias mitigation techniques** used to address any identified biases, and the steps taken to ensure alignment with ethical and legal standards. At the same time, a fairness statement can contain a warning regarding bias issues users might experience.

#### **Fairness Metrics**

To provide quantitative measures for the fairness evaluation of a machine learning model, a **confusion matrix** is quite helpful for navigating several quantitative **fairness metrics**. A **Confusion Matrix** is a table used to evaluate the performance of a classification model by comparing the actual and predicted values of a set of test data. On this matrix, you will find ratios for:

- **True Positives (TP):** True Positive is a case where the model predicted a positive value, and the actual value was also positive.

- **False Positives (FP):** False Positive is a case where the model predicted a positive value, but the actual value was negative.

- **True Negatives (TN):** True Negative is a case where the model predicted a negative value, and the actual value was also negative.

- **False Negatives (FN):** False Negative is a case where the model predicted a negative value, but the actual value was positive.

These ratios should be similar when comparing groups possessing different sensitive attributes. For example, a significant difference in FP for a sensitive attribute like gender indicates that the system tends to assign (wrongly) the positive class for people with a specific gender type. A naive approach to solving such an issue would involve hiding all known sensitive attributes from the model. Nevertheless, such a solution ignores that proxies can infer sensitive attributes. For example, in a racially segregated city, **address** is a proxy for **race**.

If we suspect a feature is a proxy for a sensitive attribute, **fairness metrics** can help us further inspect their relationship with the model's output. Fairness metrics are a set of measures that enable you to detect the presence of bias in your model. These metrics can be used to identify disparities in the decision-making process of an algorithm. However, quantitative fairness metrics may be ill-suited for certain types of systems (e.g., generative models). Even though one can explore statistical distributions of generated content (like we do in this tutorial [[👉notebook]](https://github.com/Nkluge-correa/TeenyTinyCastle/blob/master/ML-Fairness/nlp_fairness_distilgpt2.ipynb)), the exploration of biases in generative models usually follows a more qualitative and exploratory approach, where analysts try to uncover hidden (and sometimes not so hidden) tendencies and functionalities of such systems.

For applications with a **low** impact, a more straightforward fairness score (**Disparate Impact Score**) can suffice.

To apply the **Disparate Impact Score** (DIS), first, define the sensitive attribute or demographic group to evaluate. Once identified, calculate the proportion of positively impacted individuals in each group. For example, estimate the proportion of loan applications approved for each group in a credit scoring model. Next, calculate the **Disparate Impact Score** using the following formula:

`DIS = (the proportion of positively impacted individuals in group A) / (the proportion of positively impacted individuals in group B)`

Group A is the protected demographic group, and Group B is the non-protected demographic group. With this result in hand, we can start thinking about mitigation.

#### **Bias Mitigation**

**Bias mitigation techniques** are used to reduce or eliminate the impact of bias in machine learning models. These techniques ensure that the model's predictions are equitable for individuals, regardless of their demographic characteristics. For an application of **low impact**, we can use such tools to help us restore our DIS score.

A DIS score of less than 1 indicates that the model has a disparate impact on the protected group compared to the non-protected group. If the score is 1, it suggests that the model is entirely equitable. The industry standard is a [four-fifths rule](https://dictionary.apa.org/four-fifths-rule): if the unprivileged group receives a positive outcome of less than 80% of their proportion of the privileged group, this is a disparate impact violation.

When the DIS score is unsatisfactory, there are techniques to modify a dataset to attain a DIS score closer to acceptable ranges. For example, [Disparate Impact Remover](https://arxiv.org/abs/1810.01943) is a tool currently implemented in the [AI Fairness 360](https://www.ibm.com/opensource/open/projects/ai-fairness-360/) that can address this subject straightforwardly. The following tutorial focuses on how to implement this tool [[👉notebook]](https://github.com/Nkluge-correa/TeenyTinyCastle/blob/master/ML-Fairness/disparate_impact_remove_Hogwarts.ipynb).

Here are some other tools you can use to assess and improve fairness of machine learning models:

- [Dalex](https://dalex.drwhy.ai/python/api/fairness/index.html).
- [AI Fairness 360](https://www.ibm.com/opensource/open/projects/ai-fairness-360/).
- [Fairlearn](https://fairlearn.org/v0.8/auto_examples/index.html).
- [REVISE](https://github.com/princetonvisualai/revise-tool).
- [Others](https://github.com/topics/fairness-ml).
