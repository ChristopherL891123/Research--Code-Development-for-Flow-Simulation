Contents of research folder:
    MatrixGeneration.py  contains matrix generation algorithm(GENERATE), matrix printing(MatPrint),
    Matrix multiplication(MultMatrix), b vector and exact velocity and Yj points generation(B_VExact_Yj_GENERATE)

    LU.py  contains decomposition algorithm(DECOMP), forward substitution algorithm(FORWARD_SUB),
    backward substitution(BACKWARD_SUB), table generation(TabPrint), matrix equation solving algorithm(SOLVE)

    main.py contains the console executable of the research

    GUI.py contains the window executable of the research



GUI.py instructions
    1. double click on GUI.py file, a window should appear
    2. make window full screen
    3. In "Size of Matrix A to generate", type number of inner discrete points, without the boundary conditions.
    4. In "η" textbox, type value for viscosity
    5. In "Length of channel", type the value for the length of the artery
    6. In "ΔP" , type value for change in pressure
    7. In "Radius H", type value for radius of the artery.
    8. After all the values have been typed into the textboxes, click on "Submit" button.
    9. A graph and table should be shown.
    10. Many graphs and tables can be seen at the same time by changing values in the textboxes and clicking
        the submit button.
    11. To exit the window, click on the exit button or the "X" on the upper rightmost icon of the window

main.py instructions
    1. double click on the main.py file and a window should appear, make it full screen.
    2. When the "Size of matrix A to generate =" prompt appears, type number of inner discrete points,
       without the boundary conditions. Then press the "enter" key on the keyboard.
    3. When the "H =" prompt appears, type the value for the radius of the artery.
        Then press the "enter" key on the keyboard.
    4. When the "L ="  type the value for the length of the artery.
        Then press the enter key on the keyboard.
    5. When the "Delta P =" prompt appears, type value for change in pressure.
        Then press the enter key on the keyboard.
    6. When the "Viscosity =" prompt appears, type value for viscosity.
        Then press the enter key on the keyboard.
    7. A graph and table should appear.
    8. After the graph is closed, the "Size of matrix A to generate =" should appear again.