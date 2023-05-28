# 8085 Assembly Language to Hex Converter

## Overview
![General UI](https://raw.githubusercontent.com/NotSujal/8085-assembly-to-hex/main/images/general_ui.png)

The 8085 Assembly Language to Hex Converter is a user-friendly Python application developed with the tkinter library. Its primary purpose is to provide an intuitive interface for typing and transpiling (compiling/translating) code written in 8085 assembly language into hexadecimal numbers.

## How It Works
![Custom Extensions](https://raw.githubusercontent.com/NotSujal/8085-assembly-to-hex/main/images/custom_extention.png)

The converter employs a robust string manipulation system to process the code entered by the user. Each line of code is carefully filtered and converted into the corresponding hexadecimal representation, which is then added to the queue for further processing.

![Basic Options](https://raw.githubusercontent.com/NotSujal/8085-assembly-to-hex/main/images/basic_options.png)

To facilitate accurate translation, the converter relies on the specified starting locations within the code to determine the addresses of labels. This ensures that the converted code retains the correct memory addressing.

![Editor](https://raw.githubusercontent.com/NotSujal/8085-assembly-to-hex/main/images/editor.png)
![Translator](https://raw.githubusercontent.com/NotSujal/8085-assembly-to-hex/main/images/translator.png)

The application provides a convenient code editor that allows users to input and modify their 8085 assembly language code. The integrated translator then processes the code and generates the corresponding hexadecimal output, which is displayed for the user.

## Limitations
The 8085 Assembly Language to Hex Converter is focused solely on the task of translating code into hexadecimal format. It does not provide a built-in runtime environment or emulator for executing the converted code. Users are encouraged to create their own runners or utilize external tools to run the converted code on an 8085 processor.

It's important to note that due to the nature of assembly language and the complexities involved in manual code translation, identifying mistakes or errors in the code can be challenging. Inaccurate or incorrect code may result in unexpected or improper output when executed on an 8085 processor. Therefore, thorough testing and verification of the converted code is recommended before use in any critical applications.
