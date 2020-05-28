import requests,lxml.html
from lxml import etree

import tkinter as tk
from tkinter import ttk,Entry,Listbox
from tkinter.scrolledtext import ScrolledText

win=tk.Tk()
win.title('GUI')

city_label=ttk.Label(win,text='Select city : ')
city_label.grid(row=4,column=0,sticky=tk.W)

city_var=tk.StringVar()
city_name=Entry(bd=5,textvariable=city_var)
city_name.grid(row=4,column=1,sticky=tk.W)

page_label=ttk.Label(win,text='Select page : ')
page_label.grid(row=5,column=0,sticky=tk.W)

page_var=tk.StringVar()
page_number=Entry(bd=5,textvariable=page_var)
page_number.grid(row=5,column=1,sticky=tk.W)

def getPhoneNo(nodes):
    phoneNo=''
    for node in nodes:
        icon=node.xpath("@class")
        first_icon=icon[0]
        iconsToNumbers=[
            'mobilesv icon-acb','mobilesv icon-yz',
            'mobilesv icon-wx','mobilesv icon-vu',
            'mobilesv icon-ts','mobilesv icon-rq',
            'mobilesv icon-po','mobilesv icon-nm',
            'mobilesv icon-lk','mobilesv icon-ji']
        
        if first_icon in iconsToNumbers:
            phoneNo+=str(iconsToNumbers.index(first_icon))

        signs=['mobilesv icon-dc','mobilesv icon-fe',
               'mobilesv icon-hg','mobilesv icon-ba']

        if first_icon==signs[0]:phoneNo+='+'
        if first_icon==signs[1]:phoneNo+='('
        if first_icon==signs[2]:phoneNo+=')'
        if first_icon==signs[3]:phoneNo+='-'
    return phoneNo

def action1():
    Paragraphs=[]
    count=0
    def fetchUrlAndgivePhoneNo(url):
        
        agent = {"User-Agent":'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36'}
        html = requests.get(url, headers=agent)
        doc = lxml.html.fromstring(html.content)
        el=doc.xpath("//p[@class='contact-info ']")

        for e in el:
            tree=(etree.tostring(e, encoding='unicode'))
            parsed=etree.fromstring(tree)
            nodes1=parsed.xpath('/p/span/a/b/span')
            nodes2=parsed.xpath('/p/span/a/span')
            
            if nodes1 ==[]:
                phoneNo=getPhoneNo(nodes2)
            elif nodes2 ==[]:
                phoneNo=getPhoneNo(nodes1)

            Paragraphs.append(phoneNo)
        return Paragraphs
    url_name='https://www.justdial.com/'+city_var.get()+'/Provision-Stores'+'/page-'+page_var.get()
    phoneNumbers=fetchUrlAndgivePhoneNo(url_name)
    #print(phoneNumbers)
    lbx=Listbox()
    lbx.grid(row=6,column=1)
    textBox = ScrolledText(win, borderwidth=3, relief="sunken")
    textBox.grid(column=0,row=7, columnspan=6, rowspan=1, sticky='W')
    
    for i in range(len(phoneNumbers)):
        lbx.insert(i,phoneNumbers[i])
        textBox.insert(tk.END,phoneNumbers[i]+"\n")
        
    
submit_button=ttk.Button(win,text='get Phone Numbers',command=action1)
submit_button.grid(row=6,column=0)
win.mainloop()

