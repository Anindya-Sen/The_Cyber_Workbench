# A26- Research and implement a system bug.


For this activity, I researched and implemented a fix for a registration-form bug based on a real issue I came across while joining the UCC (University Computer Club) at UWA. During the registration process, the form first asked for my given name, so I entered my first name there. After that, it asked for any other name. I did not have any other name to enter in that sense, although I do have a surname/family name, but the form did not ask for that separately. When I tried to continue without filling in the “other name” field, the system treated it as compulsory. Since I had nothing suitable to enter there, I wrote “N/A” just to move forward. After registration, my name appeared incorrectly as “Anindya N/A.” From a system-design point of view, this showed two clear bugs: first, the form validation forced users to enter data into a field that should have been optional, and second, the system displayed that placeholder text as if it were part of the real name.
After thinking about the problem properly, I realised that the issue was not only a bad label on the form, but also poor validation logic and poor name formatting logic. A better design would separate the name into fields such as given name, surname/family name, and an optional other name/middle name field. The bug could be reduced by making only the essential fields compulsory and allowing optional fields to remain empty. For example, the validation logic should look more like this.

**A26(Code Interraction Attachment 2)- Code snippet 1 for improvement.txt**

This fixes the first problem because it stops the system from forcing users to enter meaningless placeholder values such as “N/A” just to pass validation. In my view, this is a much better design because it matches how names are actually structured and avoids collecting false data.
The second part of the bug was how the system displayed the final name. The old behaviour likely joined every field directly without checking whether the value was meaningful. That is why “Anindya N/A” appeared. A better implementation would only combine fields that contain real data and ignore placeholders or blank optional fields. For example.

**A26(Code Interraction Attachment 2)- Code snippet 2 for improvement.txt**

This solves the display issue because the system no longer treats placeholder text as part of the official name. If the optional field is empty, it is simply skipped. If someone had a real middle name or second given name, it could still be included correctly. This makes the name output cleaner, more accurate, and much more user-friendly.
I also thought about how the form itself could be improved from the front-end side, because part of the confusion came from the wording of the fields. The label “any other name” is unclear and can easily confuse users. A clearer version would explicitly mark the field as optional and explain what it means. This small interface change would already reduce a lot of confusion, because the user can clearly understand which fields are required and which ones are optional. In my opinion, this is a good example of how even a small system bug can affect real users and create poor-quality stored data. What I found most useful about this activity is that it showed me that fixing a bug is not only about correcting code. It is also about understanding the user’s situation, improving the logic behind the form, and making the interface clearer so the same mistake does not happen again.


### *Evidences attached on this Github Repository sub-folder*
