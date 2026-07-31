.PHONY: build serve clean check

build: clean
	hugo --minify

serve:
	hugo server --disableFastRender

clean:
	rm -rf dist resources/_gen

check: clean
	hugo --minify --panicOnWarning --printPathWarnings
	python3 scripts/validate_build.py
