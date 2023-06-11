import os

main_dir = 'C:/Users/Hp/Downloads/[FreeCourseSite.com] Udemy - Machine Learning A-Z™ - AI, Python & R + ChatGPT Bonus [2023]​'
os.chdir(main_dir)


sub_folders = os.listdir()[2:]
for folder in sub_folders:
    new_dir = f"{main_dir}/{folder}"
    os.chdir(new_dir)
    print(os.getcwd())

    for file in os.listdir():
        #getNameExtensionOfFiles
        name, extension = os.path.splitext(file)

        #for deleting files with content of R programming language in it
        if 'R' in name.split():
            print(name+extension)
            os.remove(name+extension)

        else:
            #for deleting subtitle files of other lanugages
            if extension == '.vtt':
                if name.split()[-1] != 'English':
                    print(name+extension)
                    os.remove(name+extension)
