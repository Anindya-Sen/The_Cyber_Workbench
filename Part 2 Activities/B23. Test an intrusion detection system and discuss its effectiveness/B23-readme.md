# B23. Test an intrusion detection system and discuss its effectiveness.


For this activity, I chose to test Suricata as an intrusion detection system (IDS) inside my Kali Linux virtual machine. I selected Suricata because it is a well-known open-source IDS and because I wanted to do something practical rather than only describe what an IDS is in theory. The main aim of the activity was to see how an IDS behaves in a real setup, how it is configured, what kind of output it produces, and then discuss how effective it actually feels in practice. I wanted this activity to match the instruction properly, so I made sure that I did not only install the tool, but actually ran it, generated traffic for it to inspect, reviewed the logs it created, and then evaluated the outcome.

I started from the beginning inside VirtualBox Kali Linux. First, I updated the package lists and installed Suricata through the terminal. After installation, I checked that it had installed properly by using the build information command. Once that was done, I updated the rule set using suricata-update, because I understood that an IDS is only as useful as the rules or detection logic it has available. After that, I checked the Suricata rules directory to make sure the rule file had been created successfully. I then identified the active network interface inside Kali using commands such as ip a and ip route, because Suricata needed to know which interface it should monitor. After finding the correct interface, I checked the main Suricata configuration file and verified that the rules path and rule file settings were correct.

Once the setup was ready, I ran a configuration test using Suricata’s test mode. This was an important step because it confirmed that the configuration file, rules, and interface settings were valid before I tried live monitoring. After the configuration test passed, I launched Suricata in live monitoring mode on the chosen network interface. At that point, Suricata was actively listening to traffic on the system. To test it, I opened a second terminal and generated safe network activity from my own virtual machine. I used normal traffic such as browsing, ping requests, and curl web requests, because I wanted to create traffic that Suricata could observe in a controlled and safe way. I then stopped Suricata and moved into the /var/log/suricata directory to inspect the logs it had created, especially eve.json, fast.log, and the general log files.

When I reviewed the results, I found that Suricata had clearly been running properly and processing traffic, because the log output contained event data and system statistics. In eve.json, I could see entries showing that traffic had been observed and processed, including background local network activity and Suricata status information. However, I did not get strong or obvious alert events in the alert logs for the traffic I had generated. In other words, the system was functioning, but the normal test traffic I produced did not trigger a clear intrusion alert. I found this useful rather than disappointing, because it showed me something realistic about intrusion detection systems: they do not automatically raise alarms just because traffic exists. They depend on what kind of traffic is being observed and whether it actually matches suspicious patterns or rules. This helped me understand that testing an IDS is not just about forcing an alert, but also about seeing how it behaves under ordinary conditions.

From an effectiveness point of view, I would say that Suricata was still effective in some important ways, but also showed clear limitations. One major strength is that it gives very detailed visibility into traffic and produces structured logs that can be reviewed later. I could see that it was active, that it captured network-related information, and that it maintained useful records in files like eve.json. That is valuable because an IDS is not only about dramatic alerts; it is also about visibility, logging, and giving administrators evidence that can be analysed. Another strength is that Suricata felt like a serious and capable tool, and once it was set up properly, it gave a much more professional view of network monitoring than a simple traffic test alone would.

At the same time, the activity also showed me some of its limitations. Suricata was not beginner-friendly at first, because there were several setup steps involved, such as installing the software, updating rules, confirming the configuration, identifying the correct interface, and understanding which logs actually mattered. Another important limitation is that its effectiveness depends heavily on the type of traffic being tested and on the available rules. In my test, because the traffic was mostly normal and safe, it did not generate clear alerts, which means that simply running the IDS is not enough to guarantee visible detection results. This made me realise that an IDS may be working correctly even when it does not immediately show obvious alerts, and that interpreting its output requires patience and understanding rather than expecting instant dramatic results.

Overall, I think this activity fulfilled the task very well because I did not just describe an intrusion detection system in theory — I actually tested Suricata myself inside Kali Linux, went through the installation and configuration process, ran it in live mode, generated traffic for it to inspect, reviewed its output, and then discussed how effective it was. The outcome taught me that an IDS like Suricata can be very useful for monitoring and visibility, but that its value depends on proper setup, suitable rules, and meaningful traffic for testing. Even though I did not get strong alert events from my safe traffic, the activity was still successful because it gave me a realistic understanding of how an intrusion detection system operates in practice and what its strengths and weaknesses look like in a real environment.





![Tailgating example](B23-%201.suricata%20installed%20properly.png)

**Figure: Suricata installation**



![Tailgating example](B23-%202.suricata%20update.png)

**Figure: Suricata successful update**




![Tailgating example](B23-%203.my%20network%20interface.png)

**Figure: my network interface**




![Tailgating example](B23-%204.suricata%20configuration%20test%20passed.png)

**Figure: Suricata configuration test**





![Tailgating example](B23-%205.suricata%20running%20live.png)

**Figure: Suricata running live**





![Tailgating example](B23-%206.suricata%20traffic%20generated.png)

**Figure: Traffic generated to test Suricata**





![Tailgating example](B23-%207.suricata%20Alert%20output%20from%20eve.json.png)

**Figure: Suricata Alert output from “eve.json”**
