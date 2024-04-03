WIDTH = 600

BASE = One-does-not-simply-start-a-story-with-And-they-all-lived-happily-ever-after
SVG = $(BASE).svg
DESTBASE = $(BASE)-$(WIDTH)
DESTBASE_default = $(SVG)
PNG = $(DESTBASE).png
JPEG = $(DESTBASE).jpg
WEBP = $(DESTBASE).webp

EMBEDDED_PHOTO1__PATH = one-does-not-simply.jpg

all: $(PNG) $(JPEG) $(WEBP)

$(PNG): $(SVG) $(EMBEDDED_PHOTO1__PATH)
	inkscape --export-filename=$@ --export-width=$(WIDTH) $<
	optipng $@

$(DESTBASE_default).webp: $(WEBP)
	cp -f $< $@

$(WEBP): $(PNG)
	gm convert $< $@

$(JPEG): $(PNG)
	gm convert $< $@

_CLEAN_IMAGES_PREFIX = One-does-not

clean:
	rm -f $(_CLEAN_IMAGES_PREFIX)*.png $(_CLEAN_IMAGES_PREFIX)*.jpg $(_CLEAN_IMAGES_PREFIX)*.webp

upload: all
	sky -x up $(WEBP)
