#!/usr/bin/env python
# coding=utf-8
#
# Based on Inkscape's text_split.py .
# Shlomi Fish puts all his changes under CC0 .
#
# Copyright (C) 2009 Karlisson Bezerra, contato@nerdson.com
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA
# 02110-1301, USA.
#

import inkex
from inkex import (
    TextElement, FlowRoot, Tspan, Rectangle
)


class TextSplit(inkex.EffectExtension):
    """Split text up."""
    def add_arguments(self, pars):
        pars.add_argument(
            "--tab",
            help="The selected UI-tab when OK was pressed")
        pars.add_argument(
            "-s", "--splittype", default="word", help="type of split")
        pars.add_argument(
            "-p", "--preserve", type=inkex.Boolean, default=True,
            help="Preserve original")

    def split_lines(self, node, textlines):
        """Returns a list of lines"""
        lines = []
        count = 1

        for elem in node:
            pass

        text = TextElement(**node.attrib)

        for elem in textlines:
            # handling flowed text nodes
            if 1:  # isinstance(node, FlowRoot):
                fontsize = node.style.get("font-size", "12px")
                fs = self.svg.unittouu(fontsize)

                # selects the flowRegion's child (svg:rect) to get @X and @Y
                if 0:
                    flowref = node.findone('svg:flowRegion')[0]

                    if isinstance(flowref, Rectangle):
                        text.set("x", flowref.get("x"))
                        text.set(
                            "y", str(
                                float(flowref.get("y")) + fs * count))
                        count += 1
                    else:
                        inkex.debug(
                            "This type of text element isn't supported. "
                            "First unflow text.")
                        break

                # now let's convert flowPara into tspan
                tspan = Tspan()
                tspan.set("sodipodi:role", "line")
                tspan.text = elem.text
                x = node.get("x")
                y = node.get("y")
                tspan.set("x", x)
                tspan.set("y", y)
                lines.append(tspan)

            # lines.append(text)

        return lines

    def split_words(self, node):
        """Returns a list of words"""
        words = []

        # Function to recursively extract text
        def plain_str(elem):
            words = []
            if elem.text:
                words.append(elem.text)
            for n in elem:
                words.extend(plain_str(n))
                if n.tail:
                    words.append(n.tail)
            return words

        # if text has more than one line, iterates through elements
        lines = self.split_lines(node)
        if not lines:
            return words

        for line in lines:
            # gets the position of text node
            x = float(line.get("x"))
            y = line.get("y")

            # gets the font size. if element doesn't have a style attribute,
            # it assumes font-size = 12px
            fontsize = line.style.get("font-size", "12px")
            fs = self.svg.unittouu(fontsize)

            # extract and returns a list of words
            words_list = "".join(plain_str(line)).split()
            prev_len = 0

            # creates new text nodes for each string in words_list
            for word in words_list:
                tspan = Tspan()
                tspan.text = word

                text = TextElement(**line.attrib)
                tspan.set('sodipodi:role', "line")

                # positioning new text elements
                x = x + prev_len * fs
                prev_len = len(word)
                text.set("x", str(x))
                text.set("y", str(y))

                text.append(tspan)
                words.append(text)

        return words

    def split_letters(self, node):
        """Returns a list of letters"""

        letters = []

        words = self.split_words(node)
        if not words:
            return letters

        for word in words:

            x = float(word.get("x"))
            y = word.get("y")

            # gets the font size. If element doesn't have a style
            # attribute, it assumes font-size = 12px
            fontsize = word.style.get("font-size", "12px")
            fs = self.svg.unittouu(fontsize)

            # for each letter in element string
            for letter in word[0].text:
                tspan = Tspan()
                tspan.text = letter

                text = TextElement(**node.attrib)
                text.set("x", str(x))
                text.set("y", str(y))
                x += fs

                text.append(tspan)
                letters.append(text)
        return letters

    def set_lines(self, elem, textlines):
        """docstring for set_lines"""

        def _set_childs(elem, nodes):
            elem.remove_all()
            elem.add(*nodes)
        nodes = self.split_lines(elem, textlines)
        _set_childs(elem, nodes)

    def effect(self):
        """Applies the effect"""

        split_type = self.options.splittype
        split_type = "line"
        preserve = self.options.preserve

        class TextLine:
            """docstring for TextLine"""
            def __init__(self, text, height=16):
                self.height = height
                self.text = text

        # checks if the selected elements are text nodes
        for elem in self.svg.selection.get(TextElement, FlowRoot):
            pass
        # for elem in self.svg.get(TextElement, FlowRoot):
        for elem in [self.svg.getElementById("text7731")]:
            if split_type == "line":
                # elem2 = elem.clone()
                if 1:
                    elem2 = elem.copy()
                else:
                    elem2 = TextElement()
                # elem2.id("text2")
                textlines = []
                textlines.append(TextLine(text="I AM NOT A"))
                textlines.append(TextLine(text="MERE MORAL"))
                textlines.append(TextLine(text="COMPASS!"))
                self.set_lines(elem, textlines)

                textlines = []
                textlines.append(TextLine(text="I AM A MORAL"))
                textlines.append(TextLine(text="GLOBAL"))
                textlines.append(TextLine(text="POSITIONING"))
                textlines.append(TextLine(text="SYSTEM!"))
                elem2.remove_all()
                self.set_lines(elem2, textlines)

                y = elem2.y + 170
                elem2.set("y", str(y))
                self.svg.add(elem2)
            elif split_type == "word":
                nodes = self.split_words(elem)
            elif split_type == "letter":
                nodes = self.split_letters(elem)

            # preserve original element
            if False:
                if not preserve and nodes:
                    parent = elem.getparent()
                    parent.remove(elem)
        # assert 0


if __name__ == '__main__':
    TextSplit().run()
