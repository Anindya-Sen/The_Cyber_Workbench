# B25. Design and implement a threat intelligence module of your choice.


For Activity B25, I designed and implemented a simple threat intelligence module called an IOC Checker using Python. IOC stands for Indicator of Compromise, which is information that may suggest suspicious or malicious activity. Examples include suspicious IP addresses, domain names, URLs, and file hashes. I chose an IOC checker because it is a practical example of how threat intelligence is used in cybersecurity. Instead of only explaining the concept, I created a working tool that checks whether a suspicious indicator appears in a known list.

The main purpose of my module was to help a user quickly check an IP address, domain, URL, or file hash against a small threat intelligence database. I created this database inside the Python script, with sample malicious indicators grouped into categories such as IPs, domains, URLs, and hashes. When the user enters an indicator, the program checks it against the correct category and reports whether it was found.

The module works in a simple process. First, the user enters an IOC into the program. The program then uses pattern matching to identify what type of IOC it is. For example, 185.220.101.32 is recognised as an IP address, malicious-example.com is recognised as a domain, and a long hexadecimal value can be recognised as a file hash. This step is important because the program needs to know which part of the database to check.

After identifying the IOC type, the program compares the input with the matching threat intelligence list. If the IOC appears in the database, the program reports “MALICIOUS / FOUND”. If it does not appear, it reports “Not found in IOC database”. I also added a response for invalid inputs, so if the user enters something that is not recognised as an IP address, domain, URL, or hash, the program returns “Invalid or unsupported IOC format”.
I tested the module using different inputs to make sure it worked properly. When I entered a known suspicious IP address such as 185.220.101.32, the program correctly detected it as an IP address and marked it as malicious. When I entered a normal domain such as google.com, the program recognised it as a domain but reported that it was not found in the IOC database. This showed that the program does not blindly mark every input as dangerous. It only flags indicators that match the known IOC list.

During testing, I improved the output to make it clearer. Instead of only showing whether an IOC was found, the program now displays the original IOC, its detected type, and its final status. This makes the result easier to understand and more useful for a basic security investigation.

This activity helped me understand that threat intelligence is not just about collecting security information. It is about using that information to support investigation and decision-making. My IOC checker shows how suspicious indicators can be checked quickly against known threat data. Although the tool is simple, it follows the same basic idea used in real security environments: identify the indicator, compare it with known malicious data, and produce a clear result.

One limitation of my module is that it uses a small built-in database instead of a live threat intelligence feed. In a real environment, IOC lists would usually be updated from external security sources. Another limitation is that the module only checks for exact matches, so an indicator written in a different format may not be detected. However, for this activity, the module successfully demonstrates the basic purpose of a threat intelligence system in a simple and practical way.

Overall, I designed and implemented a Python-based IOC checker that can check IP addresses, domains, URLs, and file hashes against a known IOC list. The module identifies the type of IOC, compares it with the correct database category, and gives a clear result. This helped me apply threat intelligence in a practical way and understand how IOC checking can support cybersecurity investigations.



### **Python Script Evidence on Github**

