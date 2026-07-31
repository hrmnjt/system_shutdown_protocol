.PHONY: build serve clean check portable

build: clean
	hugo --minify

serve:
	hugo server --disableFastRender

clean:
	rm -rf dist release resources/_gen

check: clean
	hugo --minify --panicOnWarning --printPathWarnings
	python3 scripts/validate_build.py

portable: check
	python3 scripts/package_portable.py
