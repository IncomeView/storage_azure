.PHONY: help publish upload discover knowledge all

help:
	@echo ""
	@echo "Storage Azure Commands"
	@echo ""
	@echo "make publish      -> Generate datasets locally"
	@echo "make upload       -> Upload datasets to ADLS"
	@echo "make catalog      -> Generate dataset catalog"
	@echo "make discover     -> Inspect ADLS"
	@echo "make knowledge    -> Generate knowledge base"
	@echo "make all          -> Publish, Upload and Knowledge"
	@echo ""

publish:
	python tests/test_publish_project.py

upload:
	python tests/test_upload_project.py

catalog:
	python tests/test_catalog.py

discover:
	python tests/test_containers.py
	python tests/test_paths.py
	python tests/test_project_files.py
	python tests/test_dataset_exists.py

knowledge:
	python scripts/generate_project_knowledge_base.py

all:
	$(MAKE) publish
	$(MAKE) upload
#	$(MAKE) knowledge