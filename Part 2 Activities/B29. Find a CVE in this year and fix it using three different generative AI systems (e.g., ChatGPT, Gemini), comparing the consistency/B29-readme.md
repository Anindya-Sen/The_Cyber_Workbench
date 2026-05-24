# B29. Find a CVE in this year and fix it using three different generative AI systems (e.g., ChatGPT, Gemini), comparing the consistency.


For this activity, I selected a real vulnerability published in 2026, reproduced it in a controlled local environment on Kali Linux, and then consulted three generative AI systems to generate a fix. I compared the responses across all three systems for consistency and quality, applied the fix I found most useful, and verified that it resolved the vulnerability.


## The CVE

I selected CVE-2026-42208, a critical pre-authentication SQL injection vulnerability in LiteLLM Proxy, an open-source AI gateway used to manage and route requests to large language model providers such as OpenAI and Anthropic.

| Field | Detail |
|---|---|
| **CVE ID** | CVE-2026-42208 |
| **CVSS Score** | 9.3 (Critical) |
| **Weakness** | CWE-89: SQL Injection |
| **Affected Versions** | LiteLLM 1.81.16 through 1.83.6 |
| **Fixed Version** | 1.83.7 (recommended: 1.83.10-stable) |
| **Published** | April 2026 |
| **CISA KEV Listed** | Yes |


The vulnerability exists in LiteLLM Proxy's API key verification logic. When a request arrives, the proxy reads the Authorization: Bearer header and looks up the token value in its database. In the affected versions, the token value is dropped directly into the SQL query string using Python f-string interpolation rather than being passed as a separate parameter. This means an attacker can send a crafted bearer token containing SQL syntax that breaks out of the string literal and alters the query's logic entirely, bypassing authentication without any valid credentials.


The vulnerable code pattern:


```python
# VULNERABLE -- f-string embeds user input directly into SQL
query = f"SELECT * FROM LiteLLM_VerificationToken WHERE token = '{bearer_token}'"
cursor.execute(query)
```


Sending Authorization: Bearer ' OR '1'='1 causes the database to execute:

```python
SELECT * FROM LiteLLM_VerificationToken WHERE token = '' OR '1'='1'
```


The condition '1'='1' is always true, so the query returns a valid user record and authentication is bypassed entirely.



## Reproducing the Vulnerability

I set up the vulnerable version of LiteLLM (v1.83.6) inside a Python virtual environment on Kali Linux and wrote a short Python script that reproduced the exact vulnerable SQL pattern using SQLite. Running the script confirmed that the injection payload ' OR '1'='1 successfully bypassed authentication on the vulnerable version, returning a valid user record that should have been inaccessible.


## Consulting Three AI Systems


I presented the same prompt to ChatGPT (GPT-4o), Google Gemini, and Anthropic Claude. The prompt described the CVE, showed the vulnerable code, demonstrated the attack payload, and asked each system to explain the vulnerability, provide a fix, explain why the fix works, and suggest any additional security measures.


### ChatGPT

ChatGPT approached the activity from a vulnerability management and dependency patching perspective rather than addressing the code-level root cause directly. It did not explain why the code was vulnerable in terms of how the SQL parser processes the injected input, and it did not provide a corrected version of the vulnerable function. Instead, it guided through a structured process: installing the vulnerable version of LiteLLM (v1.83.6) inside an isolated virtual environment, using a Python vulnerability scanning tool called pip-audit to confirm the package was flagged as vulnerable, and then upgrading to the patched release.

The fix it recommended:

```python
pip install --upgrade "litellm>=1.83.10"
```


Verification was done by re-running pip-audit after the upgrade and comparing version outputs saved to text files before and after the patch. It also suggested restarting the LiteLLM proxy and confirming the service still responded correctly to a health check, to show the upgrade did not break functionality.

The additional recommendations focused on process and evidence rather than technical hardening -- taking screenshots at each stage, saving scan output files, and including a written disclaimer that the activity was performed only inside a local VM and not against any public system.




### Gemini

Gemini took a more technical and exploitation-focused approach. Rather than treating the fix as a simple package upgrade, it demonstrated the vulnerability through a time-based blind SQL injection technique. It used a PostgreSQL-specific timing function embedded in the bearer token payload:

```python
time curl -X POST http://127.0.0.1:4000/chat/completions \
  -H "Authorization: Bearer ' OR (SELECT pg_sleep(5)) IS NULL --" \
  -H "Content-Type: application/json" \
  -d '{"model": "gpt-3.5-turbo", "messages": [{"role": "user", "content": "hi"}]}'
```



The logic behind this is that if the injected SQL is actually executed by the database, the pg_sleep(5) call will force a five-second delay in the response. A response that takes five seconds or more confirms the input was parsed as executable SQL rather than a literal string. A baseline request with a normal token should return near-instantly.

