import xmlschema
xdata = r'D:\\xml\\banhang.xml'
xschema = r'D:\\xml\\hanghoa.xsd'
schema = xmlschema.XMLSchema(xschema) 
if schema.is_valid(xdata): 
     print("file xml hợp lệ.")
else:
    print("file xml không hợp lệ.")

      
