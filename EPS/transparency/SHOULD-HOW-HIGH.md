# High

EPS uses an evaluation matrix to calculate impacts associated with an application. The three categories in this matrix are **Low**, **Intermediate**, and **High**. From low to high, each category has a set of suggestions to guide future implementations.

EPS measures the impact level of an application regarding transparency through a correlation between the algorithmic complexity and how critical the system decision is considering the scope of use.

The following intended uses are representative of the High-impact level:

- **Public administration:** AI algorithms used to improve decision-making, increase efficiency, enhance public services, and improve communication with citizens.

- **Predictive policing:** AI algorithms used to aid in crime prevention and allocate police resources.

- **Facial recognition:** AI algorithms utilized to recognize and track individuals via face images.

- **Healthcare diagnosis:** AI algorithms used to assist in medical diagnosis.

The following recommendations are for an application evaluated to a **High** impact level regarding the principle of **transparency**.

## Recommendations

An application with a **High level  of impact** should implement the following measures:

- Details about the model and dataset must be provided in a **model card**. [Model cards](https://arxiv.org/abs/1810.03993) offer an easy way to ensure _transparency_ and _accountability_. In a **High-impact** application, the following information should be disclosed:

  - General information about the responsible developers (e.g., development team leader).
  - General information about the nature of the model (e.g., what type of model?).
  - A performance report.
  - The origins of the data used in data collection, pre-processing, and possible sources of bias that may influence future statistical models.
  - Adequate operational domain and out-of-scope applications.
  - Model's performance against fairness metrics and a Fairness Statement;

- In **High** impact applications, models should be made available for auditing. In situations where intellectual property must be preserved, confidentiality agreements or NDAs can be used to avoid breaches in intellectual property. However, this should not preclude the publication of conclusions drawn from the access and analysis of the model. Auditors can be formed by, but not exclusively, stakeholders such as:

  - Third-party auditors;
  - Competent authorities;
  - Trusted intermediaries (e.g., regulators, researchers, and courts).

White-box models should always be preferred in terms of transparency. Black-box models should be avoided in **High-Impact** applications since the interpretability of opaque models (_like deep neural networks_) is still challenging. Simultaneously, shallow models (_to the greatest extent possible_) should be prioritized when using Machine Learning since they are easier to interpret.

## How to increase transparency?

### Model Cards for Model Reporting

[**Model cards**](https://arxiv.org/abs/1810.03993) are short documents accompanying machine learning models. Such cards provide details and performance characteristics of a model in question, helping to visualize transparency and accountability behaviors in developing autonomous systems.

Platforms like Hugging Face incentivize the display of model cards and dataset cards for all objects hosted in the Hub. [Here](https://huggingface.co/docs/hub/model-cards) and [here](https://huggingface.co/docs/hub/datasets-cards), you can find examples of how to develop your own model and dataset cards. We also provide a tutorial on generating this kind of report [[👉 notebook]((https://github.com/Nkluge-correa/TeenyTinyCastle/blob/master/ML-Accountability/Model-Reporting/model_card_generator.ipynb))].

### Computer Vision Applications

One of the main ideas behind XAI is that "_complex systems (like neural networks) need to be interpretable to humans._" In response to the concerns raised against model opacity, the field of interpretability (specifically in CV applications) has formed two standard approaches: **feature visualization** and **saliency mapping**.

Platforms like Hugging Face incentivize the display of model cards and dataset cards for all objects hosted in the Hub. [Here](https://huggingface.co/docs/hub/model-cards) and [here](https://huggingface.co/docs/hub/datasets-cards), you can find examples of how to develop your own model and dataset cards, while [here](https://huggingface.co/spaces/huggingface/Model_Cards_Writing_Tool) you can find and application to help you fill this document. We also provide a tutorial on generating this kind of report [[👉 notebook]((https://github.com/Nkluge-correa/TeenyTinyCastle/blob/master/ML-Accountability/Model-Reporting/model_card_generator.ipynb))].

- **Note:** We also recommend the study of the "_[Circuits](https://distill.pub/2020/circuits/)_" series, which thoroughly explains how features and activation maps can be interpreted. Also, for a comprehensive explanation of the limitations and difficulties related to saliency mapping techniques, we recommend "_[Evaluating Saliency Map Explanations for Convolutional Neural Networks: A User Study](https://arxiv.org/abs/2002.00772)_".

The idea of building saliency maps is based on a technique called **Integrated Gradients**. Proposed in "_[Axiomatic Attribution for Deep Networks](https://arxiv.org/abs/1703.01365)_", this methodology uses the gradient of a model to determine what _influences_ the individual inputs (_like words in a sentence or pixels in an image_) have on the output of a model. This methodology can be used in multi-modal models that combine CV with, for example, NLP. This tutorial shows how to interpret diffusion models in this fashion [[👉notebook](https://github.com/Nkluge-correa/TeenyTinyCastle/blob/master/ML-Explainability/CV/diffusion_interpreter.ipynb)]. Meanwhile, the subsequent tutorial explains the **LIME** methodology (_Local Interpretable Model-agnostic Explanations_), which also employs gradient integration techniques in the explanation of CV models [[👉notebook](https://github.com/Nkluge-correa/TeenyTinyCastle/blob/master/ML-Explainability/CV/CNN_attribution_maps_with_LIME.ipynb)].

Also, the following libraries can help you further push the interpretability of CV models:

- [Captum](https://captum.ai/).
- [Diffusers-Interpret](https://github.com/JoaoLages/diffusers-interpret).
- [Alibi](https://github.com/SeldonIO/alibi).
- [Lime](https://github.com/marcotcr/lime).

### Natural Language Processing Applications

Local Interpretable Model-agnostic Explanations can also be employed in NLP models, producing a saliency mapping on tokens instead of pixels. The following tutorials present demonstrations of how to apply gradient integration techniques to different types of models used in language processing [[👉notebook](https://github.com/Nkluge-correa/TeenyTinyCastle/blob/master/ML-Explainability/NLP/lime_for_NLP.ipynb)] [[👉notebook](https://github.com/Nkluge-correa/TeenyTinyCastle/blob/master/ML-Explainability/NLP/integrated_gradients_in-_keras_nlp.ipynb)] [[👉notebook](https://github.com/Nkluge-correa/TeenyTinyCastle/blob/master/ML-Explainability/NLP/gradient_explanations_BERT.ipynb)].

Another way to explore language and ML models, in general, is by investigating the data on which they were trained. Suppose we have text datasets of manageable size. In that case, one can also use **text mining** techniques to examine the distribution of patterns (e.g., sentiment, word recurrence, toxicity, etc.) in a text corpus. In this tutorial, we demonstrate how to use introductory text mining techniques [[👉notebook](https://github.com/Nkluge-correa/TeenyTinyCastle/blob/master/ML-Explainability/NLP/text_mining.ipynb)]. For working with large scale datasets, one can use automated tagging pipelines like the ones used in to create the [Dolma Dataset](https://arxiv.org/abs/2402.00159). This [repository](https://github.com/allenai/dolma) contains several tools (toxicity classifiers) used for generating high-quality pre-training datasets.

Another way to interpret language models, at least those representing language as dense vectors, is by analyzing word/token embeddings. Embeddings are dense vector representations of words (or sub-words) that capture semantic and syntactic information about the tokens they represent. In the following tutorials, you can learn how to create and interpret a word2vector model and the embedding layer of a pre-trained language model [[👉notebook](https://github.com/Nkluge-correa/TeenyTinyCastle/blob/master/ML-Explainability/NLP/word2vec.ipynb)] [[👉notebook](https://github.com/Nkluge-correa/TeenyTinyCastle/blob/master/ML-Explainability/NLP/investigating_word_embeddings.ipynb)].

Since transformers are the foundational architecture behind most state-of-the-art NLP systems nowadays, understanding their workings and interpreting their behavior is paramount. In the following tutorial, we dissect the transformer architecture and show how to explore the attention mechanism and its outputs to a transformer residual stream [[👉notebook](https://github.com/Nkluge-correa/TeenyTinyCastle/blob/master/ML-Explainability/NLP/dissecting_gpt2.ipynb)]. Meanwhile, OpenAI's [Transformer Debugger (TDB)](https://github.com/openai/transformer-debugger) is a tool that supports investigations into specific behaviors of small transformer-based language models, presenting several automated interpretability techniques. Simply put, it can aid developers in answering questions like, "_Why does the model output token A instead of token B for this prompt?_" or "_Why does attention head H attend to token T for this prompt?_".

Also, the following libraries can help you further push the interpretability of NLP models:

- [Interpret-Text](https://github.com/interpretml/interpret-text).
- [Captum](https://captum.ai/).
- [Alibi](https://github.com/SeldonIO/alibi).
- [Lime](https://github.com/marcotcr/lime).

### Classification/Forecasting Applications

Many commercial ML applications train classification or regression models with **tabular data**. The following notebook elaborates on how to interpret the classifications provided by the outputs of these types of models using techniques such as statistical database analysis, **Breakdown plots**, **Interactive Breakdown plots**, **Shapley Additive Explanations**, and **LIME** [[👉notebook](https://github.com/Nkluge-correa/TeenyTinyCastle/blob/master/ML-Explainability/Tabular/interpreter_for_tabular.ipynb)].

Occasionally, statistical analysis may fail to provide a compelling justification for a particular classification. **What-if** tools can give us a more precise (and causally related) insight into these circumstances. In the next tutorial, we offer a demonstration of how to investigate how inputs and parameters affect the model's outputs using **what-if** tools [[👉notebook](https://github.com/Nkluge-correa/TeenyTinyCastle/blob/master/ML-Explainability/Tabular/fairness_xai_COMPAS.ipynb)].

Also, the following libraries can help you further push the interpretability of ML models in general:

- [What-If-Tool](https://github.com/PAIR-code/what-if-tool).
- [InterpretML](https://github.com/interpretml/interpret).
- [DALEX](https://github.com/ModelOriented/DALEX).
- [Alibi](https://github.com/SeldonIO/alibi).
- [Lime](https://github.com/marcotcr/lime).

### Data Transparency for Foundational Models

High-impact applications should extend transparency beyond the system to the dataset itself, as in the case of high-impact applications built on top of foundation models. A **foundation model** is a large model trained at scale on a large corpus of unlabeled data (typically by self-supervised learning), resulting in a model that can adapt to a wide range of downstream tasks.

However, auditing massive datasets has been a challenge that accompanied these foundational models since their inception. Searching for strings or image data on datasets containing billions of samples can be time-consuming if we do not use the proper tools. [**Data portraits**](https://dataportraits.org/) is a proposal that allows developers to shrink datasets to "_3%_" of their current size, allowing for fast auditing and efficient transparency. For more instructions on how to use this tool, explore Data Portraits [GitHub repository](https://github.com/ruyimarone/data-portraits).

In cases where the creation of data portraits is not possible, documenting datasets in a structured way is a recommended measure. **Data Cards** are structured summaries of essential facts about various aspects of ML datasets stakeholders need across a project's lifecycle for responsible AI development. To aid you in the development of a data card, we recommend "[The Data Cards Playbook](https://sites.research.google/datacardsplaybook/)," which can help dataset producers and publishers adopt a people-centered approach to transparency in dataset documentation. Below, we have other tools you can use to aid in this process:

- [Croissant](https://github.com/mlcommons/croissant/).
- [Dataset Card Creation Guide](https://github.com/huggingface/datasets/blob/main/templates/README_guide.md).
