# Low

EPS uses an evaluation matrix to calculate impacts associated with an application. The three categories in this matrix are **Low**, **Intermediate**, and **High**. From low to high, each category has a set of suggestions.

EPS measures the level of impact of an application regarding reliability through an inverse correlation with the **fault tolerance** of an application. At the same time, this fault tolerance evaluation considers the context of an application and its scope of use. An application with a **low level of impact** has considerable leniency in case of failure.

The following intended uses are representative of the **Low** level of impact:

- **Spam filters:** Machine learning algorithms used to filter out spam emails from your inbox.

- **Image recognition:** AI algorithms used to recognize and classify objects, digits, and other types of images that do not contain sensitive information.

- **Recommendation engines:** AI-powered recommendation engines suggest products or services based on a user's past behavior and preferences.

- **Entertainment:** AI-powered systems used for games and other recreational activities.

The following recommendations are for an application evaluated as having a **Low** impact level regarding the principle of **reliability**.

## Recommendations

An application with a **low level of impact** should implement the following measures:

- **Robust training:** AI models should perform well on a wide range of inputs and be able to generalize to unseen samples outside of their training distributions.

- **Rigorous testing:** The system should be evaluated on unseen data or standard benchmarks from the field.

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

  - In AI development, **Hyperparameter tuning** is the problem of choosing a set of optimal hyperparameters for a learning algorithm. Algorithms that can search and find optimal solutions in this space can help you improve the performance of your models. Utilities like the Keras Tuner [[👉notebook](https://github.com/Nkluge-correa/teeny-tiny_castle/blob/master/ML%20Intro%20Course/10_hyperparameter_tuning.ipynb)], or [Ray Tune](https://pytorch.org/tutorials/beginner/hyperparameter_tuning_tutorial.html), can help you in this process.

### Rigorous Testing

**Rigorous testing** regarding **reliability** involves evaluating the system's ability to perform its intended functions accurately, efficiently, and consistently over a range of scenarios with unseen data. The standard ML workflow, where we separate training samples for further testing, may need to be more of an evaluation. Because of this, it is a common and highly recommended practice to evaluate your model's performance on standard benchmarks.

> **Note: It is also common for private organizations to have their own set of evaluation benchmarks. If your organization does not have one, we suggest creating one (or adopting open benchmarks for internal use).**

Here are some tools that can be used to benchmark different types of ML systems:

- [SecML](https://github.com/pralab/secml) is an open-source Python library for the security evaluation of Machine Learning algorithms that can be used to evaluate many ML models. We offer a basic tutorial on its use on the following link [[👉notebook](https://github.com/Nkluge-correa/teeny-tiny_castle/blob/master/ML%20Adversarial/evasion_attacks.ipynb)].
- The [Language Model Evaluation Harness](https://github.com/EleutherAI/lm-evaluation-harness) is a framework for few-shot evaluation of language models with hundreds of benchmarks ready for evaluation, being the backbone for famous [LLM leaderboards](https://huggingface.co/spaces/HuggingFaceH4/open_llm_leaderboard). Other types of evaluation harnesses are also available [here](https://decodingtrust.github.io/) (with a focus on Trustworthiness) and [here](https://github.com/embeddings-benchmark/) (with a focus on the evaluation of text embeddings).
- [FACET](https://facet.metademolab.com/) is a benchmark evaluating the fairness of vision models across classification, detection, instance segmentation, and visual grounding tasks that involve people.
- While benchmarks like [COCO](https://github.com/cocodataset/cocoapi) can help you evaluate the object detection skills of computer vision models, benchmarks like [Q-Bench](https://q-future.github.io/Q-Bench/) and [HRS-Bench](https://github.com/hrsbench/HRS_Bench) can help you assess multi-modal models.
