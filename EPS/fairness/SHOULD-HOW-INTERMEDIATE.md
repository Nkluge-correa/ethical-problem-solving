# Intermediate

EPS uses an evaluation matrix to calculate impacts associated with an application. The three categories in this matrix are **Low**, **Intermediate**, and **High**. From low to high, each category has a set of suggestions.

EPS measures the level of impact of an application regarding fairness through how sensitive attributes or proxies are related to the workings of a given AI system and application.

The following intended uses are representative of the intermediate** level of impact:

- **Personal assistants:** Text- or voice-activated personal assistants used to respond to user commands.

- **Chatbots:** AI-powered systems used to handle customer service.

- **Target Ads:** Recommender systems used to deliver targeted ads to individuals or groups.

- **Image or video generation:** AI-powered systems used to create synthetic images or videos.

- **Text generation:** AI algorithms used to generate text, like writing assistants and code autocompletion tools.

The following recommendations are for an application evaluated as having an **Intermediate** impact level regarding the principle of **fairness**.

## Recommendations

An application with an **intermediate level of impact** should implement the following measures:

- **Model card:** Details about the model and dataset must be provided in a [model card](https://arxiv.org/abs/1810.03993). It is an easy way to disclose possible or potential biases. For applications with an **intermediate** level of impact, the **model card** should be accompanied by a justification for utilizing sensitive attributes, or proxies, in the application.

- **Fairness Statement:** This assertion outlines the organization's approach to the issue of fairness in the performance of the system or application. For applications with an **intermediate** level of impact, the **fairness statement** should also be accompanied by a fairness evaluation (e.g., **fairness metric scores**).

- **Monitoring and Explaining:** While metrics such as a **Disparate Impact Score** are a simple way to make biases evident, they might be too simplistic for applications with an **intermediate** level of impact. Tracking the model's performance in production and measuring the impact of sensitive attributes in a model's output is necessary to prevent unfair outcomes.

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

In regards to fairness metrics, here are some of the most used methods in the field:

- **Statistical Parity Ratio (SPR):** SPR compares the proportion of members of a given group that were classified for the positive class (i.e., correctly or not, a.k.a., TP + FP) to another group (privileged | unprivileged).

- **Equal Opportunity Ratio (EOR):** EOR compares the true positive rate (i.e., TPR, a.k.a., _Sensitivity/Recall_) of different groups (privileged | unprivileged).

- **Predictive Parity Ratio (PPR):** PPR compares the positive predictive value (i.e., PPV, a.k.a., _Precision_) of different groups (privileged | unprivileged).

- **Predictive Equality Ratio (PER):** PER compares the false positive rate (FPR, a.k.a., _fall-out/false alarm ratio_) of different groups (privileged | unprivileged).

- **Accuracy Equality Ratio (AER):** Accuracy Equality Ratio compares the proportion of group members that were correctly classified (i.e., _accuracy_) to another group (privileged | unprivileged).

- **Equalized Odds (EO):** EO is the most restrictive quantitative metric of ML Fairness. This criterion is only satisfied if both groups (privileged | unprivileged) have equal TPR and FPR.

Considering applications with an **intermediate level of impact**, we recommend metrics such as **statistical parity ratio**, **equal opportunity ratio**, and **accuracy equality ratio**, which should help clarify fairness issues. However, considering that **sensitive attributes** may play a part in the decision-making process of an algorithm, the choice of a **fairness metric** should come with a clear justification.

- **Note:** It has been shown that it is [impossible to satisfy all fairness metrics simultaneously.](https://arxiv.org/abs/2007.06024) ([source]([text](https://arxiv.org/abs/1609.05807))). Thus, the choice of which metric to use must be made according to the context of an application (i.e., benefit awarding, medical diagnosis, etc.).

#### **Bias Mitigation**

**Bias mitigation techniques** are used to reduce or eliminate the impact of bias in machine learning models. These techniques ensure that the model's predictions are equitable for individuals, regardless of their demographic characteristics. For an application of an **intermediate level of impact,** these should be useful:

- **Data Preprocessing:** It involves cleaning and preparing the data to remove possible sources of bias in the dataset. It includes eliminating features, samples, and balancing the data to ensure it represents all demographic groups fairly.

- **Model Retraining:** Retraining the model on a more diverse dataset or with more varied features can help reduce bias. It is already possible to find datasets where diversity is protected. For example, the [**FairFace**](https://github.com/joojs/fairface) dataset has a balanced race, gender, and age distribution of images of human faces. At the same time, such datasets can be used to evaluate models.

- **Regularization & Reweighting:** These are techniques used to penalize the model for making decisions that disproportionately affect certain demographic groups and for altering the feature values in a dataset, distancing the model from the true distribution. Optimizing for fairness instead of accuracy can help create models that produce equitable outputs.

The following libraries can help you further push for bias-reduction in your models:

- [Dalex](https://dalex.drwhy.ai/python/api/fairness/index.html).
- [AI Fairness 360](https://www.ibm.com/opensource/open/projects/ai-fairness-360/).
- [Fairlearn](https://fairlearn.org/v0.8/auto_examples/index.html).
- [REVISE](https://github.com/princetonvisualai/revise-tool).
- [Others](https://github.com/topics/fairness-ml).

Also, the following tutorials focus on the application of fairness metrics in different contexts and more [[👉notebook](https://github.com/Nkluge-correa/TeenyTinyCastle/blob/master/ML-Fairness/fair_metrics_Credit_card_approval.ipynb),
[👉notebook](https://github.com/Nkluge-correa/TeenyTinyCastle/blob/master/ML-Fairness/fair_metrics_celeba.ipynb),
[👉notebook](https://github.com/Nkluge-correa/TeenyTinyCastle/blob/master/ML-Fairness/nlp_fairness_distilgpt2.ipynb)].

### Monitoring and Explaining

In real-world scenarios, ML models have to deal with dynamic environments. Datasets can only be a snapshot of reality, forcing us to constantly adapt and refine the supervision signal we feed to our models. Monitoring is vital for tracking the model's performance during production. Issues like model biases can be resolved by regularly monitoring how the model performs over time.

Those responsible for developing or overseeing automated systems should conduct proactive equity assessments during the model's design phase, during development, testing, and beyond. Model sunset should be considered an option when a model is irreparably dysfunctional.

These are a few steps to elevate the monitoring of a model:

- **Real-world testing:** Evaluating the algorithm's performance in real-world scenarios aims to ensure fair outcomes and not adversely affect any particular demographic group.

- **User Feedback:** User feedback on the algorithm's outcomes contributes to identifying any biases or disparities that may not be captured by other metrics or evaluation techniques.

- **Continuous Monitoring:** Continuously monitor the algorithm's outcomes and re-evaluate it as new data and situations arise.

- **Updates:** Regularly update the algorithm and its evaluation methods as needed to ensure that it remains fair and equitable.

Explaining an ML model's operation can also illustrate how sensitive attributes influence this algorithmic process. In some industries, such as finance or healthcare, there may even be legal or regulatory requirements for explaining the impact of sensitive attributes in AI models.

Compliance with these regulations is essential for avoiding legal and reputational risks. Here, **Fairness** and **Transparency** intersect. The following tutorials are focused on **Explainable** and **Interpretable** AI [[👉notebook](https://github.com/Nkluge-correa/TeenyTinyCastle/blob/master/ML-Explainability/Tabular/fairness_xai_COMPAS.ipynb), [👉notebook](https://github.com/Nkluge-correa/TeenyTinyCastle/blob/master/ML-Explainability/Tabular/interpreter_for_tabular.ipynb)]. Also, we recommend the "_[Explanatory Model Analysis](https://ema.drwhy.ai/)_" guidebook to address the intersection of **Fairness** and **Transparency**."
