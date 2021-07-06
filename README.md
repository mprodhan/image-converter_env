The Image Converter

In this short mini project, a main fucntion that converts images to a thumbnail.
In order to make this happen and not override the original files, a make_dirs function
needed to be created, which would create a director, similar to the way we create our directories
in our terminal/linux terminal/windows command prompt. Each step to creating this project
will be broken down as to create an elementary understanding of the project.

Step 1: Determine a library and other modules appropriate for the project.

In uderstanding why we have to determine where our folders that exists or does not yet exit,
the sys module had to be imported. The module comes from python proper and it provides access
to some variables or maintained by the interpreter and interacts strongly with the interpreter (1).
This way, the argv variable was accessed and used to create an order of parsing the command to
access the file, images.py, images directory and a new directory, png_folder. So the command
would be displayed as follows:

            python images.py images/ png_folder/
            images.py --> sys.argv[0]
            (this command is implicit as python is our developer environemnt and assumes that [0]
            is our python program.)
            images --> sys.argv[1]
            new_directory --> sys.argv[2]

The sys.argv is then used to assign image_folderto 1 and image_output to 2. The image_folder
is with its intended folder, images and the new_directory can be name anything. For example,
the 'png_folder' got used as new_directory. The other module we are using is the 'os' module,
also implicit in python.

Step 2: Create a helper function

In this step, we create a helper function make_dir(output_images), with the output_images passed
as an arrgument. The argument is being passed because we will be using the 'os' module (2). The 'os'
is as the name suggests, accesses our terminal or cmd_prompt functionalities and creates the
new_direcotory. This helper function gets passed to the main(args) function.

Step 3: Create the main(args) function

The main function is, as stated, the functtion that passes all of the functions and arguments from
the helper functions. If there is a reason for how helper functions and main functions work, it is
that a helper function is the run in the mill functtion. This is a convention, for creating functions,
that are simple but powerful and to the point, instead of spaghetti coding. The main function then calls
the helper functions and makes the output comprehensive. This way, the main function is not riddled with
too many, details but, that anyone reading the code can tell, what the functions are doing because, they
are readable.

The main function here, calls the make_dir function and then loops through the image folder. The
image_folder consists of the images. The three things, that need to be accomoplished with this function,
is to create the new_directory by calling the helper function, transform the .jpg file to .png, and to
create a thumbnail of the png images.

In running the for loop, the PIL module also known as the pillow library application (3),
had to be installed, in order to access the images, run them through the for loop and use the tranformed
images to .png to resize by the use of the  img.thumbnail((x,y)) to reduce the image into a clear thumbnail
file.

Finally, the codes are then run through the filename, by creating the following code:

    if __name__ == '__main__':
    main(sys.argv[1:]) (4)

What this means is that, the __name__ is the name of the file and it is passed through,
the main function as a whole summarized versions of the helper and main functions, which will
parse the output via  main(sys.srgv[1:]). The main function via 'args' argument is passing the
sys,srgv list.



Sources:
(1): The sys module
https://docs.python.org/3/library/sys.html

(2): The os module
https://docs.python.org/3/library/os.html

(3): pillow (PIL) documentation Library
https://pillow.readthedocs.io/en/stable/

(4) Stackoverflow (if __name__ == '__main__')
https://stackoverflow.com/questions/419163/what-does-if-name-main-do







