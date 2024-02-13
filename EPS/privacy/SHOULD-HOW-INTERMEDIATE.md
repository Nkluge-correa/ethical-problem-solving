# Intermediate

EPS uses an evaluation matrix to calculate impacts associated with an application. The three categories in this matrix are **Low**, **Intermediate**, and **High**. From low to high, each category has a set of suggestions.

EPS measures the privacy level of an application by how much personal and sensitive data is required. An application with an **intermediate level of impact** uses (collects or stores) personal data intentionally.

The following intended uses are representative of the **Intermediate** level of impact:

- **Recommendation engines:** AI-powered recommendation engines suggest products or services based on a user's past behavior and preferences.

- **Entertainment:** AI-powered systems used for games and other recreational activities.

- **Target Ads:** Recommender systems used to deliver targeted ads to individuals or groups.

- **Autonomous vehicles:** Self-driving cars use AI to navigate and make decisions on the road.
  
The following recommendations are for an application evaluated as having an **Intermediate** impact level regarding the principle of **privacy**.

## Recommendations

An application with an **Intermediate level of impact** should implement the following measures:

- **Encryption techniques:**  **Symmetric** or **Asymmetric** encryption techniques, secure communication through safe protocols (**HTTPS** and **TLS**), and regularly updating security software (**firewalls** and **antivirus**) can help protect data against unauthorized access.

- **Privacy by Design:** Data minimization techniques, such as **data augmentation** and sampling, can help minimize the amount of data collected. **Anonymization** helps the developer deal with personal or sensitive data. De-identification techniques, such as **data masking**, remove identifying characteristics from data to ensure another level of data protection.

- **Data Governance:** Governance platforms and **data mapping tools** can help developers and responsible stakeholders track and monitor data collection and use practices.

- **Privacy Policies:** Privacy policies should be used to clearly explain how data will be - _or not_ - collected, used, and shared. In situations where personal data will be collected, **consent forms** should be used to obtain permission from individuals.

## How to increase Privacy?

### **Encryption**

There are many encryption techniques used to safeguard data. The two great families of encryption algorithms are known as **symmetric** and **asymmetric**.

Symmetric encryption can be used for safely storing data, securely transmitting data, and encrypting session data for secure communication in real-time applications. Some of the most standard symmetric encryption algorithms are AES (**Advanced Encryption Standard**), DES (**Data Encryption Standard**), and 3DES (**Triple Data Encryption Standard**). Current transfer protocols (like **HTTPS**, empowered by **TLS**) use these types of encryption to ensure safe networking.

Asymmetric encryption can be used mainly for verification purposes, like certifying the authenticity and integrity of data and securing network traffic. Some of the most standard asymmetric encryption algorithms are RSA (**Rivest-Shamir-Adleman**), ECC (**Elliptic Curve Cryptography**), and ECDH (**Elliptic-curve Diffie–Hellman**).

Developers who need to gain expertise in cyber security should avoid building their encryption methods and rely on the trusted services of platforms that provide secure back-end infrastructure. **Choosing a reliable PaaS for data protection is beyond the scope of EPS.**

Applications with an **Intermediate** level of impact, i.e., collecting or storing personal data intentionally, should add extra layers of encryption inside their private network to reinforce in-house security. For example, organizations that allow collaborators to access their internal network remotely should use encryption techniques (like **VPN** - _Virtual Private Network_) to secure network trafficking. Examples of tools that can be used for this include:

