# 📡 Router Uptime Monitor

📌 **Project Overview** 
I'm building a Python-based uptime monitor that runs on my Raspberry Pi 5 to track the availability of my home router.

As a university student, I'm often away from home — but I still get contacted whenever devices lose internet connectivity. This tool is meant to help me monitor the router's status so I can keep tabs on connection health and understand recurring issues remotely.

The script is being developed to run on Ubuntu Linux (on Raspberry Pi) but will be portable to other Linux environments.

---

🚧 **Current Progress**

| Area                          | Status         | Notes                                                                |
|-------------------------------|----------------|----------------------------------------------------------------------|
| Python ping monitoring script | ✅Completed    | Written a script to ping router and track status                     |
| Logging to text file          | ✅Completed    | Added basic logging for uptime and downtime                          |
| Optional Cron automation      | ✅Completed    | Will run script every 3 hours, on login, and on boot                 |
| Email alert system            | ✅Completed    | Secure alerts via SMTP with `.env` variables                         |
| Project documentation         | ✅Completed    | Writing this README and usage instructions                           |
| Git setup with .gitignore     | ✅Completed    | Setting up repo to exclude logs and secrets                          |
| GitHub publishing             | ✅Completed    | Repo will be pushed and maintained on GitHub                         |
| optional Grafana logging      | 🔜 Planned     | Will integrate for better visualization of uptime metrics            |
| Docker/Kubernetes deployment  | 🔜 Planned     | Containerization and deployment via Minikube for DevOps practice     |

---

📊 **Features (Planned/Building)**

✅ Pings router IP. Resources used to studying network pinging: https://how.dev/answers/how-to-ping-multiple-ip-addresses-using-python-script
 
✅ Logs timestamps and connectivity status 

✅ Can be scheduled via `cron` 

✅ Runs on boot and every 3 hours

✅ Will support email alerts when router is down 

✅ Portable across Raspberry Pi and Linux machines

✅ Logs and credentials excluded from GitHub repo

---

🧠 **Learning Goals**

- Learn some networking skills and commands
- Understanding how to automate tasks and monitor even when im not home
- Really starting to understand how gitignores and .env files are useful in development
