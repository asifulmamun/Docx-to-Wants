sourcePath = './docs/'
distPath = './output/'



"""
    Docx to Txt File
    pip3 install mammoth
"""
import mammoth
filename = 'Abdus Sattar.docx'
sourceFiles = sourcePath+filename
distFilesTxt = distPath+'output.txt'
with open(sourceFiles, "rb") as docx_file:
    result = mammoth.extract_raw_text(docx_file)
    text = result.value # The raw text
    with open(distFilesTxt, 'w') as text_file:
        text_file.write(text)



""" 
    Docs to Image Extract
    pip install docx2txt
"""
# import docx2txt
# filename = 'Abdus Sattar.docx'
# sourceFiles = sourcePath+filename
# text = docx2txt.process(sourceFiles, distPath)




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