import sys
from quiz_maker.question_extractor.JSONQuestionExtractor import JSONQuestionExtractor
from quiz_maker.output_generator.HTMLOutputGenerator import HTMLOutputGenerator
from argparse import ArgumentParser


if __name__ == '__main__':
    parser = ArgumentParser(
        prog='Quiz Maker',
        description='make quiz',
        epilog=''
    )
    parser.add_argument('-i', '--in-file')
    parser.add_argument('-o', '--out-file')
    args = parser.parse_args()

    in_file = args.in_file
    out_file = args.out_file

    extractor = JSONQuestionExtractor()
    generator = HTMLOutputGenerator()

    try:
        generator.write(extractor.read(in_file), out_file)
    except:
        # print useful messages
        sys.exit(1)
    
    sys.exit(0)