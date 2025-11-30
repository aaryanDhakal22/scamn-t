🛡️ Phishing Flooder — Defensive Automation Against a Real-World Attack

(Created after a family phishing incident)

📌 Overview

In late 2019, my cousin’s Facebook account was compromised as part of a serial phishing attack.
The attacker used the hacked account to message all friends:

“Look at this funny image 😂”
(with a fake but very convincing Facebook-lookalike login page)

Because the domain looked legitimate, multiple people entered their credentials — but fortunately, none of our mutual friends were hacked afterward.

During the recovery process, I built this small defensive script whose sole purpose was to:

✔️ Send randomized, useless login data to the attacker’s phishing form
✔️ Pollute their database with garbage
✔️ Force higher operational cost, ideally encouraging them to drop/reset the stolen-credential table

This does not hack anything, does not break into systems, and works only on open phishing webforms already exposed to the public.

It simply automates typing fake credentials into the phishing page.

⚠️ Disclaimer
This project is for educational and defensive cybersecurity awareness only.
Do not use it against legitimate systems. Automation against phishing sites is allowed only when the malicious form is already publicly accessible.
I am not responsible for any misuse.

🎯 Purpose

This script was created strictly for phishing response mitigation after a real attack.
The goals were:

Demonstrate how automation can protect less technical users

Provide a way to pollute malicious datasets

Show that a few lines of Python can disrupt low-effort cybercriminal operations

Encourage friends/family to understand and recognize phishing attempts

🧠 How It Works

The phishing page was just a simple username/password form.
This script:

Waits 3 seconds so the user can switch to the phishing tab

Randomly picks names + passwords from local text files

Types them into the fake login form using pyautogui

Repeats the process 100 times

Navigates back and continues the loop

It’s essentially a “credential spammer” that overloads the attacker with meaningless data.

📁 Files

main.py — Main automation script

names.txt — List of fake usernames

pass.txt — List of throwaway passwords

(All sample data must be non-sensitive.)

🧾 Lessons Learned

Even convincing phishing websites can be identified by inspecting the URL.

Automation isn’t just for developers — it can be used to defend family and friends.

Flooding malicious data collection points is a surprisingly effective method to reduce impact of credential theft.

Teaching non-technical users to spot suspicious links is the best long-term defense.

🛡️ Final Note

I don’t know how much of the prevention was due to this script — but none of our mutual friends were hacked afterward, and that alone made the effort worth it.

If this script helps someone else understand phishing attacks better, or encourages them to build their own defensive automation, then the project has done its job.
