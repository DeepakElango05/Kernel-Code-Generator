
import os

from CodeGenConfig import *

def generate_file()->None:
    with open(f"{CodeGeneratorConfig.file_name}.c","w") as c_file:

        for header in CodeGeneratorConfig.required_headers:
            c_file.write(f"#include<linux/{header}.h>\n")

        c_file.write("\n"*3)

        c_file.write(f"MODULE_AUTHOR(\"{CodeGeneratorConfig.author_name}\");\n")
        c_file.write(f"MODULE_DESCRIPTION(\"{CodeGeneratorConfig.file_description}\");\n")
        c_file.write(f"MODULE_LICENSE(\"{CodeGeneratorConfig.License}\");\n")

        c_file.write("\n"*3)

        if CodeGeneratorConfig.file_design!="mod":
            #Creating the init function
            c_file.write("int module_init(void)\n");
            c_file.write("\n{\n")
            c_file.write("\t/*USER CODE BEGIN*/\n")
            c_file.write("\t/*USER CODE END*/\n")
            c_file.write("\treturn 0;\n}")
                
            #Creating space between init and exit function
            c_file.write("\n"*3)

            #Creating the exit function 
            c_file.write("void module_exit(void)\n")
            c_file.write("\n{\n")
            c_file.write("\t/*USER CODE BEGIN*/\n")
            c_file.write("\t/*USER CODE END*/\n")
            c_file.write("}\n")
        else:
            #Creating the init function
            c_file.write(f"static int __init {CodeGeneratorConfig.init_function_name}(void)\n")
            c_file.write("{\n")
            c_file.write("\t/*USER CODE BEGIN*/\n")
            c_file.write("\t/*USER CODE END*/\n")
            c_file.write("\treturn 0;\n}")

            #Creating empty line between init and exit function
            c_file.write("\n"*3)

            #Creating the exit function
            c_file.write(f"static void __exit {CodeGeneratorConfig.cleanup_function_name}(void)\n")
            c_file.write("{\n")
            c_file.write("\t/*USER CODE BEGIN*/\n")
            c_file.write("\t/*USER CODE END*/\n")
            c_file.write("}")
            
            #creating new lines
            c_file.write("\n"*3)

            #creating module init and exit
            c_file.write(f"module_init({CodeGeneratorConfig.init_function_name});\n")
            c_file.write(f"module_exit({CodeGeneratorConfig.cleanup_function_name});\n")


if __name__=="__main__":
        generate_file()



