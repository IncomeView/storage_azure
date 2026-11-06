.PHONY: \
	help \
	publish-dataset \
	uplod-dataset \
	publish-project \
	upload-project \
	publish-all \
	upload-all \
	catalog \
	discover \
	knowledge \
	all

help:
	@echo ""
	@echo "Storage Azure Commands"
	@echo ""
	@echo "DATASET"
	@echo "  make publish-dataset DATASET=ipca_geral"
	@echo "  make upload-dataset DATASET=ipca_geral"
	@echo ""
	@echo "PROJECT"
	@echo "  make publish-project PROJECT=inflation_bcb"
	@echo "  make upload-project PROJECT=inflation_bcb"
	@echo ""
	@echo "ALL PROJECTS"
	@echo "  make publish-all"
	@echo "  make upload-all"
	@echo ""
	@echo "DISCOVERY"
	@echo "  make catalog"
	@echo "  make discover"
	@echo ""
	@echo "DOCUMENTATION"
	@echo "  make knowledge"
	@echo ""
	@echo "FULL FLOW"
	@echo "  make all"
	@echo ""

# DATASET
publish-dataset:
	python scripts/publish_dataset.py \
		--dataset $(DATASET)

upload-dataset:
	python scripts/upload_dataset.py \
		--dataset $(DATASET)

# PROJECT
publish-project:
	python scripts/publish_project.py \
		--project $(PROJECT)

upload-project:
	python scripts/upload_project.py \
		--project $(PROJECT)

# ALL PROJECTS
publish-all:
	python scripts/publish_all_projects.py

upload-all:
	python scripts/upload_all_projects.py

# DISCOVERY
catalog:
	python tests/test_catalog.py

discover:
	python tests/test_containers.py
	python tests/test_paths.py
	python tests/test_project_files.py
	python tests/test_dataset_exists.py

# DOCUMENTATION
knowledge:
	python scripts/generate_project_knowledge_base.py

# PIPELINE
all:
	$(MAKE) publish-all
	$(MAKE) upload-all
