# High

EPS uses an evaluation matrix to calculate impacts associated with an application. The three categories in this matrix are **Low**, **Intermediate**, and **High**. From low to high, each category has a set of suggestions to guide future implementations.

EPS measures the level of impact of an application regarding truthfulness through how likely it is to cause harm if its outputs are not entirely truthful. An application with a **high level of impact** is expected to cause harm, given that its use involves deceiving or manipulating humans intentionally.

The following intended uses are representative of the High-impact level:

- **Deepfakes and Photo-realistic Image Generation:** Generative AI that can create or manipulate content, particularly images and videos, that convincingly depict false events or scenarios.

The following recommendations are related to the principle of **truthfulness** in applications with a **High** level of impact.

## Recommendations

An application with a **high level of impact** should implement the following measures:

- **Disclosure:** Non-disclosure of AI involvement can lead to a sense of deception, especially if users are unaware that they are interacting with an AI system.

- **Retrieval Augmented Generation:** It improves the quality of outputs by grounding the model on external sources of knowledge to supplement the internal representation of information.

- **Watermarking:** It involves tracing the origin or ownership of the AI system, its components, or outputs. It can help protect against unauthorized modifications or tampering with AI outputs.

- **Moderation:** It involves automated processes and human oversight to ensure the generated content meets the desired standards.

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

### Watermarking

In AI development, watermarking is embedding a recognizable signal into the output of an artificial intelligence model, such as text or an image, to identify that content was produced by that given model,  which carries that specific watermark. That watermark can then be detected by algorithms designed to scan for it, allowing us to monitor the usage of generative models and differentiate AI-generated from human-generated content ([source](https://arxiv.org/abs/2301.10226), [source](https://arxiv.org/abs/2305.12502)).

Watermarking can also help protect organizations against unauthorized modifications or tampering with their product outputs. It emerges as a potential tool for truthfulness in scenarios where generative models can produce photo-realistic content and perform human-like actions. The following tools can help you utilize watermarking in applications that use GenAI:

- [ML Model Watermarking](https://github.com/SAP/ml-model-watermarking).
- [LM-watermarking](https://github.com/jwkirchenbauer/lm-watermarking).
- [WatermarkDM](https://github.com/yunqing-me/WatermarkDM).
- [Invisible-watermark](https://github.com/Stability-AI/invisible-watermark-gpu).

The followng tutorial show analysis of LMM watermarking [[👉notebook](https://github.com/jwkirchenbauer/lm-watermarking/blob/main/experiments/watermarking_analysis.ipynb)] [[👉notebook](https://github.com/jwkirchenbauer/lm-watermarking/blob/main/experiments/watermarking_example_finding.ipynb)].

We also recommend the addition of C2PA-style metadata to generated content, in addition to watermarks. [C2PA](https://c2pa.org/) is an open technical standard that allows organizations to embed metadata in media to verify its origin. Such implementation will enable users and auditing bodies to use tools like [Content Credentials Verify](https://contentcredentials.org/verify) and [Truepic](https://truepic.com/) to verify the provenance of a given piece of content, like an image.

> **Note:** C2PA-style metadata can be removed accidentally or intentionally. Hence, adding identifiable metadata should not be considered a robust solution for creating accountable data provenance.

### Moderation

Moderation for generative models that mimic human activities is challenging. However, in high-impact applications, we recommend human in-the-loop assessment as a necessary condition for deployment. In terms of truthfulness, moderation for high-impact applications involves monitoring the use of a system to ensure its use does not support activities that actively seek to deceive people (e.g., generating photo-realistic images of public figures).

Hence, besides all the tools already mentioned in section **Retrieval-Augmented Generation** for automated fact-checking, high-impact applications require organizations to incorporate a team of human moderators to review and monitor the systems use, much in line with the read teaming ([source](https://arxiv.org/abs/2209.07858)).

If all guardrails fail to prevent falsehood generation (disclosure, RAG, watermarking, and moderation), responsible sunsetting (model termination) should be considered the only viable solution.
