dict={"atomic habits":700,"the are of not giving fuck":690,"thinks like money by james clear":800}
max_value=max(dict,key=dict.get)
print(max_value,dict[max_value])
dict2={"yash":700,"jiggle":690,"physics":800}
book={**dict,**dict2}
print(book)