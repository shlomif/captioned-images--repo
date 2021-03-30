SVG = friends--yeah-like-i-could-lose-it.svg
PNG = $(SVG).png
PNG600 = $(SVG)-600w.png
JPEG = $(SVG).jpg
WEBP = $(SVG).webp
WEBP600 = $(SVG)-600w.webp

WIDTH = 800

all: $(PNG) $(JPEG) $(WEBP) $(WEBP600)

$(PNG): $(SVG)
	inkscape --export-type=png --export-filename=$@ --export-width=$(WIDTH) $<

$(PNG600): $(SVG)
	inkscape --export-type=png --export-filename=$@ --export-width=600 $<

$(WEBP600) $(WEBP): %.webp: %.png
	gm convert $< $@

$(JPEG): $(PNG)
	gm convert $< $@

upload: all
	rsync --progress -v -a --inplace $(PNG) $(SVG) $(WEBP) *.jpg $(__HOMEPAGE_REMOTE_PATH)/friends--yeah-like-i-could-lose-it/
