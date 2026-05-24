# B22. Enhance the cybersecurity of a website from your community.

## Overview

I selected a real local community website in Lynwood, WA and conducted a non-invasive, read-only security assessment. The aim was to identify existing security weaknesses and provide practical fixes the organisation could act on. No attacks were attempted, no data was accessed, and nothing on the website was modified.



## Target Website

| Field | Detail |
|---|---|
| **Organisation** | Lynwood Support |
| **Website** | lynwoodsupport.com.au |
| **Location** | Lynwood, Western Australia 6147 |
| **Contact Email** | info@lynwoodsupport.com.au |
| **About** | Local NDIS disability support and personal care provider |
| **Platform** | WordPress 7.0, WooCommerce, Elementor |
| **Server** | LiteSpeed / PHP 8.2.31 |

Lynwood Support is a community-facing NDIS provider. Their website is used by clients and families to find service information and submit enquiries. Given that the audience includes people with disabilities, the security of user interactions on this site carries real importance.



## Tools Used

•	securityheaders.com — assessed HTTP security response headers

•	SSL Labs (ssllabs.com) — assessed SSL/TLS certificate and protocol configuration

•	curl on Kali Linux — pulled raw server response headers directly from the terminal

•	Browser page source inspection — checked for version disclosures in the HTML


All tools are free and publicly available. None of them send attacks or access anything beyond what a normal browser already sees.




## Security Findings


### Issue 1 (Risk high) — Missing HTTP Security Headers
Running the website through securityheaders.com returned a failing grade. Five critical HTTP security headers are completely absent from all public-facing pages of the site.
The headers currently returned by the homepage are:

•	HTTP/2 200

•	x-powered-by: PHP/8.2.31

•	content-type: text/html; charset=UTF-8

•	server: LiteSpeed


None of the standard security headers are present. What makes this more notable is that the WordPress login page (/wp-login.php) does send some of these headers correctly — meaning the server is capable of sending them, they just have not been applied to the rest of the site.


What each missing header means:

•	X-Frame-Options: Without this, the site can be embedded invisibly in an iframe on a malicious page, enabling clickjacking attacks on contact forms.

•	Content-Security-Policy: Without this, there are no restrictions on which scripts the browser can run — a serious risk if any content injection occurs.

•	Referrer-Policy: Without this, sensitive page names such as /ndis-personal-care are leaked to third-party sites when users click external links.

•	X-Content-Type-Options: Without this, browsers may misinterpret uploaded file types, which can be exploited in certain attack scenarios.

•	Strict-Transport-Security (HSTS): Without this, the first connection attempt always goes over plain HTTP before being redirected, leaving a window for interception on shared networks.



**Fix:** Add the following to the WordPress .htaccess file or install the free plugin Headers Security Advanced and HSTS WP which applies all of these automatically through the WordPress dashboard.

```python
<IfModule mod_headers.c>
  Header always set X-Frame-Options "SAMEORIGIN"
  Header always set X-Content-Type-Options "nosniff"
  Header always set Referrer-Policy "strict-origin-when-cross-origin"
  Header always set Strict-Transport-Security "max-age=31536000; includeSubDomains"
</IfModule>
```



### Issue 2 (Risk Medium)— PHP Version Exposed

Every HTTP response from the server includes , which advertises the exact PHP version to anyone who checks the headers. This serves no purpose for legitimate visitors, but it does make the site a more attractive target if a vulnerability is ever discovered in that specific version.

**Fix:** Add the following two lines to the .htaccess file to suppress the header:

```python
Header unset X-Powered-By
Header always unset X-Powered-By
```



### Issue 3 (Risk Medium)— WordPress and Plugin Versions Visible in Page Source

Viewing the page source reveals the exact version of every major component on the site. The following are directly visible in the HTML:

•	WordPress 7.0 — via a generator meta tag

•	WooCommerce 9.3.3 — via a generator meta tag

•	Elementor 3.25.4 — via a generator meta tag

•	Yoast SEO 23.8 — visible in an HTML comment

•	Over 10 additional plugins — each with their version exposed via ?ver= parameters in stylesheet and script URLs


This creates a complete fingerprint of the site's technology stack. An attacker can cross-reference every version against public vulnerability databases and identify exactly which known CVEs apply — all without sending a single malicious request.



**Fix:** Add the following to the theme's  file. The first block removes the generator tags; the second strips version numbers from all asset URLs.

```python
remove_action('wp_head', 'wp_generator');
function strip_ver($src) {
  if (strpos($src,'ver=')) $src = remove_query_arg('ver',$src);
  return $src; }
add_filter('style_loader_src','strip_ver',9999);
add_filter('script_loader_src','strip_ver',9999);
```


### Responsible Disclosure


After completing the assessment, I contacted Lynwood Support at info@lynwoodsupport.com.au to responsibly disclose the findings. The email outlined each issue in plain language, explained the risks to their clients, and offered to share the specific fixes with their web developer at no cost.
At the time of writing, I have not yet received a response. The full findings and all recommended fixes remain ready to share if they reply.
This activity was carried out entirely within my own Kali Linux virtual machine. No attacks were launched, no data was accessed beyond what any browser can see, and nothing on the site was modified. The purpose was entirely defensive.


![Tailgating example](B22--website-fix-email%20sent.png)

**Figure: Email sent to Lynwood Support**





Tool 1 used: https://securityheaders.com/?q=https%3A%2F%2Flynwoodsupport.com.au%2F&followRedirects=on


Tool 2 used: https://www.ssllabs.com/ssltest/analyze.html?d=lynwoodsupport.com.au

