sourcePath = './docs/'
distPath = './output/'
distPathOnly = 'output'


"""
    Docx to Txt File
    pip3 install mammoth
"""
# import mammoth
# filename = 'Abdus Sattar.docx'
# sourceFiles = sourcePath+filename
# distFilesTxt = distPath+'output.txt'
# with open(sourceFiles, "rb") as docx_file:
#     result = mammoth.extract_raw_text(docx_file)
#     text = result.value # The raw text
#     with open(distFilesTxt, 'w') as text_file:
#         text_file.write(text)



""" 
    Docs to Image Extract
    pip install docx2txt
"""
# import docx2txt
# filename = '2. akhtaruzzaman khan.docx'
# sourceFiles = sourcePath+filename
# text = docx2txt.process(sourceFiles, distPath)

""" 
    Docx to image - using
        Also features:
            extracts text from docx files
            extracts images from docx files
            no dependencies (docx2python requires pytest to test)
    pip install docx2python
"""
# from docx2python import docx2python
# filename = '1. abdul mannan sarkar.docx'
# sourceFiles = sourcePath+filename
# docx2python(sourceFiles, 'output')


from docx2python import docx2python
import os
 
# Get the list of all files and directories
path = sourcePath
dir_list = os.listdir(path)

# Find all files and loop file name in file_names
for file_names in dir_list:
    if file_names.endswith(".docx"):
        print(file_names)
        try: 
            os.makedirs(os.path.join(distPathOnly, file_names))
        except OSError as error: 
            print(error)
        sourceFiles = path+file_names    
        docx2python(sourceFiles, distPath+file_names)
        print(sourceFiles)




"""
    Docs Marge 
    pip install aspose-words
"""
# import aspose.words as aw
# distFilesDocs = distPath+'output.docx'
# fileNames = [ sourcePath+"Abdus Sattar.docx", sourcePath+"salam.docx" ]
# output = aw.Document()
# # Remove all content from the destination document before appending.
# output.remove_all_children()
# for fileName in fileNames:
#     input = aw.Document(fileName)
#     # Append the source document to the end of the destination document.
#     output.append_document(input, aw.ImportFormatMode.KEEP_SOURCE_FORMATTING)
# output.save(distFilesDocs)