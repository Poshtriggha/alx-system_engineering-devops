Postmortem: Web Stack Outage Incident

Issue Summary:

Duration: February 16, 2024, 08:30 AM - 12:45 PM (UTC)
Impact: The outage affected the core authentication service, resulting in a 30% degradation of user access, leading to login failures and slowed response times.
Root Cause: The issue originated from an unanticipated surge in authentication requests overwhelming the system due to a misconfigured load balancer.
Timeline:

08:30 AM: Issue detected through monitoring alerts indicating a sudden spike in authentication errors.
08:35 AM: Initial assumption focused on database issues; investigation began into database servers and connection pools.
09:15 AM: Database servers were ruled out; attention shifted to load balancer configuration.
10:00 AM: Misleading path - load balancer logs indicated normal traffic; attention diverted to application servers.
11:00 AM: Realization that the load balancer misconfiguration caused uneven distribution of requests among application servers.
11:30 AM: Incident escalated to the System Reliability Engineering (SRE) team for specialized support.
12:45 PM: Load balancer configuration adjusted to evenly distribute authentication requests; service restored to normalcy.
Root Cause and Resolution:

Root Cause: The misconfiguration of the load balancer led to an uneven distribution of authentication requests among application servers. This created a bottleneck, resulting in login failures and slowed response times.
Resolution: The load balancer configuration was corrected to evenly distribute incoming authentication requests. This relieved the stress on the system and restored normal service functionality.
Corrective and Preventative Measures:

To Improve/Fix:
Enhanced Monitoring: Implement real-time monitoring for load balancer metrics to quickly identify irregularities.
Load Testing: Regularly conduct load testing to simulate traffic spikes and ensure the system can handle increased loads.
Automated Alerts: Set up automated alerts for specific load balancer thresholds to proactively identify potential issues.
Tasks to Address the Issue:
Load Balancer Review: Conduct a comprehensive review of load balancer configurations to identify and correct any potential misconfigurations.
Documentation Update: Update documentation to include clear guidelines for load balancer configuration changes, ensuring future changes follow best practices.
Training: Provide additional training for the operations team on load balancer management and troubleshooting techniques.
Post-Incident Review: Schedule a post-incident review with the SRE team to analyze the incident response and identify areas for improvement.
