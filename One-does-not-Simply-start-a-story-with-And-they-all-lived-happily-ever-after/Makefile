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
# all: $(NOBRANDING_PERSON_PNG) $(NOBRANDING_PERSON_WEBP) $(NOBRANDING_PERSON_JPEG) $(NOBRANDING_PERSON_PNG)

$(PNG): $(SVG) $(EMBEDDED_PHOTO1__PATH)
	inkscape --export-filename=$@ --export-width=$(WIDTH) $<
	optipng $@

$(DESTBASE_default).webp: $(WEBP)
	cp -f $< $@

$(WEBP): $(PNG)
	gm convert $< $@

$(JPEG): $(PNG)
	gm convert $< $@

clean:
	rm -f emma-*.png emma-*.jpg emma-*.webp

upload: all
	sky -x up $(WEBP)

# upload: all
#	rsync --progress -v -a --inplace human-hacking-field-guide-logo.svg hhfg-ad.svg hhfg-ad.svg.png $(__HOMEPAGE_REMOTE_PATH)/hhfg-graphics-demo/
