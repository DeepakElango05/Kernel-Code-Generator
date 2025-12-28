# KERNAL CODE GENERATOR

## Description
This Project can be used to generate a kernal module c file based on the inputs from the Configuration python file.

## Usage
1. Configure your module kernal file's name, license type, decription , author and how the file should be designed
2. For using modern file design you have mention "mod" in file_design member

## NOTE
1. Care need to be taken care while giving value to the file_design member it can be "mod" or any other name. For any string other than "mod" the code will be generated in standard module design.
2. The file generated can have any unexpected output if the CodeGenerator.py file is modified.
