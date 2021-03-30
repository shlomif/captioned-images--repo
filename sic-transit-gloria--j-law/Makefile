#
# Makefile
# Shlomi Fish, 2021-03-30 21:13
#

CUT_HEIGHT := 1114
HEIGHT_CUT_JLAW := Jennifer_Lawrence_at_San_Diego_Comic-Con_2015--height$(CUT_HEIGHT)px.png
SRC := Jennifer_Lawrence_at_San_Diego_Comic-Con_2015.jpg

WIDTH := 1067
WIDTH := 100%
WIDTH :=

all: $(HEIGHT_CUT_JLAW)

$(HEIGHT_CUT_JLAW): $(SRC)
	# gm convert -crop "100%"x$(CUT_HEIGHT)+0+0 $< $@
	gm convert $< -gravity north -crop "$(WIDTH)"x$(CUT_HEIGHT)+0+0 $@
	# optipng -o7 $@

clean:
	rm -f $(HEIGHT_CUT_JLAW)

view: test
	gwenview $(HEIGHT_CUT_JLAW)

test: clean all
	perl -E 'use Image::Size qw/ imgsize /; my (undef, $$h) = (imgsize(shift)); die "h==$$h" if $$h != shift' -- "$(HEIGHT_CUT_JLAW)" "$(CUT_HEIGHT)"

# vim:ft=make
#
