# Intermediate

EPS uses an evaluation matrix to calculate impacts associated with an application. The three categories in this matrix are **Low**, **Intermediate**, and **High**. From low to high, each category has a set of suggestions to guide future implementations.

EPS measures the impact level of an application regarding transparency through a correlation between the algorithmic complexity and how critical the system decision is considering the scope of use.

The following intended uses are representative of the Intermediate-impact level:

- **Target ads:** Recommender systems used to deliver targeted ads to individuals or groups.

- **Image or video generation:** AI-powered systems used to create synthetic images or videos.

- **Text generation:** AI algorithms used to generate text, like writing assistants and code autocompletion tools.

- **Weather forecast:** AI-powered models used to predict the weather.

The following recommendations are for an application evaluated to an **Intermediate** impact level regarding the principle of **transparency**.

## Recommendations

An application with an **Intermediate level of impact** should implement the following measures:

- Details about the model and dataset must be provided in a **model card**. [Model cards](https://arxiv.org/abs/1810.03993) offer an easy way to ensure _transparency_ and _accountability_. In an **Intermediate-impact** application, the following information should be disclosed:

  - General information about the responsible developers (e.g., development team leader).
  - General information about the nature of the model (e.g., what type of model?).
  - A performance report.
  - The origins of the data used in data collection, pre-processing, and possible sources of bias that may influence future statistical models.
  - Adequate operational domain and out-of-scope applications.
  - Model's performance against fairness metrics and a Fairness Statement.
  - (When possible) Make the training dataset available for audits.
    - (If making the training data available is impossible) Provide a transparency report on the used dataset (e.g., a statistical analysis on used features and potential biases).
  - A recommendation for human oversight when utilizing the application.

White-box models should always be preferred when it comes to transparency. However, Black-box models have more leeway when dealing with low-impact situations due to the inexpressibility of possible errors. Black-box models should be used in **Intermediate** impact applications only if the general behavior of the algorithm is interpretable. Simultaneously, shallow models (_to the greatest extent possible_) should be prioritized when using Machine Learning since they are easier to interpret.

## How to increase transparency?

### Model Cards for Model Reporting

[**Model cards**](https://arxiv.org/abs/1810.03993) are short documents accompanying machine learning models. Such cards provide details and performance characteristics of a model in question, helping to visualize transparency and accountability behaviors in developing autonomous systems.

Platforms like Hugging Face incentivize the display of model cards and dataset cards for all objects hosted in the Hub. [Here](https://huggingface.co/docs/hub/model-cards) and [here](https://huggingface.co/docs/hub/datasets-cards), you can find examples of how to develop your own model and dataset cards, while [here](https://huggingface.co/spaces/huggingface/Model_Cards_Writing_Tool) you can find and application to help you fill this document. We also provide a tutorial on generating this kind of report [[👉 notebook]((https://github.com/Nkluge-correa/teeny-tiny_castle/blob/master/ML%20Accountability/Model%20Cards/model_card_generator.ipynb))].

### Computer Vision Applications

One of the main ideas behind XAI is that "_complex systems (like neural networks) need to be interpretable to humans._" In response to the concerns raised against model opacity, the field of interpretability (specifically in CV applications) has formed two standard approaches: **feature visualization** and **saliency mapping**.

The ensuing tutorial presents an interpretability analysis of the inner workings of a CNN using **feature visualization techniques** [[👉notebook](https://github.com/Nkluge-correa/teeny-tiny_castle/blob/master/ML%20Explainability/CV%20Interpreter/CNN_feature_visualization.ipynb)]. Meanwhile, the following tutorial focuses on saliency mapping techniques. Saliency maps provide an interpretable technique to investigate hidden layers in CNNs [[👉notebook](https://github.com/Nkluge-correa/teeny-tiny_castle/blob/master/ML%20Explainability/CV%20Interpreter/CNN_attribution_maps_with_LIME.ipynb)].

- **Note:** We also recommend the study of the "_[Circuits](https://distill.pub/2020/circuits/)_" series, which thoroughly explains how features and activation maps can be interpreted. Also, for a comprehensive explanation of the limitations and difficulties related to saliency mapping techniques, we recommend "_[Evaluating Saliency Map Explanations for Convolutional Neural Networks: A User Study](https://arxiv.org/abs/2002.00772)_".

The idea of building saliency maps is based on a technique called **Integrated Gradients**. Proposed in "_[Axiomatic Attribution for Deep Networks](https://arxiv.org/abs/1703.01365)_", this methodology uses the gradient of a model to determine what _influences_ the individual inputs (_like words in a sentence or pixels in an image_) have on the output of a model. This methodology can be used in multi-modal models that combine CV with, for example, NLP. This tutorial shows how to interpret diffusion models in this fashion [[👉notebook](https://github.com/Nkluge-correa/teeny-tiny_castle/blob/master/ML%20Explainability/CV%20Interpreter/diffusion_interpreter.ipynb)]. Meanwhile, the subsequent tutorial explains the **LIME** methodology (_Local Interpretable Model-agnostic Explanations_), which also employs gradient integration techniques in the explanation of CV models [[👉notebook](https://github.com/Nkluge-correa/teeny-tiny_castle/blob/master/ML%20Explainability/CV%20Interpreter/CNN_attribution_maps_with_LIME.ipynb)].

Also, the following libraries can help you further push the interpretability of CV models:

- [Captum](https://captum.ai/).
- [Diffusers-Interpret](https://github.com/JoaoLages/diffusers-interpret).
- [Alibi](https://github.com/SeldonIO/alibi).
- [Lime](https://github.com/marcotcr/lime).

### Natural Language Processing Applications

Local Interpretable Model-agnostic Explanations can also be employed in NLP models, producing a saliency mapping on tokens instead of pixels. The following tutorials present demonstrations of how to apply gradient integration techniques to different types of models used in language processing [[👉notebook](https://github.com/Nkluge-correa/teeny-tiny_castle/blob/master/ML%20Explainability/NLP%20Interpreter/lime_for_NLP.ipynb)] [[👉notebook](https://github.com/Nkluge-correa/teeny-tiny_castle/blob/master/ML%20Explainability/NLP%20Interpreter/integrated_gradients_in%20_keras_nlp.ipynb)] [[👉notebook](https://github.com/Nkluge-correa/teeny-tiny_castle/blob/master/ML%20Explainability/NLP%20Interpreter/gradient_explanations_BERT.ipynb)].

Another way to explore language and ML models, in general, is by investigating the data they were trained on. Suppose we have text datasets of manageable size. In that case, one can also use **text mining** techniques to examine the distribution of patterns (e.g., sentiment, word recurrence, toxicity, etc.) in a text corpus. In this tutorial, we demonstrate how to use introductory text mining techniques [[👉notebook](https://github.com/Nkluge-correa/teeny-tiny_castle/blob/master/ML%20Explainability/NLP%20Interpreter/text_mining.ipynb)].

Finally, another way to interpret language models, at least those representing language as dense vectors, is by analyzing word/token embeddings. Embeddings are dense vector representations of words (or sub-words) that capture semantic and syntactic information about the tokens they represent. In the following tutorials, you can learn how to create and interpret a word2vector model and the embedding layer of a pre-trained language model [[👉notebook](https://github.com/Nkluge-correa/teeny-tiny_castle/blob/master/ML%20Explainability/NLP%20Interpreter/word2vec.ipynb)] [[👉notebook](https://github.com/Nkluge-correa/teeny-tiny_castle/blob/master/ML%20Explainability/NLP%20Interpreter/investigating_word_embeddings.ipynb)].

Also, the following libraries can help you further push the interpretability of NLP models:

- [Interpret-Text](https://github.com/interpretml/interpret-text).
- [Captum](https://captum.ai/).
- [Alibi](https://github.com/SeldonIO/alibi).
- [Lime](https://github.com/marcotcr/lime).

### Classification/Forecasting Applications

Many commercial ML applications train classification or regression models with **tabular data**. The following notebook elaborates on how to interpret the classifications provided by the outputs of these types of models using techniques such as statistical database analysis, **Breakdown plots**, **Interactive Breakdown plots**, **Shapley Additive Explanations**, and **LIME** [[👉notebook](https://github.com/Nkluge-correa/teeny-tiny_castle/blob/master/ML%20Explainability/Tabular%20Interpreter/interpreter_for_tabular.ipynb)].

Also, the following libraries can help you further push the interpretability of ML models in general:

- [InterpretML](https://github.com/interpretml/interpret).
- [DALEX](https://github.com/ModelOriented/DALEX).
- [Alibi](https://github.com/SeldonIO/alibi).
- [Lime](https://github.com/marcotcr/lime).
