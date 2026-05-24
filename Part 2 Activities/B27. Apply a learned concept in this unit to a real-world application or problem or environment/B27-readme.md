# B27. Apply a learned concept in this unit to a real-world application/problem/environment.


For this activity, I applied the cybersecurity concept of data classification to a real-world environment by creating a custom GPT inside ChatGPT that helps classify information based on sensitivity. I chose this concept because throughout the unit, it became clear to me that cybersecurity is not only about stopping attackers, but also about understanding what kind of data is being handled, how sensitive it is, and how it should be protected. In real workplaces, especially in companies dealing with clients, proposals, internal documents, screenshots, and digital files every day, one of the easiest ways to create security and privacy problems is by not knowing what information is safe to share and what information needs stronger protection. Because of that, I wanted to apply the idea of data classification to a practical environment by building something that could actually assist with that decision-making process instead of leaving it only as theory.

To do this, I created a custom GPT in ChatGPT and designed it to act as a Data Classification Assistant. The purpose of the GPT was to take text, screenshots, and other content and classify them into labels such as Public, Internal, Confidential, or Highly Sensitive / Restricted. I did not want it to simply give a label and stop there, so I designed it to work in a more structured way. I configured it so that whenever a user gives it content, it first looks for sensitive indicators such as names, email addresses, phone numbers, financial information, client data, source code, API keys, internal strategy, contracts, or other information that should not be exposed casually. After identifying those indicators, it then gives a classification label, explains why that label fits, points out what sensitive elements were found, and suggests how that information should be handled. In this way, the GPT was not only classifying data, but also helping the user understand the reasoning behind the classification, which made it much more useful as a real-world security support tool.

What made this activity a true application of a learned concept is that I did not just create the GPT once and leave it there. I treated it more like a real security solution that needed testing and refinement. After creating the initial version, I tested it repeatedly with different kinds of examples, including clearly public information, internal notes, confidential client-style material, screenshots, and highly sensitive items such as credentials or financial details. Through those tests, I noticed that some results were too broad, some were too relaxed, and some needed clearer judgment when screenshots were involved. Because of that, I went back into the GPT instructions again and again and improved its behaviour after each round of testing. For example, I strengthened the rules around screenshots so that it would pay closer attention to browser tabs, side panels, usernames, notifications, file names, and meeting links. I also made the instructions stricter for things like passwords, API keys, tokens, banking details, and client information so that the GPT would classify them more cautiously. This repeated reconfiguration was one of the most important parts of the activity, because it showed that applying a cybersecurity concept in practice is not just about building something once, but about improving it until it becomes more accurate and reliable.

I also made the GPT more effective by giving it a clear workflow to follow every time. Instead of allowing it to answer in a loose or inconsistent way, I configured it to always return its result in a structured format: the classification, the sensitive indicators found, the reason for the classification, a handling recommendation, and a confidence level. This made the tool more consistent and much easier to use. I found that this step was very important because even a good idea can become unreliable if the output style keeps changing. By forcing the GPT into a clearer decision structure, the classification process became more disciplined and closer to how a real company might want such a tool to behave.

Overall, I found this activity extremely meaningful because it allowed me to take a concept from the unit and apply it to a realistic modern environment in a practical way. Rather than only writing about data classification in theory, I turned it into a working tool that could help people think more carefully about what kind of information they are handling. The real-world application here was very clear: in any workplace, and especially in client-facing or AI-related environments, misclassifying information can lead to privacy leaks, oversharing, and poor security decisions. By creating and refining this GPT, I was able to apply the unit concept directly to that problem. I think this matched the activity very well because it showed not only that I understood the concept, but that I could also use it to build something practical, test it, improve it, and apply it to a real-world cybersecurity need.




![Tailgating example](B27-%201.GPT%20creation.png)

**Figure: Creation of the GPT**




![Tailgating example](B27-%202.1-response.png)

**Figure: Response 1**



![Tailgating example](B27-%202.2-response.png)

**Figure: Response 2**






GPT created: https://chatgpt.com/g/g-6a12da2ad9948191a0aa6eb97a9770fb-data-classification-assistant
