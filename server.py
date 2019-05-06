import http.server
import socketserver
import termcolor
import json
import http.client
from Seq import Seq



# Define the Server's port

PORT = 8000





# Class with our Handler. It is a called derived from BaseHTTPRequestHandler

# It means that our class inheritates all his methods and properties

class TestHandler(http.server.BaseHTTPRequestHandler):


    def split_arguments(self,path):
        dictionare= dict()
        if '?' in path:
            arguments=path.split('?')[1]
            arguments_lists=arguments.split('&')
            for argument in arguments_lists:
                if '=' in argument:
                    dictionare[argument.split('=')[0]] = argument.split('=')[1]
        return dictionare






    def do_GET(self):

        code=200

        json_answer= False

        """This method is called whenever the client invokes the GET method

        in the HTTP protocol request"""
        # Print the request line
        termcolor.cprint(self.requestline, 'green')


        if self.path == "/" or self.path =="/index3.html":
            with open("index3.html","r") as f:
                contents = f.read()



        elif '/listSpecies' in self.path:
            try:
                parameters=''
                specie = ''

                if specie in parameters:
                    parameters = self.split_arguments(self.path)
                    if 'limit' in parameters:
                        try:
                            limit=int(parameters['limit'])
                        except:
                            limit= 0
                    else:
                        limit= 0

                    if limit!=0:
                        user_limit=self.path.split('?')[1].split("limit=")[1].split('&')[0]
                        print(user_limit)
                        conn = http.client.HTTPConnection('rest.ensembl.org')
                        conn.request("GET", "/info/species?content-type=application/json")
                        r1 = conn.getresponse()
                        print()
                        print("Response received: ", end='')
                        print(r1.status, r1.reason)
                        text_json = r1.read().decode("utf-8")
                        response = json.loads(text_json)
                        list_species = response['species']
                        conn.close()


                        if 'json' in parameters:
                            try:
                                json_answer=True
                                new_list=list_species[1:limit]
                                contents=json.dumps(list_species)

                            except KeyError:
                                code = 400
                                with open('error.html', 'r') as f:
                                    contents = f.read()

                            except TypeError:
                                code = 400
                                with open('error.html', 'r') as f:
                                    contents = f.read()

                        else:
                            contents = """
                                               <html>
                                               <body style= "background-color:mediumaquamarine">
                                               <ol>"""
                        cont = 0


                        for specie in list_species:
                            contents = contents + "<li>" + specie['display_name'] + "</li>"
                            cont = cont + 1
                            if (cont == int (user_limit)):
                                break

                            contents = contents + """
                                               </ol>
                                               </html>
                                               </body>
                                               """
                    else:
                        conn = http.client.HTTPConnection('rest.ensembl.org')
                        conn.request("GET", "/info/species?content-type=application/json")
                        r1 = conn.getresponse()
                        print()
                        print("Response received: ", end='')
                        print(r1.status, r1.reason)
                        text_json = r1.read().decode("utf-8")
                        response = json.loads(text_json)
                        list_species = response['species']
                        conn.close()
                        contents = """
                                               <html>
                                               <body style= "background-color:mediumaquamarine">
                                               <ol>"""

                        for specie in list_species:
                            contents = contents + "<li>" + specie['display_name'] + "</li>"
                            contents = contents + """
                                               </ol>
                                               </html>
                                               </body>
                                               """

                        if 'json' in parameters:
                            try:
                                json_answer = True
                                contents = json.dumps(list_species)

                            except KeyError:
                                code = 400
                                with open('error.html', 'r') as f:
                                    contents = f.read()

                            except TypeError:
                                code = 400
                                with open('error.html', 'r') as f:
                                    contents = f.read()


            except KeyError:
                code = 400
                with open('error.html','r') as f:
                    contents=f.read()

            except TypeError:
                code = 400
                with open('error.html','r') as f:
                    contents=f.read()





        elif 'karyotype' in self.path:
            try:
                parameters = self.split_arguments(self.path)

                if 'specie' in parameters:
                    specie = parameters['specie']
                    conn = http.client.HTTPConnection('rest.ensembl.org')
                    conn.request("GET", "/info/assembly/"+specie+"?content-type=application/json")
                    r1 = conn.getresponse()
                    text_json2 = r1.read().decode("utf-8")
                    response2 = json.loads(text_json2)
                    list_chromosomes = response2['karyotype']

                    if 'json' in parameters:
                        try:
                            json_answer=True
                            print(list_chromosomes)
                            contents=json.dumps(list_chromosomes)

                        except KeyError:
                            code = 400
                            with open('error.html', 'r') as f:
                                contents = f.read()

                        except TypeError:
                            code = 400
                            with open('error.html', 'r') as f:
                                contents = f.read()


                    else:
                        contents = """
                                                             <html>
                                                               <body style= "background-color:mediumaquamarine">
                                                               <ul>"""

                        for number in list_chromosomes:
                            contents = contents + "<li>" + number + "</li>"
                            contents = contents + """

                                                           </ul>
                                                           </html>
                                                           </body>"""

                else:
                    code = 400
                    with open('error.html', 'r') as f:
                        contents = f.read()


            except KeyError:
                code = 400
                with open('error.html','r') as f:
                    contents=f.read()

            except TypeError:
                codigo = 400
                with open('error.html','r') as f:
                    contents=f.read()




        elif '/chromosomeLength' in self.path:
            try:
                parameters = self.split_arguments(self.path)
                if len(parameters)> 1:
                    specie= parameters['specie']
                    chromo= parameters['chromo']
                    print (specie)
                    print (chromo)
                    conn = http.client.HTTPConnection('rest.ensembl.org')
                    conn.request("GET", "/info/assembly/" + specie + "?content-type=application/json")
                    r1 = conn.getresponse()
                    text_json3 = r1.read().decode("utf-8")
                    response3 = json.loads(text_json3)
                    chromosome_length = response3['top_level_region']

                    if 'json' in parameters:
                        try:
                            json_answer = True
                            print(chromosome_length)
                            contents = json.dumps(chromosome_length)

                        except KeyError:
                            code = 400
                            with open('error.html', 'r') as f:
                                contents = f.read()

                        except TypeError:
                            code = 400
                            with open('error.html', 'r') as f:
                                contents = f.read()

                    else:
                        chro_length=0
                        for element in chromosome_length:
                            if (element['name']== chromo):
                                chro_length = str(element['length'])
                        contents = """
                                                                   <html>
                                                                   <body style= "background-color:mediumaquamarine">
                                                                   <ul>"""
                        contents = contents + "<li>" + chro_length + "</li>"
                        contents = contents + """
                                                                  </ul>
                                                                   </html>
                                                                   </body>
                                                                   """
                else:
                    code = 400
                    with open('error.html', 'r') as f:
                        contents = f.read()


            except KeyError:
                code = 400
                with open('error.html','r') as f:
                    contents=f.read()

            except TypeError:
                code = 400
                with open('error.html','r') as f:
                    contents=f.read()







        elif '/geneSeq'  in self.path:
            try:
                parameters = self.split_arguments(self.path)
                gene=parameters['gene']
                conn = http.client.HTTPConnection('rest.ensembl.org')
                conn.request("GET", "/homology/symbol/human/" + gene + "?content-type=application/json")
                print ("/homology/symbol/human/" + gene + "?content-type=application/json")
                r1 = conn.getresponse()
                text_json4 = r1.read().decode("utf-8")
                print (text_json4)
                response4 = json.loads(text_json4)
                id = response4['data'][0]['id']
                conn.request("GET", "/sequence/id/" + id + "?content-type=application/json")
                r1 = conn.getresponse()
                text_json41 = r1.read().decode("utf-8")
                print(text_json41)
                response41 = json.loads(text_json41)
                chain = response41['seq']

                if 'json' in parameters:
                    try:

                        json_answer = True
                        info = dict()
                        info['seq'] = chain
                        print(chain)
                        contents = json.dumps(info)

                    except KeyError:
                        code = 400
                        with open('error.html', 'r') as f:
                            contents = f.read()

                    except TypeError:
                        code = 400
                        with open('error.html', 'r') as f:
                            contents = f.read()

                else:
                    contents = """
                                                                   <html>
                                                                   <body style= "background-color:mediumaquamarine">
                                                                   <ul>"""
                    contents = contents + "<li>" + chain + "</li>"
                    contents = contents + """
                                                                   </ul>
                                                                   </html>
                                                                   </body>
                                                                   """

            except KeyError:
                code = 400
                with open('error.html','r') as f:
                    contents=f.read()

            except TypeError:
                code = 400
                with open('error.html','r') as f:
                    contents=f.read()



        elif '/geneInfo' in self.path:
            try:
                parameters = self.split_arguments(self.path)
                gene = parameters['gene']
                conn = http.client.HTTPConnection('rest.ensembl.org')
                conn.request("GET", "/homology/symbol/human/" + gene + "?content-type=application/json")
                print("/homology/symbol/human/" + gene + "?content-type=application/json")
                r1 = conn.getresponse()
                text_json5 = r1.read().decode("utf-8")
                print(text_json5)
                response5 = json.loads(text_json5)
                id = response5['data'][0]['id']
                conn.request("GET", "/overlap/id/" + id + "?feature=gene;content-type=application/json")
                r1 = conn.getresponse()
                text_json51 = r1.read().decode("utf-8")
                response51 = json.loads(text_json51)

                if 'json' in parameters:
                    try:
                        json_answer = True
                        start = response51[0]['start']
                        end = response51[0]['end']
                        identify = response51[0]['id']
                        length = end - start
                        chromo = response51[0]['seq_region_name']
                        info = dict()
                        info['start']=start
                        info['end'] = end
                        info['identify'] = identify
                        info['length'] = length
                        info['chromo'] = chromo
                        contents = json.dumps(info)

                    except KeyError:
                        code = 400
                        with open('error.html', 'r') as f:
                            contents = f.read()

                    except TypeError:
                        code = 400
                        with open('error.html', 'r') as f:
                            contents = f.read()

                else:
                    start = response51[0]['start']
                    end = response51[0]['end']
                    identify = response51[0]['id']
                    length = end - start
                    chromo = response51[0]['seq_region_name']
                    contents = """
                                          <html>
                                            <body style = "background-color:mediumaquamarine;">
                                            <ul><font >ID: """+ str(identify)+"""</font></ul>
                                            <ul><font >Start: """+ str(start)+"""</font></ul>
                                            <ul><font >End: """ + str(end)+ """</font></ul>
                                            <ul><font >Lenght: """ + str(length)+ """</font></ul>    
                                            <ul><font >Chromosome: """+ chromo+ """</font></ul>
                                            </body>
                                            </html>
                                                                        """

            except KeyError:
                code = 400
                with open('error.html','r') as f:
                    contents=f.read()

            except TypeError:
                code = 400
                with open('error.html','r') as f:
                    contents=f.read()




        elif '/geneCalc' in self.path:
            try:
                parameters = self.split_arguments(self.path)
                gene = parameters['gene']
                conn = http.client.HTTPConnection('rest.ensembl.org')
                conn.request("GET", "/homology/symbol/human/" + gene + "?content-type=application/json")
                print("/homology/symbol/human/" + gene + "?content-type=application/json")
                r1 = conn.getresponse()
                text_json6 = r1.read().decode("utf-8")
                print(text_json6)
                response6 = json.loads(text_json6)
                id = response6['data'][0]['id']
                conn.request("GET", "/sequence/id/" + id + "?content-type=application/json")
                r1 = conn.getresponse()
                text_json61 = r1.read().decode("utf-8")
                print(text_json61)
                response61 = json.loads(text_json61)
                chain = response61['seq']
                s1=Seq(chain)
                total_length=len(chain)
                percA = s1.perc('A')
                percC = s1.perc('C')
                percG = s1.perc('G')
                percT = s1.perc('T')

                if 'json' in parameters:
                    try:
                        json_answer = True
                        info = dict ()
                        info['percA']=percA
                        info['percC'] = percC
                        info['percG'] = percG
                        info['percT'] = percT
                        info['total_length'] = total_length
                        contents = json.dumps(info)

                    except KeyError:
                        code = 400
                        with open('error.html', 'r') as f:
                            contents = f.read()

                    except TypeError:
                        code = 400
                        with open('error.html', 'r') as f:
                            contents = f.read()

                else:
                    contents = """
                                                      <html>
                                                        <body style = "background-color:mediumaquamarine;">
                                                        <ul><font >Total length of the Gene: """ + str(total_length) + """</font></ul>
                                                        <ul><font >Perc of A: """ + str(percA) + """%</font></ul>
                                                        <ul><font >Perc of C: """ + str(percC) + """%</font></ul>
                                                        <ul><font >Perc of G: """ + str(percG) + """%</font></ul>
                                                        <ul><font >Perc of T: """ + str(percT) + """%</font></ul>
                                                        </body>
                                                        </html>"""

            except KeyError:
                code = 400
                with open('error.html','r') as f:
                    contents=f.read()

            except TypeError:
                code = 400
                with open('error.html','r') as f:
                    contents=f.read()



        elif '/geneList' in self.path:
            try:
                parameters = self.split_arguments(self.path)
                chromo = parameters['chromo']
                start=parameters['start']
                end=parameters['end']
                conn = http.client.HTTPConnection('rest.ensembl.org')
                conn.request("GET", "/overlap/region/human/" + str(chromo) + ":" + str(start) + "-" + str(end) + "?content-type=application/json;feature=gene;feature=transcript;feature=cds;feature=exon")
                r1 = conn.getresponse()
                text_json7 = r1.read().decode("utf-8")
                response7 = json.loads(text_json7)
                print(response7)

                if 'json' in parameters:
                    try:
                        variable = ''
                        json_answer=True
                        response_list=[]
                        for i in response7:
                            if (i['feature_type']== "gene"):
                                variable = (str(i['external_name']) + " " + str(i['start']) + " " + str(i['end']))
                                response_list.append(variable)
                        contents = json.dumps(response_list)

                    except KeyError:
                        code = 400
                        with open('error.html', 'r') as f:
                            contents = f.read()

                    except TypeError:
                        code = 400
                        with open('error.html', 'r') as f:
                            contents = f.read()

                else:
                    contents = """
                                                                               <html>
                                                                               <body style= "background-color:mediumaquamarine">
                                                                               <ul>                                             
                                                                                            """

                    for i in response7:
                        if (i['feature_type'] == "gene"):
                            contents = contents + "<li>" + (str(i['external_name']) + " " + str(i['start']) + " " + str(i['end'])) + "</li>"
                            contents = contents + """</ul></body></html>"""


            except KeyError:
                code = 400
                with open('error.html','r') as f:
                    contents=f.read()

            except TypeError:
                code = 400
                with open('error.html','r') as f:
                    contents=f.read()






        else:
            code = 404
            with open("error.html","r") as f:
                contents = f.read()




        # Generating the response message
        self.send_response(code)  # -- Status line: OK!
        # Define the content-type header:

        if (json_answer):
            self.send_header('Content-Type','application/json')
        else:
            self.send_header('Content-Type', 'text/html')



        self.send_header('Content-Length', len(str.encode(contents)))

        # The header is finished
        self.end_headers()
        # Send the response message
        self.wfile.write(str.encode(contents))
        return


# ------------------------

# - Server MAIN program
# ------------------------
# -- Set the new handler
Handler = TestHandler
socketserver.TCPServer.allow_reuse_address = True
# -- Open the socket server
with socketserver.TCPServer(("", PORT), Handler) as httpd:



    print("Serving at PORT", PORT)



    # -- Main loop: Attend the client. Whenever there is a new

    # -- clint, the handler is called

    try:

        httpd.serve_forever()

    except KeyboardInterrupt:

        print("")

        print("Stoped by the user")

        httpd.server_close()
print("")
print("Server Stopped")