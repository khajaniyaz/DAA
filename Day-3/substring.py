def substring_search(main_string, sub_string):
    return main_string.find(sub_string)
main_string= "Hello, welcome to the world of python!"
sub_string="Python"
result=substring_search(main_string, sub_string)
print("Substring founnd at index: ", result if result!=-1 else "substring not found")
