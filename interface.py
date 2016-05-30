#!/usr/bin/python
# -*- coding:utf-8 -*-
import cgi
import cgitb
cgitb.enable()
##############other imports
import basic
import os
############obligatory file topping
os.chdir ('/tmp')
##################################
print ("Content-Type:text/html; charset=utf-8")
print("")
print ("<html><body>")
#############################################getting form data
request = cgi.FieldStorage()# got the form info, if any
#############################################################
#if 


##############################################################
if "copy" in request and "dir1" in request and "dir2"in request:
    directions = [request["dir1"].value, request["dir2"].value]
    basic.framer1 (directions)
    print (''' Done!''')
##############################################################
else:
    print ("List of regex to copy:")
    print ('''<form method="get">''')
##############################################################
#printing True's from the list of regs
    formatsTrue = basic.accessFormats ()
    for i in formatsTrue:
        output_line = \
        '''<input type="checkbox" name={0}, value ={0} checked>{0}<br/>''' 
        output_line = output_line.format(i)
        print (output_line)
##############################################################
#printing False's from the list of regs
    formatsFalse = basic.accessFormats (False) 
    for i in formatsFalse:
        output_line = '''<input type="checkbox" name={0}, value ={0}>{0}<br/>''' 
        output_line = output_line.format(i)
        print (output_line)
##############################################################
        print (''' List of regex not to copy''')
        print ("<br/>")
# printing Trues from the list of nonregs 
    formatsTrue = basic.accessFormats (True, 'nonformats')
    for i in formatsTrue:
        output_line = \
        '''<input type="checkbox" name={0}, value ={0} checked>{0}<br/>''' 
        output_line = output_line.format(i)
        print (output_line)
##############################################################
# printing Falses from the list of nonregs 
    formatsFalse = basic.accessFormats (False, 'nonformats') 
    for i in formatsFalse:
        output_line = '''<input type="checkbox" name={0}, value ={0}>{0}<br/>''' 
        output_line = output_line.format(i)
        print (output_line)


#printing fields for source and target directories
    print ('''
    <input type = "text" name = "dir1"/>from<br/>
    <input type = "text" name = "dir2"/>to<br/>
    <input type="submit" name = "copy" value = "copy"/><br/>''')

##############################################################
    print ('''</form>''')
    

print ("</body></html>")
