LOGIN="/service/api/login"

import urllib.request, urllib.parse
import json
import datetime
from xml.dom.minidom import parse
import xml.dom.minidom



class Cmis:
    def __init__(self,configfile):
        self.ticket = None
        if configfile:
            from importlib.machinery import SourceFileLoader
            config = SourceFileLoader("gdaconfig", "/etc/gda/config.py" ).load_module()
            
            self.host = config.alfrescoconfig['hostname']
            self.port = config.alfrescoconfig['port']
            self.username = config.alfrescoconfig['username']
            self.password = config.alfrescoconfig['password']
        else:
            self.host = 'localhost'
            self.port = '8080'
            self.username = 'admin'
            self.password = 'password'            
            

    def composeURL(self, url):
        composedurl = 'http://%s:%s/alfresco%s' % (self.host, self.port, url)

        return composedurl
    
    def login(self):
        data = {
            'username' : self.username,
            'password' : self.password
        }

        data = json.dumps(data).encode('utf8')
              
        loginurl=self.composeURL(LOGIN)
        
        req  = urllib.request.Request( loginurl, data=data, headers={'content-type': 'application/json'})
        try:
            resp = urllib.request.urlopen(req)
        except:
            print('Connection error')
            return False

        resp=json.loads(resp.read().decode('utf8'))
        self.ticket = resp['data']['ticket']
        return True

    def getDocPath(self, filename, data):
        path = data.strftime('%Y/%m/%d/')+filename
        return path
        
    

    def getChilds(self,protopath):
        url = '/service/cmis/p/Siti/protocollo/documentLibrary/' + protopath + '/children?alf_ticket=' + self.ticket

        childurl = self.composeURL(url)

        items = []
        i=0
        
        try:
            req = urllib.request.Request( childurl )
       
            resp = urllib.request.urlopen(req)
            resp = resp.read().decode('utf8')
        except urllib.error.HTTPError:
            print('alfresco objet not found %s' % childurl)
            return items
            
      
        dom = xml.dom.minidom.parseString(resp)

        for entry in dom.getElementsByTagName("entry"):
            item = {}
            for title in entry.getElementsByTagName("title"):
                title=title.firstChild.wholeText

            for path in entry.getElementsByTagName("cmisra:pathSegment"):
                path=path.firstChild.wholeText

            item['title']=title
            item['path']=path          
#            item['quotedpath']=urllib.parse.quote_plus(protopath+'/'+path)
            item['cmispath']=protopath+'/'+path
            item['id']=i
            i=i+1

            items.append(item)

        return items

    def getFile(self,path):
        url = '/service/cmis/p/Siti/protocollo/documentLibrary/' + urllib.parse.quote(path) + '/content?alf_ticket=' + self.ticket

        fileurl = self.composeURL(url)

        req = urllib.request.Request(fileurl)
               
        resp = urllib.request.urlopen(req)

        resp = resp.read()

        return resp
                

if __name__ == "__main__":
  
    cmis = Cmis('/etc/gda/config.py')
    if not cmis.login():
        print('out')
        exit(1)

    protodata = datetime.date(2018, 2, 26)
    path = cmis.getDocPath('201800007774',protodata)
    files=cmis.getChilds(path)
#    print(files)

    for f in files:
        print(cmis.getFile(f['cmispath']))
    


