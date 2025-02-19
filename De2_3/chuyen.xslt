<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet xmlns:xsl="http://www.w3.org/1999/XSL/Transform" version="2.0">
    <xsl:output method="html" indent="yes" encoding="UTF-8"/>
     <xsl:template match = "/">
        <html>
          <body>
             <table border = "1">
                 <tr>
                   <th>mã nhân viên</th>
                   <th>mã dự án</th>
                   <th>ngày nghiêm thu</th>
                   <th>đánh giá</th>
                             
                 </tr>

               <xsl:for-each select="QLDA/nvda">
                    <xsl:if test="danhgia = 'đạt'">
                        <tr>
                            <td><xsl:value-of select="manv"/></td>
                            <td><xsl:value-of select="mada"/></td>
                            <td><xsl:value-of select="date"/></td>
                            <td><xsl:value-of select="danhgia"/></td>
                        </tr>
                    </xsl:if>
                </xsl:for-each>

             </table>
          
          
          </body>
        
        </html>
          
     </xsl:template>
</xsl:stylesheet>