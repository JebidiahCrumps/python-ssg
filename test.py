import markdown

def md2html():

    #make sure to have "import markdown" at the top
    #This block of code will ask for a file name
    #then open that file read it and turn
    #it into HTML with a default css theme

    print("Enter the markdown filename: ")
    fileName = input()

    try:
        with open(fileName) as file:
            pass
    except IOError as e:
        print("Unable to open file")  # Does not exist OR no read permissions
        exit()
    input_file = open(fileName)

    text = input_file.read()

    html = markdown.markdown(text)

    output_file = open("TheHTML.html", "w")

    output_file.write(html)

    print("Converted!")

md2html()
