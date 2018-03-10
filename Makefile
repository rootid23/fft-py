.PHONY:	fmt

#List all sub-dirs
SUBDIRS := $(wildcard */)
SRCS = $(wildcard $(addsuffix *.py,$(SUBDIRS)))

#Run formatter on all files
fmt:
	$(foreach f,$(SRCS),${PWD}/fmt.sh $(f);)

#Debug var value use print-SUBDIRS
print-%:
	@echo '$*=$($*)'

clean:
	@echo "Cleaning pyc files"
	find . -name "*.pyc" | xargs rm -rf

# vim: noexpandtab
