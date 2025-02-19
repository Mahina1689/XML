from lxml import etree
xmlfile = r'D:\xml\cau2duan\thamgia.xml'
xsltfile = r'D:\xml\cau2duan\chuyen.xslt'
xml = etree.parse(xmlfile)
xslt = etree.parse(xsltfile)
biendoi = etree.XSLT(xslt)
kq = biendoi(xml)
outra = r'D:\xml\cau2duan\inra.html'
with open (outra, 'wb') as opf:
    opf.write(etree.tostring(kq, pretty_print = True))
print("chuyển đổi thành công")