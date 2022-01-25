#/usr/bin/python
#CPE Retriever v1.1 - by Theo Thevenin

import sys
import requests
import asyncio
import aiohttp

async def get_cpes(session, url):
	f = open("cots_list.csv", "a")
	async with session.get(url) as resp:
		cpe = await resp.json()
		i = cpe["result"].keys()
		try:
			print(cpe["result"]["cpes"][0]["cpe23Uri"])
			f.write(cpe["result"]["cpes"][0]["cpe23Uri"]+",")
		except:
			pass
	f.close()
		
async def main():
	if len(sys.argv) < 2 or len(sys.argv) > 3:
		raise Exception("Please specify the COTS input file and your NVD API key (optional). Usage : python3 cpe_retriever.py <INPUT.TXT> [apiKey]")
		
	if len(sys.argv) == 3:
		if len(sys.argv[2]) == 36:
			api=sys.argv[2]
			base_url = f"https://services.nvd.nist.gov/rest/json/cpes/1.0?resultsPerPage=1&apiKey={api}&keyword="
		else:
			raise Exception("Please enter a valid NVD API key.")
	else:
		base_url = "https://services.nvd.nist.gov/rest/json/cpes/1.0?resultsPerPage=1&keyword="
	list = open(sys.argv[1], "r", errors="ignore")
	connector = aiohttp.TCPConnector(limit=20)
	async with aiohttp.ClientSession(trust_env=True, connector=connector) as session:
		tasks = []
		for line in list:
			keywords = line
			url = base_url+keywords
			tasks.append(asyncio.ensure_future(get_cpes(session, url)))
		cpe_list = await asyncio.gather(*tasks)
	list.close

if (sys.platform.startswith('win')):
	asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
    
asyncio.run(main())