Gemini offered two remediation options. The first was a quick operational workaround -- disabling error logs in LiteLLM's configuration to remove the vulnerable code path that processes failed credentials:

```python
litellm --port 4000 --config '{"general_settings": {"disable_error_logs": true}}'
```

The second was the permanent fix -- upgrading the package past the patched version ceiling:


```python
pip install litellm>=1.83.7 --upgrade
```


Verification was done by re-running the same timing attack after the fix and confirming the response returned to baseline speed (0.0 to 0.1 seconds), demonstrating that the injected SQL was no longer being executed.




### Claude

Claude's response was the most structured and the easiest to follow. It explained exactly what happens at the SQL parser level when the injection payload is received -- specifically, how the single quote in the payload terminates the string literal prematurely and allows the OR clause to become valid SQL logic that is always true. This step-by-step explanation made the mechanism of the attack genuinely clear rather than just labelling it as SQL injection.


The fix Claude provided:

```python
# FIXED -- bearer_token is passed as a parameter, never embedded in SQL text
query = "SELECT * FROM LiteLLM_VerificationToken WHERE token = ?"
cursor.execute(query, (bearer_token,))
```


Claude explained that with a parameterized query, the database engine receives the query structure and the value in two separate steps. The query is compiled first, and its structure is locked before the value is ever substituted. This means no amount of SQL syntax in the value can change what the query does -- the injection payload is treated as a plain string of characters that simply fails to match any token in the database.

Claude's additional recommendations were specific and prioritised: hashing tokens before storage, using hmac.compare_digest() for constant-time comparison, validating input length before querying, and ensuring the database user has the minimum privileges needed.



## Comparison
All three AI systems identified CVE-2026-42208 as a SQL injection vulnerability in LiteLLM and recommended upgrading to a patched version as the primary fix. Beyond that, their approaches diverged significantly.


| Criterion | ChatGPT | Gemini | Claude |
|---|---|---|---|
| **Correctly identified root cause** | Partially – named it SQL injection but did not explain the code-level cause | Partially – demonstrated the effect but did not explain f-string interpolation | Yes – explained how the single quote breaks the string literal at parser level |
| **Provided code-level fix (parameterized query)** | No – upgrade only | No – upgrade only | Yes – showed fixed function with parameterized query |
| **Explained attack mechanism clearly** | No | Partially – showed timing behavior but not why the code allows it | Yes – more detailed |
| **Explained why the fix prevents injection** | No | No | Yes – explained query compilation before value substitution |
| **Demonstration method** | `pip-audit` version scan | Time-based blind SQL injection via `pg_sleep` | Standalone Python PoC script with SQLite |
| **Setup complexity** | Low | High – requires PostgreSQL backend | Very low – Python only, no server needed |
| **Fix options offered** | Upgrade only | Workaround + permanent upgrade | Code patch + upgrade |
| **Overall clarity and usability** | Moderate – good for patch management process | Moderate – good technical depth but complex to execute | High – clearest explanation and most actionable fix |



## Applying the Fix

I found Claude's response to be the most understandable and useful. Its explanation of the parser-level mechanism behind the attack gave me a clear understanding of not just what to change, but why the change works. I applied the parameterized query fix from Claude's response to the vulnerable function and upgraded the installed LiteLLM package to the official patched version (v1.83.10-stable).



## Verifying the Fix


After applying the fix, I re-ran the same test script with the same injection payloads. All attack attempts were blocked -- the payloads were treated as literal strings by the database engine and returned no matching records. Legitimate authentication with a valid key continued to work correctly.

Before fix: Injection payload ' OR '1'='1 bypasses authentication and returns a valid user record.

After fix: The same payload is rejected. The database treats it as a plain string value, finds no match, and denies access.



## Conclusion
CVE-2026-42208 is a critical SQL injection vulnerability in LiteLLM Proxy caused by embedding user-supplied input directly into SQL query strings. All three AI systems identified the same root cause and agreed on the same fix. The consistency across ChatGPT, Gemini, and Claude on the core solution confirms that parameterized queries are the universally recognised defence against this class of vulnerability.
I applied Claude's fix because it was the clearest and most thoroughly explained. Understanding exactly why the fix works -- not just how to implement it -- is more valuable for writing secure code going forward than simply copying a corrected function. The fix was verified to be effective, blocking all tested injection attempts while preserving normal functionality.




![Tailgating example](B29%20risk%20identified.png)

**Figure: Vulnerabilities identified**




![Tailgating example](B29%20output%20-%20vulnerability%20and%20fix%20demonstrated.png)

**Figure: Vulnerability Fixed proof**





ChatGPT response: https://chatgpt.com/share/6a12ca6f-13f0-83ec-8716-b8de54c6f47c

Gemini response: https://gemini.google.com/share/82960d5ede91

*Claude response: Inside the attached pdf*

