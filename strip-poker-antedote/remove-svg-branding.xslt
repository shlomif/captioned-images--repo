<xsl:stylesheet version = '1.0'
    xmlns="http://www.w3.org/1999/xhtml"
    xmlns:h="http://www.w3.org/1999/xhtml"
    xmlns:svg="http://www.w3.org/2000/svg"
    xmlns:xhtml="http://www.w3.org/1999/xhtml"
    xmlns:xsl='http://www.w3.org/1999/XSL/Transform'
    >

    <xsl:output method="xml" version="1.0" encoding="UTF-8" indent="yes" />

    <xsl:template match="/">
        <xsl:apply-templates select="node()|@*"/>
    </xsl:template>

    <xsl:template match="node()|@*">
        <xsl:copy>
            <xsl:apply-templates select="node()|@*"/>
        </xsl:copy>
    </xsl:template>

    <xsl:template match="//svg:text[./svg:tspan[text() = 'shlomifish.org']]">
    </xsl:template>

</xsl:stylesheet>
