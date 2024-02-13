# Low

EPS uses an evaluation matrix to calculate any potential impacts connected with an application. The three impact categories in this matrix are **Low**, **Intermediate**, and **High**. From low to high, each category has a set of suggestions.

EPS measures the level of impact of an application regarding sustainability through how likely they are to cause environmental harm. We quantify environmental harm in the EPS with two metrics: **energy consumption** (kWh) and **estimated carbon emissions** (KgCO2eq). KgCO2eq is a standardized measure used to express the global warming potential of various greenhouse gases. An application with a **low level of impact** is unlikely to cause harm, i.e., has an energy consumption and estimated carbon emissions lower than 0.1 kWh and 0.05 KgCO2eq during training.

Here are some examples of applications classified as low impact according to the EPS:

- **Shallow ML models:** Linear Regression algorithms, Random Forest classifiers, and other small ML models.

- **Small Neural Networks:** Neural networks that do not require extensive training or specialized hardware, e.g., a dense network used for digit classification.

The following recommendations are related to the principle of **sustainability** in applications with a **Low** level of impact.

## Recommendations

An application with a **low level of impact** does not require any particular intervention in its development and use. However, we recommend two practices to ensure your system remains in this minimal state:

- **Carbon Tracking:** Carbon tracking allows organizations to quantify their environmental impact for accountability and monitoring.

- **Collaborative and open-source initiatives:** Participating in collaborative and open-source initiatives helps the community minimize the amount of resources required to create and re-create the same types of technologies.

It should be a standard practice to monitor one's carbon footprint. At the same time, this monitoring should guarantee your application remains below the threshold of **low level of impact** (<  0.1 kWh and < 0.05 KgCO2eq). For example, suppose your system has to deal with millions of calls a minute. In that case, the related energy consumption values might exceed the proposed threshold, even if your application did not require many resources during development.

At the same time, if you are developing an application in which the solution can be achieved by the use of an already open-source model, you should avoid the reinvention of systems that have already proven their capabilities for a wide range of downstream tasks.

## How to increase sustainability?

### Carbon Tracking

**Carbon tracking** is an essential practice in managing the environmental impacts of AI systems. Organizations can comprehensively understand their carbon footprint by calculating and monitoring quantities like energy consumption and estimated carbon emissions. This information is a foundation for driving sustainable practices, optimizing energy efficiency, reducing greenhouse gas emissions, and investing in offsets. But how can one measure their carbon footprint?

Carbon footprint is an index that makes it possible to compare the total amount of greenhouse gases an activity adds to the atmosphere, i.e., how much carbon dioxide equivalents (CO2eq) have been produced. CO2eq is the product of two main factors ([source](https://arxiv.org/abs/1911.08354)): **C** and **E:**

- **C** = the carbon intensity of the electricity consumed (grams of CO₂ emitted per kilowatt-hour of electricity).

- **E** = the energy consumed by the computational process (kilowatt-hour).

The carbon intensity is the weighted average of the emissions from the different energy sources tied to the energy grid being utilized. This measure changes depending on your location, while the world average emission by kWh is 475 gCO2.eq ([source](https://www.iea.org/reports/global-energy-co2-status-report-2019/emissions)). Hence, if you know the carbon intensity of your energy grid and the amount of energy used, you can estimate your carbon emissions and footprint.

Luckily, you do not have to calculate these values by hand since much of it is already hand-coded in tools designed to perform the type of tracking we are recommending. For example, [CodeCarbon](https://github.com/mlco2/codecarbon) is a Python library for estimating and tracking carbon emissions related to computational processes. The following tutorial teaches how to use the main functionalities of this library [[👉notebook](https://github.com/Nkluge-correa/teeny-tiny_castle/blob/master/ML%20Accountability/CO2%20Emission%20Report/emission_tracker.ipynb)]. To learn more about what CodeCarbon can offer (e.g., visualization panels for emission reports), read their [documentation](https://mlco2.github.io/codecarbon/), and see how carbon tracking can be implemented as a part of tools aimed at helping developers choose the most carbon-efficient algorithm with the [Model Inference Emission Visualizer](https://tw-yoo.github.io/miev/#/).

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

- This **repository** lists several open-source LLMs, together with their respective licenses ([source](https://github.com/eugeneyan/open-llms?tab=readme-ov-file#open-llms)).
