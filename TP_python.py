import argparse 

parser = argparse.ArgumentParser()
parser.add_argument("-i", "--input_directory",
                    action="store",
                    type=str,
                    required=True,
                    help="Input directory, please make sure you have insert the input directory, containing the markdown files.",
                    )
parser.add_argument("-o", "--output-directory",
                    action="store",
                    type=str,
                    required=True,
                    help="Ouput directory, please make sure you have insert an ouput directory.",
                    )
parser.add_argument("-t", "--template-directory",
                    action="store",
                    type=str,
                    help="Template directory, please make sure you have insert an template directory.",
                    )
arg = parser.parse_args()
