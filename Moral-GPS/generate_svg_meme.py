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
    TextElement, Tspan
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

        for elem in textlines:
            # handling flowed text nodes
            # fontsize = node.style.get("font-size", "12px")
            # fs = self.svg.unittouu(fontsize)

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

    def set_lines(self, elem, textlines):
        """docstring for set_lines"""

        def _set_childs(elem, nodes):
            elem.remove_all()
            elem.add(*nodes)
        nodes = self.split_lines(elem, textlines)
        _set_childs(elem, nodes)

    def effect(self):
        """Applies the effect"""

        class TextLine:
            """docstring for TextLine"""
            def __init__(self, text, height=16):
                self.height = height
                self.text = text.upper()

        # checks if the selected elements are text nodes
        # for elem in self.svg.selection.get(TextElement, FlowRoot):
        for elem in [self.svg.getElementById("text7731")]:
            if 1:
                elem2 = elem.copy()
            else:
                elem2 = TextElement()

            textlines = []
            textlines.append(TextLine(text="I am not a"))
            textlines.append(TextLine(text="mere moral"))
            textlines.append(TextLine(text="compass!"))
            self.set_lines(elem, textlines)

            textlines = []
            textlines.append(TextLine(text="I am a moral"))
            textlines.append(TextLine(text="Global"))
            textlines.append(TextLine(text="Positioning"))
            textlines.append(TextLine(text="System!"))
            elem2.remove_all()
            self.set_lines(elem2, textlines)

            y = elem2.y + 170
            elem2.set("y", str(y))
            self.svg.add(elem2)


if __name__ == '__main__':
    TextSplit().run()
