# AIA - Consumer Rights

You will find all the questions for our impact assessment on **consumer rights** here. All questions are stored as YAML files. These specification files are structured as shown below:

```yaml
question: "The question you wish to implement."
multiple: false # If is not multiple choice, else, `true`.
options: 
  - Option 1
  - Option 2
  - Option 3
scores: # The number of options and respective scores should match, and be in the same order.
  - 1.0
  - 2.0
  - 3.0
principle1: true # If this question evaluates this principle, else, `false`.
principle2: true
principle3: true
information: "An informative that may help the user understand the question." # If no information is to be given, set the value to `null`.
```

You can create as many questions as you want. Only remember that this demo will display them in ascending order, using their number as a sorting key.
