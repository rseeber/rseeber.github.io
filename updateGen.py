"""
<h1>Personal Updates:</h1>
                    <br>
                    <h2>New paper about Noncomplience with Cybersecurity standards in Universities and Colleges of USA</h2>
                    <p><em>September 11, 2024</em></p>
                    <p>I recently read a <a href="https://arxiv.org/abs/2409.00546">research paper</a> over on Arxiv.org about cybersecurity in higher education. 
                        The researches found that nearly all higher education institutions are heavily lagging behind in updating their
                        cybersecurity policies as new standards are released by NIST. The paper, published August 2024, found that even high level, 
                        prestigous universities were not up to date with standards even after having nearly 8 years to adjust since they were released in 2016.
                        <br><br>
                        Personally, I find this worrying because of the large number of other nodes that most college email accounts
                        have access to. The fact that even the more prestigous colleges in the US are failing on multiple levels
                        in their stated cybersecurity policies should raise alarm bells for everyone, especially for college students. That's not even to mention
                        the kind of internal issues that institutions are suseptible to due to these failures of policy.
                    </p>
"""
import os.path

def toHTML(text):
    output = ""
    for c in text:
        if (c == '\n'):
            output += "<br>"
        else:
            output += c
    return output


title = input("Enter title: \n> ")
# TODO: automate
date = input("Enter date: \n> ")
# get body from input file
inputFile = open(input("inputFile directory:\n> "), 'r')
body = inputFile.read()
#body = input("Paste body: \n\n> ")

file = ""
salt = 0
#check for collision
while (1):
    #get the unique name from the hash name
    fileName = "update_" + str(hash(title+date+str(salt))) + ".html"
    file = "updatePages/"+fileName
    
    if (not os.path.isfile(file)):
        break
    salt += 1

f = open(file, "x")


html = "<h2>"+title+"</h2>\n"
html += "<p><em>"+date+"</p></em>\n"
body = toHTML(body)
html += "<p>"+body+"</p>"

f.write(html)
print("finished!")