import http.client
import json

PORT = 8000
SERVER = 'localhost'

print("\nConnecting to server: {}:{}\n".format(SERVER, PORT))

# Connect with the server
conn = http.client.HTTPConnection(SERVER, PORT)


#Gene list
conn.request("GET", "/listSpecies?json=1")
r1 = conn.getresponse()
print("Json's response of list species: ")
print("Response received!: {} {}\n".format(r1.status, r1.reason))
data1 = r1.read().decode("utf-8")
response = json.loads(data1)
print (response)
print('')
print('')


#Karyotype
conn.request("GET", "/karyotype?specie=mouse&json=1")
r2 = conn.getresponse()
print("Json's response of karyotype: ")
print("Response received!: {} {}\n".format(r2.status, r2.reason))
data2 = r2.read().decode("utf-8")
response = json.loads(data2)
print (response)
print('')
print('')


#Chromosome length
conn.request("GET", "/chromosomeLength?specie=mouse&chromo=18&json=1")
r3 = conn.getresponse()
print("Json's response of chromosome length:")
print("Response received!: {} {}\n".format(r3.status, r3.reason))
data3 = r3.read().decode("utf-8")
response = json.loads(data3)
print(response)
print('')
print('')


#Gene seq
conn.request("GET", "/geneSeq?gene=FRAT1&json=1")
r4 = conn.getresponse()
print("Json's response of gene seq: ")
print("Response received!: {} {}\n".format(r4.status, r4.reason))
data4 = r4.read().decode("utf-8")
response = json.loads(data4)
print(response)
print('')
print('')


#Gene info
conn.request("GET", "/geneInfo?gene=FRAT1&json=1")
r5 = conn.getresponse()
print("Json's response of gene info: ")
print("Response received!: {} {}\n".format(r5.status, r5.reason))
data5 = r5.read().decode("utf-8")
response = json.loads(data5)
print(response)
print('')
print('')


#Gene cal
conn.request("GET", "/geneCal?gene=FRAT1&json=1")
r6 = conn.getresponse()
print("Json's response of gene cal: ")
print("Response received!: {} {}\n".format(r6.status, r6.reason))
data6 = r6.read().decode("utf-8")
response = json.loads(data6)
print(response)
print('')
print('')


#gene list
conn.request("GET", "/geneList?chromo=1&start=0&end=30000&json=1")
r7 = conn.getresponse()
print("Json's response of gene list: ")
print("Response received!: {} {}\n".format(r7.status, r7.reason))
data7 = r7.read().decode("utf-8")
response = json.loads(data7)
print (response)


