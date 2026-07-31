.PHONY: build serve clean check

build:
	hugo --minify

serve:
	hugo server --disableFastRender

clean:
	rm -rf dist resources/_gen

check:
	hugo --minify --panicOnWarning --printPathWarnings
	@test -f dist/index.html
	@bad=0; \
	for file in $$(find dist -type f \( -name '*.html' -o -name '*.css' \)); do \
	  if grep -E '(href|src)="(/|https?://)' "$$file"; then bad=1; fi; \
	done; \
	if test $$bad -ne 0; then \
	  echo 'Absolute or external asset/link found; review offline behavior.'; exit 1; \
	fi
