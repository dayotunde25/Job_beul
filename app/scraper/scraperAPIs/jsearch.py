import requests

url = "https://jsearch.p.rapidapi.com/search"

querystring = {"query":"","page":"1","num_pages":"1","date_posted":"3days"}

headers = {
	"x-rapidapi-key": "b85e43b376msh24baf6ffbcfeeb3p14438ajsn3a55fc11c03d",
	"x-rapidapi-host": "jsearch.p.rapidapi.com"
}

response = requests.get(url, headers=headers, params=querystring)

print(response.json())



{
  "status": "OK",
  "request_id": "e0ce4e30-9640-413f-9fa2-a8e1f681cecc",
  "parameters": {
    "query": "cyber security",
    "page": 1,
    "num_pages": 1,
    "date_posted": "3days",
    "country": "us",
    "language": "en"
  },
  "data": [
    {
      "job_id": "xWxRT0mZoH8S__eTAAAAAA==",
      "job_title": "Counterintelligence Cyber SME with Security Clearance",
      "employer_name": "Deck Prism, LLC",
      "employer_logo": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcT3JR89UJ84bSDU4vLt4kKnTG4x8uZwHj4729rj&s=0",
      "employer_website": null,
      "job_publisher": "LinkedIn",
      "job_employment_type": "Full-time",
      "job_employment_types": [
        "FULLTIME"
      ],
      "job_apply_link": "https://www.linkedin.com/jobs/view/counterintelligence-cyber-sme-with-security-clearance-at-deck-prism-llc-4293789319?utm_campaign=google_jobs_apply&utm_source=google_jobs_apply&utm_medium=organic",
      "job_apply_is_direct": false,
      "apply_options": [
        {
          "publisher": "LinkedIn",
          "apply_link": "https://www.linkedin.com/jobs/view/counterintelligence-cyber-sme-with-security-clearance-at-deck-prism-llc-4293789319?utm_campaign=google_jobs_apply&utm_source=google_jobs_apply&utm_medium=organic",
          "is_direct": false
        },
        {
          "publisher": "Teal",
          "apply_link": "https://www.tealhq.com/job/cyber-security-sme-ts-sci_27229f35-db43-4cc6-84c6-f051ccc94713?included_keywords=jafan&page=9&utm_campaign=google_jobs_apply&utm_source=google_jobs_apply&utm_medium=organic",
          "is_direct": false
        },
        {
          "publisher": "BeBee",
          "apply_link": "https://us.bebee.com/job/aafd18d80d696943f59fe9b61d092354?utm_campaign=google_jobs_apply&utm_source=google_jobs_apply&utm_medium=organic",
          "is_direct": false
        },
        {
          "publisher": "Jobg8",
          "apply_link": "https://jobs.jobg8.com/jobs/counterintelligence-cyber-sme-with-security-clearance-in-washington-washington-dc-united-states/5673-2996496581C5?utm_campaign=google_jobs_apply&utm_source=google_jobs_apply&utm_medium=organic",
          "is_direct": false
        },
        {
          "publisher": "Sologig",
          "apply_link": "https://www.sologig.com/job/J3V7P56Y90QYVTNZ8XB?utm_campaign=google_jobs_apply&utm_source=google_jobs_apply&utm_medium=organic",
          "is_direct": false
        },
        {
          "publisher": "Jobilize",
          "apply_link": "https://www.jobilize.com/job/us-dc-washington-industrial-security-policy-sme-ts-sci-clearance-jobs?utm_campaign=google_jobs_apply&utm_source=google_jobs_apply&utm_medium=organic",
          "is_direct": false
        }
      ],
      "job_description": "Desired, senior level cyber SME that has experience supporting CI investigations. Experience with hardware and software computer forensics, especially in support of investigations is ideal. Experience conducting analysis of adversary cyber threats against US networks or Insider threat is relevant as well. Individual must have minimum of fifteen years of experience in conducting complex CI program activities with a federal agency such as the DOE, FBI, CIA or DOD. Candidate must possess experience conducting interviews, and research. This may be a combination of private sector, civil service, or military experience. Individual must display maturity in assessing issues and communicating with individuals of varying levels of responsibility and management; have the ability to identify counterintelligence and foreign intelligence indicators; review inspectable data and information that involves cross-checking, analyzing, and interpreting relevant information. Individual must have excellent team-building, liaison, oral and written communication skills and proven ability to perform under pressure. Additionally, the individual must have the ability to respond to specific tasks driven by mission requirements; ability to conduct professional interviews; ability to assess/integrate the implications of data for the inspections being conducted. Candidate will be expected to have knowledge of the requirements for developing a CI program. This Cyber CI: Position requires individual to have earned a Bachelor’s Degree from an accredited university or college. An Advanced Degree in a relevant technical field is desirable. Individual must have conducted cyber counterintelligence investigations as a primary case agent for a federal agency such as the DOE, FBI, CIA or DOD.",
      "job_is_remote": false,
      "job_posted_at": "2 days ago",
      "job_posted_at_timestamp": 1756598400,
      "job_posted_at_datetime_utc": "2025-08-31T00:00:00.000Z",
      "job_location": "Washington, DC",
      "job_city": "Washington",
      "job_state": "District of Columbia",
      "job_country": "US",
      "job_latitude": 38.9071923,
      "job_longitude": -77.0368707,
      "job_benefits": null,
      "job_google_link": "https://www.google.com/search?q=jobs&gl=us&hl=en&udm=8#vhid=vt%3D20/docid%3DxWxRT0mZoH8S__eTAAAAAA%3D%3D&vssid=jobs-detail-viewer",
      "job_salary": null,
      "job_min_salary": null,
      "job_max_salary": null,
      "job_salary_period": null,
      "job_highlights": {
        "Qualifications": [
          "Experience with hardware and software computer forensics, especially in support of investigations is ideal",
          "Experience conducting analysis of adversary cyber threats against US networks or Insider threat is relevant as well",
          "Individual must have minimum of fifteen years of experience in conducting complex CI program activities with a federal agency such as the DOE, FBI, CIA or DOD",
          "Candidate must possess experience conducting interviews, and research",
          "This may be a combination of private sector, civil service, or military experience",
          "Individual must display maturity in assessing issues and communicating with individuals of varying levels of responsibility and management; have the ability to identify counterintelligence and foreign intelligence indicators; review inspectable data and information that involves cross-checking, analyzing, and interpreting relevant information",
          "Individual must have excellent team-building, liaison, oral and written communication skills and proven ability to perform under pressure",
          "Additionally, the individual must have the ability to respond to specific tasks driven by mission requirements; ability to conduct professional interviews; ability to assess/integrate the implications of data for the inspections being conducted",
          "Candidate will be expected to have knowledge of the requirements for developing a CI program",
          "This Cyber CI: Position requires individual to have earned a Bachelor’s Degree from an accredited university or college",
          "Individual must have conducted cyber counterintelligence investigations as a primary case agent for a federal agency such as the DOE, FBI, CIA or DOD"
        ]
      },
      "job_onet_soc": "55301900",
      "job_onet_job_zone": null
    },
    {
      "job_id": "wBapOcGrz4KMAv9gAAAAAA==",
      "job_title": "Palo Alto Cyber Security Engineer, Mid",
      "employer_name": "BOOZ, ALLEN & HAMILTON, INC.",
      "employer_logo": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRA6_xjmivev1fdSnDkygDVA7J2Ajz2DDD6Gwj-&s=0",
      "employer_website": null,
      "job_publisher": "Indeed",
      "job_employment_type": "Full-time",
      "job_employment_types": [
        "FULLTIME"
      ],
      "job_apply_link": "https://www.indeed.com/viewjob?jk=1f2e44a5df8c9076&utm_campaign=google_jobs_apply&utm_source=google_jobs_apply&utm_medium=organic",
      "job_apply_is_direct": false,
      "apply_options": [
        {
          "publisher": "Indeed",
          "apply_link": "https://www.indeed.com/viewjob?jk=1f2e44a5df8c9076&utm_campaign=google_jobs_apply&utm_source=google_jobs_apply&utm_medium=organic",
          "is_direct": false
        },
        {
          "publisher": "SimplyHired",
          "apply_link": "https://www.simplyhired.com/job/1PXF57qUel_bdTMd8OhastgkNtjhx13SJVeedkwYun_LEKFiNYvrFg?utm_campaign=google_jobs_apply&utm_source=google_jobs_apply&utm_medium=organic",
          "is_direct": false
        },
        {
          "publisher": "Women For Hire- Job Board",
          "apply_link": "https://jobs.womenforhire.com/job/usa/washington-dc/palo-alto-cyber-security-engineer-mid-718744/?utm_campaign=google_jobs_apply&utm_source=google_jobs_apply&utm_medium=organic",
          "is_direct": false
        },
        {
          "publisher": "Jobcase",
          "apply_link": "https://www.jobcase.com/jobs/view/n/U-122764059040?jlsrc=3&utm_term=Palo+Alto+Cyber+Security+Engineer,+Mid&utm_campaign=google_jobs_apply&utm_source=google_jobs_apply&utm_medium=organic",
          "is_direct": false
        },
        {
          "publisher": "Talent.com",
          "apply_link": "https://www.talent.com/view?id=8c62bce87d3a&utm_campaign=google_jobs_apply&utm_source=google_jobs_apply&utm_medium=organic",
          "is_direct": false
        },
        {
          "publisher": "Build Submarines",
          "apply_link": "https://jobs.buildsubmarines.com/jobs/433554009-palo-alto-cyber-security-engineer-mid-at-booz-allen-hamilton-inc?utm_campaign=google_jobs_apply&utm_source=google_jobs_apply&utm_medium=organic",
          "is_direct": false
        },
        {
          "publisher": "WhatJobs",
          "apply_link": "https://www.whatjobs.com/jobs/network-security?id=2120762004&utm_campaign=google_jobs_apply&utm_source=google_jobs_apply&utm_medium=organic",
          "is_direct": false
        },
        {
          "publisher": "BeBee",
          "apply_link": "https://us.bebee.com/job/e5dc9bf7bacfbaeac3dce0035834dcde?utm_campaign=google_jobs_apply&utm_source=google_jobs_apply&utm_medium=organic",
          "is_direct": false
        }
      ],
      "job_description": "Palo Alto Cyber Security Engineer, Mid\nThe Opportunity:\n\nAre you looking for a career-defining opportunity to share your expertise in designing, developing, and implementing innovative network security solutions to support our country's critical infrastructure and fortify our nation's digital defenses? As a systems security and next-generation firewall engineer, you will be responsible for the enterprise-wide deployment of the Palo Alto Networks Security Operating Platform and its associated Panorama management framework. We need your experience to oversee the development and implementation of advanced security solutions to deliver robust threat prevention and improve the overall enterprise security posture.\n\nOn our team, you'll supervise and mentor a team as they troubleshoot and analyze complex network challenges for customers using your deep knowledge of Palo Alto's key security features, including App-ID, User-ID, Threat Prevention, and GlobalProtect. You'll manage the research of new technologies and market trends to further develop and refine our security solutions and ensure continuous alignment with the evolving threat landscape.\n\nIn this role, you'll closely impact mission success, protecting data and networks from malicious payloads and actors. With mentoring, challenging hands-on problem-solving, and opportunities to learn new tools and skills, we focus on growing as a team to make the best solutions for our customers.\n\nWork with us as we secure and protect our nation's most sensitive capabilities.\n\nWhat You'll Work On:\n• Develop relationships quickly and easily with other teams, communicating the complexities of security with a wide variety of audiences, including senior management.\n• Manage infrastructure and cybersecurity controls, including enhanced detection and vulnerability capabilities and improved event correlation in large enterprises.\n• Lead risk and vulnerability assessments in network, system, and application areas, and leverage big data analytics and traditional security event types to identify advanced threats or indicators of compromise.\n\nJoin us. The world can't wait.\n\nYou Have:\n• Experience configuring, managing, and optimizing Palo Alto Firewalls directly and via Panorama\n• Knowledge of multi-domain architectures, including data center, WAN, and LAN in virtualized architectures\n• Active TS/SCI clearance; willingness to take a polygraph exam\n• Associate's degree and 5+ years of experience supporting IT projects and activities, Bachelor's degree and 3+ years of experience supporting IT projects and activities or Master's degree and 1+ years of experience supporting IT projects and activities\n• DoD 8570 IAT Level II Certification, including Security+ CE, CCNA-Security, GSEC, SSCP, CySA+, GICSP, or CND Certification\n• Ability to obtain a DoD 8570 Cybersecurity Service Provider - Infrastructure Support Certification (CSSP-IS), including CEH, CySA+, GICSP, SSCP, CHFI, CFR, Cloud+, or CND Certification, within 60 days of start date\n\nNice If You Have:\n• Experience with Linux OS administration and management\n• Experience with Gigamon appliances and network taps\n• Ability to be a self-starter, work without considerable direction, and work with a team\n• Possession of excellent verbal and written communication skills, including for coordinating efforts and establishing customer relations\n\nClearance:\n\nApplicants selected will be subject to a security investigation and may need to meet eligibility requirements for access to classified information; TS/SCI clearance is required.\n\nCompensation\n\nAt Booz Allen, we celebrate your contributions, provide you with opportunities and choices, and support your total well-being. Our offerings include health, life, disability, financial, and retirement benefits, as well as paid leave, professional development, tuition assistance, work-life programs, and dependent care. Our recognition awards program acknowledges employees for exceptional performance and superior demonstration of our values. Full-time and part-time employees working at least 20 hours a week on a regular basis are eligible to participate in Booz Allen's benefit programs. Individuals that do not meet the threshold are only eligible for select offerings, not inclusive of health benefits. We encourage you to learn more about our total benefits by visiting the Resource page on our Careers site and reviewing Our Employee Benefits page.\n\nSalary at Booz Allen is determined by various factors, including but not limited to location, the individual's particular combination of education, knowledge, skills, competencies, and experience, as well as contract-specific affordability and organizational requirements. The projected compensation range for this position is $77,600.00 to $176,000.00 (annualized USD). The estimate displayed represents the typical salary range for this position and is just one component of Booz Allen's total compensation package for employees. This posting will close within 90 days from the Posting Date.\n\nIdentity Statement\n\nAs part of the application process, you are expected to be on camera during interviews and assessments. We reserve the right to take your picture to verify your identity and prevent fraud.\n\nWork Model\nOur people-first culture prioritizes the benefits of flexibility and collaboration, whether that happens in person or remotely.\n• If this position is listed as remote or hybrid, you'll periodically work from a Booz Allen or client site facility.\n• If this position is listed as onsite, you'll work with colleagues and clients in person, as needed for the specific role.\n\nCommitment to Non-Discrimination\n\nAll qualified applicants will receive consideration for employment without regard to disability, status as a protected veteran or any other status protected by applicable federal, state, local, or international law.",
      "job_is_remote": false,
      "job_posted_at": "1 day ago",
      "job_posted_at_timestamp": 1756684800,
      "job_posted_at_datetime_utc": "2025-09-01T00:00:00.000Z",
      "job_location": "Washington, DC",
      "job_city": "Washington",
      "job_state": "District of Columbia",
      "job_country": "US",
      "job_latitude": 38.9071923,
      "job_longitude": -77.0368707,
      "job_benefits": [
        "health_insurance"
      ],
      "job_google_link": "https://www.google.com/search?q=jobs&gl=us&hl=en&udm=8#vhid=vt%3D20/docid%3DwBapOcGrz4KMAv9gAAAAAA%3D%3D&vssid=jobs-detail-viewer",
      "job_min_salary": 77600,
      "job_max_salary": 176000,
      "job_salary_period": "YEAR",
      "job_highlights": {
        "Qualifications": [
          "Experience configuring, managing, and optimizing Palo Alto Firewalls directly and via Panorama",
          "Knowledge of multi-domain architectures, including data center, WAN, and LAN in virtualized architectures",
          "Active TS/SCI clearance; willingness to take a polygraph exam",
          "Associate's degree and 5+ years of experience supporting IT projects and activities, Bachelor's degree and 3+ years of experience supporting IT projects and activities or Master's degree and 1+ years of experience supporting IT projects and activities",
          "DoD 8570 IAT Level II Certification, including Security+ CE, CCNA-Security, GSEC, SSCP, CySA+, GICSP, or CND Certification",
          "Ability to obtain a DoD 8570 Cybersecurity Service Provider - Infrastructure Support Certification (CSSP-IS), including CEH, CySA+, GICSP, SSCP, CHFI, CFR, Cloud+, or CND Certification, within 60 days of start date",
          "Experience with Linux OS administration and management",
          "Experience with Gigamon appliances and network taps",
          "Ability to be a self-starter, work without considerable direction, and work with a team",
          "Possession of excellent verbal and written communication skills, including for coordinating efforts and establishing customer relations",
          "Applicants selected will be subject to a security investigation and may need to meet eligibility requirements for access to classified information; TS/SCI clearance is required"
        ],
        "Benefits": [
          "At Booz Allen, we celebrate your contributions, provide you with opportunities and choices, and support your total well-being",
          "Our offerings include health, life, disability, financial, and retirement benefits, as well as paid leave, professional development, tuition assistance, work-life programs, and dependent care",
          "Full-time and part-time employees working at least 20 hours a week on a regular basis are eligible to participate in Booz Allen's benefit programs",
          "Individuals that do not meet the threshold are only eligible for select offerings, not inclusive of health benefits",
          "We encourage you to learn more about our total benefits by visiting the Resource page on our Careers site and reviewing Our Employee Benefits page",
          "Salary at Booz Allen is determined by various factors, including but not limited to location, the individual's particular combination of education, knowledge, skills, competencies, and experience, as well as contract-specific affordability and organizational requirements",
          "The projected compensation range for this position is $77,600.00 to $176,000.00 (annualized USD)"
        ],
        "Responsibilities": [
          "As a systems security and next-generation firewall engineer, you will be responsible for the enterprise-wide deployment of the Palo Alto Networks Security Operating Platform and its associated Panorama management framework",
          "We need your experience to oversee the development and implementation of advanced security solutions to deliver robust threat prevention and improve the overall enterprise security posture",
          "On our team, you'll supervise and mentor a team as they troubleshoot and analyze complex network challenges for customers using your deep knowledge of Palo Alto's key security features, including App-ID, User-ID, Threat Prevention, and GlobalProtect",
          "You'll manage the research of new technologies and market trends to further develop and refine our security solutions and ensure continuous alignment with the evolving threat landscape",
          "In this role, you'll closely impact mission success, protecting data and networks from malicious payloads and actors",
          "Develop relationships quickly and easily with other teams, communicating the complexities of security with a wide variety of audiences, including senior management",
          "Manage infrastructure and cybersecurity controls, including enhanced detection and vulnerability capabilities and improved event correlation in large enterprises",
          "Lead risk and vulnerability assessments in network, system, and application areas, and leverage big data analytics and traditional security event types to identify advanced threats or indicators of compromise",
          "If this position is listed as remote or hybrid, you'll periodically work from a Booz Allen or client site facility",
          "If this position is listed as onsite, you'll work with colleagues and clients in person, as needed for the specific role"
        ]
      },
      "job_onet_soc": "15112200",
      "job_onet_job_zone": "4"
    },
    {
      "job_id": "dv7Ok-6l9PDQSQZaAAAAAA==",
      "job_title": "Senior Cybersecurity Analyst with Security Clearance",
      "employer_name": "Zero Point, Incorporated",
      "employer_logo": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRfw3jzzsOpistQQ-7auyIDyW0-2NRvy_8oDTts&s=0",
      "employer_website": "http://www.zeropointusa.com/",
      "job_publisher": "LinkedIn",
      "job_employment_type": "Full-time",
      "job_employment_types": [
        "FULLTIME"
      ],
      "job_apply_link": "https://www.linkedin.com/jobs/view/senior-cybersecurity-analyst-with-security-clearance-at-zero-point-incorporated-4293787180?utm_campaign=google_jobs_apply&utm_source=google_jobs_apply&utm_medium=organic",
      "job_apply_is_direct": false,
      "apply_options": [
        {
          "publisher": "LinkedIn",
          "apply_link": "https://www.linkedin.com/jobs/view/senior-cybersecurity-analyst-with-security-clearance-at-zero-point-incorporated-4293787180?utm_campaign=google_jobs_apply&utm_source=google_jobs_apply&utm_medium=organic",
          "is_direct": false
        },
        {
          "publisher": "CareerBuilder",
          "apply_link": "https://www.careerbuilder.com/job/J3T1KN6DZR6DL6R1F1K?utm_campaign=google_jobs_apply&utm_source=google_jobs_apply&utm_medium=organic",
          "is_direct": false
        },
        {
          "publisher": "BeBee",
          "apply_link": "https://us.bebee.com/job/3e748e000ff28abecb297c6163ab3172?utm_campaign=google_jobs_apply&utm_source=google_jobs_apply&utm_medium=organic",
          "is_direct": false
        },
        {
          "publisher": "Jobg8",
          "apply_link": "https://jobs.jobg8.com/jobs/senior-management-analyst-with-security-clearance-in-washington-washington-dc-united-states/5673-2996545273F9?utm_campaign=google_jobs_apply&utm_source=google_jobs_apply&utm_medium=organic",
          "is_direct": false
        },
        {
          "publisher": "Jobs Trabajo.org",
          "apply_link": "https://us.trabajo.org/job-3013-fdf23401b2c58f4e56b7f62b38da2356?utm_campaign=google_jobs_apply&utm_source=google_jobs_apply&utm_medium=organic",
          "is_direct": false
        },
        {
          "publisher": "Learn4Good",
          "apply_link": "https://www.learn4good.com/jobs/washington/district-of-columbia/info_technology/4320160927/e/?utm_campaign=google_jobs_apply&utm_source=google_jobs_apply&utm_medium=organic",
          "is_direct": false
        },
        {
          "publisher": "Jobrapido",
          "apply_link": "https://us.jobrapido.com/jobpreview/4165889196449333248?utm_campaign=google_jobs_apply&utm_source=google_jobs_apply&utm_medium=organic",
          "is_direct": false
        }
      ],
      "job_description": "PRIMARY OBJECTIVE OF POSITION: The Senior Cybersecurity Analyst serves as a subject-matter expert in Cybersecurity Policy, Planning, and Risk Management Framework (RMF) implementation. This role is responsible for tracking the status of Authority To Operate (ATOs) and other Risk Management Framework (RMF) functions, reviewing, analyzing, and interpreting cybersecurity policies, while also guiding and tracking the integration of cybersecurity engineering principles throughout system lifecycles. The incumbent will act as a trusted consultant to leadership, bridging the gap between compliance requirements, operational readiness, and technical solutions. MAJOR DUTIES & RESPONSIBILITIES:\n• Review cybersecurity policies, procedures, and directives to ensure compliance with DoN, DoD, and federal regulations (e.g., DoD 8500-series, NIST SP 800-series, Clinger Cohen Act, and various Defense Acquisition polices\n• Advise program leadership on emerging cybersecurity directives, regulatory and statutory changes, and policy impacts to mission systems\n• Monitor and track system authorization (ATO) efforts under the NAVSEA Risk Management Framework and provide early warnings of issues or when progress may be off track\n• Monitor and track various data calls for compliance in accordance with specific directives (OPORD, TASKORD, etc.)\n• Conduct and review system and program risk assessments to identify cybersecurity risks and provide strategies for remediation and mitigation\n• Lead strategic initiatives to strengthen cybersecurity posture across programs, balancing operational effectiveness with security imperatives\n• Represent the program office in high-level working groups, interagency forums, and technical exchanges\n• Partner with program managers, system engineers, and contractors to ensure cybersecurity is integrated throughout acquisition and development phases\n• Participate in the change management process, including conducting security impact analyses and making recommendations to program management for approvals MINIMUM QUALIFICATIONS:\n• SECRET Clearance is required to start the position\n• Bachelor's degree or higher from an accredited college or university in a cybersecurity-related field\n• Minimum 8-10 years of progressively responsible experience in cybersecurity policy, compliance, and engineering\n• Demonstrated experience with DoN/DoD cybersecurity programs, RMF, and secure systems engineering\n• Proven track record of reviewing policy documents, advising leadership, and implementing engineering solutions\n• Strong understanding of Navy acquisition processes and mission systems\n• Ability to translate complex technical requirements into actionable policy\n• Exceptional communication, negotiation, and stakeholder engagement skills\n• Proficiency in vulnerability management, system hardening, and secure configuration\n• Proven leadership in cross-functional cybersecurity initiative",
      "job_is_remote": false,
      "job_posted_at": "2 days ago",
      "job_posted_at_timestamp": 1756598400,
      "job_posted_at_datetime_utc": "2025-08-31T00:00:00.000Z",
      "job_location": "Washington, DC",
      "job_city": "Washington",
      "job_state": "District of Columbia",
      "job_country": "US",
      "job_latitude": 38.9071923,
      "job_longitude": -77.0368707,
      "job_benefits": null,
      "job_google_link": "https://www.google.com/search?q=jobs&gl=us&hl=en&udm=8#vhid=vt%3D20/docid%3Ddv7Ok-6l9PDQSQZaAAAAAA%3D%3D&vssid=jobs-detail-viewer",
      "job_salary": null,
      "job_min_salary": null,
      "job_max_salary": null,
      "job_salary_period": null,
      "job_highlights": {
        "Qualifications": [
          "Bachelor's degree or higher from an accredited college or university in a cybersecurity-related field",
          "Minimum 8-10 years of progressively responsible experience in cybersecurity policy, compliance, and engineering",
          "Demonstrated experience with DoN/DoD cybersecurity programs, RMF, and secure systems engineering",
          "Proven track record of reviewing policy documents, advising leadership, and implementing engineering solutions",
          "Ability to translate complex technical requirements into actionable policy",
          "Proficiency in vulnerability management, system hardening, and secure configuration",
          "Proven leadership in cross-functional cybersecurity initiative"
        ],
        "Responsibilities": [
          "PRIMARY OBJECTIVE OF POSITION: The Senior Cybersecurity Analyst serves as a subject-matter expert in Cybersecurity Policy, Planning, and Risk Management Framework (RMF) implementation",
          "This role is responsible for tracking the status of Authority To Operate (ATOs) and other Risk Management Framework (RMF) functions, reviewing, analyzing, and interpreting cybersecurity policies, while also guiding and tracking the integration of cybersecurity engineering principles throughout system lifecycles",
          "The incumbent will act as a trusted consultant to leadership, bridging the gap between compliance requirements, operational readiness, and technical solutions",
          "Review cybersecurity policies, procedures, and directives to ensure compliance with DoN, DoD, and federal regulations (e.g., DoD 8500-series, NIST SP 800-series, Clinger Cohen Act, and various Defense Acquisition polices",
          "Advise program leadership on emerging cybersecurity directives, regulatory and statutory changes, and policy impacts to mission systems",
          "Monitor and track system authorization (ATO) efforts under the NAVSEA Risk Management Framework and provide early warnings of issues or when progress may be off track",
          "Monitor and track various data calls for compliance in accordance with specific directives (OPORD, TASKORD, etc.)",
          "Conduct and review system and program risk assessments to identify cybersecurity risks and provide strategies for remediation and mitigation",
          "Lead strategic initiatives to strengthen cybersecurity posture across programs, balancing operational effectiveness with security imperatives",
          "Represent the program office in high-level working groups, interagency forums, and technical exchanges",
          "Partner with program managers, system engineers, and contractors to ensure cybersecurity is integrated throughout acquisition and development phases",
          "Participate in the change management process, including conducting security impact analyses and making recommendations to program management for approvals MINIMUM QUALIFICATIONS:",
          "SECRET Clearance is required to start the position",
          "Strong understanding of Navy acquisition processes and mission systems",
          "Exceptional communication, negotiation, and stakeholder engagement skills"
        ]
      },
      "job_onet_soc": "15112200",
      "job_onet_job_zone": "4"
    },
    {
      "job_id": "5Gqsa-sh_qNe3u1EAAAAAA==",
      "job_title": "Cybersecurity Policy and Program Analyst",
      "employer_name": "Aretum",
      "employer_logo": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSzgC_0xgAYkzAUC5N8H42V-JMa6SYsMRseJDyW&s=0",
      "employer_website": "https://aretum.com/",
      "job_publisher": "LinkedIn",
      "job_employment_type": "Full-time",
      "job_employment_types": [
        "FULLTIME"
      ],
      "job_apply_link": "https://www.linkedin.com/jobs/view/cybersecurity-policy-and-program-analyst-at-aretum-4293849689?utm_campaign=google_jobs_apply&utm_source=google_jobs_apply&utm_medium=organic",
      "job_apply_is_direct": false,
      "apply_options": [
        {
          "publisher": "LinkedIn",
          "apply_link": "https://www.linkedin.com/jobs/view/cybersecurity-policy-and-program-analyst-at-aretum-4293849689?utm_campaign=google_jobs_apply&utm_source=google_jobs_apply&utm_medium=organic",
          "is_direct": false
        },
        {
          "publisher": "ZipRecruiter",
          "apply_link": "https://www.ziprecruiter.com/c/Aretum/Job/Cybersecurity-Policy-and-Program-Analyst/-in-Arlington,VA?jid=f01b25c57c2b8527&utm_campaign=google_jobs_apply&utm_source=google_jobs_apply&utm_medium=organic",
          "is_direct": true
        },
        {
          "publisher": "Indeed",
          "apply_link": "https://www.indeed.com/viewjob?jk=35384d1d3e91a503&utm_campaign=google_jobs_apply&utm_source=google_jobs_apply&utm_medium=organic",
          "is_direct": false
        },
        {
          "publisher": "Glassdoor",
          "apply_link": "https://www.glassdoor.com/job-listing/cybersecurity-policy-and-program-analyst-aretum-JV_IC1130337_KO0,40_KE41,47.htm?jl=1009862295663&utm_campaign=google_jobs_apply&utm_source=google_jobs_apply&utm_medium=organic",
          "is_direct": true
        },
        {
          "publisher": "Teal",
          "apply_link": "https://www.tealhq.com/job/policy-and-program-analyst_980b29c4-52c8-4336-a77d-7398972fcb86?utm_campaign=google_jobs_apply&utm_source=google_jobs_apply&utm_medium=organic",
          "is_direct": false
        },
        {
          "publisher": "Snagajob",
          "apply_link": "https://www.snagajob.com/jobs/1157876678?utm_campaign=google_jobs_apply&utm_source=google_jobs_apply&utm_medium=organic",
          "is_direct": false
        },
        {
          "publisher": "Adzuna",
          "apply_link": "https://www.adzuna.com/details/5378861861?utm_campaign=google_jobs_apply&utm_source=google_jobs_apply&utm_medium=organic",
          "is_direct": true
        },
        {
          "publisher": "Job Peeks",
          "apply_link": "https://jobpeeks.com/jobs/cybersecurity-policy-and-program-analyst/1edbb170-c39d-470f-a3a2-e5ce40789de3?utm_campaign=google_jobs_apply&utm_source=google_jobs_apply&utm_medium=organic",
          "is_direct": false
        }
      ],
      "job_description": "Aretum is a mission-driven organization committed to delivering innovative, technology-enabled solutions to our customers across defense, civilian, and homeland security sectors. Our teams work at the intersection of strategy, technology, and transformation, helping agencies solve their most critical challenges. We believe in investing in our people and creating a culture where collaboration, inclusion, and professional growth are at the forefront.\n\nJoin us to be part of meaningful work that drives national impact and grow your career alongside exceptional peers.\n\nJob Summary\n\nDue to the nature of our work as a federal consulting organization, employees may be expected to handle Controlled Unclassified Information (CUI) and must adhere to applicable safeguarding and compliance requirements. Additionally, all team members may be called upon to support proposal efforts as needed. This could include resume formatting, providing skills alignment summaries, participating in meetings, or contributing to solutioning activities based on subject matter expertise or functional experience.\n\nResponsibilities\n\n• Provides support as a policy and program analyst to help an organization define its strategic vision and approach\n\n• Define outcomes for standards technical priorities\n\n• Determine/define document type and strategic direction for standards intent\n\n• Draft standards initiative strategic intent document\n\n• Mapping of interagency R&R across standards work\n\n• Determine service delivery engagement for standards technical priorities, based on strategic mapping\n\n• Partnership building across interagencies\n\n• Analyzes feedback and data prior to, during, and after stakeholder workshops\n\n• Creates template(s), as applicable\n\n• Revises draft strategy based on CATT tasker, Executive Governance Council (EGC)\n\n• Aligns Technology Strategy Objectives with relevant CSD Plan Objectives, including FY25 draft AOP\n\n• Advises on implementation planning\n\n• Provides support in developing standards to execute strategic plans and governance\n\n• Define outcomes for standards technical priorities\n\n• Determine/define document type and strategic direction for standards intent\n\n• Draft standards initiative strategic intent document\n\n• Mapping of interagency R&R across standards work\n\n• Determine service delivery engagement for standards technical priorities, based on strategic mapping\n\n• Partnership building support for interagency and international standards work\n\n• Conducts interviews for SMEs\n\n• Supports the buildout of decks for interviews of SMEs\n\n• Delivers meeting synopsis and themes from SME interview\n\nRequirements\n\n• Strong coordination skills - able to recognize or establish appropriate protocols between high level government managers and able to display strong persuasion skills to build consensus\n\n• Strong communication skills through both writing, building out documents and briefings, and acting as a facilitator\n\n• Strong comfort level with MS tools such as Word, Excel, PowerPoint, SharePoint, and Teams - especially with tools like SharePoint and Teams has the ability to utilize these tools in a manner that benefits process development and recognition\n\n• Understanding of documents to build out strategy and governance for an organization such as Strategic Plans, Strategic Roadmaps, Implementation Roadmaps, Mission & Vision statements\n\n• Background working within a technical organization - IT related - strong preference towards cybersecurity\n\n• 7-10 years experience, BA or BS in relevant field such as Business Management, Communications, Organizational Management, Computer Science, Engineering\n\n• DHS Suitability/preferably with CISA\n\nPreferred Qualifications\n\n• Ideally has prior experience working with a cybersecurity organization like CISA\n\nWork Environment & Physical Requirements\n• This job operates in a professional office environment. This role routinely uses standard office equipment\n• The physical demands described here are representative of those that must be met by an employee to successfully perform the essential functions of this job{{:}}\n• Prolonged periods sitting at a desk and working on a computer\n• Must be able to lift up to 15 pounds at times\n• Ability to travel occasionally, if required by the position\n• May require viewing and working with a screen for extended periods of time\n\nTravel Requirement\n\nTravel to client locations is required for this position and may vary based on project needs.\n\nEEO & Pay Transparency Statement\n\nAretum is committed to fostering a workplace rooted in excellence, integrity, and equal opportunity for all. We adhere to merit-based hiring practices, ensuring that all employment decisions are made based on qualifications, skills, and ability to perform the job, without preference or consideration of factors unrelated to job performance.\n\nAs an Equal Opportunity Employer, Aretum complies with all applicable federal, state, and local employment laws.\n\nWe are proud to support our nation's veterans and military families, providing career opportunities that honor their service and experience.\n\nIf you require a reasonable accommodation during the hiring process due to a disability, please contact our Talent Acquisition team for assistance.\n\nIn compliance with Executive Order 13665, Aretum will not discharge or otherwise discriminate against employees or applicants for inquiring about, discussing, or disclosing their own pay or that of another employee or applicant.\n\nU.S. Work Authorization\n\nApplicants must be U.S. citizens and currently authorized to work in the United States on a full-time basis. This position supports a federal government contract and therefore requires an active Public Trustclearance or the ability to obtain one.\n\nBenefits\n• Health Care Plan (Medical, Dental & Vision)\n• Retirement Plan (401k, IRA)\n• Life Insurance (Basic, Voluntary & AD&D)\n• Paid Time Off (Vacation, Sick & Public Holidays)\n• Family Leave (Maternity, Paternity)\n• Short Term & Long-Term Disability\n• Training & Development",
      "job_is_remote": false,
      "job_posted_at": "16 hours ago",
      "job_posted_at_timestamp": 1756756800,
      "job_posted_at_datetime_utc": "2025-09-01T20:00:00.000Z",
      "job_location": "Arlington, VA",
      "job_city": "Arlington",
      "job_state": "Virginia",
      "job_country": "US",
      "job_latitude": 38.8816208,
      "job_longitude": -77.09098089999999,
      "job_benefits": [
        "dental_coverage",
        "health_insurance",
        "paid_time_off"
      ],
      "job_google_link": "https://www.google.com/search?q=jobs&gl=us&hl=en&udm=8#vhid=vt%3D20/docid%3D5Gqsa-sh_qNe3u1EAAAAAA%3D%3D&vssid=jobs-detail-viewer",
      "job_salary": null,
      "job_min_salary": null,
      "job_max_salary": null,
      "job_salary_period": null,
      "job_highlights": {
        "Qualifications": [
          "Strong coordination skills - able to recognize or establish appropriate protocols between high level government managers and able to display strong persuasion skills to build consensus",
          "Strong communication skills through both writing, building out documents and briefings, and acting as a facilitator",
          "Strong comfort level with MS tools such as Word, Excel, PowerPoint, SharePoint, and Teams - especially with tools like SharePoint and Teams has the ability to utilize these tools in a manner that benefits process development and recognition",
          "Understanding of documents to build out strategy and governance for an organization such as Strategic Plans, Strategic Roadmaps, Implementation Roadmaps, Mission & Vision statements",
          "Background working within a technical organization - IT related - strong preference towards cybersecurity",
          "7-10 years experience, BA or BS in relevant field such as Business Management, Communications, Organizational Management, Computer Science, Engineering",
          "DHS Suitability/preferably with CISA",
          "Work Environment & Physical Requirements",
          "Prolonged periods sitting at a desk and working on a computer",
          "Must be able to lift up to 15 pounds at times",
          "Applicants must be U.S. citizens and currently authorized to work in the United States on a full-time basis",
          "This position supports a federal government contract and therefore requires an active Public Trustclearance or the ability to obtain one"
        ],
        "Benefits": [
          "Health Care Plan (Medical, Dental & Vision)",
          "Retirement Plan (401k, IRA)",
          "Life Insurance (Basic, Voluntary & AD&D)",
          "Paid Time Off (Vacation, Sick & Public Holidays)",
          "Family Leave (Maternity, Paternity)",
          "Short Term & Long-Term Disability",
          "Training & Development"
        ],
        "Responsibilities": [
          "This could include resume formatting, providing skills alignment summaries, participating in meetings, or contributing to solutioning activities based on subject matter expertise or functional experience",
          "Provides support as a policy and program analyst to help an organization define its strategic vision and approach",
          "Define outcomes for standards technical priorities",
          "Determine/define document type and strategic direction for standards intent",
          "Draft standards initiative strategic intent document",
          "Mapping of interagency R&R across standards work",
          "Determine service delivery engagement for standards technical priorities, based on strategic mapping",
          "Partnership building across interagencies",
          "Analyzes feedback and data prior to, during, and after stakeholder workshops",
          "Creates template(s), as applicable",
          "Revises draft strategy based on CATT tasker, Executive Governance Council (EGC)",
          "Aligns Technology Strategy Objectives with relevant CSD Plan Objectives, including FY25 draft AOP",
          "Advises on implementation planning",
          "Provides support in developing standards to execute strategic plans and governance",
          "Define outcomes for standards technical priorities",
          "Determine/define document type and strategic direction for standards intent",
          "Draft standards initiative strategic intent document",
          "Mapping of interagency R&R across standards work",
          "Determine service delivery engagement for standards technical priorities, based on strategic mapping",
          "Partnership building support for interagency and international standards work",
          "Conducts interviews for SMEs",
          "Supports the buildout of decks for interviews of SMEs",
          "Delivers meeting synopsis and themes from SME interview",
          "This job operates in a professional office environment",
          "This role routinely uses standard office equipment",
          "The physical demands described here are representative of those that must be met by an employee to successfully perform the essential functions of this job{{:}}",
          "Ability to travel occasionally, if required by the position",
          "May require viewing and working with a screen for extended periods of time",
          "Travel to client locations is required for this position and may vary based on project needs"
        ]
      },
      "job_onet_soc": "15112200",
      "job_onet_job_zone": "4"
    },
    {
      "job_id": "_38g2ZGHdX7qrvUFAAAAAA==",
      "job_title": "Cyber Security and Information Assurance Specialist Jobs",
      "employer_name": "Agile Defense, Inc.",
      "employer_logo": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSLs9fIcNVy-1pHKwl63M_KJQCHkkI8erZfuKCz&s=0",
      "employer_website": "http://www.agiledefense.com/",
      "job_publisher": "Security Clearance Jobs",
      "job_employment_type": "Full-time",
      "job_employment_types": [
        "FULLTIME"
      ],
      "job_apply_link": "https://www.clearancejobs.com/jobs/8511113/cyber-security-and-information-assurance-specialist?utm_campaign=google_jobs_apply&utm_source=google_jobs_apply&utm_medium=organic",
      "job_apply_is_direct": false,
      "apply_options": [
        {
          "publisher": "Security Clearance Jobs",
          "apply_link": "https://www.clearancejobs.com/jobs/8511113/cyber-security-and-information-assurance-specialist?utm_campaign=google_jobs_apply&utm_source=google_jobs_apply&utm_medium=organic",
          "is_direct": false
        },
        {
          "publisher": "LinkedIn",
          "apply_link": "https://www.linkedin.com/jobs/view/cyber-security-and-information-assurance-specialist-at-agile-defense-4291160810?utm_campaign=google_jobs_apply&utm_source=google_jobs_apply&utm_medium=organic",
          "is_direct": false
        },
        {
          "publisher": "Indeed",
          "apply_link": "https://www.indeed.com/viewjob?jk=884faf1d3aa15aa1&utm_campaign=google_jobs_apply&utm_source=google_jobs_apply&utm_medium=organic",
          "is_direct": true
        },
        {
          "publisher": "ZipRecruiter",
          "apply_link": "https://www.ziprecruiter.com/c/Agile-Defense/Job/Cyber-Security-and-Information-Assurance-Specialist/-in-Arlington,VA?jid=bc449d992f00fd98&utm_campaign=google_jobs_apply&utm_source=google_jobs_apply&utm_medium=organic",
          "is_direct": false
        },
        {
          "publisher": "Glassdoor",
          "apply_link": "https://www.glassdoor.com/job-listing/cyber-security-and-information-assurance-specialist-agile-defense-JV_IC1130337_KO0,51_KE52,65.htm?jl=1009859194245&utm_campaign=google_jobs_apply&utm_source=google_jobs_apply&utm_medium=organic",
          "is_direct": true
        },
        {
          "publisher": "Startup Jobs",
          "apply_link": "https://startup.jobs/cyber-security-and-information-assurance-specialist-agile-defense-7158810?utm_campaign=google_jobs_apply&utm_source=google_jobs_apply&utm_medium=organic",
          "is_direct": false
        },
        {
          "publisher": "Jobcase",
          "apply_link": "https://www.jobcase.com/jobs/view/n/U-122772034363?jlsrc=3&utm_term=Cyber+Security+and+Information+Assurance+Specialist&utm_campaign=google_jobs_apply&utm_source=google_jobs_apply&utm_medium=organic",
          "is_direct": false
        },
        {
          "publisher": "Adzuna",
          "apply_link": "https://www.adzuna.com/details/5376745281?utm_campaign=google_jobs_apply&utm_source=google_jobs_apply&utm_medium=organic",
          "is_direct": false
        }
      ],
      "job_description": "At Agile Defense we know that action defines the outcome and new challenges require new solutions. That's why we always look to the future and embrace change with an unmovable spirit and the courage to build for what comes next.\n\nOur vision is to bring adaptive innovation to support our nation's most important missions through the seamless integration of advanced technologies, elite minds, and unparalleled agility-leveraging a foundation of speed, flexibility, and ingenuity to strengthen and protect our nation's vital interests.\n\nRequisition # 1147\nJob Title: Cyber Security and Information Assurance Specialist\nLocation: 875 N Randolph St. Arlington, Virginia 22203\nClearance Level: Active DoD - Top Secret\nRequired Certification(s):\n• 8570.01-M IAT/IAM II (Sec+ Required, CISSP Preferred)\n• Position requires the candidate to maintain an active passport. If the candidate does not have an active passport, they must obtain one within the first 3 months.\n\nSUMMARY\n\nAgile Defense LLC provides all IT support, software development, Network Engineering, and Service Desk support to the Air Force Office of Scientific Research (AFOSR). The mission of AFOSR is to identify opportunities for significant scientific advancements and breakthrough research around the world, and to bring together researchers and resources to advance revolutionary basic research for Air Force needs.\nThe primary focus is on three areas. Risk Management Framework controls compliance and verification, DISA STIG and IAVA remediation and reporting, and IT Security monitoring and configuration with tools such as HBSS, ACAS, and Splunk in a DoD environment (Air Force). As part of the 3-member Information Assurance and Cyber Security team, you will be managed by the Cyber Security Lead (ISSO) to support and maintain the overal IA health, compliance and reporting requirements for this contract.\n\nJOB DUTIES AND RESPONSIBILITIES\n\n• Support operational requirements, which are tasks that are necessary to sustain day-to-day AFOSR functions and are usually ongoing and repetitive\n• Configure and use IT Security monitoring tools such as HBSS, ACAS, and Splunk to track and report on our IT security posture.\n• Work closely with the Network Engineering team to evaluate and perform hands-on mitigation of STIGs for network devices and servers.\n• Report to and work daily with the AFOSR ISSM in support of DoD and Air Force IA/cyber business.\n• Track and administer Information Assurance programs and business for AFOSR in accordance with ISSO direction.\n• Help ensure AFOSR is in full compliance with relevant Federal, DoD, USAF, Air Material Command (AFMC), Air Force Research Lab (AFRL) and organizational regulations, instructions, and procedures.\n• Compile network accreditation documentation for pertinent systems, including RMF Assessment & Authorization (A&A), Enterprise Mission Assurance Support Service (eMASS) data elements, reports and artifacts in accordance with AFI 17-101, Risk Management Framework.\n• Coordinate with internal contractor resources, Cyber Security Team Lead, Contracting Officer Representative (COR), the AFOSR ISSO and external governance and reporting entities on relevant security matters.\n• Track, update, coordinate and report compliance with network and systems security directives; vulnerability scans; malicious logic protections and incidents; account initiation, validation, and termination; and reviews of audit and systems logs.\n• Review DoD and Air Force approved products and software lists to ensure vetted materials and software capabilities are used by AFOSR personnel. New software must go through the relevant agency test and certification process.\n• Provide analysis and recommendations to the CORs, the AFOSR CITO, Chief Technology Officer, ISSM, other contractor teams and AFOSR leadership regarding security implications of applications, systems, and initiatives.\n• Maintain a current Disaster Recovery Plan for all AFOSR-managed systems, data and processes in support of and aligned with AFOSR's Continuity of Operations Plan (COOP).\n• Assess and adapt operations to comply with changes in official government policies.\n• Ensure all members being serviced by the organization are made aware of their duties, restrictions, procedures and regulations relating to information security.\n• Support semi-annual self- inspections in accordance with and at the direction of the AFOSR Self Inspection Program (SIP) or Management Internal Control Toolset (MICT) program.\n• Extended hours should be rare; however at times extended hours to support business or operations surges or workload may be needed.\n\nQUALIFICATIONS Required Certifications\n\n• 8570.01-M IAT/IAM II (Sec+ Required, CISSP Preferred)\n• Position requires the candidate to maintain an active passport. If the candidate does not have an active passport, they must obtain one within the first 3 months.\nEducation, Background, and Years of Experience\n• 5+ Years of experience desired\n• BA/BS Degree in Computer Science or other related field\n• Experience with DoD and USAF information security policies and instructions, strong knowledge of the Air Force Risk Management Framework (RMF) process.\n\nADDITIONAL SKILLS & QUALIFICATIONS Required Skills\n\n• Ability to provide quick and thorough tactical security advice needed to support the government Information System Security Manager (ISSM) and Chief Information Technology Officer (CITO) with all Cyber/IA-related activities.\n• Excellent written and verbal communication.\n• Strong knowledge and experience working in Windows 10/11 environments. Experience with Linux OS.\n• Ability to work independently and as a team.\n• Critical thinking skills.\n• Ability to work with senior leaders of the organization.\nPreferred Skills\n• Be familiar with DoD Instructions (DODI) and Air Force Instructions (AFI) and Manuals (AFMAN)\n\nWORKING CONDITIONS Environmental Conditions\n\n• Possible off-hours work to support releases and outages. General office environment with a fast-pace ops tempo. Work is generally sedentary in nature, but may require standing and walking for up to 10% of the time. The working environment is generally favorable. Lighting and temperature are adequate, and there are not hazardous or unpleasant conditions caused by noise, dust, etc. Work is generally performed within an office environment, with standard office equipment available.\nStrength Demands\n• Sedentary - 10 lbs. Maximum lifting, occasional lift/carry of small articles. Some occasional walking or standing may be required. Jobs are sedentary if walking and standing are required only occasionally, and all other sedentary criteria are met.\n\nPhysical Requirements\n\n• Stand or Sit; Walk; Repetitive Motion; Use Hands / Fingers to Handle or Feel; Stoop, Kneel, Crouch, or Crawl; See\n\nEmployees of Agile Defense are our number one priority, and the importance we place on our culture here is fundamental. Our culture is alive and evolving, but it always stays true to its roots. Here, you are valued as a family member, and we believe that we can accomplish great things together. Agile Defense has been highly successful in the past few years due to our employees and the culture we create together.\n\nWhat makes us Agile? We call it the 6Hs, the values that define our culture and guide everything we do. Together, these values infuse vibrancy, integrity, and a tireless work ethic into advancing the most important national security and critical civilian missions. It's how we show up every day. It's who we are.\n\nWe also believe in supporting our employees by offering a competitive and comprehensive benefits package. To explore the benefits we offer, please visit our website under the Careers section.\n\nHappy - Be Infectious.\nHappiness multiplies and creates a positive and connected environment where motivation and satisfaction have an outsized effect on everything we do.\n\nHelpful - Be Supportive.\nBeing helpful is the foundation of teamwork, resulting in a supportive atmosphere where collaboration flourishes, and collective success is celebrated.\n\nHonest - Be Trustworthy.\nHonesty serves as our compass, ensuring transparent communication and ethical conduct, essential to who we are and the complex domains we support.\n\nHumble - Be Grounded.\nSuccess is not achieved alone, humility ensures a culture of mutual respect, encouraging open communication, and a willingness to learn from one another and take on any task.\n\nHungry - Be Eager.\nOur hunger for excellence drives an insatiable appetite for innovation and continuous improvement, propelling us forward in the face of new and unprecedented challenges.\n\nHustle - Be Driven.\nHustle is reflected in our relentless work ethic, where we are each committed to going above and beyond to advance the mission and achieve success.\n\nEqual Opportunity Employer/Protected Veterans/Individuals with Disabilities",
      "job_is_remote": false,
      "job_posted_at": "10 hours ago",
      "job_posted_at_timestamp": 1756778400,
      "job_posted_at_datetime_utc": "2025-09-02T02:00:00.000Z",
      "job_location": "Arlington, VA",
      "job_city": "Arlington",
      "job_state": "Virginia",
      "job_country": "US",
      "job_latitude": 38.8816208,
      "job_longitude": -77.09098089999999,
      "job_benefits": null,
      "job_google_link": "https://www.google.com/search?q=jobs&gl=us&hl=en&udm=8#vhid=vt%3D20/docid%3D_38g2ZGHdX7qrvUFAAAAAA%3D%3D&vssid=jobs-detail-viewer",
      "job_salary": null,
      "job_min_salary": null,
      "job_max_salary": null,
      "job_salary_period": null,
      "job_highlights": {
        "Qualifications": [
          "Position requires the candidate to maintain an active passport",
          "If the candidate does not have an active passport, they must obtain one within the first 3 months",
          "New software must go through the relevant agency test and certification process",
          "Position requires the candidate to maintain an active passport",
          "If the candidate does not have an active passport, they must obtain one within the first 3 months",
          "Education, Background, and Years of Experience",
          "BA/BS Degree in Computer Science or other related field",
          "Experience with DoD and USAF information security policies and instructions, strong knowledge of the Air Force Risk Management Framework (RMF) process",
          "Ability to provide quick and thorough tactical security advice needed to support the government Information System Security Manager (ISSM) and Chief Information Technology Officer (CITO) with all Cyber/IA-related activities",
          "Excellent written and verbal communication",
          "Strong knowledge and experience working in Windows 10/11 environments",
          "Experience with Linux OS",
          "Ability to work independently and as a team",
          "Critical thinking skills",
          "Ability to work with senior leaders of the organization",
          "Maximum lifting, occasional lift/carry of small articles",
          "Jobs are sedentary if walking and standing are required only occasionally, and all other sedentary criteria are met",
          "Stand or Sit; Walk; Repetitive Motion; Use Hands / Fingers to Handle or Feel; Stoop, Kneel, Crouch, or Crawl; See",
          "Honest - Be Trustworthy",
          "Honesty serves as our compass, ensuring transparent communication and ethical conduct, essential to who we are and the complex domains we support",
          "Success is not achieved alone, humility ensures a culture of mutual respect, encouraging open communication, and a willingness to learn from one another and take on any task"
        ],
        "Responsibilities": [
          "Risk Management Framework controls compliance and verification, DISA STIG and IAVA remediation and reporting, and IT Security monitoring and configuration with tools such as HBSS, ACAS, and Splunk in a DoD environment (Air Force)",
          "As part of the 3-member Information Assurance and Cyber Security team, you will be managed by the Cyber Security Lead (ISSO) to support and maintain the overal IA health, compliance and reporting requirements for this contract",
          "Support operational requirements, which are tasks that are necessary to sustain day-to-day AFOSR functions and are usually ongoing and repetitive",
          "Configure and use IT Security monitoring tools such as HBSS, ACAS, and Splunk to track and report on our IT security posture",
          "Work closely with the Network Engineering team to evaluate and perform hands-on mitigation of STIGs for network devices and servers",
          "Report to and work daily with the AFOSR ISSM in support of DoD and Air Force IA/cyber business",
          "Track and administer Information Assurance programs and business for AFOSR in accordance with ISSO direction",
          "Help ensure AFOSR is in full compliance with relevant Federal, DoD, USAF, Air Material Command (AFMC), Air Force Research Lab (AFRL) and organizational regulations, instructions, and procedures",
          "Compile network accreditation documentation for pertinent systems, including RMF Assessment & Authorization (A&A), Enterprise Mission Assurance Support Service (eM",
          "ASS) data elements, reports and artifacts in accordance with AFI 17-101, Risk Management Framework",
          "Coordinate with internal contractor resources, Cyber Security Team Lead, Contracting Officer Representative (COR), the AFOSR ISSO and external governance and reporting entities on relevant security matters",
          "Track, update, coordinate and report compliance with network and systems security directives; vulnerability scans; malicious logic protections and incidents; account initiation, validation, and termination; and reviews of audit and systems logs",
          "Review DoD and Air Force approved products and software lists to ensure vetted materials and software capabilities are used by AFOSR personnel",
          "Provide analysis and recommendations to the CORs, the AFOSR CITO, Chief Technology Officer, ISSM, other contractor teams and AFOSR leadership regarding security implications of applications, systems, and initiatives",
          "Maintain a current Disaster Recovery Plan for all AFOSR-managed systems, data and processes in support of and aligned with AFOSR's Continuity of Operations Plan (COOP)",
          "Assess and adapt operations to comply with changes in official government policies",
          "Ensure all members being serviced by the organization are made aware of their duties, restrictions, procedures and regulations relating to information security",
          "Support semi-annual self- inspections in accordance with and at the direction of the AFOSR Self Inspection Program (SIP) or Management Internal Control Toolset (MICT) program",
          "Extended hours should be rare; however at times extended hours to support business or operations surges or workload may be needed",
          "Possible off-hours work to support releases and outages",
          "General office environment with a fast-pace ops tempo",
          "Work is generally sedentary in nature, but may require standing and walking for up to 10% of the time",
          "The working environment is generally favorable",
          "Work is generally performed within an office environment, with standard office equipment available",
          "Sedentary - 10 lbs",
          "Some occasional walking or standing may be required"
        ]
      },
      "job_onet_soc": "15112200",
      "job_onet_job_zone": "4"
    },
    {
      "job_id": "atE-aLFmlEZMbRmZAAAAAA==",
      "job_title": "Cyber Security Job Training Program",
      "employer_name": "Year Up United",
      "employer_logo": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTh4PWS0AYaSV-CMnUV3528vaGhq31j4gRorjOE&s=0",
      "employer_website": "http://www.yearup.org/",
      "job_publisher": "Snagajob",
      "job_employment_type": "Full-time",
      "job_employment_types": [
        "FULLTIME"
      ],
      "job_apply_link": "https://www.snagajob.com/jobs/1158007436?utm_campaign=google_jobs_apply&utm_source=google_jobs_apply&utm_medium=organic",
      "job_apply_is_direct": false,
      "apply_options": [
        {
          "publisher": "Snagajob",
          "apply_link": "https://www.snagajob.com/jobs/1158007436?utm_campaign=google_jobs_apply&utm_source=google_jobs_apply&utm_medium=organic",
          "is_direct": false
        }
      ],
      "job_description": "Year Up United is a one-year or less, intensive job training program that provides young adults with in-classroom skill development, access to internships and/or job placement services, and personalized coaching and mentorship. Year Up United participants also receive an educational stipend.\n\nThe program combines technical and professional training with access to internships and job placement support through our industry-leading talent placement firm YUPRO Placement. If you receive an internship, it may be at Fannie Mae, Merck, Okta, or Salesforce among many other leading organizations in the National Capital Region area.\n\nAre you eligible?\nYou can apply to Year Up United if you are:\n- A high school graduate or GED recipient\n- Eligible to work in the U.S.\n- Available Monday-Friday throughout the duration of the program\n- Highly motivated to learn technical and professional skills\n- Have not obtained a BachelorÊ¼s degree\n- You may be required to answer additional screening questions when applying\n\nWhat will you gain?\nProfessional business and communication skills, interviewing and networking skills, resume building, ongoing support and guidance to help you launch your career. During the internship phase, Year Up United students earn an educational stipend of $525 per week.\n\nIn-depth classes include:\n- Network Security & Support\n- Data Analytics\n- IT Support\n- Project Management\n- Banking\n\nGet the skills and opportunity you need to launch your professional career.\n75% of Year Up United graduates are employed and/or enrolled in postsecondary education within 4 months of graduation. Employed graduates earn an average starting salary of fifty-three thousand dollars per year.\nPandoLogic. Category:General, Location:Alexandria, VA-22312\n\nYear Up United is a one-year or less, intensive job training program that provides young adults with in-classroom skill development, access to internships and/or job placement services, and personalized coaching and mentorship. Year Up United participants also receive an educational stipend.\n\nThe program combines technical and professional training with access to internships and job placement support through our industry-leading talent placement firm YUPRO Placement. If you receive an internship, it may be at Fannie Mae, Merck, Okta, or Salesforce among many other leading organizations in the National Capital Region area.\n\nAre you eligible?\nYou can apply to Year Up United if you are:\n- A high school graduate or GED recipient\n- Eligible to work in the U.S.\n- Available Monday-Friday throughout the duration of the program\n- Highly motivated to learn technical and professional skills\n- Have not obtained a BachelorÊ¼s degree\n- You may be required to answer additional screening questions when applying\n\nWhat will you gain?\nProfessional business and communication skills, interviewing and networking skills, resume building, ongoing support and guidance to help you launch your career. During the internship phase, Year Up United students earn an educational stipend of $525 per week.\n\nIn-depth classes include:\n- Network Security & Support\n- Data Analytics\n- IT Support\n- Project Management\n- Banking\n\nGet the skills and opportunity you need to launch your professional career.\n75% of Year Up United graduates are employed and/or enrolled in postsecondary education within 4 months of graduation. Employed graduates earn an average starting salary of fifty-three thousand dollars per year.\nPandoLogic. Category:General, Location:Alexandria, VA-22312",
      "job_is_remote": false,
      "job_posted_at": "4 hours ago",
      "job_posted_at_timestamp": 1756800000,
      "job_posted_at_datetime_utc": "2025-09-02T08:00:00.000Z",
      "job_location": "Alexandria, VA",
      "job_city": "Alexandria",
      "job_state": "Virginia",
      "job_country": "US",
      "job_latitude": 38.804693,
      "job_longitude": -77.0435257,
      "job_benefits": null,
      "job_google_link": "https://www.google.com/search?q=jobs&gl=us&hl=en&udm=8#vhid=vt%3D20/docid%3DatE-aLFmlEZMbRmZAAAAAA%3D%3D&vssid=jobs-detail-viewer",
      "job_salary": null,
      "job_min_salary": null,
      "job_max_salary": null,
      "job_salary_period": null,
      "job_highlights": {
        "Qualifications": [
          "A high school graduate or GED recipient",
          "Eligible to work in the U.S",
          "Highly motivated to learn technical and professional skills",
          "Have not obtained a BachelorÊ¼s degree",
          "75% of Year Up United graduates are employed and/or enrolled in postsecondary education within 4 months of graduation",
          "A high school graduate or GED recipient",
          "Eligible to work in the U.S",
          "Highly motivated to learn technical and professional skills",
          "Have not obtained a BachelorÊ¼s degree"
        ],
        "Benefits": [
          "Year Up United participants also receive an educational stipend",
          "The program combines technical and professional training with access to internships and job placement support through our industry-leading talent placement firm YUPRO Placement",
          "Available Monday-Friday throughout the duration of the program",
          "Professional business and communication skills, interviewing and networking skills, resume building, ongoing support and guidance to help you launch your career",
          "During the internship phase, Year Up United students earn an educational stipend of $525 per week",
          "Employed graduates earn an average starting salary of fifty-three thousand dollars per year",
          "Year Up United is a one-year or less, intensive job training program that provides young adults with in-classroom skill development, access to internships and/or job placement services, and personalized coaching and mentorship",
          "Year Up United participants also receive an educational stipend",
          "The program combines technical and professional training with access to internships and job placement support through our industry-leading talent placement firm YUPRO Placement",
          "Available Monday-Friday throughout the duration of the program",
          "Professional business and communication skills, interviewing and networking skills, resume building, ongoing support and guidance to help you launch your career",
          "During the internship phase, Year Up United students earn an educational stipend of $525 per week"
        ],
        "Responsibilities": [
          "IT Support"
        ]
      },
      "job_onet_soc": "15112200",
      "job_onet_job_zone": "4"
    },
    {
      "job_id": "hgDCS_vVQZ2HQI0-AAAAAA==",
      "job_title": "Cyber Security Privileged Access Management (PAM) Analyst - Full-time",
      "employer_name": "Bank of America",
      "employer_logo": null,
      "employer_website": "http://www.bankofamerica.com/",
      "job_publisher": "Snagajob",
      "job_employment_type": "Full-time",
      "job_employment_types": [
        "FULLTIME"
      ],
      "job_apply_link": "https://www.snagajob.com/jobs/1140560439?utm_campaign=google_jobs_apply&utm_source=google_jobs_apply&utm_medium=organic",
      "job_apply_is_direct": false,
      "apply_options": [
        {
          "publisher": "Snagajob",
          "apply_link": "https://www.snagajob.com/jobs/1140560439?utm_campaign=google_jobs_apply&utm_source=google_jobs_apply&utm_medium=organic",
          "is_direct": false
        }
      ],
      "job_description": "Cyber Security Privileged Access Management (PAM) Analyst\n\nCharlotte, North Carolina;Washington, District of Columbia; Addison, Texas; Jacksonville, Florida; Denver, Colorado; Jersey City, New Jersey; Chicago, Illinois\n• *To proceed with your application, you must be at least 18 years of age.**\n\nAcknowledge\n\nRefer a friend\n• *To proceed with your application, you must be at least 18 years of age.**\n\nAcknowledge (https://ghr.wd1.myworkdayjobs.com/Lateral-US/job/Charlotte/Cyber-Security-Privileged-Access-Management--PAM--Analyst\\_25029922)\n• *Job Description:**\n\nAt Bank of America, we are guided by a common purpose to help make financial lives better through the power of every connection. We do this by driving Responsible Growth and delivering for our clients, teammates, communities and shareholders every day.\n\nBeing a Great Place to Work is core to how we drive Responsible Growth. This includes our commitment to being an inclusive workplace, attracting and developing exceptional talent, supporting our teammates’ physical, emotional, and financial wellness, recognizing and rewarding performance, and how we make an impact in the communities we serve.\n\nBank of America is committed to an in-office culture with specific requirements for office-based attendance and which allows for an appropriate level of flexibility for our teammates and businesses based on role-specific considerations.\n\nAt Bank of America, you can build a successful career with opportunities to learn, grow, and make an impact. Join us!\n• *Position Summary:**\n\nGlobal Information Security (GIS) is responsible for protecting bank information systems, confidential and proprietary data, and customer information. GIS develops the bank’s Information Security strategy and policy, manages the Information Security program, identifies and addresses vulnerabilities and operates a global security operations center that monitors, detects and responds to cybersecurity incidents. Within GIS, Identity and Access Management (IAM) is a security discipline that enables the right individuals to access the right resources at the right times and in the right context. IAM addresses the mission-critical need to ensure appropriate access to the resources across increasingly heterogeneous technology environments, and to meet increasingly rigorous compliance requirements.\n• *Role Description:**\n\n+ This role is primarily responsible for ensuring that relevant Privileged Access Controls are adequately enforced across platforms and applications to comply with IAM Standard.\n\n+ Partner with PAM Governance leads to ensure that Privileged Access Controls are appropriately measured, reported and governed.\n\n+ Apply industry PAM best practices, templates, and documentation while also proposing improvements based on practical knowledge.\n\n+ Document and convey PAM related requirements to technology partners to build/implement enhanced PAM solutions that are efficient, effective, and modern and able to result in material risk reduction in sustainable manner.\n\n+ Collaborate with stakeholders to develop PAM requirements that iteratively support long term PAM modernization and transformation (covers Process, Data and Technology aspects).\n\n+ Provide education to team members and technology partners regarding the proposed changes to PAM controls.\n\n+ Partners with the policy governance team for socialization and publication of proposed changes to the PAM Standard\n\n+ Takes accountability for addressing PAM risks. Proactively identify risk and ways to continuously enhance and improve BAC’s PAM controls. Implement and take decisive actions in finding solutions. Drives towards intended outcomes.\n\n+ Engage senior management to provide factual, transparent, and timely reporting on existing and emerging PAM or information security risks.\n\n+ Active participation in GIS IAM/PAM forums including but not limited to Monthly IAM Stakeholder Forum and Control Owner Forum for standard and Single Process Inventory (SPI) enhancements.\n\n+ Supports audit issues for closure and sustainability\n• *Required Qualifications:**\n\n+ 7 years relevant hands-on experience in PAM in complex and heterogenous technology environment.\n\n+ Deep experience with Linux, Windows, Cloud scale Identity, Access Management (Single Sign-On, Multi Factor Authentication), Authorization services or design and architecture of PAM services\n\n+ Deep knowledge of bank financial practices and policies and ability to adapt to fast changing environment\n\n+ Working level experience with IAM platforms such as Ping Identity, Active Directory OpenLDAP, OpenDJ\n\n+ Experience in consumption of Web Service APIs such as JSON / XML\n\n+ Hands on experience and involvement in large and complex projects.\n\n+ Expert level knowledge of privileged access management methodologies and techniques for on-prem and Cloud implementation.\n\n+ Expert level knowledge of authentication platforms such as Active Directory, LDAP, Kerberos, LDAP, Radius.\n\n+ Expert knowledge of PAM related tools which support session proxy, vaulting, just-in-time provision, integration with service management tool would be an advantage.\n\n+ Deep security knowledge which covers core technology infrastructure (network, storage, servers, databases, etc.) identity management and application security practice.\n\n+ Deep knowledge on Federation platforms or protocols such as Oauth, OpenID, SAML, WS-Fed, etc.\n\n+ Good knowledge and understanding of PAM-specific laws, rules, and regulations within the financial services sector.\n\n+ Proficient in Microsoft Office suite of products with ability to quickly analyze and synthesize large volumes of data.\n\n+ Familiarity with security standards such as NIST, ISO/EC, FFIEC.\n\n+ Understanding and interpreting BAC’s established information security Policy, Standards, Procedure and Guides, and applying this knowledge to related PAM decisions and response.\n\n+ Possession of CISSP certification would be an advantage.\n\n+ Knowledge of Compliance Certifications such as SOX, SOC, SOC2.\n\n+ Serve as the Subject Matter Experts in advising BAC business and technology counterparts on effective ways to achieve or exceed compliance with applicable Policy, Standards, Procedures and Guides.\n\n+ Proficient in articulating facts and data-driven plans and to partner with stakeholders to implement intended solutions to drive risk reductions and adherence to PAM standards.\n\n+ Strong attention to detail and advanced analytical skills.\n\n+ Excellent communication and presentation skills. Able to effectively prioritize multiple tasks.\n\n+ Proven track record in delivering outcomes that result in sustainable risk reductions in PAM.\n\n+ Ability to work independently on initiatives with little oversight. Motivated and willing to learn.\n\n+ Confident and effective in delivering messages across a wide spectrum of individuals with varying degrees of technical and business understanding\n\nThis job will be open and accepting applications for a minimum of seven days from the date it was posted\n• *Shift:**\n\n1st shift (United States of America)\n• *Hours Per Week:**\n\n40\n\nBank of America and its affiliates consider for employment and hire qualified candidates without regard to race, religious creed, religion, color, sex, sexual orientation, genetic information, gender, gender identity, gender expression, age, national origin, ancestry, citizenship, protected veteran or disability status or any factor prohibited by law, and as such affirms in policy and practice to support and promote the concept of equal employment opportunity, in accordance with all applicable federal, state, provincial and municipal laws. The company also prohibits discrimination on other bases such as medical condition, marital status or any other factor that is irrelevant to the performance of our teammates.\n\nTo view the \"Know your Rights\" poster, CLICK HERE (https://www.eeoc.gov/sites/default/files/2023-06/22-088\\_EEOC\\_KnowYourRights6.12.pdf) .\n\nView the LA County Fair Chance Ordinance (https://dcba.lacounty.gov/wp-content/uploads/2024/08/FCOE-Official-Notice-Eng-Final-8.30.2024.pdf) .\n\nBank of America aims to create a workplace free from the dangers and resulting consequences of illegal and illicit drug use and alcohol abuse. Our Drug-Free Workplace and Alcohol Policy (“Policy”) establishes requirements to prevent the presence or use of illegal or illicit drugs or unauthorized alcohol on Bank of America premises and to provide a safe work environment.\n\nBank of America is committed to an in-office culture with specific requirements for office-based attendance and which allows for an appropriate level of flexibility for our teammates and businesses based on role-specific considerations. Should you be offered a role with Bank of America, your hiring manager will provide you with information on the in-office expectations associated with your role. These expectations are subject to change at any time and at the sole discretion of the Company. To the extent you have a disability or sincerely held religious belief for which you believe you need a reasonable accommodation from this requirement, you must seek an accommodation through the Bank’s required accommodation request process before your first day of work.\n\nThis communication provides information about certain Bank of America benefits. Receipt of this document does not automatically entitle you to benefits offered by Bank of America. Every effort has been made to ensure the accuracy of this communication. However, if there are discrepancies between this communication and the official plan documents, the plan documents will always govern. Bank of America retains the discretion to interpret the terms or language used in any of its communications according to the provisions contained in the plan documents. Bank of America also reserves the right to amend or terminate any benefit plan in its sole discretion at any time for any reason.\n\nCyber Security Privileged Access Management (PAM) Analyst\n\nCharlotte, North Carolina;Washington, District of Columbia; Addison, Texas; Jacksonville, Florida; Denver, Colorado; Jersey City, New Jersey; Chicago, Illinois\n• *To proceed with your application, you must be at least 18 years of age.**\n\nAcknowledge\n\nRefer a friend\n• *To proceed with your application, you must be at least 18 years of age.**\n\nAcknowledge (https://ghr.wd1.myworkdayjobs.com/Lateral-US/job/Charlotte/Cyber-Security-Privileged-Access-Management--PAM--Analyst\\_25029922)\n• *Job Description:**\n\nAt Bank of America, we are guided by a common purpose to help make financial lives better through the power of every connection. We do this by driving Responsible Growth and delivering for our clients, teammates, communities and shareholders every day.\n\nBeing a Great Place to Work is core to how we drive Responsible Growth. This includes our commitment to being an inclusive workplace, attracting and developing exceptional talent, supporting our teammates’ physical, emotional, and financial wellness, recognizing and rewarding performance, and how we make an impact in the communities we serve.\n\nBank of America is committed to an in-office culture with specific requirements for office-based attendance and which allows for an appropriate level of flexibility for our teammates and businesses based on role-specific considerations.\n\nAt Bank of America, you can build a successful career with opportunities to learn, grow, and make an impact. Join us!\n• *Position Summary:**\n\nGlobal Information Security (GIS) is responsible for protecting bank information systems, confidential and proprietary data, and customer information. GIS develops the bank’s Information Security strategy and policy, manages the Information Security program, identifies and addresses vulnerabilities and operates a global security operations center that monitors, detects and responds to cybersecurity incidents. Within GIS, Identity and Access Management (IAM) is a security discipline that enables the right individuals to access the right resources at the right times and in the right context. IAM addresses the mission-critical need to ensure appropriate access to the resources across increasingly heterogeneous technology environments, and to meet increasingly rigorous compliance requirements.\n• *Role Description:**\n\n+ This role is primarily responsible for ensuring that relevant Privileged Access Controls are adequately enforced across platforms and applications to comply with IAM Standard.\n\n+ Partner with PAM Governance leads to ensure that Privileged Access Controls are appropriately measured, reported and governed.\n\n+ Apply industry PAM best practices, templates, and documentation while also proposing improvements based on practical knowledge.\n\n+ Document and convey PAM related requirements to technology partners to build/implement enhanced PAM solutions that are efficient, effective, and modern and able to result in material risk reduction in sustainable manner.\n\n+ Collaborate with stakeholders to develop PAM requirements that iteratively support long term PAM modernization and transformation (covers Process, Data and Technology aspects).\n\n+ Provide education to team members and technology partners regarding the proposed changes to PAM controls.\n\n+ Partners with the policy governance team for socialization and publication of proposed changes to the PAM Standard\n\n+ Takes accountability for addressing PAM risks. Proactively identify risk and ways to continuously enhance and improve BAC’s PAM controls. Implement and take decisive actions in finding solutions. Drives towards intended outcomes.\n\n+ Engage senior management to provide factual, transparent, and timely reporting on existing and emerging PAM or information security risks.\n\n+ Active participation in GIS IAM/PAM forums including but not limited to Monthly IAM Stakeholder Forum and Control Owner Forum for standard and Single Process Inventory (SPI) enhancements.\n\n+ Supports audit issues for closure and sustainability\n• *Required Qualifications:**\n\n+ 7 years relevant hands-on experience in PAM in complex and heterogenous technology environment.\n\n+ Deep experience with Linux, Windows, Cloud scale Identity, Access Management (Single Sign-On, Multi Factor Authentication), Authorization services or design and architecture of PAM services\n\n+ Deep knowledge of bank financial practices and policies and ability to adapt to fast changing environment\n\n+ Working level experience with IAM platforms such as Ping Identity, Active Directory OpenLDAP, OpenDJ\n\n+ Experience in consumption of Web Service APIs such as JSON / XML\n\n+ Hands on experience and involvement in large and complex projects.\n\n+ Expert level knowledge of privileged access management methodologies and techniques for on-prem and Cloud implementation.\n\n+ Expert level knowledge of authentication platforms such as Active Directory, LDAP, Kerberos, LDAP, Radius.\n\n+ Expert knowledge of PAM related tools which support session proxy, vaulting, just-in-time provision, integration with service management tool would be an advantage.\n\n+ Deep security knowledge which covers core technology infrastructure (network, storage, servers, databases, etc.) identity management and application security practice.\n\n+ Deep knowledge on Federation platforms or protocols such as Oauth, OpenID, SAML, WS-Fed, etc.\n\n+ Good knowledge and understanding of PAM-specific laws, rules, and regulations within the financial services sector.\n\n+ Proficient in Microsoft Office suite of products with ability to quickly analyze and synthesize large volumes of data.\n\n+ Familiarity with security standards such as NIST, ISO/EC, FFIEC.\n\n+ Understanding and interpreting BAC’s established information security Policy, Standards, Procedure and Guides, and applying this knowledge to related PAM decisions and response.\n\n+ Possession of CISSP certification would be an advantage.\n\n+ Knowledge of Compliance Certifications such as SOX, SOC, SOC2.\n\n+ Serve as the Subject Matter Experts in advising BAC business and technology counterparts on effective ways to achieve or exceed compliance with applicable Policy, Standards, Procedures and Guides.\n\n+ Proficient in articulating facts and data-driven plans and to partner with stakeholders to implement intended solutions to drive risk reductions and adherence to PAM standards.\n\n+ Strong attention to detail and advanced analytical skills.\n\n+ Excellent communication and presentation skills. Able to effectively prioritize multiple tasks.\n\n+ Proven track record in delivering outcomes that result in sustainable risk reductions in PAM.\n\n+ Ability to work independently on initiatives with little oversight. Motivated and willing to learn.\n\n+ Confident and effective in delivering messages across a wide spectrum of individuals with varying degrees of technical and business understanding\n\nThis job will be open and accepting applications for a minimum of seven days from the date it was posted\n• *Shift:**\n\n1st shift (United States of America)\n• *Hours Per Week:**\n\n40\n\nBank of America and its affiliates consider for employment and hire qualified candidates without regard to race, religious creed, religion, color, sex, sexual orientation, genetic information, gender, gender identity, gender expression, age, national origin, ancestry, citizenship, protected veteran or disability status or any factor prohibited by law, and as such affirms in policy and practice to support and promote the concept of equal employment opportunity, in accordance with all applicable federal, state, provincial and municipal laws. The company also prohibits discrimination on other bases such as medical condition, marital status or any other factor that is irrelevant to the performance of our teammates.\n\nTo view the \"Know your Rights\" poster, CLICK HERE (https://www.eeoc.gov/sites/default/files/2023-06/22-088\\_EEOC\\_KnowYourRights6.12.pdf) .\n\nView the LA County Fair Chance Ordinance (https://dcba.lacounty.gov/wp-content/uploads/2024/08/FCOE-Official-Notice-Eng-Final-8.30.2024.pdf) .\n\nBank of America aims to create a workplace free from the dangers and resulting consequences of illegal and illicit drug use and alcohol abuse. Our Drug-Free Workplace and Alcohol Policy (“Policy”) establishes requirements to prevent the presence or use of illegal or illicit drugs or unauthorized alcohol on Bank of America premises and to provide a safe work environment.\n\nBank of America is committed to an in-office culture with specific requirements for office-based attendance and which allows for an appropriate level of flexibility for our teammates and businesses based on role-specific considerations. Should you be offered a role with Bank of America, your hiring manager will provide you with information on the in-office expectations associated with your role. These expectations are subject to change at any time and at the sole discretion of the Company. To the extent you have a disability or sincerely held religious belief for which you believe you need a reasonable accommodation from this requirement, you must seek an accommodation through the Bank’s required accommodation request process before your first day of work.\n\nThis communication provides information about certain Bank of America benefits. Receipt of this document does not automatically entitle you to benefits offered by Bank of America. Every effort has been made to ensure the accuracy of this communication. However, if there are discrepancies between this communication and the official plan documents, the plan documents will always govern. Bank of America retains the discretion to interpret the terms or language used in any of its communications according to the provisions contained in the plan documents. Bank of America also reserves the right to amend or terminate any benefit plan in its sole discretion at any time for any reason.",
      "job_is_remote": false,
      "job_posted_at": "1 day ago",
      "job_posted_at_timestamp": 1756684800,
      "job_posted_at_datetime_utc": "2025-09-01T00:00:00.000Z",
      "job_location": "Washington, DC",
      "job_city": "Washington",
      "job_state": "District of Columbia",
      "job_country": "US",
      "job_latitude": 38.9071923,
      "job_longitude": -77.0368707,
      "job_benefits": null,
      "job_google_link": "https://www.google.com/search?q=jobs&gl=us&hl=en&udm=8#vhid=vt%3D20/docid%3DhgDCS_vVQZ2HQI0-AAAAAA%3D%3D&vssid=jobs-detail-viewer",
      "job_salary": null,
      "job_min_salary": null,
      "job_max_salary": null,
      "job_salary_period": null,
      "job_highlights": {
        "Qualifications": [
          "*To proceed with your application, you must be at least 18 years of age.**",
          "Apply industry PAM best practices, templates, and documentation while also proposing improvements based on practical knowledge",
          "7 years relevant hands-on experience in PAM in complex and heterogenous technology environment",
          "Deep experience with Linux, Windows, Cloud scale Identity, Access Management (Single Sign-On, Multi Factor Authentication), Authorization services or design and architecture of PAM services",
          "Deep knowledge of bank financial practices and policies and ability to adapt to fast changing environment",
          "Working level experience with IAM platforms such as Ping Identity, Active Directory OpenLDAP, OpenDJ",
          "Experience in consumption of Web Service APIs such as JSON / XML",
          "Hands on experience and involvement in large and complex projects",
          "Expert level knowledge of privileged access management methodologies and techniques for on-prem and Cloud implementation",
          "Expert level knowledge of authentication platforms such as Active Directory, LDAP, Kerberos, LDAP, Radius",
          "Expert knowledge of PAM related tools which support session proxy, vaulting, just-in-time provision, integration with service management tool would be an advantage",
          "Deep security knowledge which covers core technology infrastructure (network, storage, servers, databases, etc.) identity management and application security practice",
          "Deep knowledge on Federation platforms or protocols such as Oauth, OpenID, SAML, WS-Fed, etc",
          "Good knowledge and understanding of PAM-specific laws, rules, and regulations within the financial services sector",
          "Proficient in Microsoft Office suite of products with ability to quickly analyze and synthesize large volumes of data",
          "Familiarity with security standards such as NIST, ISO/EC, FFIEC",
          "Understanding and interpreting BAC’s established information security Policy, Standards, Procedure and Guides, and applying this knowledge to related PAM decisions and response",
          "Possession of CISSP certification would be an advantage",
          "Knowledge of Compliance Certifications such as SOX, SOC, SOC2",
          "Serve as the Subject Matter Experts in advising BAC business and technology counterparts on effective ways to achieve or exceed compliance with applicable Policy, Standards, Procedures and Guides",
          "Strong attention to detail and advanced analytical skills",
          "Excellent communication and presentation skills",
          "Able to effectively prioritize multiple tasks",
          "Proven track record in delivering outcomes that result in sustainable risk reductions in PAM",
          "Ability to work independently on initiatives with little oversight",
          "Motivated and willing to learn",
          "Confident and effective in delivering messages across a wide spectrum of individuals with varying degrees of technical and business understanding",
          "*To proceed with your application, you must be at least 18 years of age.**",
          "*To proceed with your application, you must be at least 18 years of age.**",
          "IAM addresses the mission-critical need to ensure appropriate access to the resources across increasingly heterogeneous technology environments, and to meet increasingly rigorous compliance requirements",
          "Partner with PAM Governance leads to ensure that Privileged Access Controls are appropriately measured, reported and governed",
          "Apply industry PAM best practices, templates, and documentation while also proposing improvements based on practical knowledge",
          "Document and convey PAM related requirements to technology partners to build/implement enhanced PAM solutions that are efficient, effective, and modern and able to result in material risk reduction in sustainable manner",
          "Collaborate with stakeholders to develop PAM requirements that iteratively support long term PAM modernization and transformation (covers Process, Data and Technology aspects)",
          "7 years relevant hands-on experience in PAM in complex and heterogenous technology environment",
          "Deep experience with Linux, Windows, Cloud scale Identity, Access Management (Single Sign-On, Multi Factor Authentication), Authorization services or design and architecture of PAM services",
          "Deep knowledge of bank financial practices and policies and ability to adapt to fast changing environment",
          "Working level experience with IAM platforms such as Ping Identity, Active Directory OpenLDAP, OpenDJ",
          "Experience in consumption of Web Service APIs such as JSON / XML",
          "Hands on experience and involvement in large and complex projects",
          "Expert level knowledge of privileged access management methodologies and techniques for on-prem and Cloud implementation",
          "Expert level knowledge of authentication platforms such as Active Directory, LDAP, Kerberos, LDAP, Radius",
          "Expert knowledge of PAM related tools which support session proxy, vaulting, just-in-time provision, integration with service management tool would be an advantage",
          "Deep security knowledge which covers core technology infrastructure (network, storage, servers, databases, etc.) identity management and application security practice",
          "Deep knowledge on Federation platforms or protocols such as Oauth, OpenID, SAML, WS-Fed, etc",
          "Good knowledge and understanding of PAM-specific laws, rules, and regulations within the financial services sector",
          "Proficient in Microsoft Office suite of products with ability to quickly analyze and synthesize large volumes of data",
          "Familiarity with security standards such as NIST, ISO/EC, FFIEC",
          "Understanding and interpreting BAC’s established information security Policy, Standards, Procedure and Guides, and applying this knowledge to related PAM decisions and response",
          "Possession of CISSP certification would be an advantage",
          "Knowledge of Compliance Certifications such as SOX, SOC, SOC2",
          "Serve as the Subject Matter Experts in advising BAC business and technology counterparts on effective ways to achieve or exceed compliance with applicable Policy, Standards, Procedures and Guides",
          "Proficient in articulating facts and data-driven plans and to partner with stakeholders to implement intended solutions to drive risk reductions and adherence to PAM standards",
          "Strong attention to detail and advanced analytical skills",
          "Excellent communication and presentation skills",
          "Able to effectively prioritize multiple tasks",
          "Proven track record in delivering outcomes that result in sustainable risk reductions in PAM",
          "Ability to work independently on initiatives with little oversight",
          "Motivated and willing to learn",
          "Confident and effective in delivering messages across a wide spectrum of individuals with varying degrees of technical and business understanding"
        ],
        "Benefits": [
          "*Hours Per Week:**",
          "*Hours Per Week:**"
        ],
        "Responsibilities": [
          "Global Information Security (GIS) is responsible for protecting bank information systems, confidential and proprietary data, and customer information",
          "GIS develops the bank’s Information Security strategy and policy, manages the Information Security program, identifies and addresses vulnerabilities and operates a global security operations center that monitors, detects and responds to cybersecurity incidents",
          "IAM addresses the mission-critical need to ensure appropriate access to the resources across increasingly heterogeneous technology environments, and to meet increasingly rigorous compliance requirements",
          "This role is primarily responsible for ensuring that relevant Privileged Access Controls are adequately enforced across platforms and applications to comply with IAM Standard",
          "Partner with PAM Governance leads to ensure that Privileged Access Controls are appropriately measured, reported and governed",
          "Document and convey PAM related requirements to technology partners to build/implement enhanced PAM solutions that are efficient, effective, and modern and able to result in material risk reduction in sustainable manner",
          "Collaborate with stakeholders to develop PAM requirements that iteratively support long term PAM modernization and transformation (covers Process, Data and Technology aspects)",
          "Provide education to team members and technology partners regarding the proposed changes to PAM controls",
          "Partners with the policy governance team for socialization and publication of proposed changes to the PAM Standard",
          "Takes accountability for addressing PAM risks",
          "Proactively identify risk and ways to continuously enhance and improve BAC’s PAM controls",
          "Implement and take decisive actions in finding solutions",
          "Drives towards intended outcomes",
          "Engage senior management to provide factual, transparent, and timely reporting on existing and emerging PAM or information security risks",
          "Active participation in GIS IAM/PAM forums including but not limited to Monthly IAM Stakeholder Forum and Control Owner Forum for standard and Single Process Inventory (SPI) enhancements",
          "Supports audit issues for closure and sustainability",
          "Proficient in articulating facts and data-driven plans and to partner with stakeholders to implement intended solutions to drive risk reductions and adherence to PAM standards",
          "Global Information Security (GIS) is responsible for protecting bank information systems, confidential and proprietary data, and customer information",
          "GIS develops the bank’s Information Security strategy and policy, manages the Information Security program, identifies and addresses vulnerabilities and operates a global security operations center that monitors, detects and responds to cybersecurity incidents",
          "This role is primarily responsible for ensuring that relevant Privileged Access Controls are adequately enforced across platforms and applications to comply with IAM Standard",
          "Provide education to team members and technology partners regarding the proposed changes to PAM controls",
          "Partners with the policy governance team for socialization and publication of proposed changes to the PAM Standard",
          "Takes accountability for addressing PAM risks",
          "Proactively identify risk and ways to continuously enhance and improve BAC’s PAM controls",
          "Implement and take decisive actions in finding solutions",
          "Drives towards intended outcomes",
          "Engage senior management to provide factual, transparent, and timely reporting on existing and emerging PAM or information security risks",
          "Active participation in GIS IAM/PAM forums including but not limited to Monthly IAM Stakeholder Forum and Control Owner Forum for standard and Single Process Inventory (SPI) enhancements",
          "Supports audit issues for closure and sustainability"
        ]
      },
      "job_onet_soc": "15112200",
      "job_onet_job_zone": "4"
    },
    {
      "job_id": "2vNNRUJ38wv9yLEBAAAAAA==",
      "job_title": "Advanced Security Engineer - Cyber Security Job at Relativity in Mount Rainier",
      "employer_name": "Relativity",
      "employer_logo": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcR7PiS0DT3oF88pAE3fZX-tfIQS3qxD8WvKPU3G&s=0",
      "employer_website": "https://www.relativity.com",
      "job_publisher": "Recruit.net",
      "job_employment_type": "Full-time",
      "job_employment_types": [
        "FULLTIME"
      ],
      "job_apply_link": "https://www.recruit.net/job/advanced-security-engineer-cyber-security-jobs/029AE4641450A53B?utm_campaign=google_jobs_apply&utm_source=google_jobs_apply&utm_medium=organic",
      "job_apply_is_direct": false,
      "apply_options": [
        {
          "publisher": "Recruit.net",
          "apply_link": "https://www.recruit.net/job/advanced-security-engineer-cyber-security-jobs/029AE4641450A53B?utm_campaign=google_jobs_apply&utm_source=google_jobs_apply&utm_medium=organic",
          "is_direct": false
        }
      ],
      "job_description": "Advanced Security Engineer - Cyber Security Join to apply for the Advanced Security Engineer - Cyber Security role at Relativity Advanced Security Engineer - Cyber Security 3 days ago Be among the first 25 applicants Join to apply for the Advanced Security Engineer - Cyber Security role at Relativity Get AI-powered advice on this job and more exclusive features.\nJob Overview As an Advanced Cyber Security Engineer, you will ensure the security of Relativity’s network and infrastructure.\nIn this role, the main responsibilities will be to investigate and analyze emerging threats against our assets, identities, and clients.\nYou will also provide actionable remediation guidance to end users and collaborate with highly skilled cyber experts to anticipate and mitigate evolving threats using world-class toolsets and next generation capabilities.\nPosting Type Remote Job Overview As an Advanced Cyber Security Engineer, you will ensure the security of Relativity’s network and infrastructure.\nIn this role, the main responsibilities will be to investigate and analyze emerging threats against our assets, identities, and clients.\nYou will also provide actionable remediation guidance to end users and collaborate with highly skilled cyber experts to anticipate and mitigate evolving threats using world-class toolsets and next generation capabilities.\nResponsibilities Job Description and Requirements Review, validation, and triage of alerts and technical analysis of log data from a diverse inventory of sensors, correlated signature logic, and threat intelligence sources.\nAssess the impact of security events by leveraging host, cloud, and network-based indicators and evidence to deliver actionable incident escalations.\nAct as the initial point of escalation for cyber security events and drive investigation to completion.\n- Perform accurate and in-depth near real-time analysis of correlated logs and alerts from a multitude of devices with a focus on the classification of events that constitute security incidents.\nProactively and iteratively search through collected telemetry to detect and isolate advanced threats that evade existing security solutions.\nAssist in the development of incident handling policies and procedures to align with global industry standards.\nEngage in the continuous research of emerging threats and apply appropriate countermeasures within the context of a rapidly changing environment.\nServe as a subject matter expert in the mechanism and analysis of observed malicious activity.\n- Perform consistent tuning of alerting and provide support to junior team members in detection engineering Maintain security infrastructure and take accountability for ensuring the tooling configuration is updated as required Assist on projects as and when required Preferred Qualifications Bachelor’s Degree (or equivalent professional/military experience) 3 years of experience in Incident Response, Incident Analysis, or Computer Forensics Familiarity with industry standard security devices and their configuration Exposure to the analysis of malicious code to explore infection and propagation mechanisms Experience leveraging scripting languages to solve for information security use cases Outstanding work ethic with a passion for Cyber Security Certifications: One of more of the following certifications are preferred (GCFA, GCIA, GCIH, GCFA, GNFA, GREM, OSCP, or CEH) Experience working in a SaaS environment operating on a global scale.\nExperience in the legal space and with a high understanding of e-discovery and litigation.\nExperience working with cloud environments such as Azure, GCP, or AWS.\nMinimum Qualifications Strong cyber incident response skills (such as: Network forensics, memory forensics, and/or packet analysis) Working knowledge of TCP/IP, network services, cryptography and web application attacks Ability to collaborate within a cross-functional team to execute on high-level objectives and drive the maturation of Relativity’s security posture Understanding of methods and tools utilized by attackers to access private systems and data Capability to independently manage the prioritization of complex events Understanding of infection mechanisms, malicious behavior, exploitation techniques, and mitigating controls.\nRelativity is committed to competitive, fair, and equitable compensation practices.\nThis position is eligible for total compensation which includes a competitive base salary, an annual performance bonus, and long-term incentives.\nThe expected salary range for this role is between following values: $104,000 and $156,000 The final offered salary will be based on several factors, including but not limited to the candidate's depth of experience, skill set, qualifications, and internal pay equity.\nHiring at the top end of the range would not be typical, to allow for future meaningful salary growth in this position.Seniority level Seniority levelMid-Senior level Employment type Employment typeFull-time Job function Job functionInformation Technology IndustriesSoftware Development Referrals increase your chances of interviewing at Relativity by 2x Get notified about new Security Engineer jobs in Washington, United States . Staff Security Engineer, Smart Contracts Seattle, WA $220,000.00-$260,000.00 1 day ago Seattle, WA $171,900.00-$249,100.00 1 day ago Redmond, WA $100,600.00-$215,400.00 1 week ago Greater Seattle Area $168,000.00-$228,000.00 3 days ago Senior Security Engineer - Northwest region (Seattle, WA) Greater Seattle Area $190,000.00-$245,000.00 2 weeks ago Washington, United States $70.00-$80.00 1 week ago Staff Security Engineer, Vulnerability Operations United States $210,000.00-$316,000.00 2 weeks ago Microsoft Identity & Devices Security Architect - Client Consulting Seattle, WA $130,000.00-$180,000.00 2 weeks ago Sumner, WA $128,419.00-$204,100.00 1 month ago Seattle, WA $199,800.00-$289,050.00 2 weeks ago Senior Security Engineer IS – Identity & Access Management *Virtual* Washington, United States $54.56-$97.32 1 month ago Linux Cryptography and Security EngineerProject Consultant (Engineer) - Telecommunications / SecurityLinux Cryptography and Security EngineerLinux Cryptography and Security Engineer Seattle, WA $175,000.00-$250,000.00 2 weeks ago Linux Cryptography and Security EngineerSr.\nStaff Security Operations Engineer – VM & Offensive Security - REMOTE Seattle, WA $120,000.00-$260,000.00 1 week ago Seattle, WA $139,100.00-$206,000.00 6 days ago We’re unlocking community knowledge in a new way.\nExperts add insights directly into each article, started with the help of AI.\nJ-18808-Ljbffr",
      "job_is_remote": false,
      "job_posted_at": "12 hours ago",
      "job_posted_at_timestamp": 1756771200,
      "job_posted_at_datetime_utc": "2025-09-02T00:00:00.000Z",
      "job_location": "Mt Rainier, MD",
      "job_city": "Mt Rainier",
      "job_state": "Maryland",
      "job_country": "US",
      "job_latitude": 38.936433,
      "job_longitude": -76.9609825,
      "job_benefits": [
        "health_insurance"
      ],
      "job_google_link": "https://www.google.com/search?q=jobs&gl=us&hl=en&udm=8#vhid=vt%3D20/docid%3D2vNNRUJ38wv9yLEBAAAAAA%3D%3D&vssid=jobs-detail-viewer",
      "job_salary": null,
      "job_min_salary": null,
      "job_max_salary": null,
      "job_salary_period": null,
      "job_highlights": {},
      "job_onet_soc": "15112200",
      "job_onet_job_zone": "4"
    },
    {
      "job_id": "0JZm4o6w9zXH9WLiAAAAAA==",
      "job_title": "Cloud Cybersecurity (CC) Subject Matter Expert (SME)",
      "employer_name": "AttainX, Inc.",
      "employer_logo": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQcw16mU1qWk_iW6txiL2Sv0j3pT4Ssp7SBwKdx&s=0",
      "employer_website": "https://attainx.com",
      "job_publisher": "LinkedIn",
      "job_employment_type": "Full-time",
      "job_employment_types": [
        "FULLTIME"
      ],
      "job_apply_link": "https://www.linkedin.com/jobs/view/cloud-cybersecurity-cc-subject-matter-expert-sme-at-attainx-inc-4293731778?utm_campaign=google_jobs_apply&utm_source=google_jobs_apply&utm_medium=organic",
      "job_apply_is_direct": false,
      "apply_options": [
        {
          "publisher": "LinkedIn",
          "apply_link": "https://www.linkedin.com/jobs/view/cloud-cybersecurity-cc-subject-matter-expert-sme-at-attainx-inc-4293731778?utm_campaign=google_jobs_apply&utm_source=google_jobs_apply&utm_medium=organic",
          "is_direct": false
        },
        {
          "publisher": "Cleared Careers",
          "apply_link": "https://clearedcareers.com/job/728551/cloud-cybersecurity-cc-subject-matter-expert-sme/?utm_campaign=google_jobs_apply&utm_source=google_jobs_apply&utm_medium=organic",
          "is_direct": false
        },
        {
          "publisher": "Ladders",
          "apply_link": "https://www.theladders.com/job/cloud-cybersecurity-cc-subject-matter-expert-sme-attainxinc-alexandria-va_82879505?utm_campaign=google_jobs_apply&utm_source=google_jobs_apply&utm_medium=organic",
          "is_direct": false
        },
        {
          "publisher": "JobGet",
          "apply_link": "https://www.jobget.com/jobs/job/82e1fd26-7315-42ce-bcbd-336a03b2f8bc?utm_campaign=google_jobs_apply&utm_source=google_jobs_apply&utm_medium=organic",
          "is_direct": true
        },
        {
          "publisher": "Dr. Job",
          "apply_link": "https://www.drjobpro.com/job/view/MEFBJ7HO6XLIH93?utm_campaign=google_jobs_apply&utm_source=google_jobs_apply&utm_medium=organic",
          "is_direct": true
        },
        {
          "publisher": "Snagajob",
          "apply_link": "https://www.snagajob.com/jobs/1157375092?utm_campaign=google_jobs_apply&utm_source=google_jobs_apply&utm_medium=organic",
          "is_direct": true
        },
        {
          "publisher": "JobNet",
          "apply_link": "https://www.jobnet.com.au/us/en/search-jobs-in-Alexandria,-Virginia,-USA/CLOUD-CYBERSECURITY-CC-SUBJECT-MATTER-EXPERT-SME-F940A320D548687623/?utm_campaign=google_jobs_apply&utm_source=google_jobs_apply&utm_medium=organic",
          "is_direct": false
        },
        {
          "publisher": "LazyApply",
          "apply_link": "https://lazyapply.com/jobpreview/cloud-cybersecurity-cc-subject-matter-expert-sme-attainxinc-alexandria-va_82879505?utm_campaign=google_jobs_apply&utm_source=google_jobs_apply&utm_medium=organic",
          "is_direct": false
        }
      ],
      "job_description": "Attainx Inc.\n\nJob Title: Cloud Cybersecurity (CC) Subject Matter Expert (SME)\n\nLocation: Washington, DC area; Hybrid\n\nClearance: Active Top Secret SCI or Tier 5 (favorable adjudication)\n\nCitizenship: US Citizenship required.\n\nExemption Status: Exempt\n\nPosition type: Full time.\n\nSalary: $140,000 - $250,000 wage range. You will receive a competitive total rewards package that is applicable to the U.S. only. The salary range may vary based on experience, skillset, and geographical location.\n\nAttainX Inc. is seeking a seasoned Cloud Cybersecurity Subject Matter Expert (SME) to provide strategic cyber leadership and support for cloud security operations across Military Community and Family Policy (MC&FP) systems. The CC SME will guide security posture, risk management, and compliance activities, applying deep knowledge of federal frameworks and advanced cybersecurity protocols within cloud environments. This role is critical to safeguarding sensitive systems that support military families and operations.\n\nQualifications and Education Requirements:\n• Bachelor’s degree in Computer Science, IT, Information Systems, or related field.\n• Minimum 8 years of experience managing federal government cybersecurity projects of similar size and complexity within cloud environments.\n• Experience providing support for large Department of Defense contracts with a preference for MC&FP or related support activities\n• At least 8 years of hands-on experience with:\n• NIST RMF and NIST SP 800-53,\n• DISA STIGs,\n• SCAP tools and reporting,\n• IAVAs,\n• FISMA compliance.\n• Must have one or more of the following certifications:\n• CISM, CISSO, FITSP-M, GCIA, GCSA, GCIH, GSLC, GICSP, CISSP, CISSP-ISSMP.\n• Must be a U.S. Citizen with an active TS SCI or Active Favorable Tier 5 investigation adjudication.\n\nJob Duties:\n• Provide cybersecurity oversight and leadership for all cloud-based systems supporting MC&FP.\n• Guide implementation and compliance with NIST RMF, FISMA, STIGs, SCAP, and IAVAs.\n• Lead the development and execution of cybersecurity strategies tailored to cloud environments.\n• Coordinate vulnerability management and remediation efforts based on assessments and penetration testing.\n• Support DoD defensive cyber operational activities including incident handling, response, reporting, and recovery.\n• Collaborate with system owners, developers, and stakeholders to ensure continuous cyber risk awareness and mitigation.\n\nNon-Essential Functions:\n• General Duty Requirements.\n\nAbout Us:\n\nAttainX Inc. is SBA Certified 8(a), Women Owned Small Business (WOSB), Economically Disadvantaged WOSB (EDWOSB), CMMI Level 3, ISO 9001:2015 certified QMS and Silver Level SaFe Partner. For more than 12 years, AttainX, Inc. has delivered emergent technologies, software products, and high-quality services that meet the needs of our Federal Government customers.\n\nThe last 4 years have shown significant company growth as we have increased our contracts portfolio and hold the “Best in Class” contract vehicles, GSA MAS and OASIS Small Business and 8(a) Pools 1, 2 and 3. In addition, we are prime on several Agency Specific IDIQ’s and BPA’s with the National Oceanic and Atmospheric Administration, Department of Energy, Navy, Health and Human Service and the Defense Intelligence Agency.\n\nAttainX is dedicated to quality and best practices for the services we provide. We understand our people are the key ingredient to ensuring our customers Mission and Goals are met with excellence.\n\nBenefits:\n\nWe are proud to offer competitive compensation and benefits packages to include paid vacation, medical, dental, vision, matching 401K plan, tuition/training reimbursement, and Long & Short-Term Disability.\n\nEEO Commitment:\n\nAttainX Inc. is an Equal Opportunity Employer. All qualified applicants will receive consideration for employment without regard to race, color, religion, sex (including pregnancy, sexual orientation, or gender identity), national origin, age, disability, genetic information, veteran status, or any other status protected by applicable federal, state, or local law.\n\nWe are committed to providing equal employment opportunities for individuals with disabilities and protected veterans in compliance with Section 503 of the Rehabilitation Act of 1973 and the Vietnam Era Veterans’ Readjustment Assistance Act (VEVRAA).\n\nAccommodations:\n\nIf you are an individual with a disability and would like to request a reasonable workplace accommodation, please send an email to HR@AttainX.com. Indicate the specifics of the assistance needed.\n\nPhysical Demands:\n\nSitting and working on a computer for long, continuous periods each day; effective communications by telephone, email, and face-to-face; standing, walking, and sitting; handling and feeling objects or controls; reaching; talking and hearing; lifting and/or moving up to 10 pounds; and specific vision abilities including close vision, distance vision, color vision, peripheral vision, depth perception, and the ability to adjust and focus.\n\nWork Environment: The noise level in the work environment is usually moderate.\n\nCompensation details: 140000-250000 Yearly Salary",
      "job_is_remote": false,
      "job_posted_at": "1 day ago",
      "job_posted_at_timestamp": 1756684800,
      "job_posted_at_datetime_utc": "2025-09-01T00:00:00.000Z",
      "job_location": "Alexandria, VA",
      "job_city": "Alexandria",
      "job_state": "Virginia",
      "job_country": "US",
      "job_latitude": 38.804693,
      "job_longitude": -77.0435257,
      "job_benefits": [
        "health_insurance",
        "paid_time_off",
        "dental_coverage"
      ],
      "job_google_link": "https://www.google.com/search?q=jobs&gl=us&hl=en&udm=8#vhid=vt%3D20/docid%3D0JZm4o6w9zXH9WLiAAAAAA%3D%3D&vssid=jobs-detail-viewer",
      "job_salary": null,
      "job_min_salary": null,
      "job_max_salary": null,
      "job_salary_period": null,
      "job_highlights": {
        "Qualifications": [
          "Citizenship: US Citizenship required",
          "Bachelor’s degree in Computer Science, IT, Information Systems, or related field",
          "Minimum 8 years of experience managing federal government cybersecurity projects of similar size and complexity within cloud environments",
          "Experience providing support for large Department of Defense contracts with a preference for MC&FP or related support activities",
          "At least 8 years of hands-on experience with:",
          "NIST RMF and NIST SP 800-53,",
          "DISA STIGs,",
          "SCAP tools and reporting,",
          "IAVAs,",
          "FISMA compliance",
          "Must have one or more of the following certifications:",
          "CISM, CISSO, FITSP-M, GCIA, GCSA, GCIH, GSLC, GICSP, CISSP, CISSP-ISSMP",
          "Must be a U.S. Citizen with an active TS SCI or Active Favorable Tier 5 investigation adjudication",
          "Sitting and working on a computer for long, continuous periods each day; effective communications by telephone, email, and face-to-face; standing, walking, and sitting; handling and feeling objects or controls; reaching; talking and hearing; lifting and/or moving up to 10 pounds; and specific vision abilities including close vision, distance vision, color vision, peripheral vision, depth perception, and the ability to adjust and focus"
        ],
        "Benefits": [
          "Salary: $140,000 - $250,000 wage range",
          "You will receive a competitive total rewards package that is applicable to the U.S. only",
          "The salary range may vary based on experience, skillset, and geographical location",
          "We are proud to offer competitive compensation and benefits packages to include paid vacation, medical, dental, vision, matching 401K plan, tuition/training reimbursement, and Long & Short-Term Disability",
          "Compensation details: 140000-250000 Yearly Salary"
        ],
        "Responsibilities": [
          "The CC SME will guide security posture, risk management, and compliance activities, applying deep knowledge of federal frameworks and advanced cybersecurity protocols within cloud environments",
          "This role is critical to safeguarding sensitive systems that support military families and operations",
          "Provide cybersecurity oversight and leadership for all cloud-based systems supporting MC&FP",
          "Guide implementation and compliance with NIST RMF, FISMA, STIGs, SCAP, and IAVAs",
          "Lead the development and execution of cybersecurity strategies tailored to cloud environments",
          "Coordinate vulnerability management and remediation efforts based on assessments and penetration testing",
          "Support DoD defensive cyber operational activities including incident handling, response, reporting, and recovery",
          "Collaborate with system owners, developers, and stakeholders to ensure continuous cyber risk awareness and mitigation"
        ]
      },
      "job_onet_soc": "15112200",
      "job_onet_job_zone": "4"
    },
    {
      "job_id": "wcElpQ4khmLiDQoqAAAAAA==",
      "job_title": "Cybersecurity Program Manager Jobs",
      "employer_name": "Leidos",
      "employer_logo": null,
      "employer_website": "http://www.leidos.com/",
      "job_publisher": "Security Clearance Jobs",
      "job_employment_type": "Full-time",
      "job_employment_types": [
        "FULLTIME"
      ],
      "job_apply_link": "https://www.clearancejobs.com/jobs/8489439/cybersecurity-program-manager?utm_campaign=google_jobs_apply&utm_source=google_jobs_apply&utm_medium=organic",
      "job_apply_is_direct": false,
      "apply_options": [
        {
          "publisher": "Security Clearance Jobs",
          "apply_link": "https://www.clearancejobs.com/jobs/8489439/cybersecurity-program-manager?utm_campaign=google_jobs_apply&utm_source=google_jobs_apply&utm_medium=organic",
          "is_direct": false
        }
      ],
      "job_description": "R-00164690\n\nDescription\n\nThe Homeland and Force Protection Business Area has an immediate opening for a Cybersecurity Program Manager to support our customer’s mission critical malware analysis programs. This position is an exciting opportunity to leverage your leadership skills and lead the nation’s defensive cyber operations supporting malware detection and defeat as well as reverse engineering. If you are looking to join and lead a team of the best cybersecurity professionals in the industry supporting our nation’s front line of defense against cyber threats, this is the job for you.\n\nPrimary Responsibilities\n\nThe Malware Analysis Program Manager will lead a team of 20 cybersecurity professionals with responsibilities to assist our customer in continuing to evolve cybersecurity technologies to answer leading edge security problems to include advanced visualization solutions, exfiltration detection modeling and analysis, malware detection, reverse engineering, automated analysis and modeling, and sandbox analysis systems. The duties for this position will also include management and delivery of key weekly, monthly, quarterly and yearly reporting and trend analysis relating customer CMA mission areas as well as project and program timeline development and implementation aligned to customer goals and cyber threat analysis output expectations.\n\nBasic Qualifications\n• Bachelor’s Degree\n• Minimum of 15 years of experience leading teams of 20 or more malware analysts or cyber security professionals\n• Active TS/SCI clearance\n• Ability to establish common processes across tasks for system-wide, cross-task activities such as configuration management, risk management, performance measurement, subcontractor management, security, process improvement, and quality assurance via the PMP.\n• Previous experience in cybersecurity team management, cyber strategic planning and/or cyber operations\n• Experience maintaining oversight of support team strategy and deliverables to customers\n• Experience coordinating across customers for resource planning and allocation to mission needs, both steady state and ad-hoc\n• Ability to communicate with customer leadership and ensure core mission requirements are met on schedule and cost with proactive efficiency implementation\n• Provide management of support personnel and operational needs to proactively cover any mission gaps and surge needs predicated on emergent operational necessity\n\nPreferred Qualifications\n• CISA or DHS cybersecurity experience – either as a manager or as a technical SME\n• Cybersecurity technical experience in the areas of Advanced Persistent Threat (APT) analysis, YARA rule crafting, or developing and maintaining a secure analysis environment\n\nCome break things (in a good way). Then build them smarter.\n\nWe're the tech company everyone calls when things get weird. We don’t wear capes (they’re a safety hazard), but we do solve high-stakes problems with code, caffeine, and a healthy disregard for “how it’s always been done.”\n\nOriginal Posting: August 15, 2025\nFor U.S. Positions: While subject to change based on business needs, Leidos reasonably anticipates that this job requisition will remain open for at least 3 days with an anticipated close date of no earlier than 3 days after the original posting date as listed above.\n\nPay Range: Pay Range $126,100.00 - $227,950.00\n\nThe Leidos pay range for this job level is a general guideline only and not a guarantee of compensation or salary. Additional factors considered in extending an offer include (but are not limited to) responsibilities of the job, education, experience, knowledge, skills, and abilities, as well as internal equity, alignment with market data, applicable bargaining agreement (if any), or other law.",
      "job_is_remote": false,
      "job_posted_at": "2 days ago",
      "job_posted_at_timestamp": 1756598400,
      "job_posted_at_datetime_utc": "2025-08-31T00:00:00.000Z",
      "job_location": "Arlington, VA",
      "job_city": "Arlington",
      "job_state": "Virginia",
      "job_country": "US",
      "job_latitude": 38.8816208,
      "job_longitude": -77.09098089999999,
      "job_benefits": null,
      "job_google_link": "https://www.google.com/search?q=jobs&gl=us&hl=en&udm=8#vhid=vt%3D20/docid%3DwcElpQ4khmLiDQoqAAAAAA%3D%3D&vssid=jobs-detail-viewer",
      "job_salary": null,
      "job_min_salary": null,
      "job_max_salary": null,
      "job_salary_period": null,
      "job_highlights": {
        "Qualifications": [
          "Bachelor’s Degree",
          "Minimum of 15 years of experience leading teams of 20 or more malware analysts or cyber security professionals",
          "Active TS/SCI clearance",
          "Ability to establish common processes across tasks for system-wide, cross-task activities such as configuration management, risk management, performance measurement, subcontractor management, security, process improvement, and quality assurance via the PMP",
          "Previous experience in cybersecurity team management, cyber strategic planning and/or cyber operations",
          "Experience maintaining oversight of support team strategy and deliverables to customers",
          "Experience coordinating across customers for resource planning and allocation to mission needs, both steady state and ad-hoc",
          "Ability to communicate with customer leadership and ensure core mission requirements are met on schedule and cost with proactive efficiency implementation",
          "Provide management of support personnel and operational needs to proactively cover any mission gaps and surge needs predicated on emergent operational necessity"
        ],
        "Benefits": [
          "Pay Range: Pay Range $126,100.00 - $227,950.00",
          "The Leidos pay range for this job level is a general guideline only and not a guarantee of compensation or salary"
        ],
        "Responsibilities": [
          "The Malware Analysis Program Manager will lead a team of 20 cybersecurity professionals with responsibilities to assist our customer in continuing to evolve cybersecurity technologies to answer leading edge security problems to include advanced visualization solutions, exfiltration detection modeling and analysis, malware detection, reverse engineering, automated analysis and modeling, and sandbox analysis systems",
          "The duties for this position will also include management and delivery of key weekly, monthly, quarterly and yearly reporting and trend analysis relating customer CMA mission areas as well as project and program timeline development and implementation aligned to customer goals and cyber threat analysis output expectations",
          "Come break things (in a good way)"
        ]
      },
      "job_onet_soc": "11919900",
      "job_onet_job_zone": "4"
    }
  ]
}