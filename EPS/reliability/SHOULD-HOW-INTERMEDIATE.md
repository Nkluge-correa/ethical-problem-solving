# Intermediate

EPS uses an evaluation matrix to calculate impacts associated with an application. The three categories in this matrix are **Low**, **Intermediate**, and **High**. From low to high, each category has a set of suggestions.

EPS measures the level of impact of an application regarding reliability through an inverse correlation with the **fault tolerance** of an application. At the same time, this fault tolerance evaluation considers the context of an application and its scope of use. An application with an **intermediate level of impact** has some leniency in case of failure.

The following intended uses are representative of the **Intermediate** level of impact:

- **Navigation:** AI systems used for navigation and orientation.

- **Climate modeling:** AI algorithms used to model climate change and predict its impact on ecosystems.

- **Predictive policing:** AI algorithms used to predict crime and allocate police resources.

- **Legislative process:** AI algorithms utilized to assist in bill drafting and legal research, develop predictive models, engage with constituents, and analyze voting patterns.

- **Text generation:** AI algorithms used in text generation, like chatbots or coding assistants.

The following recommendations are for an application evaluated as having an **Intermediate** impact level regarding the principle of **reliability**.

## Recommendations

An application with an **Intermediate level of impact** should implement the following measures:

- **Robust training:** AI models should perform well on a wide range of inputs and should be able to generalize to unseen samples outside of their training and validation distributions.

- **Rigorous testing:** The system should be evaluated on unseen data or standard benchmarks from the field

- **Continuous monitoring:** It ensures that AI systems produce reliable results over time by monitoring, tracking, and handling errors.

- **Adversarial machine learning:** When used the right way, adversarial ML can help AI applications defend against adversarial attacks.

## How to increase reliability?

### Robust Training

To achieve a low error rate, developers must invest in robust training methods, especially when dealing with noisy or incomplete data. The goal is to ensure that AI models perform well on a wide range of inputs, which can prevent unforeseeable mishaps regarding contingent inputs. Here are some techniques and tools for robust training in AI development:

