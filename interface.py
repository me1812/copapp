#!/usr/bin/python
# -*- coding:utf-8 -*-
import cgi
import cgitb
cgitb.enable()
##############other imports
import basic
############obligatory file topping
print ("Content-Type:text/html; charset=utf-8")
print()
print ("<html><body>")
#############################################getting form data
request = cgi.FieldStorage()# got the form info, if any
#############################################################
if 


##############################################################
if "copy" in request and "dir1" in request and "dir2"in request:
    basic.framer1 (request["dir1".value], request["dir2".value]) 
    print (''' Done!''')
    #print ('''<form method="get">
    #<input type = "text" name = "dir1"/><br/>
    #<input type = "text" name = "dir2"/><br/>
    #<input type="submit" name = "copy" value = "copy"/><br/>
    #<input type ="submit" name = "newList" value = "New List"/><br/>
    #<input type ="submit" name = "default" value="Default List"/><br/>
    #<input type "submit" name = "add" value = "Add Item"/><br/>
    #<input type "submit" name = "delete" value = "Delete Item"/><br/>
    #
    #</form>''')
else:
    #formats = basic.accessFormats (items_to_display = False)
    #print ('''<form method="get">''')
    #for i in formats:
    #    print ('''<input type = checkbox ''')
    <input type = "text" name = "dir1"/><br/>
    <input type = "text" name = "dir2"/><br/>
    <input type="submit" name = "copy" value = "copy"/><br/>
    </form>''')

print "</body></html>"