- [Hotspot Shield](https://www.hotspotshield.com/).
- [PrivadoVPN](https://privadovpn.com/).
- [atlasVPN](https://atlasvpn.com/).

As external sources of knowledge, forums like [security.stackexchange](https://security.stackexchange.com/) can help developers with doubts about security issues (_the help of professionals/experts should always be welcomed and prioritized over AI-assisted input_).

### Privacy by Design (**Data minimization**, **Data anonymization**)

Data minimization is a process that entails solely collecting, storing, and processing the data needed for a particular purpose. Data minimization intends to lessen the danger of data breaches while protecting people's privacy.

There are many strategies developers can use to minimize data storage and collection. For example:

- Developers should restrict data collection processes to only what is necessary and sufficient. Meanwhile, data that has no use for the intended purposes of the application should be deleted or not collected in the first place.

- After all data types considered essential to the application are defined, the collection should be dutifully informed (and consented) to the data subjects.

- Data sampling can give analysts insight into the whole distribution. For example, a surveyor may collect data from a sample of 1000 people to represent the opinion of a city's population.

- Another way to minimize the data needed is to use data augmentation techniques to mimic true data. For example, Fake data can be used to test in production software. Libraries like [Faker](https://github.com/faker-js/faker) can help you with this task. One can even find [companies](https://www.tonic.ai/) that provide data augmentation and mimicking services.

- As an organizational policy, data that has lived past its usefulness should be disposed of. Also, data hoarding should be discouraged. Policies like this can help organizations minimize their data storage costs.

In regards to data anonymization, here are some methods developers can use to improve their practices:

- [**Federated learning**](https://arxiv.org/abs/1907.09693) is a machine learning technique that trains models on decentralized data, such as data stored on a user's device. It can be useful for organizations that want to train AI models without centralizing user data.

- [**Differential privacy**](https://link.springer.com/chapter/10.1007/978-3-540-79228-4_1) is a method of publicly sharing information about a dataset while keeping information about individuals in the dataset private. It does this by adding noise to the data before analysis.

There are several tools available to implement **federated learning** and **differential privacy:**

- [**TensorFlow Federated**](https://www.tensorflow.org/federated) (**TFF**) is an open-source framework developed by Google for implementing federated learning. It allows developers to train machine learning models on decentralized data using **TensorFlow**. **TFF** supports several types of federated learning, including horizontal and vertical federated learning.

- [**PySyft**](https://openmined.github.io/PySyft/index.html) is an open-source library built on top of **PyTorch** that allows for secure and privacy Policy-preserving machine learning. It implements federated learning, differential privacy, and multi-party computation. **PySyft** also provides tools for encrypting and decrypting data and performing secure computation on encrypted data.

- [**Federated learning simulation with JAX**](https://github.com/google/fedjax) (**FedJAX**) is a JAX-based open-source library for Federated Learning simulations that emphasizes ease-of-use in research.

Other techniques of data anonymization are data masking and data de-identification. Data masking hides sensitive information by replacing it with other characters or values. Meanwhile, data de-identification extracts identifiers, such as name, address, and social security number, from data. Data anonymization also hides personal identifiers and sensitive attributes from data through modification techniques such as **character shuffling**, **encryption**, and **word or character substitution**. Here are some tools to perform these anonymization techniques:

- [Informatica's Data Masking](https://www.informatica.com/in/#fbid=9vZBZqgVrvi).
- [IBM's Optim Data Masking](https://www.ibm.com/docs/en/iotdm).
- [ARX Data Anonymization](https://arx.deidentifier.org/).
- [Amnesia](https://amnesia.openaire.eu/).
- [Anonimatron](https://realrolfje.github.io/anonimatron/).

### Data Governance (**Data Mapping**)

Insufficient insight into massive data pools can lead to data hoarding and poorly managed data storage. Administrators may face a challenge when databases are too big: "_how to visualize what is happening in my database efficiently_." Data governance platforms or mapping tools can help administrators track and monitor data collection and efficiently use practices.

Data governance platforms are software tools that help organizations manage and govern their data. They allow organizations to establish policies and procedures for data management, including data collection, storage, and use. They also provide mechanisms to monitor compliance with these policies, such as data lineage and quality monitoring. Some examples of data governance platforms include:

- [Amundsen](https://www.amundsen.io/).
- [DataHub](https://datahub.io/)
- [Apache Atlas](https://atlas.apache.org/#/).

Data mapping tools visually represent the relationships between different data elements and their use across an organization. They map the data flow, identify data owners and stewards, and help create an understanding of the impact of data governance policies on data usage. Some examples of data mapping tools include:

- [Carto](https://carto.com/).
- [Talend Open Studio](https://www.talend.com/products/talend-open-studio/).
- [Karma](https://usc-isi-i2.github.io/karma/).

These tools track and monitor data collection and use practices and help organizations to ensure compliance with local regulations. Organizations can also build their data mapping tools. Languages like Python have a long list of data visualization libraries that can assist in the creation of informational dashboards, such as:

- [Dash](https://dash.plotly.com/).
- [Plotly](https://plotly.com/python/).
- [Seaborn](https://seaborn.pydata.org/).
- [Matplotlib](https://matplotlib.org/).
- [Pandas](https://pandas.pydata.org/).

### Privacy Policies

Privacy policies are a way to communicate to users how their data will be collected and used. Best practice privacy policies are available to all users and clearly specify the information being monitored (e.g., name, address, etc). You can use an online privacy policy generator to generate a privacy policy [here](https://www.privacypolicies.com/privacy-policy-generator/).

In the case that data is collected, consent forms should be used. For more information, follow the recommendations of your local [GDPR](https://www.gov.br/cidadania/pt-br/acesso-a-informacao/lgpd).