- **Data Quality Checks** are a set of processes and techniques used to assess the reliability of a dataset. In it, we seek to clean and filter our datasets concerning some quality criteria (e.g., the removal of outliers, toxic text, NSFW images, etc.). Here are some tools you can use in this process:

  - Scikit-learn offers a quick way to remove outliers from a dataset with their [novelty and outlier detection utilities](https://scikit-learn.org/stable/modules/outlier_detection.html).
  - One of the most commonly used filtering approaches for large text datasets is the methods used in the creation of the MassiveText dataset, documented in the [Gopher paper](https://paperswithcode.com/paper/scaling-language-models-methods-analysis-1).
  - The [Dolma Toolkit](https://github.com/allenai/dolma/tree/main/docs#dolma-toolkit-documentation) enables dataset curation for pretraining AI models, with features like deduplication and built-in taggers, including language detection, toxicity detection, perplexity scoring, and common filtering recipes.
  - [Langcheck](https://langcheck.readthedocs.io/en/latest/metrics.html) is a Python library that offers several metrics to evaluate the quality (e.g., factual consistency and toxicity) of text samples. Also, one can use already trained models, like [Toxic-Bert](https://huggingface.co/unitary/toxic-bert) and [ToxicityModel](https://huggingface.co/nicholasKluge/ToxicityModel) for this exact purpose.
  - Libraries like [NSFW Detection](https://github.com/GantMan/nsfw_model), and ML models like [NSFWDetector](https://github.com/lovoo/NSFWDetector), [NSFW-Resnet](https://github.com/yangbisheng2009/nsfw-resnet), and [SD Safety Checker](https://github.com/woctezuma/stable-diffusion-safety-checker) can be used to filter unwanted images from CV datasets.

- **Training Improvements** are techniques that allow ML models to perform better during training. Given the significant amount of heuristic knowledge used in designing successful ML experiments, following the hypersettings stipulated by similar projects or celebrated studies is a good practice. However, if you cannot access those, hyperparameter searching can be a valuable ally in optimizing any training run.

  - In AI development, **Hyperparameter tuning** is the problem of choosing a set of optimal hyperparameters for a learning algorithm. Algorithms that can search and find optimal solutions in this space can help you improve the performance of your models. Utilities like the Keras Tuner [[👉notebook](https://github.com/Nkluge-correa/teeny-tiny_castle/blob/master/ML%20Adversarial/adversarial_training_cv.ipynb)], or [Ray Tune](https://pytorch.org/tutorials/beginner/hyperparameter_tuning_tutorial.html), can help you in this process.

### Rigorous Testing

**Rigorous testing** regarding **reliability** involves evaluating the system's ability to perform its intended functions accurately, efficiently, and consistently over a range of scenarios with unseen data. The standard ML workflow, where we separate training samples for further testing, may not be enough of an evaluation. Because of this, it is a common and highly recommended practice to evaluate your model's performance on standard benchmarks.

> **Note: It is also common for private organizations to have their own set of evaluation benchmarks.**

Here are some tools that can be used to benchmark different types of ML systems:

- [SecML](https://github.com/pralab/secml) is an open-source Python library for the security evaluation of Machine Learning algorithms that can be used to evaluate many ML models. We offer a basic tutorial on its use on the following link [[👉notebook](https://github.com/Nkluge-correa/teeny-tiny_castle/blob/master/ML%20Adversarial/evasion_attacks.ipynb)].
- The [Language Model Evaluation Harness](https://github.com/EleutherAI/lm-evaluation-harness) is a framework for few-shot evaluation of language models with hundreds of benchmarks ready for evaluation, being the backbone for famous [LLM leaderboards](https://huggingface.co/spaces/HuggingFaceH4/open_llm_leaderboard). Other types of evaluation harnesses are also available [here](https://decodingtrust.github.io/) (with a focus on Trustworthiness) and [here](https://github.com/embeddings-benchmark/) (with a focus on the evaluation of text embeddings).
- [FACET](https://facet.metademolab.com/) is a benchmark evaluating the fairness of vision models across classification, detection, instance segmentation, and visual grounding tasks that involve people.
- While benchmarks like [COCO](https://github.com/cocodataset/cocoapi) can help you evaluate the object detection skills of computer vision models, benchmarks like [Q-Bench](https://q-future.github.io/Q-Bench/) and [HRS-Bench](https://github.com/hrsbench/HRS_Bench) can help you assess multi-modal models.

### Continuous Monitoring

**Continuously monitoring** a machine learning system is essential for maintaining the system's performance, reliability, and compliance.
Ml models deployed and not monitored may present unsatisfactory behavior if not appropriately maintained, making the monitoring part of an MLOps cycle an integral part of AI development.

You can learn more on the matter with the following guides:

- [A Comprehensive Guide on How to Monitor Your Models in Production](https://neptune.ai/blog/how-to-monitor-your-models-in-production-guide), by Neptune.ai.

- [A Guide to Monitoring Machine Learning Models in Production](https://developer.nvidia.com/blog/a-guide-to-monitoring-machine-learning-models-in-production/), by Kurtis Pykes.

- For developers using applications based on OpenAI's services, we recommend their [production best practices](https://platform.openai.com/docs/guides/production-best-practices) guide and [safety best practices](https://platform.openai.com/docs/guides/safety-best-practices) guidebook.

> **Note: It is essential to critically assess when ML models should be taken out of production (sunset).**

### Adversarial Machine Learning

**Adversarial machine learning (AML)** is a subfield of machine learning that focuses on developing algorithms and techniques that can withstand and respond to adversarial attacks. **Adversarial attacks** are a type of threat where an attacker deliberately manipulates the
inputs of ML models, intending to cause them to produce incorrect outputs.

Security engineers can use **AML** to improve the robustness of ML models by identifying vulnerabilities and developing countermeasures to mitigate the impact of adversarial attacks. A range of techniques has been developed for **AML**, including **adversarial training** (_training models on adversarial examples_) and **defensive distillation** (_creating a distilled version of a model resistant to adversarial attacks_).

In **adversarial training**, we generate adversarial examples and use them as samples for training (or fine-tuning) the original model, making it more robust. The following tutorial focuses on how to create an adversarial dataset to train and test the reliability of a **CNN** model utilizing the [**Fast Gradient Sign Method**](https://arxiv.org/abs/1412.6572)[[👉notebook](https://github.com/Nkluge-correa/teeny-tiny_castle/blob/master/ML%20Adversarial/adversarial_training_cv.ipynb)]. Meanwhile, this tutorial focuses on how to create an adversarial dataset to train and test the robustness of **NLP** models utilizing the [**TextAttack**](https://github.com/QData/TextAttack)[[👉notebook](https://github.com/Nkluge-correa/teeny-tiny_castle/blob/master/ML%20Adversarial/adversarial_training_nlp.ipynb)]. Also, for applications involving NLP, the article  "_[Red Teaming Language Models with Language Models](https://arxiv.org/abs/2202.03286)_" provides excellent insights into the process of adversarially training language models.

Another technique from AML is **Defensive distillation**, which involves training a model on the outputs of another model, which has been trained on perturbed data. This kind of [expert distillation](https://arxiv.org/abs/1503.02531) is a commonly used technique in ML, using the knowledge stored in one model (_expert_) to help train a second one (_apprentice_).

The process of **defensive distillation** involves the following steps:

1. **Train an apprentice:** The apprentice model is trained on the original uncorrupted training data.

2. **Perturb the training data:** We generate adversarial examples by perturbing the original training data with small amounts of adversarial distortion.

3. **Train an adversarial expert:** The expert model is trained on the adversarial examples generated in step 2.

4. **Use the expert model to retrain the apprentice:** The expert model can be used for inference in an assisted training regime, where its outputs are used to help the apprentice model become more resilient against adversaries.

The following tutorials focus on how to create adversarial examples against **CNNs**[[👉notebook](https://github.com/Nkluge-correa/teeny-tiny_castle/blob/master/ML%20Adversarial/evasion_attacks_FGSM.ipynb)] and **language models** [[👉notebook](https://github.com/Nkluge-correa/teeny-tiny_castle/blob/master/ML%20Adversarial/adversarial_text_attack.ipynb)_].

**Note: It is worth noting that while adversarial training improves the model's robustness against adversaries, such regimes usually deteriorate the model's performance due to model collapse. Preventing model collapse is a nontrivial challenge during model fine-tuning and extended training.**
