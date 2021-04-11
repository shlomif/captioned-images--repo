#
# Makefile
# Shlomi Fish, 2021-03-30 21:13
#

CUT_HEIGHT := 1114
HEIGHT_CUT_JLAW := Jennifer_Lawrence_at_San_Diego_Comic-Con_2015--height$(CUT_HEIGHT)px.png
SRC := Jennifer_Lawrence_at_San_Diego_Comic-Con_2015.jpg
SVG := sic-transit-gloria--j-law--Demotivational_Poster.svg
PNG := $(SVG).png
JPEG := $(SVG).jpg
WEBP := $(SVG).webp

WIDTH = 600
CUT_WIDTH := $(shell imgsize -r "$(SRC)" | perl -lnaE 'print $$F[0]')
# WIDTH := 100%
# WIDTH :=

all: $(PNG) $(JPEG) $(WEBP) $(HEIGHT_CUT_JLAW)

$(HEIGHT_CUT_JLAW): $(SRC)
	# gm convert -crop "100%"x$(CUT_HEIGHT)+0+0 $< $@
	gm convert $< -gravity north -crop "$(CUT_WIDTH)"x$(CUT_HEIGHT)+0+0 $@
	# optipng -o7 $@

$(PNG): $(SVG) $(PHOTO_DEST) $(HEIGHT_CUT_JLAW)
	inkscape --export-png=$@ --export-width=$(WIDTH) $<
	optipng $@

$(WEBP): $(PNG)
	gm convert $< $@

$(JPEG): $(PNG)
	gm convert $< $@

clean:
	rm -f $(HEIGHT_CUT_JLAW)

view: test
	gwenview $(HEIGHT_CUT_JLAW)

test: clean all
	perl -E 'use Image::Size qw/ imgsize /; my (undef, $$h) = (imgsize(shift)); die "h==$$h" if $$h != shift' -- "$(HEIGHT_CUT_JLAW)" "$(CUT_HEIGHT)"

# vim:ft=make
#
