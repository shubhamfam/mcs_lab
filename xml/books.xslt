<xsl:template match="/">
  <html>
  <body>
    <h2>Book Store</h2>
    <table border="1">
      <tr bgcolor="#9acd32">
        <th>Title</th>
        <th>Author</th>
        <th>Price</th>
        <th>Year</th>
      </tr>
      <xsl:for-each select="catalog/cd">
      <tr>
        <td><xsl:value-of select="TITLE" /></td>
        <td><xsl:value-of select="ARTIST" /></td>
        <td><xsl:value-of select="PRICE" /></td>
        <td><xsl:value-of select="YEAR" /></td>
      </tr>
      </xsl:for-each>
    </table>
  </body>
  </html>
</xsl:template>
</xsl:stylesheet>