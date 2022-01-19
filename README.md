**---------- CPE Retriever script v1.1 - by rammam ------------**

_Usage : python3 cpe_retriever.py <INPUT.txt> [apiKey]_

Recommended formatting for the input file :

line 1>GNU Bash 4.3.10

line 2>libarchive 3.3.1

etc..
**--------------------------------------------------------------------**

**Changes :**

v1.1 : Added asynchronous API requests, API key support, and Windows support

v1.0 : Initial version

**--------------------------------------------------------------------**

This Python 3 script gets COTS names and versions from a user-supplied input file, and sends them to the NIST's CPE search API.

The API returns a json response containing the corresponding CPE 2.3 URIs.

Then, the script puts the CPE URIs in a csv output file.

The request rate is about 10/min, and can be increased to 100/min with a NIST API key (obtainable on the NIST's website). 

**-------------------------------------------------------------------**

