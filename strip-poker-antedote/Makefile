WIDTH = 600

BASE = captioned-image--strip-poker-antedote
SVG = $(BASE).svg
DESTBASE = $(BASE)-$(WIDTH)
DESTBASE_default = $(SVG)
PNG = $(DESTBASE).png
JPEG = $(DESTBASE).jpg
WEBP = $(DESTBASE).webp

EMBEDDED_PHOTO1__PATH = mr-t--0777d5ee0f4dee5a88fafaf140e2a058e2841e47_hq.jpg

all: $(PNG) $(JPEG) $(WEBP)

$(PNG): $(SVG) $(EMBEDDED_PHOTO1__PATH)
	inkscape --export-filename=$@ --export-width=$(WIDTH) $<
	optipng $@

p.svg: $(SVG)
	xsltproc -o $@ remove-svg-branding.xslt $<

all: p.svg

$(DESTBASE_default).webp: $(WEBP)
	cp -f $< $@

$(WEBP): $(PNG)
	gm convert $< $@

$(JPEG): $(PNG)
	gm convert $< $@

$(PHOTO_INTERIM1): $(PHOTO_BASE).jpg
	gm convert -crop 2560x1177 $< $@

_CLEAN_IMAGES_PREFIX = captioned-image--strip-poker-antedote

clean:
	rm -f $(_CLEAN_IMAGES_PREFIX)*.png $(_CLEAN_IMAGES_PREFIX)*.jpg $(_CLEAN_IMAGES_PREFIX)*.webp

upload: all
	sky -x up $(WEBP)
