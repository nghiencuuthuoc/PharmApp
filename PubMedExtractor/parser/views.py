from django.http import HttpResponse
from django.shortcuts import render
from django.http import HttpResponse
#from urllib import request as response
from bs4 import BeautifulSoup as bs
import re
import requests
import xlsxwriter
import io
# Create your views here.

#Function to Load Home Page
def home(request):
    return render(request,'home.html');

def getHTMLdocument(url):
    response=requests.get(url)
    return response.text

#Fuction to Render and extract
def parse(request):
  searchText=request.POST['wikilink']
  pagecount=request.POST['nos']
  pages=0
  url="https://pubmed.ncbi.nlm.nih.gov/?term="+searchText+"&page="+str(pages)
  title=[]
  author=[]
  cite=[]
  abstractUrls=[]
  abstract=[]
  
  while True:
    html_doc=getHTMLdocument(url)
    soupObject=bs(html_doc,'html.parser')
    
    #Extracting Title
    titleContents=soupObject.findAll('a',class_='docsum-title',href=True)
    for titleContent in titleContents:
        title.append(titleContent.text)
    
    #EXtracting Authors    
    authorContents=soupObject.findAll('span',class_='docsum-authors full-authors')
    for authorContent in authorContents:
        author.append(authorContent.text)
    
   #EXtracting Cite    
    citeContents=soupObject.findAll('span',class_='docsum-journal-citation full-journal-citation')
    for citeContent in citeContents:
        cite.append(citeContent.text)
        
    #Getting Abstract
    for link in soupObject.findAll('a',class_='docsum-title'):
        abstractUrls.append(link.get('href'))
    
    for items in abstractUrls:
        abstract.append(getAbstract(items))
    
    pages=pages+1
    url="https://pubmed.ncbi.nlm.nih.gov/?term="+searchText+"&page="+str(pages)
    
    
    if(pages==int(pagecount)+1):
        break
    
  zipped=zip(title,author,cite,abstract)
  
  global dataZip
  def dataZip():
    title.insert(0,"Title")
    author.insert(0,"Author(s)")
    abstract.insert(0,"Abstract")
    cite.insert(0,"Citation")
    pipe=[title,author,abstract,cite]
    return pipe
     
  return render(request,'summary.html',{'print':zipped});

#get Abstract from each page
def getAbstract(siteUrl):
    
    siteUrl="https://pubmed.ncbi.nlm.nih.gov/"+siteUrl
    
    html_doc=getHTMLdocument(siteUrl)
    soupObject=bs(html_doc,'html.parser')
    abstract=[]
    
    #Extracting Title
    abstractContents=soupObject.find('div',class_='abstract-content selected')
    if(abstractContents==None):
        return abstractContents
    else:
        return abstractContents.text


def xlMaker(request):
        output = io.BytesIO()      
        workbook = xlsxwriter.Workbook(output)
        worksheet = workbook.add_worksheet()

        data = dataZip()
        data=zip(data[0],data[1],data[2],data[3])
        row=0
        column=0

        for v,x,y,z in data:
            worksheet.write(row,column,v)
            worksheet.write(row,column+1,x)
            worksheet.write(row,column+2,y)
            worksheet.write(row,column+3,z)
            row+=1
    
        # Close the workbook before sending the data.
        workbook.close()
        # Rewind the buffer.
        output.seek(0)
        # Set up the Http response.
        filename = 'data_Extract.xlsx'
        response = HttpResponse(
            output,
            content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'
        )
        response['Content-Disposition'] = 'attachment; filename=%s' % filename

        return response    