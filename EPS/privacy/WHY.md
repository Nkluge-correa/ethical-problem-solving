# What is Privacy? 🔎

_5-minute read_

Privacy is essential in developing AI applications for two crucial reasons. Firstly, increased privacy protects against cybercrimes such as identity theft or financial fraud. Secondly, privacy encourages public trust in AI systems. However, AI privacy differs from general data privacy because of the peculiarities involved in training state-of-the-art ML models, which are highly data-hungry, among other quirks characteristic of ML.

According to [Worldwide AI Ethics](https://nkluge-correa.github.io/worldwide_AI-ethics/), privacy is the notion that:

> "_the individual's right to "expose oneself voluntarily, and to the extent desired, to the world." In AI ethics, this principle upholds the right of a person to control the exposure and availability of personal information when mined as training data for AI systems. This principle is also related to concepts such as data minimization, anonymity, informed consent, and other data protection-related concepts_."

AI privacy demands that the public be protected by built-in privacy safeguards, data minimization, use, and collection constraints. Any automated system that collects, uses, shares, or stores personal data should meet these standards. One precise measure to evaluate the impact level of an AI-empowered application regarding privacy is the use and collection of _sensitive data_.

However, what is the difference between _personal_ and _sensitive_ data?

- **Personal Data:** _Personal data can be thought of as information that can be used to identify an individual, like an address, a name, a social security number, etc._

- **Sensitive Data:** _Sensitive data is personal data considered more private or sensitive than other types of personal data. It may include information such as an individual's financial, medical, or personal history. Sensitive data can also be information that can be used to characterize an individual into specific target groups, like gender, ethnicity, race, etc._

The specific types of sensitive data can vary depending on the context and the applicable laws and regulations. For example, financial information may be more sensitive in some countries than medical information, while the opposite may be true in others. Usually, the local data protection regulation ([**GDPR**](https://www.gov.br/cidadania/pt-br/acesso-a-informacao/lgpd)) can guide on what types of data demand greater rigor and how to handle them ethically.

There are several ways to approach privacy in the development of AI applications:

- **Privacy by design:** AI systems should be designed with privacy in mind from the outset. This may entail employing approaches such as differential privacy or federated learning.

- **Consent:** Obtaining permission from individuals before collecting or using their data is crucial. Clear and transparent privacy policies and consent forms settle this issue.

- **Anonymization:** Anonymizing data, or removing personally identifiable information, protects individuals while providing the data necessary for AI applications.

- **Data minimization:** Only collecting and using the minimum personal data necessary usually improves compliance with local regulatory demands.

- **Data governance:** Establishing explicit policies and processes for collecting, using, and sharing personal data can help ensure that AI applications comply with people's right to privacy.

- **Third-Party Audits:** An independent evaluation to ensure that organizations effectively manage and safeguard personal data in compliance with relevant laws and ethical standards.

Overall, protecting the privacy of individuals is vital for the legal compliance, customer trust, reputation, and innovation of enterprises. Something that can help them maintain and sustainably grow.

## Why Should You Care? 🤔

The pervasive integration of surveillance and data collection is now at the heart of many business models, with organizations tracking public behavior, creating individual profiles, and using this granular-level information as input into automated systems designed to influence behavior.

Data brokers (e.g., Google, Meta, Microsoft, etc.) play a significant role by amassing vast amounts of personal information in this landscape. The collected information is often traded or sold, contributing to a network of data exchanges. For the user or consumer, opting out of data brokers and managing personal data is frequently challenging.

Privacy policies throughout applications are usually presented in a way that is not friendly to the general public. At the same time, certain UX features, like cookies, third-party or not, are often "sold" as necessary to enable the application functionality. These are some of the overall challenges of the field, and the following cases underline the problems associated with data privacy regarding the general public.

### TikTok Security Concerns

TikTok, a short-form video application, became popular among teenagers worldwide in 2019.

The app collects user data to accurately curate content for users' "for you" pages. However, in the past few years, TikTok was discovered to spy on high-profile US journalists and track data of [non-TikTok users](https://www.consumerreports.org/electronics-computers/privacy/tiktok-tracks-you-across-the-web-even-if-you-dont-use-app-a4383537813/).

Although, in TikTok's case, some data collection is necessary to improve the system's accuracy, the scope of the collection and severe security concerns raised alarm bells in several countries, most notably the US. Since then, other companies have implemented similar short-form video features, such as YouTube's [shorts](https://www.youtube.com/creators/shorts/), Instagram's [reels](https://about.instagram.com/blog/announcements/introducing-instagram-reels-announcement), and Snapchat's [stories](https://www.snapchat.com/discover). It is still unknown if such platforms perform the same type of user monitoring TikTok utilized.

### Cambridge Analytica

[Cambridge Analytica](https://ieeexplore.ieee.org/document/8436400), founded in 2013, was a company that combined predictive and classification techniques to support strategic communication during election processes. Cambridge Analytica took part in more than 44 election processes worldwide and has been the subject of several criminal investigations in the United States of America and the United Kingdom.

The company collected personal data from over 50 million Facebook, Google, Twitter, Instagram, and WhatsApp profiles, and the data was allegedly used to create psychological profiles of users, which were then utilized for targeted political advertising. Cambridge Analytica was accused of using this information to influence voter behavior in various political campaigns, including the 2016 US presidential election and the Brexit referendum.

## Final Remarks

The public should be free from unchecked data collection and surveillance; these technologies should be subject to heightened oversight that includes at least an assessment of their potential harms and scope to protect its users' privacy and civil liberties. Traditional terms of service —_the block of text users are accustomed to navigating through when using a website or digital app_— are insufficient for preserving privacy.

## Extra Reading

- Lei Nº 13.709. _[Lei Geral de Proteção de Dados](https://lgpd-brazil.info/)_. 2018.
- European Data Protection Supervisor. [European Commission's GDPR Review: stronger European solidarity for the enforcement of the GDPR](https://edps.europa.eu/press-publications/press-news/press-releases/2020/european-commissions-gdpr-review-stronger_en). _Online_, 2020.
- Kateifides, A. _et al._ [Comparing privacy laws: GDPR v. LGPD](https://www.dataguidance.com/sites/default/files/gdpr_v_lgpd_revised_edition.pdf), 2018.
- The White House. [Blueprint for AI Bill of Rights](https://www.whitehouse.gov/ostp/ai-bill-of-rights/#discrimination). _Online_, 2022.
- Singapore Government Agency Website. [Singapore's Personal Data Protection Commission](https://www.pdpc.gov.sg/). _Online._
- Singapore Government Agency Website. [Advisory Guidelines on Key Concepts in the Personal Data Protection Act](https://www.pdpc.gov.sg/guidelines-and-consultation/2020/03/advisory-guidelines-on-key-concepts-in-the-personal-data-protection-act). _Online_. ([PDF here](https://www.pdpc.gov.sg/-/media/Files/PDPC/PDF-Files/Advisory-Guidelines/AG-on-Key-Concepts/Advisory-Guidelines-on-Key-Concepts-in-the-PDPA-17-May-2022.pdf)).
- Singapore Government Agency Website. [Guide to Data Protection by Design for ICT Systems](https://www.pdpc.gov.sg/help-and-resources/2019/05/guide-to-data-protection-by-design-for-ict-systems). _Online_.   ([PDF here](https://www.pdpc.gov.sg/-/media/Files/PDPC/PDF-Files/Other-Guides/Guide-to-Data-Protection-by-Design-for-ICT-Systems-(310519).pdf))
- Singapore Government Agency Website. [Guide to Data Protection Impact Assessments](https://www.pdpc.gov.sg/help-and-resources/2017/11/guide-to-data-protection-impact-assessments). _Online_. ([PDF here](https://www.pdpc.gov.sg/-/media/Files/PDPC/PDF-Files/Other-Guides/DPIA/Guide-to-Data-Protection-Impact-Assessments-14-Sep-2021.pdf)).
- [Introduction to the study of Cryptography (with Python)](https://www.tutorialspoint.com/cryptography_with_python/cryptography_with_python_quick_guide.htm). _Online_. ([PDF here](https://www.tutorialspoint.com/cryptography_with_python/cryptography_with_python_tutorial.pdf)).
