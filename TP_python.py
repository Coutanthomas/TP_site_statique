import argparse
from pathlib import Path
import os
import glob
import math
import sys


parser = argparse.ArgumentParser()
parser.add_argument("-i", "--input-directory",
                    action="store",
                    type=str,
                    required=True,
                    help="Input directory, containing the markdown files.",
                    )
parser.add_argument("-o", "--output-directory",
                    action="store",
                    type=str,
                    required=True,
                    help="Ouput directory, containing the markdown files translate in html.",
                    )
parser.add_argument("-t", "--template-directory",
                    action="store",
                    type=str,
                    default=None,
                    help="Template directory, containing web pages template.",
                    )
parser.add_argument("-n", "--new-name-template",
                    action="store",
                    type=str,
                    help="Name for your new template, with all files translate.",
                    )
args = parser.parse_args()

### Verification des entrees 

if not os.path.exists(args.input_directory):
    print(args.input_directory + " : The path you chose does not exist. Please make sure you have insert a write input directory")
    sys.exit()

if not os.path.exists(args.output_directory):
    print("creating output_directory " + args.output_directory)
    os.makedirs(args.output_directory)
#else:
    #print(args.output_directory + " The output directory already exist, please enter a new directory name.")
    #sys.exit()
    #print(args.output_directory + " : The path you chose does not exist. Please make sure you have insert a write output directory")


#if not os.path.exists(args.template_directory):
#    print("there are no template selected, you only have a conversion markdown to html")
#else:
#    print("Generate with template " + os.path.basename(args.template_directory))   

list_att = []

def marktohtml(line):
    cont_nb_element_list = "0"
    compteur_list = "1"
    html_line = ""
    if line[:3] == "###":
        html_line = "<h3>" + line[3:].rstrip() + "</h3>"
    elif line[:2] == '##':
        html_line = "<h2>" + line[2:].rstrip() + "</h2>"
    elif line[:1] == "#":
        html_line = "<h1>" + line[1:].rstrip() + "</h1>"
    elif line.count("*") >= 1:
        if line.count("*")%2 == 0:
            html_line = "<em>".join(line.split("*"))
            html_line = html_line.split(" ")
            deb = ""
            tour = []
            cont = []
            new = ""
            new1 = []
            for i in html_line:
                if i[-4:].count("<em>"):
                    deb = deb + "0"
                    new = i[:-4] + "</em>"
                    new1.append(new)
                    cont.append(len(tour))
                tour.append(1)
            k = deb.count("0")
            while k > 0:
                html_line[cont[k-1]] = new1[k-1]
                k -= 1
            html_line = " ".join(html_line)
            print("non")
        else:  
            cont_nb_element_list += 1
            list_att.append(line)
            "".join(list_att)     
    elif line.count("http://") >= 1:
        html_line = line.split(" ")
        tour = []
        cont = []
        toto = ""
        new = ""
        new1 = []
        for i in html_line:
            if i.count("http://"):
                toto = toto + "0"
                new ="<a href=\"" + i + "\">" + i +"</a>"
                new1.append(new)
                cont.append(len(tour))
            tour.append(1)
        k = toto.count("0")
        while k > 0:
            html_line[cont[k-1]] = new1[k-1]
            k -= 1
        html_line = " ".join(html_line)
    else:
        html_line = line
    compteur_list = compteur_list + cont_nb_element_list
    print(compteur_list) 
    return html_line
    

def convert(path):
    convhtml = ""
    with open(path,'r') as f:
        for line in f:
           convhtml = convhtml + marktohtml(line) 
    return convhtml


def newname1(listmd):
    name = ""
    name = name + (os.path.basename(listmd))[:-2] + "html"
    return name


def savnew():
    i = 0
    tr = len(listmd)
    while i < tr:
        with open(args.output_directory + newname1(listmd[i]), "w") as fichier:
            fichier.write(convert(listmd[i]))
        i += 1

def insert_in_template(name_temp):
    cont = len(listmd)
    i = 0
    save = ""
    with open(args.template_directory, "r") as fichier_t:
        for line_t in fichier_t:
            if line_t.count("<REPLACE_ME>"):
                while cont > 0:    
                    with open(args.output_directory + newname1(listmd[cont-1]), "r") as fichier_o:
                        for line_o in fichier_o:
                            save = save + line_o
                        os.remove(args.output_directory + newname1(listmd[cont-1]))
                    cont -= 1
                    i = 1   
            save = save + line_t
    with open(args.output_directory + name_temp + ".html", "w") as fichier_S:
        fichier_S.writelines(save)
    if i != 1:
        print("We don't find <REPLACE_ME>")

listmd = glob.glob(args.input_directory + "/*.md")

if args.template_directory is None:
    print("You don't have chose any template did you just want to translate markdown in html ? (Y/N)")
    if input() == "y":
        print("markdown translate in html on " + args.output_directory)
        savnew()
    else:
        print("exit")
        sys.exit()

if args.template_directory:
    if not args.new_name_template:
        savnew()
        insert_in_template("your_new_template")
        print("Done, with default name: \"your_new_template\"")
    else:
        name_temp = args.new_name_template
        savnew()
        insert_in_template(name_temp)
        print("Done")

