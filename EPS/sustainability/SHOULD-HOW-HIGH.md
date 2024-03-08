# High

EPS uses an evaluation matrix to calculate any potential impacts connected with an application. The three impact categories in this matrix are **Low**, **Intermediate**, and **High**. From low to high, each category has a set of suggestions.

EPS measures the level of impact of an application regarding sustainability through how likely they are to cause environmental harm. We quantify environmental harm in the EPS with two metrics: **energy consumption** (kWh) and **estimated carbon emissions** (KgCO2eq). KgCO2eq is a standardized measure used to express the global warming potential of various greenhouse gases. An application with a **high level of impact** is likely to cause severe harm, i.e., has an energy consumption and estimated carbon emissions higher than 1,500 kWh and 500 KgCO2eq during training. For example, BLOOM-175B produced 24.7 tonnes of CO2eq if we consider only the dynamic power consumption and 50.5 tonnes if accounting for all processes related to equipment manufacturing and operational energy consumption ([source](https://arxiv.org/abs/2211.02001)).

Here are some examples of applications classified as **high-impact** according to the EPS:

- **Deep neural networks** with more than 2 billion parameters or models trained severely pass the [optimal data scaling point](https://www.cerebras.net/model-lab/) ([source](https://arxiv.org/abs/2203.15556)).

The following recommendations are related to the principle of **sustainability** in applications with a **High** level of impact.

## Recommendations

An application with a **High level of impact** should implement the following measures:

- **Carbon Tracking:** Carbon tracking allows organizations to quantify their environmental impact for accountability and monitoring.

- **Use of open-source initiatives:** Participating in collaborative and open-source initiatives helps the community minimize the amount of resources required to create and re-create the same types of technologies.

- **Energy-efficient models and hardware:** Designing AI models that prioritize energy efficiency while selecting energy-efficient hardware components for training and inference can reduce AI systems' energy consumption and resource requirements.

- **Lifecycle assessment:** Applying lifecycle assessment (**LCA**) methods can help you evaluate and quantify the ecological impact involved in developing an ML model.

- **Carbon Offset:** Offsetting carbon footprints allows organizations to take responsibility for their greenhouse gas emissions by investing in projects that reduce or capture equivalent emissions.

## How to increase sustainability?

### Carbon Tracking

**Carbon tracking** is an essential practice in managing the environmental impacts of AI systems. Organizations can comprehensively understand their carbon footprint by calculating and monitoring quantities like energy consumption and estimated carbon emissions. This information is a foundation for driving sustainable practices, optimizing energy efficiency, reducing greenhouse gas emissions, and investing in offsets. But how can one measure their carbon footprint?

Carbon footprint is an index that makes it possible to compare the total amount of greenhouse gases an activity adds to the atmosphere, i.e., how much carbon dioxide equivalents (CO2eq) have been produced. CO2eq is the product of two main factors ([source](https://arxiv.org/abs/1911.08354)): **C** and **E:**

- **C** = the carbon intensity of the electricity consumed (grams of CO₂ emitted per kilowatt-hour of electricity).

- **E** = the energy consumed by the computational process (kilowatt-hour).

The carbon intensity is the weighted average of the emissions from the different energy sources tied to the energy grid being utilized. This measure changes depending on your location, while the world average emission by kWh is 475 gCO2.eq ([source](https://www.iea.org/reports/global-energy-co2-status-report-2019/emissions)). Hence, if you know the carbon intensity of your energy grid and the amount of energy used, you can estimate your carbon emissions and footprint.

Luckily, you do not have to calculate these values by hand since much of it is already hand-coded in tools designed to perform the type of tracking we are recommending. For example, [CodeCarbon](https://github.com/mlco2/codecarbon) is a Python library for estimating and tracking carbon emissions related to computational processes. The following tutorial teaches how to use the main functionalities of this library [[👉notebook](https://github.com/Nkluge-correa/TeenyTinyCastle/blob/master/ML-Accountability/CO2-Emission-tracking/emission_tracker.ipynb)]. To learn more about what CodeCarbon can offer (e.g., visualization panels for emission reports), read their [documentation](https://mlco2.github.io/codecarbon/), and see how carbon tracking can be implemented as a part of tools aimed at helping developers choose the most carbon-efficient algorithm with the [Model Inference Emission Visualizer](https://tw-yoo.github.io/miev/#/).

Besides CodeCarbon, here are some other tools that you can use to estimate your carbon emissions:

- [Machine Learning Emissions Calculator](https://mlco2.github.io/impact/) is a tool to estimate the carbon emissions based on your energy consumption and geo-location/cloud provider, training ML models produce.

- [Eco2AI](https://github.com/sb-ai-lab/Eco2AI) and [Carbontracker](https://github.com/lfwa/carbontracker?tab=readme-ov-file#carbontracker) are two other Python libraries for emission tracking during the training of deep learning models.

- [MLflow-emissions-sdk](https://github.com/datarootsio/mlflow-emissions-sdk) is a log management tool that helps you integrate carbon tracking into your ML workflow (it uses CodeCarbon under the hood).

### Use of open-source initiatives

Open-source initiatives provide ways for sharing knowledge, research, and their byproducts, allowing developers to build upon the work of others and preventing organizations from repeatedly reinventing the same piece of software. By openly sharing code, models, datasets, and resources, these initiatives enable collective innovation and iteration, leading to a more sustainable AI ecosystem. If you would like to, for example, train a computer vision model for object detection, instead of training your CNN from scratch, you can download the pre-trained weights from something like Resnet and fine-tune it by a fraction of the resources required to train it.

Many platforms make models and datasets available to developers, while major deep learning frameworks already come with models and datasets integrated into their ecosystem. Below is a non-exhaustive list of open-source resources that can help you develop AI solutions without reinventing the wheel:

- **Torchvision** contains definitions of several models and their pre-trained weights for different tasks, including image classification, pixel-wise semantic segmentation, object detection, instance segmentation, person keypoint detection, video classification, and optical flow ([source](https://pytorch.org/vision/stable/models.html#models-and-pre-trained-weights)).

- **PyTorch Hub** contains a great variety of models for several different applications (language, vision, audio, generative, etc.) ([source](https://pytorch.org/hub/)).

- **TensorFlow** also possesses a large list of models and datasets as part of its open-source platform for ML ([source](https://www.tensorflow.org/resources/models-datasets)) ([source](https://github.com/tensorflow/models/tree/master/official#tensorflow-official-models)) ([source](https://www.tensorflow.org/datasets)).

- **Kaggle** also has hundreds of trained, ready-to-deploy machine learning models, besides a great number of datasets hosted in their platform ([source](https://www.kaggle.com/models)).

- **Hugging Face** provides an excellent UI for selecting already-trained models for dozens of tasks ([source](https://huggingface.co/tasks)).

- **Timm** is a library tied to the Hugging Face ecosystem that contains several SOTA computer vision models and utilities ([source](https://github.com/pprp/timm?tab=readme-ov-file#pytorch-image-models)).

- This **repository** lists several open-source LLMs and their respective licenses ([source](https://github.com/eugeneyan/open-llms?tab=readme-ov-file#open-llms)).

### Energy-efficient models and hardware

The development stage of a particular system can be a critical moment in attaining sustainability, given that the model design considerably influences the energy consumption of the whole system. Specific design and architectural choices significantly impact the resources needed for training and running inference on large models.

There are three main components we have to consider before training a large model if we wish to optimize its resource consumption: model **architecture**, **dataset size**, and the **hardware** the models are going to be trained:

In terms of **architecture**, when creating a large neural network, we aspire to use the best and most efficient components, given that these can shorten the required training, i.e., faster training runs -> less computation -> reduced costs. Here are some examples of how you can achieve this:

- In the case of computer vision, certain types of basic operations can be optimized to require less computations. For example, when creating a CNN, instead of using the standard convolutional layer, [depthwise separable convolutions](https://arxiv.org/abs/1610.02357), which are a type of layer implemented on standard DL libraries ([TensorFlow](https://www.tensorflow.org/api_docs/python/tf/keras/layers/DepthwiseConv2D), [PyTorch](https://github.com/seungjunlee96/Depthwise-Separable-Convolution_Pytorch)), require less computation, resulting in faster training and inference, with almost no loss in performance. You can learn more about the substitution of **Conv2D** layers by **SeparableConv2D** in this tutorial [[👉notebook](https://github.com/Nkluge-correa/TeenyTinyCastle/blob/master/ML-Accountability/CO2-Emission-tracking/carbon_emission_cv.ipynb)].

- In the case of language models, the current most significant bottleneck in computational resources is the [attention mechanism](https://d2l.ai/chapter_attention-mechanisms-and-transformers/index.html), which has a quadratic computational complexity in sequence length. To alleviate this bottleneck, we have a few options. The first is to abandon attention and rely on attention-free models, like parallelizable RNNs ([RWKV](https://www.rwkv.com/)) or state space models like Mamba ([source](https://github.com/state-spaces/mamba?tab=readme-ov-file#mamba)). Currently, RWKV is already implemented in the Transformers library ([source](https://huggingface.co/docs/transformers/model_doc/rwkv)). The other option is to utilize a more efficient implementation of the attention mechanism, like [FlashAttention](https://github.com/Dao-AILab/flash-attention), which can speed up inference and training considerably. FlashAttention is already implemented in libraries like [Transformers](https://huggingface.co/docs/transformers/perf_infer_gpu_one#flashattention-2), [PyTorch](https://pytorch.org/docs/master/generated/torch.nn.functional.scaled_dot_product_attention.html), and [Optimum](https://huggingface.co/docs/transformers/perf_infer_gpu_one#-optimum). Besides, one can also implement, instead of the vanilla attention mechanism, more efficient ways to compute attention ([Sparse Attention](https://github.com/kyegomez/SparseAttention)). Many modern models, like Llama 2 and Mistral 7B, utilize attention mechanisms that allow for faster computation, like [Grouped Query Attention](https://paperswithcode.com/method/grouped-query-attention) and [Sliding Window Attention](https://paperswithcode.com/method/sliding-window-attention). Lastly, one can also develop and use sparse models, like a Sparse Mixture of Experts ([Sparse MoEs](https://huggingface.co/blog/moe)), which use far fewer resources, allowing for the training and use of much larger models for a fraction of the computational cost. [Open-source versions of Sparse MoEs](https://huggingface.co/mistralai/Mixtral-8x7B-v0.1) are already available to the public under permissive licenses.

- In the case of diffusion models, [MaskDiT](https://github.com/Anima-Lab/MaskDiT) and [Patch Diffusion](https://github.com/Zhendong-Wang/Patch-Diffusion) are techniques that allow for faster and more efficient training runs for diffusion-based models. While **MaskDiT** can reduce training runs to 30% of the time, **Patch Diffusion** promises to achieve 2x faster training. At the same time, both methods maintain comparable or better image generation quality than traditional approaches.

Regarding **dataset**, we can use scaling laws to estimate our dataset's optimal size relative to our model's size. For example, according to the [Chinchilla](https://arxiv.org/abs/2203.15556) scaling laws, we can model language modeling loss as a function of model size(the number of parameters) and training dataset size (the number of tokens). Generally, these laws point to a golden ratio of 20 tokens per parameter for a given language model, also saying that as we increase our model size, we should increase our dataset size proportionally. Hence, provided that you know the model size you wish to train, you can design your dataset according to this optimal range:

- This [tool](https://www.cerebras.net/model-lab/) can give you training and inference estimations for the resources required to train large models.

- If you are interested in training optimally sized LLMs, we recommend this [TeenyTinyLlama](https://github.com/Nkluge-correa/TeenyTinyLlama?tab=readme-ov-file#teenytinyllama-open-source-tiny-language-models-trained-in-brazilian-portuguese) repository.

- To learn about the laws that govern the scaling of computer vision models, we recommend the following study ([source](https://arxiv.org/abs/2106.04560)).

Regarding **hardware**, hardware selection is crucial in developing and deploying AI systems, directly impacting their efficiency, performance, and energy consumption. AI workloads often require extensive computational power, and selecting hardware components optimized for AI tasks can deliver superior performance while minimizing energy consumption.

As a first approach to optimizing your awareness, we recommend researching what are the most efficient:

- This [publication](https://www.tomshardware.com/features/graphics-card-power-consumption-tested) illustrates a test made with more than 50 GPUs from different brands, showing the relationship between power consumption and efficiency.

- This repository provides a simple [speed test](https://github.com/MTDoven/GPU-Speed-Test) for GPUs. It also contains comparisons of the most commercially available GPUs on the market.

- The [Deep Learning GPU Benchmark](https://mtli.github.io/gpubench/) compares GPUs in terms of their latency regarding training, inference, and complexity of the task under consideration.

This type of research will allow you to find the GPUs that can give you the most FLOPs per resource unit (kWh). Also, the hardware that usually produces better results is the most recent and expensive product in the market. State-of-the-art GPUs are generally quite expensive, but they can drastically speed up training runs and minimize costs in the long run. For example:

- Many optimization tricks are only available for the most recent graphic cards (e.g., ampere architecture, hopper architecture, etc.), like the use of [FlashAttention2](https://github.com/Dao-AILab/flash-attention).

- Ampere GPUs have exclusive math modes, like [TF32](https://pytorch.org/docs/stable/notes/cuda.html#tensorfloat-32-tf32-on-ampere-devices), that allow for a 3X increase in throughput.

- For more information on how to take the most out of your training runs, we recommend the following two articles ([source](https://huggingface.co/docs/transformers/perf_train_gpu_one), [source](https://huggingface.co/docs/transformers/perf_train_gpu_many)). Further resources for model optimization can be found [here](https://www.tensorflow.org/model_optimization) and [here](https://developer.nvidia.com/tensorrt).

Something that can also boost the efficiency of your hardware is to tailor the hardware itself to your needs. For training or inference, **field-programmable gate arrays** (**FPGAs**) are customizable circuits for specific AI tasks. These are often used in edge computing and IoT applications, given that they can achieve high performance while being power-efficient. You can learn more about FPGAs and how and when to use them [here](https://www.run.ai/guides/gpu-deep-learning/fpga-for-deep-learning). In the same spirit, **application-specific integrated circuits** (**ASICs**) can also be used to make ML pipelines more efficient ([source](https://research.ibm.com/blog/ibm-artificial-intelligence-unit-aiu)).

> **Note:** If you are interested in learning how to optimize the inference of large neural networks on CPUs, we recommend you look into projects like [Llama.cpp](https://github.com/ggerganov/llama.cpp), [Whisper.cpp](https://github.com/ggerganov/whisper.cpp), and [Llama2.c](https://github.com/karpathy/llama2.c).

The methods cited above can help you lower the resource consumption of your system, especially during training. However, a whole other family of methods can improve this efficiency even more, allowing you to fine-tune modes and serve them by a fraction of the original resources it would take. These are methods for **efficient fine-tuning** and **model quantization**.

Fine-tuning a pre-trained model to a specific task is common in modern deep learning, given that foundation models are the base for many applications and systems. This process, which involves updating the parameters of a neural network through additional gradient updates, can narrow down and maximize the capabilities of pre-trained models. However, full fine-tuning optimizes all parameters, which can be very resource-intensive, especially if your foundation model is large. To help you with this issue, you may want to employ **Parameter Efficient Fine-Tuning** (**PEFT**) techniques.

**PEFT** encompasses a collection of methods aimed at fine-tuning large models in a computationally efficient manner, preserving performance without the resource-intensive nature of full fine-tuning. This process is done by adding extra adapters (extra matrices of weights) to the linear layers on your model and training only these adapters while keeping the rest of the network frozen. This process can significantly decrease the number of trainable parameters during a fine-tuning run while generating almost the same performance as full fine-tuning. Several techniques to perform **PEFT** are already implemented in the Transformers library, which possesses excellent documentation on how to do it ([source](https://huggingface.co/docs/peft/index)). The main techniques we recommend in this section are **Low-rank adaptation** (**LoRA**), **Quantization**, and **Quantized low-rank adaptation** (**QLoRA**). These techniques are some of the most widely used, parameter-efficient finetuning techniques for training large neural networks, which, in essence, reduce the number of trainable parameters in a model or reduce the precision in which these parameters are expressed:

- With **LoRA**, instead of fine-tuning all the weights that constitute the weight matrix of the model, we only fine-tune two smaller matrices that approximate this larger matrix. These matrices form the LoRA adapter. The size of your adapter depends on how much of the network will have a corresponding adapter and what the rank of these adapters will be. As you expand the size and rank of your adapters, you approximate a full fine-tuning, i.e., LoRA is a generalization of full fine-tuning ([source](https://www.youtube.com/watch?v=DhRoTONcyZE)). You can learn more about LoRA [here](https://lightning.ai/pages/community/tutorial/lora-llm/), and the following guides explain how to configure models for LoRA and fine-tune them ([source](https://huggingface.co/docs/peft/developer_guides/lora#lora), [source](https://www.databricks.com/blog/efficient-fine-tuning-lora-guide-llms)).

- **Quantization** reduces the precision of numerical values used to store the model's parameters. For example, instead of using full-precision (float32), we can load models at half-precision (float16) or even more quantized versions (like 8-bit or 4-bit integers) and still get the same level of performance. Most of the large models developed today are trained with [half-precision](https://huggingface.co/docs/transformers/main/en/perf_train_gpu_one#mixed-precision-training) (flot16 or bfloat16). In short, the main advantage of quantizing a model is reducing memory footprint and latency, which can optimize your model's throughput and resource consumption. To perform quantization, we recommend methods like [AutoAWQ](https://github.com/casper-hansen/AutoAWQ?tab=readme-ov-file#autoawq), [AutoGPTQ](https://github.com/AutoGPTQ/AutoGPTQ?tab=readme-ov-file#autogptq), and [Bitsandbytes](https://github.com/TimDettmers/bitsandbytes). The following tutorials can help you get familiar with this process [[👉 notebook](https://colab.research.google.com/drive/1HzZH89yAXJaZgwJDhQj9LqSBux932BvY), [👉 notebook](https://colab.research.google.com/drive/1_TIrmuKOFhuRRiTWN94iLKUFu6ZX4ceb?usp=sharing), [👉 notebook](https://colab.research.google.com/drive/1ge2F1QSK8Q7h0hn3YKuBCOAS0bK8E0wf?usp=sharing)]. Also, the Transformers library has integration for all of these quantization methods ([source](https://huggingface.co/docs/transformers/v4.37.2/quantization)). CL frameworks like TensorFlow and PyTorch also provide quantization schemes and models for developers ([source](https://www.tensorflow.org/tutorials/optimization/compression), [source](https://pytorch.org/docs/stable/quantization.html)).

- **QLoRA** is a combination of the last two approaches, i.e., quantize the model -> perform a LoRA fine-tuning on its quantized version, which dramatically diminishes the memory footprint and resource consumption of very large models ([source]( https://github.com/artidoro/qlora)). The following tutorial shows how to fine-tune a 7B parameter model on consumer-grade GPU using QLoRA  [[👉 notebook](https://colab.research.google.com/github/brevdev/notebooks/blob/main/mistral-finetune.ipynb)].

> **Note:** Certain tasks are unsuitable for PEFT. For example, full fine-tuning is needed if you must train new embeddings in a language model or adapt a multilingual LLM to become monolingual. However, a PEFT with low-rank adaptations is sufficient for many tasks to produce results as good as full fine-tuning. In short, the more you need to move away from your foundation, the more you will need to adapt it.

A final point where we can squeeze efficiency out of our training is during gradient updates. Standard optimizers used in deep learning, like [Adam](https://arxiv.org/abs/1412.6980) or [AdamW](https://arxiv.org/abs/1711.05101), are memory-hungry, using up to 8 bytes per parameter. Hence, if your model has 100 million parameters, Adam would need approximately 800 megabytes of GPU memory for the weight updates. However, some techniques can help you prevent having such a severe memory footprint tied to your optimizer. For example, [Adafactor](https://arxiv.org/abs/1804.04235) only stores aggregated information (row- and column-wise sums of the rolling averages) which reduces the footprint considerably. Meanwhile, [8-bit Adam](https://github.com/TimDettmers/bitsandbytes) allows storing states in quantized form during training, allowing for less memory usage. Finally, techniques like [GaLore](https://github.com/jiaweizzhao/GaLore/tree/master), which use gradient projection to work with gradients at a lower rank (much like LoRA does with model parameters, but instead, we are dealing with low rank projections of optimizer states), allows users to train large scale models in consumer hardware with minimal code modification.

### **Lifecycle assessment and environmental impact analysis**

A **Lifecycle assessment** (**LCA**) is supposed to provide a comprehensive view of the environmental impact of a given AI system, considering all stages, from raw material extraction to disposal. This assessment enables a holistic understanding of the **sustainability** implications, including resource consumption, emissions, waste disposal, and other impacts this process might have on our environment and human lives in general.

Here, we present a small step-by-step guide toward creating your LCA:

- **Scope Definition:** First, you must clearly define the boundaries of the assessment. Identify the evaluated AI system's purpose, functional unit, and system boundaries, determining the lifecycle stages that should be included (e.g., raw material extraction, manufacturing, use, and end-of-life). The more stages you can add, the more complete your LCA will be.

- **Inventory Analysis:** Second, you must tally data on the inputs (e.g., materials, energy, water) and outputs (e.g., emissions, waste) associated with each stage of the AI system's lifecycle. This process involves gathering information on, for example, the amount of human labor employed in mineral extractions and their working conditions, the number of resources used to refine and produce hardware components, the amount of emissions generated by the use of such components, the shelf-life of such materials, the impact they are presumed to generate when disposed of,  and any other relevant parameters.

- **Impact Assessment:** Third, you must analyze the collected data to assess the environmental impacts of everything tallied during your inventory. This assessment includes translating your measures into a standard metric (e.g., CO2eq) that can be used to estimate the carbon footprint tied to your system.

- **Reporting and Communication:** Fourth, you must comprehensively prepare your results, summarizing the assessment methodology, results, and conclusions. Communicating findings to involved stakeholders is a practice that brings the sustainability principle closer to other principles, like accountability and transparency.

Creating one of these LCAs can give organizations valuable insights into the environmental implications of their operations. If you need an example of how such reports are presented, you can use the following reports as a basis ([source](https://impakter.com/index/nvidia-sustainability-report/), [source](https://www.apple.com/environment/pdf/Apple_Environmental_Progress_Report_2023.pdf)). Meanwhile, the following sources can give you recommendations for finding sustainable suppliers and a more extensive guide for building lifecycle assessments ([source](https://ecochain.com/blog/finding-sustainable-suppliers/), [source](https://ecochain.com/knowledge/life-cycle-assessment-lca-guide/)).

### Carbon Offsets

The last recommendation for **high-impact** systems and applications is offsetting. Carbon offset refers to practices that reduce greenhouse gas (GHG) emissions or increase carbon storage (e.g., through land restoration or tree planting). In essence, it is the practice of attempting to balance the impacts of your emissions, which will become evident if you have made your lifecycle assessment.

A carbon offset credit is a certified, transferable instrument representing the reduction of one metric tonne of CO2 or an equivalent amount of different GHGs. Purchasers can retire these credits to claim the underlying deduction for their greenhouse gas reduction goals. Hence, the EPS recommends that all developers of **high-impact** systems and applications **offset their emissions completely.**

You can learn more about carbon offset projects and programs and how to acquire a carbon offset credit [here](https://www.offsetguide.org/understanding-carbon-offsets/). More information on Brazil's approach to these carbon-offsetting projects can be found [here](https://www.biofilica.com.br/floresta-mais-carbono-novo-programa-do-governo-federal-incentiva-o-mercado-voluntario-de-creditos-de-carbono-de-floresta-nativa/#) and [here](https://www.gov.br/pt-br/noticias/meio-ambiente-e-clima/2020/10/floresta-carbono-incentiva-conservacao-de-vegetacao-nativa).
