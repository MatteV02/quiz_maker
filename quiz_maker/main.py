import sys
from quiz_maker.question_extractor.JSONQuestionExtractor import JSONQuestionExtractor
from quiz_maker.output_generator.HTMLOutputGenerator import HTMLOutputGenerator
from argparse import ArgumentParser, ArgumentError


if __name__ == '__main__':
    parser = ArgumentParser(
        prog='Quiz Maker',
        description='Utility to make interactive quizes from questions.\nUsage guide at https://github.com/MatteV02/quiz_maker',
        epilog='Realesed under Unlicense license by MatteV02 https://github.com/MatteV02',
        exit_on_error=False
    )
    parser.add_argument('-i', '--in-file', help='Path to the input file; supported formats: JSON')
    parser.add_argument('-o', '--out-file', help='Path to the output file; supported formats: HTML')
    try:
        args = parser.parse_args()
        in_file = args.in_file
        if in_file is None:
            raise ValueError('Missing -i argument')
        out_file = args.out_file
        if out_file is None:
            raise ValueError('Missing -o argument')
    except:
        print('quiz_maker: \tWrong usage, arguments -i|--in-file and -o|--out-file are required. No other flags are supported.\n\t\tRun with option -h for more details')
        sys.exit(1)

    extractor = JSONQuestionExtractor()
    generator = HTMLOutputGenerator()

    try:
        generator.write(extractor.read(in_file), out_file)
    except ValueError as value_error:
        if value_error.args[0] == 'JSON file structure is not conforming to the one the application expects':
            print('quiz_maker: \tWrong usage, Input file is not conforming to specifics.\n\t\tRun with option -h for more details')
            sys.exit(3)
        else:
            print('quiz_maker: \tWrong usage, Input file type is not supported.\n\t\tRun with option -h for more details')
            sys.exit(2)
    except OSError:
        print('quiz_maker: \tWrong usage, invalid output file path.\n\t\tRun with option -h for more details')
        sys.exit(1)
    
    sys.exit(0)