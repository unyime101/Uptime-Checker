# 📡 Router Uptime Monitor

📌 **Project Overview** 
I'm building a Python-based uptime monitor that runs on my Raspberry Pi 5 to track the availability of my home router.

As a university student, I'm often away from home — but I still get contacted whenever devices lose internet connectivity. This tool is meant to help me monitor the router's status so I can keep tabs on connection health and understand recurring issues remotely.

The script is being developed to run on Ubuntu Linux (on Raspberry Pi) but will be portable to other Linux environments.

---

🚧 **Current Progress**

| Area                          | Status        | Notes                                                                |
|-------------------------------|---------------|----------------------------------------------------------------------|
| Python ping monitoring script| 🚧 In Progress | Writing script to ping router and track status                       |
| Logging to text file         | 🚧 In Progress | Adding basic logging for uptime and downtime                         |
| Optional Cron automation     | 🚧 In Progress | Will run script every 3 hours, on login, and on boot                 |
| Alert thresholds             | 🔜 Planned     | Will add uptime limit warnings and router-down detection             |
| Email alert system           | 🔜 Planned     | Secure alerts via SMTP with `.env` variables                         |
| Project documentation        | 🚧 In Progress | Writing this README and usage instructions                           |
| Git setup with .gitignore    | 🚧 In Progress | Setting up repo to exclude logs and secrets                          |
| GitHub publishing            | 🔜 Planned     | Repo will be pushed and maintained on GitHub                         |
| optional Grafana logging     | 🔜 Planned     | Will integrate for better visualization of uptime metrics            |
| Docker/Kubernetes deployment | 🔜 Planned     | Containerization and deployment via Minikube for DevOps practice     |

---

📊 **Features (Planned/Building)**

🛠️ Pings router IP 
🛠️ Logs timestamps and connectivity status 
🛠️ Tracks total uptime in readable format 
🛠️ Can be scheduled via `cron` 
🛠️ Runs on boot, user login, and every 3 hours
🛠️ Will support email alerts when router is down or uptime exceeds a threshold
🛠️ Portable across Raspberry Pi and Linux machines
🛠️ Logs and credentials excluded from GitHub repo

---

🧠 **Learning Goals**

- Learn some networking skills and commands
- Understanding how to automate tasks and monitor even when im not home
