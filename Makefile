all:: library_build library_fix_permissions library_apply_patches library_apply_fixes

library_build::
	docker run --rm -v "${PWD}:/local" openapitools/openapi-generator-cli generate \
		-i /local/gitea-openapi-3.0-spec.yaml \
		-g python \
		-o /local/out/python

library_fix_permissions::
	sudo chown -R ${USER}:users out

library_apply_patches::
	find patches/ -name '*.patch' -type f -print0 | sort -z | xargs -r0 -n1 git apply --reject

library_apply_fixes::
	find . -name '*.py' -type f -exec sh -c "sed -z -i -E 's/typing.Union\[\s*\]/typing.Any/g' {}" \;

clean::
	rm -rf out

