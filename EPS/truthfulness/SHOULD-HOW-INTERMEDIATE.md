# Intermediate

EPS uses an evaluation matrix to calculate impacts associated with an application. The three categories in this matrix are **Low**, **Intermediate**, and **High**. From low to high, each category has a set of suggestions to guide future implementations.

EPS measures the level of impact of an application regarding truthfulness through how likely it is to cause harm if its outputs are not entirely truthful. An application with an **intermediate level of impact** is relatively likely to cause harm, given that its application use requires it to produce outputs grounded in facts and human knowledge.

The following intended uses are representative of the Intermediate-impact level:

- **General Assistants:** Generative AI that seeks to follow instructions and solve tasks using natural language, aided or not by other modalities.

- **Coding Assistants:** Generative AI that suggests or creates programmatic code snippets in real time.

The following recommendations are related to the principle of **truthfulness** in applications with an **Intermediate** level of impact.

## Recommendations

An application with an **intermediate level of impact** should implement the following measures:

- **Disclosure:** Non-disclosure of AI involvement can lead to a sense of deception, especially if users are unaware that they are interacting with an AI system.

- **Retrieval Augmented Generation:** It improves the quality of outputs by grounding the model on external sources of knowledge to supplement the internal representation of information.

## How to increase Truthfulness?

### Disclosure

Generative AI systems can produce content that closely resembles humane activities. That is why disclosure is crucial to inform users when AI-generated content is part of an interaction with a system or application.

With disclosure, users become aware that they are engaging with an AI, avoiding potential confusion or misunderstanding about the origin and reliability of the information provided. Also, disclosure should empower users by giving them the necessary information to make informed decisions on whether to trust the output of a particular system or not. When users know the presence of generative AI, they can adjust their expectations and behaviors accordingly. Disclosure statements can be included as **user warnings**, information within the **Terms of Service** or **User Policy**, etc. Improving upon this idea, organizations can also implement **legal disclaimers** to further protect themselves against legal liability.

The importance of disclosure is not exclusive to generative AI; it extends to all AI systems, especially in applications where AI influences choices or decisions. In the end, whether it's decision-making algorithms, image recognition models, or recommendation engines, disclosure helps avoid confusion and deception. To learn about disclosure effects on user interactions with AI, we recommend the following studies ([source](https://arxiv.org/abs/2303.06217), [source](https://arxiv.org/abs/2311.15544)).

### Retrieval-Augmented Generation

Retrieval-augmented generation (RAG) is a technique for improving the quality and accuracy of text generation by using external sources of knowledge. By grounding a generative model on trusted external sources of knowledge to supplement the internal representation of information, RAG reduces what is usually called system hallucination ([source](https://arxiv.org/abs/2104.07567)). At the same time, this source of contextual knowledge outside the base model can always be customized and updated, avoiding retraining models due to their knowledge cut-off. Currently, an extensive knowledge pool combined with an efficient retriever and generation system are the standard components for building generative systems that require factual grounding.

The static (frozen) RAG is the most straightforward implementation of this type of retrieval system, i.e., the retriever is not a trained part of the model ([source](https://arxiv.org/abs/2005.11401)), which utilizes the native in-context learning capabilities of foundation models. In this setting, models are fed relevant information retrieved from a trusted source related to a given input, and their outputs are generated about that source. However, one can also train a retriever (instead of using basic similarity search over vectors) to create an end-to-end neural network-based RAG system.

To create a searchable vector database, the following open-source projects can help you:

- [Weaviate](https://github.com/weaviate/weaviate).
- [Txtai](https://github.com/neuml/txtai).
- [Qdrant](https://github.com/qdrant/qdrant).
- [Milvus](https://github.com/milvus-io/milvus).

> **Note:** For applications where the vector database is not extensive, you can consider simply maintaining them in memory as, for example, a standard matrix of NumPy arrays. The following demo has an example of this implementation, using TF-ITF vectors and cosine similarity search ([demo](https://huggingface.co/spaces/nicholasKluge/TeenyTinyLlama-Chat)). How to create and maintain a trusted, human-curated knowledge source (e.g., Wikipedia, Stanford Encyclopedia of Philosophy, etc) is beyond the scope of the EPS.

If you want to test RAG models with pre-trained dense retrieval components, Transformers offers several models ready for use ([source](https://huggingface.co/docs/transformers/v4.14.1/model_doc/rag)).

Other tools we recommend for augmenting the creation of RAG systems are:

- [SPLADE](https://github.com/naver/splade).
- [DRAGON](https://github.com/facebookresearch/dpr-scale/tree/main/dragon).
- [Hybrid Search](https://docs.pinecone.io/docs/hybrid-search).

The following tutorials show how to use and implement vector databases for search and retrieval [[👉notebook](https://github.com/openai/openai-cookbook/blob/main/examples/vector_databases/qdrant/QA_with_Langchain_Qdrant_and_OpenAI.ipynb)] [[👉notebook](https://github.com/openai/openai-cookbook/blob/main/examples/vector_databases/weaviate/Using_Weaviate_for_embeddings_search.ipynb)] [[👉notebook](https://github.com/openai/openai-cookbook/blob/main/examples/vector_databases/pinecone/Gen_QA.ipynb)].

After implementing your chosen RAG approach, a few benchmarks should help attest if your system has improved in terms of generating falsehoods:

- [TruthfulQA](https://github.com/sylinrl/TruthfulQA) is a benchmark for evaluating the truthfulness of language models in generating answers to questions.

- [FactCheckQA](https://arxiv.org/abs/2311.06697) evaluates the model's propensity to align with content from trusted publishers in the face of uncertainty or controversy.

- [ArtiFact](https://github.com/awsaf49/artifact) is a large-scale dataset to aid in the development of generalizable and robust synthetic image detectors.

- [DeepfakeBench](https://github.com/SCLBD/DeepfakeBench) presents several standardized evaluation metrics and protocols to enhance the evaluation of generative models.

- [DEEP-VOICE](https://www.kaggle.com/datasets/birdy654/deep-voice-deepfake-voice-recognition) can be used to evaluate and develop spech models tackling the detection of AI-generated speech.

Besides, the following tools can be used to monitor and evaluate the factuality of a model's output during inference:

- [LangCheck](https://github.com/citadel-ai/langcheck).
- [Uptrain](https://github.com/uptrain-ai/uptrain).
- [DIRE](https://github.com/ZhendongWang6/DIRE).
- [Factool](https://github.com/GAIR-NLP/factool).

Other resources for automated fact-checking can be found here ([source](https://github.com/Cartus/Automated-Fact-Checking-Resources)).
