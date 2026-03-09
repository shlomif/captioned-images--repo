WIDTH = 600

BASE = pesek-zman-logo-rotated
SVG = $(BASE).svg
DESTBASE = $(BASE)-$(WIDTH)
DESTBASE_default = $(SVG)
PNG = $(DESTBASE).png
JPEG = $(DESTBASE).jpg
WEBP = $(DESTBASE).webp

EMBEDDED_PHOTO1__PATH = 72917893-cropped.png

all: $(PNG) $(JPEG) $(WEBP)
# all: $(NOBRANDING_PERSON_PNG) $(NOBRANDING_PERSON_WEBP) $(NOBRANDING_PERSON_JPEG) $(NOBRANDING_PERSON_PNG)

# SCRIPT = generate_svg_meme.py

$(SVG): source.svg
	# PYTHONPATH="/usr/share/inkscape/extensions/" python3 $(SCRIPT) $< > $@
	cp -f $< $@

$(PNG): $(SVG) $(EMBEDDED_PHOTO1__PATH)
	inkscape --export-filename=$@ --export-width=$(WIDTH) $<
	optipng $@

$(EMBEDDED_PHOTO1__PATH): 72917893.png
	magick $< -gravity Center -crop 446x100+0+0 $@

all: $(EMBEDDED_PHOTO1__PATH)

p.svg: $(SVG)
	# xsltproc -o $@ remove-svg-branding.xslt $<
	cp -f $< $@

# all: p.svg

$(DESTBASE_default).webp: $(WEBP)
	cp -f $< $@

$(WEBP): $(PNG)
	gm convert $< $@

$(JPEG): $(PNG)
	gm convert $< $@

$(PHOTO_INTERIM1): $(PHOTO_BASE).jpg
	gm convert -crop 2560x1177 $< $@


clean:
	rm -f emma-*.png emma-*.jpg emma-*.webp

upload: all
	sky -x up $(WEBP)

# upload: all
#	rsync --progress -v -a --inplace human-hacking-field-guide-logo.svg hhfg-ad.svg hhfg-ad.svg.png $(__HOMEPAGE_REMOTE_PATH)/hhfg-graphics-demo/
