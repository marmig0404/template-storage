# Template Store

Template Store is a module that compresses template images into a store.
## Usage
### Command Line
```
> templatestore -h
usage: templatestore [-h] [-s--storepath STORE_PATH] [-l] [-f FILES [FILES ...]] [-r REMOVE [REMOVE ...]]

Import images into a template store

options:
  -h, --help            show this help message and exit
  -s, --storepath STORE_PATH
                        store file to update or create, defaults to 'store'
  -l, --list            list templates in store
  -f FILES [FILES ...], --files FILES [FILES ...]
                        a file or list of files to add, ie 'img1.png img2.png'
  -r REMOVE [REMOVE ...], --remove REMOVE [REMOVE ...]
                        a file or list of files to remove, ie 'img1.png img2.png'
```
### Python Import
```
>>> from templatestore import TemplateStore
>>> ts = TemplateStore("myStoreName")	# open new template store "myStoreName"  
>>> from PIL import Image
>>> img = Image.open("myTemplate.png")
>>> ts.add_templates({"myTemplateName":img})	# add an image to the template store
>>> ts.template_store	# check the store
{'myTemplateName': <PIL.PngImageP...A350>}
>>> ts.remove_template('myTemplateName')	# remove template
>>> ts.template_store	# check store
{}
```
